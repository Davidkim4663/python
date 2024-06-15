'''
  	[문제]
	철수는 놀이공원에 갔다. 
	놀이공원 입장료는 15000원이다.
	철수는 이런저런 할인을 받아서 9000원에 입장했다.
	몇 퍼센트 할인받은 것인지 구하시오.
	   
	[정답] 
		40
  
  입장료 = 15000원
  할인받은금액 = 9000원
  할인금액 = 입장료 - 할인받은금액(6000원)
  
  15000원 : 100% : 6000 : %n
  15000n = 600000
  n = 600000 / 15000
  n = 40%
  
  
'''
original_price = 15000
discount_price = 9000

print("입장료 = ", original_price)
print("할인받은금액 = ", discount_price)

real_price = original_price - discount_price
print()
print("할인금액 = ",real_price)

discount_rate = (real_price * 100) / original_price
print("할인율 = ",discount_rate)