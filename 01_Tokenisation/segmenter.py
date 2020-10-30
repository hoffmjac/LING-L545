import sys

text = sys.stdin.read()

text = text.replace('. ', '.\n')

text = text.replace('\n\n', '\n')

text = text[:-1]

print(text)

