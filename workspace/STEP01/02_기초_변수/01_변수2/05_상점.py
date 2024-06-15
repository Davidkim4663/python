'''
	[문제]
		상점에 과일이 250개가 있다. 
		그중에 오전에 84퍼센트가 팔렸고, 
        나머지 16퍼센트는 오후에 다 팔렸다.
		오전에 팔린개수 에서 오후에 팔린 개수의 차이는 
        얼마인지 구하시오.
		
	[정답]
		170
  
  [오전]
  250개 : 100% = n개 : 84%
  100n =  21,000
  n = 210개 (오전)

  [오후]  
  250개 : 100% = n개 : 16%
  100n = 4,000
  n = 40개 (오후)
  
  차이 = 210 - 40 = 170개
'''
total = 250
percent = 100
noon = 84
afternoon = 16

noonCnt = (total * noon) // percent
afternoonCnt = (total * afternoon) // percent
print("오전 = ",noonCnt,"개") 
print("오후 = ",afternoonCnt,"개")

# 오전에 팔린 개수와 오후에 팔린 개수
comparsion = noonCnt - afternoonCnt
print("판매량 차이 = ", comparsion,"개")