msg = []

with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		# print(line.strip())
		msg.append(line.strip().split(' '))

print(msg)

for line in msg:
	time = line[0][:5]
	name = line[0][5:]
	print(name)