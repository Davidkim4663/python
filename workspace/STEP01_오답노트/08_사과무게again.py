'''

	[문제]
		사과 15개의 무게를 재었더니3kg 이었습니다. 	 	
        사과 3개 의 무게를 구하시오.
	 	소수점 두자리까지 구하시오.
	 	
	 [정답] 
	 0.6
  
  사과 15 개 = 3kg
  사과 3개 = n kg
  
  15개 : 3KG = 1개 : nKG
  15n = 3KG
15n / 15 = 3 / 15
n = 0.2

사과 1개 = 0.2 kg
사과 3개 = 사과 1개 * 3
  
  
'''

사과_15개_무게 = 3
사과_1개_무게 = 사과_15개_무게 / 15;

# 사과 1개 무게 
print(사과_1개_무게)

# 사과 3개 무게 
사과_3개_무게 = round(사과_1개_무게 * 3, 2);

print("사과 3개의 무게는 ", 사과_3개_무게,"g 입니다")

