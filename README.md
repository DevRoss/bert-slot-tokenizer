# bert_slot_tokenizer

Version 0.3

![Travis (.org)](https://img.shields.io/travis/DevRoss/bert-slot-tokenizer) ![GitHub](https://img.shields.io/github/license/devross/bert-slot-tokenizer)

**bert_slot_tokenizer** 是一个将slot filling 任务中slot解析为其他格式的工具

## 环境：

- Python 3
- Python 2

## 安装：

```shell
pip install bert-slot-tokenizer
```

## 支持的格式：

- IOB格式
- IOBS格式
- BMES格式
- SPAN格式

## 使用方法：

```python
from bert_slot_tokenizer import SlotConverter
vocab_path = 'tests/test_data/example_vocab.txt' 
# you can find a example here --> https://github.com/DevRoss/bert-slot-tokenizer/blob/master/tests/test_data/example_vocab.txt
sc = SlotConverter(vocab_path, do_lower_case=True)
text = 'Too YOUNG, too simple, sometimes naive! 蛤蛤+1s蛤蛤蛤嗝'
slot = {'蛤蛤': 'name', '+1s': 'time', '嗝': '语气'}
output_text, iob_slot = sc.convert(text, slot, fmt='IOB')
output_text, iobs_slot = sc.convert(text, slot, fmt='IOBS')
output_text, bmes_slot = sc.convert(text, slot, fmt='BMES')
output_text, span_slot = sc.convert(text, slot, fmt='SPAN')
print(output_text)
# ['too', 'young', ',', 'too', 'simple', ',', 'some', '##times', 'na', '##ive', '!', '蛤', '蛤', '+', '1', '##s', '蛤', '蛤', '蛤', '嗝']

print(iob_slot)
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-name', 'I-name', 'B-time', 'I-time', 'I-time', 'B-name', 'I-name', 'O', 'B-语气']

print(iobs_slot)
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-name', 'I-name', 'B-time', 'I-time', 'I-time', 'B-name', 'I-name', 'O', 'S-语气']

print(bmes_slot)
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-name', 'E-name', 'B-time', 'M-time', 'E-time', 'B-name', 'E-name', 'O', 'S-语气']

print(span_slot)
# [[11, 12, 'name'], [13, 15, 'time'], [16, 17, 'name'], [19, 19, '语气']]
```

## 写在最后：

感谢BERT对NLP领域的推动

感谢开源

欢迎PR和issue

联系方式： devross1997@gmail.com