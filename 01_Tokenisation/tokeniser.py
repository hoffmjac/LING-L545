import sys, re


underscoremania = "\t_\t_\t_\t_\t_\t_\t_\t_"

abbr = ['etc.', 'e.g.', 'i.e.']

id = 0

line = sys.stdin.readline()
while line:
	id += 1
	print('# sent_id =', id)
	print("# text =", line[:-1])
	line = re.sub(r'([\(\)"?:!;])', r' \g<1> ', line)
	line = re.sub(r'([^0-9]),', r'\g<1> ,', line)
	line = re.sub(r',([^0-9])', r', \g<1>', line)
	line = re.sub(r'  +', ' ', line[:-1])

	line = line.split()


	count = 0
	for entry in line:
		if entry[-1] == '.' and entry not in abbr:
			count += 1
			a = str(count) + '\t' + entry[:-1] + underscoremania
			print(a)
			count += 1
			b = str(count) + '\t' + '.' + underscoremania
			print(b)
		else:
			count += 1
			entry = str(count) + "\t" + entry + underscoremania
			print(entry)
	print()
	line = sys.stdin.readline()


print(line)

