# Plagiarism Checker in Python for text 4 lines of code only

from difflib import SequenceMatcher
with open('mp3.txt') as f1, open('text.txt') as f2:
    matches = SequenceMatcher(None, f1.read(), f2.read()).ratio()
print(f"The plagiarized content is: {matches * 100}%")


