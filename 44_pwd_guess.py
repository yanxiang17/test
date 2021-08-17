# 密碼重試程式

pwd = 'a123456'
i = 3 # 儲存機會
while i > 0:
	guess = input('請輸入密碼: ')
	if guess == pwd:
		print('登入成功!')
		break
	else:
		i -= 1
		print('密碼錯誤, 還有', i, '次機會')