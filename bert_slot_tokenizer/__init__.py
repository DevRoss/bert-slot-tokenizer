#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 2019/7/31
import json

from bert_slot_tokenizer.bert_tokenizer import tokenization


class SlotConverter:
    def __init__(self, vacab_file, do_lower_case=True):
        """ A Converter to convert plain slot to IOB format slot.
        example:
            input_text: 'Too YOUNG, too simple, sometimes naive! 蛤蛤+1s'
            input_slot: {'长者': '蛤蛤', '时间': '+1s'},

            output_text: ['too', 'young', ',', 'too', 'simple', ',', 'some', '##times', 'na', '##ive', '!', '蛤', '蛤', '+', '1', '##s']
            output_iob_slot: ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-长者', 'I-长者', 'B-时间', 'I-时间', 'I-时间']

        usage example:
        sc = SlotConverter('test_data/example_vocab.txt', do_lower_case=True)
        text = ''Too YOUNG, too simple, sometimes naive! 蛤蛤+1s'
        slot = {'长者': '蛤蛤'}  # note that this is a dict object. with the key-value pair.

        output_text, output_slot = sc.convert2iob(text, slot)
        # output_text and output_slot are both list object.

        :param vacab_file: path to vocab.txt in pre-trained bert model directory.
        :param do_lower_case: if True, all the output will be in lower case.
        """
        self.bert_tokenizer = tokenization.FullTokenizer(vacab_file, do_lower_case=do_lower_case)

    @staticmethod
    def parse_json(file):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        texts = []
        slots = []
        for i in data:
            texts.append(i['text'])
            slots.append(i['slots'])
        return texts, slots

    @staticmethod
    def kmp(main_str, pattern):
        """
        Kmp algorithm to get the begin index of slot in text if matching

        """
        nex = SlotConverter.get_next(pattern)
        i = 0  # the pointer of main_str
        j = 0  # the pointer of pattern
        while i < len(main_str) and j < len(pattern):
            if j == -1 or main_str[i] == pattern[j]:
                i += 1
                j += 1
            else:
                j = nex[j]

        if j == len(pattern):  # matched
            return i - j
        else:
            return -1

    @staticmethod
    def get_next(pattern):
        """
        """
        nex = [0] * len(pattern)
        nex[0] = -1
        i = 0
        j = -1
        while i < len(pattern) - 1:  # len(pattern)-1防止越界，因为nex前面插入了-1
            if j == -1 or pattern[i] == pattern[j]:
                i += 1
                j += 1
                nex[i] = j  # 这是最大的不同：记录next[i]
            else:
                j = nex[j]

        return nex

    @classmethod
    def tokenize(cls, begin_index: int, end_index: int, slot_key: str, ret_slot: list):
        """
        Convert to IOB format slot when given slot‘s begin/end slot index.
        We perform in place, which means re_slot will change after calling this function.
        :param begin_index: slot begin index, where the slot begins.
        :param end_index: slot begin index, where the slot ends.
        :param slot_key: the label of slot, such as 'AppName'
        :param ret_slot:
        :return:
        """
        # usage: [begin_index, end_index]
        for i in range(begin_index, end_index):
            if ret_slot[i] != 'O':
                break
            if i == begin_index:
                ret_slot[i] = 'B-' + slot_key
            else:
                ret_slot[i] = 'I-' + slot_key

    def convert2iob(self, text: str, slot: dict) -> (str, list):
        """
        convert dict slot to IOB format slot
        :param text: text with type str
        :param slot: slot with type dict
        :return: a tuple with (output_slot, output_iob_slot)
        """
        text_tokens = self.bert_tokenizer.tokenize(text)
        iob_slot = list('O' * len(text_tokens))
        for k, v in slot.items():
            slot_tokens = self.bert_tokenizer.tokenize(v)
            begin_index = SlotConverter.kmp(text_tokens, slot_tokens)
            SlotConverter.tokenize(begin_index, begin_index + len(slot_tokens), k, iob_slot)
            assert len(iob_slot) == len(text_tokens)
        return text_tokens, iob_slot


if __name__ == '__main__':
    pass
