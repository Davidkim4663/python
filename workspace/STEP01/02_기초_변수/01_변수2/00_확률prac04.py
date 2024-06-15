'''
	[문제4]
		인형 40개가있다. 인형1개는 몇퍼센트인지 구하시오.

    40개 : 100% = 1개 : n%
    40n = 100
    n = 100 / 40
    n = 2.5%    

'''		
doll = 40
percent = 100

rs = round(percent / doll, 1)
print(rs)