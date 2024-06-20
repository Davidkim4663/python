'''
	[문제]
		철수는 친구의 생일 선물로 가격이 4000원인 필통 1개와 
		가격이 700원인 공책 몇 권을 사려고 한다. 
		철수는 13000원을 가지고 있을 때,
		공책은 최대한 몇 권을 살 수 있을지 구하시오.
		공책을 최대로 구입한 후 나머지 금액도 출력하시오.
		
	[정답] 
		12
    600
    
    cash = 14000원
    pencilCase = 4000원
    book = 700
    
    가용금액 = cash - pencilCase = 10000
    max = 10000 // 700
    restMoney = 10000 % 700 
    
'''
cash = 13000
pencilCase = 4000
book = 700

print("현금 = ", cash,"원")
print("필통 = ", pencilCase,"원")
print("공책 = ", book,"원")

useMoney = cash - pencilCase #10000
max = useMoney // book 
restMoney = useMoney % book

print()
print("가용금액 =", useMoney,"개")
print("최대 ", max,"개 구입 할 수 있다.")
print("남은금액 = ",restMoney)