import sys

c = sys.stdin.read(1)

linecounter = 0
tokencounter = 0
charactercounter = 0



while c:
	
	if c == '\n':
		linecounter = linecounter+1
	elif c == " ":
		tokencounter = tokencounter+1
	else:
		charactercounter = charactercounter+1
	c = sys.stdin.read(1)

print(linecounter)
print(tokencounter)
print(charactercounter)
