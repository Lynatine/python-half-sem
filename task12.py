import re

def sol12(text):
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    unique_emails = []
    for email in emails:
        if email not in unique_emails:
            unique_emails.append(email)
    for email in unique_emails:
        print(email)

text = """Контакты:
aboba@example.com
baobab@test.org
abobik@example.com
abobus@company.ru"""

sol12(text)
