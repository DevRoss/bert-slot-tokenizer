#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import six

sys.path.append(os.path.dirname(os.getcwd()))
import bert_slot_tokenizer
from bert_slot_tokenizer.bert_tokenizer import tokenization
from bert_slot_tokenizer import SlotConverter


class UnitTests(unittest.TestCase):
    test_case1 = {'text': 'Too YOUNG, too simple, sometimes naive! 蛤蛤+1s',
                  'slots': {'长者': '蛤蛤',
                            '时间': '+1s'},
                  'target_token': ['too', 'young', ',', 'too', 'simple', ',', 'some', '##times', 'na', '##ive', '!',
                                   '蛤', '蛤', '+', '1', '##s'],
                  'target_iob_slot': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-长者', 'I-长者', 'B-时间',
                                      'I-时间', 'I-时间']
                  }
    test_case2 = {'text': '\'齉\'这个字怎么读？',
                  'slots': {'action': '怎么读'},
                  'target_token': ["'", '[UNK]', "'", '这', '个', '字', '怎', '么', '读', '？'],
                  'target_iob_slot': ['O', 'O', 'O', 'O', 'O', 'O', 'B-action', 'I-action', 'I-action', 'O']
                  }

    def convert_to_unicode_list(self, l):
        """
        string to unicode when testing with python2
        :param l:
        :return:
        """
        ret = list()
        for i in range(len(l)):
            ret.append(tokenization.convert_to_unicode(l[i]))
        return ret

    def test_import(self):
        self.assertIsNotNone(bert_slot_tokenizer)

    def test_project(self):

        sc = SlotConverter('test_data/example_vocab.txt', do_lower_case=True)

        if six.PY3:
            token1, iob_slot1 = sc.convert2iob(UnitTests.test_case1['text'], UnitTests.test_case1['slots'])
            token2, iob_slot2 = sc.convert2iob(UnitTests.test_case2['text'], UnitTests.test_case2['slots'])

            self.assertTrue(token1 == UnitTests.test_case1['target_token'], "token1")
            self.assertTrue(iob_slot1 == UnitTests.test_case1['target_iob_slot'], "iob_slot1")
            self.assertTrue(token2 == UnitTests.test_case2['target_token'], "token2")
            self.assertTrue(iob_slot2 == UnitTests.test_case2['target_iob_slot'], "iob_slot2")
        elif six.PY2:
            token1, iob_slot1 = sc.convert2iob(UnitTests.test_case1['text'], UnitTests.test_case1['slots'])
            token2, iob_slot2 = sc.convert2iob(UnitTests.test_case2['text'], UnitTests.test_case2['slots'])

            self.assertTrue(token1 == self.convert_to_unicode_list(UnitTests.test_case1['target_token']), "token1")
            self.assertTrue(iob_slot1 == self.convert_to_unicode_list(UnitTests.test_case1['target_iob_slot']),
                            "iob_slot1")
            self.assertTrue(token2 == self.convert_to_unicode_list(UnitTests.test_case2['target_token']), "token2")
            self.assertTrue(iob_slot2 == self.convert_to_unicode_list(UnitTests.test_case2['target_iob_slot']),
                            "iob_slot2")


if __name__ == '__main__':
    unittest.main()
