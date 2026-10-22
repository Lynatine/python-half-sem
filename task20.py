import re
text = """
Встречи состоятся 15.09.2067, 21.09.2067 и 03.10.2067.
Следующая встреча запланирована на 1.11.2026.
"""

dates = re.findall(r"\b\d{1,2}\.\d{2}\.\d{4}\b", text)

for date in dates:
    print(date)
