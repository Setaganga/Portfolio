#This is a very very simple regex for the email, considering that the emails are in the style of name@domain.whatever
from doctest import master
import re

phone = re.compile(r"\(?\d{3}\)?-?\d{3}-?\d{4}")
email = re.compile(r"\w+@\w+\.\w+")
matches = []

text = input()

for match in phone.findall(text):
    matches.append(f"{match}")

for match in email.findall(text):
    matches.append(f"{match}")

if len(matches) < 1:
    print("No matches found")
else:
    print(matches)
print(f"Found {len(matches)} matches in text\n")
for _ in range(len(matches)):
    print(f"{_ + 1}: {matches[_]}\n")