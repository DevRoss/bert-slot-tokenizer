#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import six

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(CUR_DIR))

from bert_slot_tokenizer import SlotConverter
from bert_slot_tokenizer.bert_tokenizer import tokenization
import bert_slot_tokenizer

class UnitTests(unittest.TestCase):
    test_case1 = {'text': 'Too YOUNG, too simple, sometimes naive! 蛤蛤+1s蛤蛤蛤嗝',
                  'slots': {'蛤蛤': '长者',
                            '+1s': '时间',
                            '嗝': '语气'},
                  'target_token': ['too', 'young', ',', 'too', 'simple', ',', 'some', '##times', 'na', '##ive', '!',
                                   '蛤', '蛤', '+', '1', '##s', '蛤', '蛤', '蛤', '嗝'],
                  'target_iob_slot': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-长者', 'I-长者', 'B-时间',
                                      'I-时间', 'I-时间', 'B-长者', 'I-长者', 'O', 'B-语气'],
                  'target_iobs_slot': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-长者', 'I-长者', 'B-时间',
                                       'I-时间', 'I-时间', 'B-长者', 'I-长者', 'O', 'S-语气'],
                  'target_bmes_slot': ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-长者', 'E-长者', 'B-时间',
                                       'M-时间', 'E-时间', 'B-长者', 'E-长者', 'O', 'S-语气'],
                  'target_span_slot': [[11, 12, '长者'], [13, 15, '时间'], [16, 17, '长者'], [19, 19, '语气']]
                  }
    test_case2 = {'text': '\'齉\'这个字怎么读？',
                  'slots': {'怎么读': 'action'},
                  'target_token': ["'", '[UNK]', "'", '这', '个', '字', '怎', '么', '读', '？'],
                  'target_iob_slot': ['O', 'O', 'O', 'O', 'O', 'O', 'B-action', 'I-action', 'I-action', 'O'],
                  'target_iobs_slot': ['O', 'O', 'O', 'O', 'O', 'O', 'B-action', 'I-action', 'I-action', 'O'],
                  'target_bmes_slot': ['O', 'O', 'O', 'O', 'O', 'O', 'B-action', 'M-action', 'E-action', 'O'],
                  'target_span_slot': [[6, 8, 'action']]
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

        sc = SlotConverter('tests/test_data/example_vocab.txt', do_lower_case=True)

        if six.PY3:
            token1, iob_slot1 = sc.convert(UnitTests.test_case1['text'], UnitTests.test_case1['slots'], fmt='IOB')
            token1, iobs_slot1 = sc.convert(UnitTests.test_case1['text'], UnitTests.test_case1['slots'], fmt='IOBS')
            token1, bmes_slot1 = sc.convert(UnitTests.test_case1['text'], UnitTests.test_case1['slots'], fmt='BMES')
            token1, span_slot1 = sc.convert(UnitTests.test_case1['text'], UnitTests.test_case1['slots'], fmt='SPAN')

            self.assertTrue(token1 == UnitTests.test_case1['target_token'], "token1")
            self.assertTrue(iob_slot1 == UnitTests.test_case1['target_iob_slot'], "iob_slot1")
            self.assertTrue(iobs_slot1 == UnitTests.test_case1['target_iobs_slot'], "iobs_slot1")
            self.assertTrue(bmes_slot1 == UnitTests.test_case1['target_bmes_slot'], "bmes_slot1")
            self.assertTrue(span_slot1 == UnitTests.test_case1['target_span_slot'], "span_slot1")

            token2, iob_slot2 = sc.convert(UnitTests.test_case2['text'], UnitTests.test_case2['slots'], fmt='IOB')
            token2, iobs_slot2 = sc.convert(UnitTests.test_case2['text'], UnitTests.test_case2['slots'], fmt='IOBS')
            token2, bmes_slot2 = sc.convert(UnitTests.test_case2['text'], UnitTests.test_case2['slots'], fmt='BMES')
            token2, span_slot2 = sc.convert(UnitTests.test_case2['text'], UnitTests.test_case2['slots'], fmt='SPAN')
            self.assertTrue(token2 == UnitTests.test_case2['target_token'], "token2")
            self.assertTrue(iob_slot2 == UnitTests.test_case2['target_iob_slot'], "iob_slot2")
            self.assertTrue(iobs_slot2 == UnitTests.test_case2['target_iobs_slot'], "iobs_slot2")
            self.assertTrue(bmes_slot2 == UnitTests.test_case2['target_bmes_slot'], "bmes_slot2")
            self.assertTrue(span_slot2 == UnitTests.test_case2['target_span_slot'], "span_slot2")

        elif six.PY2:
            token1, iob_slot1 = sc.convert(UnitTests.test_case1['text'], UnitTests.test_case1['slots'], fmt='IOB')
            token1, iobs_slot1 = sc.convert(UnitTests.test_case1['text'], UnitTests.test_case1['slots'], fmt='IOBS')
            token1, bmes_slot1 = sc.convert(UnitTests.test_case1['text'], UnitTests.test_case1['slots'], fmt='BMES')
            token1, span_slot1 = sc.convert(UnitTests.test_case1['text'], UnitTests.test_case1['slots'], fmt='SPAN')

            self.assertTrue(token1 == UnitTests.test_case1['target_token'], "token1")
            self.assertTrue(iob_slot1 == UnitTests.test_case1['target_iob_slot'], "iob_slot1")
            self.assertTrue(iobs_slot1 == UnitTests.test_case1['target_iobs_slot'], "iobs_slot1")
            self.assertTrue(bmes_slot1 == UnitTests.test_case1['target_bmes_slot'], "bmes_slot1")
            self.assertTrue(span_slot1 == UnitTests.test_case1['target_span_slot'], "span_slot1")

            token2, iob_slot2 = sc.convert(UnitTests.test_case2['text'], UnitTests.test_case2['slots'], fmt='IOB')
            token2, iobs_slot2 = sc.convert(UnitTests.test_case2['text'], UnitTests.test_case2['slots'], fmt='IOBS')
            token2, bmes_slot2 = sc.convert(UnitTests.test_case2['text'], UnitTests.test_case2['slots'], fmt='BMES')
            token2, span_slot2 = sc.convert(UnitTests.test_case2['text'], UnitTests.test_case2['slots'], fmt='SPAN')
            self.assertTrue(token2 == UnitTests.test_case2['target_token'], "token2")
            self.assertTrue(iob_slot2 == UnitTests.test_case2['target_iob_slot'], "iob_slot2")
            self.assertTrue(iobs_slot2 == UnitTests.test_case2['target_iobs_slot'], "iobs_slot2")
            self.assertTrue(bmes_slot2 == UnitTests.test_case2['target_bmes_slot'], "bmes_slot2")
            self.assertTrue(span_slot2 == UnitTests.test_case2['target_span_slot'], "span_slot2")


if __name__ == '__main__':
    unittest.main()
