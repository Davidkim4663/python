'''
	[문제2]
		인형 125개가있다. 인형1개는 몇퍼센트인지 구하시오.

    125개 : 100% = 1개 : n%
    
    125n = 100%
    n = 100 / 125
    
'''
doll = 125
percent = 100

rs = round(percent / doll, 2)
print(rs,"%")