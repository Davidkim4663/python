'''
	[문제]  
		철수는 용돈 기입장을 작성하고 있다. 
		저번 달까지 총 600원을 저축했고,
		이번 달 용돈으로 1000원을 받았다. 
		오늘 과자를 3개 사 먹었더니 현재 남은 돈은 100원이라고 할 때,
		과자 1개의 가격은 얼마인지 구하시오.  
		
	[정답] 
        500	
        
    저축한 금액 = 600
    이번 달 용돈 = 1000
    총 금액 = 1000 + 600 = 1600
    
    현재 남은 잔돈 = 100
    과자 3개의 가격 = (1600 - 100)
    과자 1개의 가격 (1600 - 100) //3    
        
        
'''

lastMonth = 600
thisMonth = 1000

saveMoney = lastMonth + thisMonth
print("얼마있니? ", saveMoney)


curMoney = 100

snack_3_price = saveMoney - curMoney
print("과자 3개의 가격 ", snack_3_price)

snack_1_price = snack_3_price // 3 
print("과자 1개의 가격 ", snack_1_price)

