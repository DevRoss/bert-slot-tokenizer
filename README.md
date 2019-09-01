# bert_slot_tokenizer

Version 0.2

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

- [IOB格式](https://en.wikipedia.org/wiki/Inside–outside–beginning_(tagging))

## 使用方法：

```python
from bert_slot_tokenizer import SlotConverter
vacab_path = 'tests/test_data/example_vocab.txt' 
# you can find a example here --> https://github.com/DevRoss/bert-slot-tokenizer/blob/master/tests/test_data/example_vocab.txt
sc = SlotConverter(vocab_path, do_lower_case=True)
text = 'Too YOUNG, too simple, sometimes naive! 蛤蛤+1s'
slot = {'name': '蛤蛤', 'time': '+1s'}
output_text, iob_slot = sc.convert2iob(text, slot)
print(output_text)
# ['too', 'young', ',', 'too', 'simple', ',', 'some', '##times', 'na', '##ive', '!', '蛤', '蛤', '+', '1', '##s']
print(iob_slot)
# ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-name', 'I-name', 'B-time', 'I-time', 'I-time']
```

## 写在最后：

感谢BERT对NLP领域的推动

感谢开源

欢迎PR和issue

联系方式： devross1997@gmail.com