# 讀取檔案
def read_file(filename):
	chatData = []
	with open(filename, 'r') as f:
		for line in f:
			# print(line)
			chatData.append(line)
	return chatData
# 改寫格式
def chatFormat(chatData ,chater_name_1, chater_name_2):
	refactorData = []
	WhosTalking = None
	for line in chatData:
		if chater_name_1 in line:
			WhosTalking = chater_name_1
			continue
		elif chater_name_2 in line:
			WhosTalking = chater_name_2
			continue
		else:
			refactorData.append(WhosTalking + ': ' + line)
	return refactorData

# 寫入檔案
def write_file(filename, refactorData):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in refactorData:
			f.write(line)
	print('檔案改寫成功')

# 執行內容
def main():
	chatData = read_file('input.txt')
	refactorData = chatFormat(chatData, 'Allen', 'Tom')
	write_file('output.txt', refactorData)

main()