# 讀取檔案
def read_file(filename):
	chatData = []
	with open(filename, 'r') as f: # utf-8-s ig能消除記憶體讀取txt時的隱藏編碼
		for line in f:
			# print(line)
			chatData.append(line) #這裡我沒有添加.strip()來移除換行符號，之後添加進檔案就不用額外多寫\n
	return chatData
# 改寫格式
def chatFormat(chatData ,user_name_1, user_name_2):
	refactorData = []
	whosTalking = None
	for line in chatData:
		if user_name_1 in line:
			whosTalking = user_name_1
			continue
		elif user_name_2 in line:
			whosTalking = user_name_2
			continue
		else:
			refactorData.append(whosTalking + ': ' + line)
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