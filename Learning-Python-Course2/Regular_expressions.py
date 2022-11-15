text = "the agent's phone number is 408-555-1234. Call soon"
"phone" in text
import re
pattern = "phone"
print(re.search(pattern, text))
pattern = "not on text"
re.search(pattern, text)
pattern = "phone"
match = re.search(pattern, text)
print(match)
print(match.span())
print(match.start())
print(match.end())
text = "my phone once, my phone twice"
match= re.search("phone", text)
print(match)
matches = re.findall("phone", text)
print(matches)
print(len(matches))

for match in re.finditer("phone", text):
    print(match.span())

text = "My phone number is 408-555-7777"
phone = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", text)
print(phone.group())
