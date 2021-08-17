# bmi顯示器

wgt = input('請輸入你的體重(公斤): ')
hgt = input('請輸入你的身高(公分): ')
wgt = float(wgt)
hgt = float(hgt)/100
bmi = wgt/hgt**2
if bmi < 18.5:
	print('體重過輕')
elif bmi >=18.5 and bmi < 24:
	print('體重正常')
elif bmi >= 24 and bmi < 27:
	print('體重過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
elif bmi >= 35:
	print('重度肥胖')