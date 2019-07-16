#txt內容統計

# 讀取檔案
def read_file(filename):
	chatData = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # utf-8-sig能消除記憶體讀取txt時的隱藏編碼
		for line in f:
			# print(line)
			chatData.append(line.strip())
	return chatData
# 改寫格式
def chatFormat(chatData ,user_name_1, user_name_2):
	refactorData = []
	user_1_word_count = 0
	user_1_sticker_count = 0
	user_1_image_count = 0
	user_2_word_count = 0
	user_2_sticker_count = 0
	user_2_image_count = 0

	for line in chatData:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		content = s[2:]
		total = 0

		if name == user_name_1:
			if s[2] == '貼圖':
				user_1_sticker_count += 1
			elif s[2] == '圖片':
				user_1_image_count += 1
			else:
				for c in content:
					user_1_word_count += len(c)
		elif name == user_name_2:
			if s[2] == '貼圖':
				user_2_sticker_count += 1
			elif s[2] == '圖片':
				user_2_image_count += 1
			else:
				for c in content:
					user_2_word_count += len(c)

	total = user_1_word_count + user_2_word_count

	refactorData.append(user_1_word_count)
	refactorData.append(user_1_sticker_count)
	refactorData.append(user_1_image_count)
	refactorData.append(user_2_word_count)
	refactorData.append(user_2_sticker_count)
	refactorData.append(user_2_image_count)
	refactorData.append(total)

	print(refactorData)

	return refactorData

# 寫入檔案
def write_file(filename, refactorData):
	with open(filename, 'w', encoding = 'utf-8') as f:

		user_1_word_count = str(refactorData[0])
		user_1_sticker_count = str(refactorData[1])
		user_1_image_count = str(refactorData[2])
		user_2_word_count = str(refactorData[3])
		user_2_sticker_count = str(refactorData[4])
		user_2_image_count = str(refactorData[5])
		total = str(refactorData[6])

		msg = 'user1總共輸入了：\n' + user_1_word_count + '個字\n' + user_1_sticker_count + '張貼圖\n' + user_1_image_count + '張圖片\n' + 'user2總共輸入了：\n' + user_2_word_count + '個字\n' + user_2_sticker_count + '張貼圖\n' + user_2_image_count + '張圖片\n' + '總共輸入了：' + total + '個字'

		f.write(msg)

		# print('使用者1總共輸入了：' , refactorData[0] , '個字\n'
		# '使用了：' , refactorData[1] , '個貼圖\n'
		# '使用了：' , refactorData[2] , '個圖片\n'
		# '使用者2總共輸入了：' , refactorData[3] , '個字\n'
		# '使用了：' , refactorData[4] , '個貼圖\n'
		# '使用了：' , refactorData[5] , '個圖片\n'
		# '兩人總共輸入了：' , refactorData[6], '個字')

	print('檔案改寫成功')

# 執行內容
def main():
	chatData = read_file('LINE_Viki.txt')
	refactorData = chatFormat(chatData, 'Allen', 'Viki')
	write_file('output.txt', refactorData)

main()