import re

text = "Это   строка    с     большим    количеством   пробелов."
text2 = "   Текст   с   пробелами   "

text = re.sub(r" {2,}", " ", text)
text2 = re.sub(r" {2,}", " ", text2).strip()
print(text)
print(text2)
