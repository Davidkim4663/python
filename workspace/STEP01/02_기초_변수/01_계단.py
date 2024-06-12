'''
	[문제]
		철수와 영희는 가위바위보 게임을 하고 있다. 
		규칙은 아래와 같다.	
		
		이기면 계단을 3칸 올라간다.
		비기면 계단을 1칸 올라간다. 
    	지면   계단을 2칸 내려간다.
		
		철수는 4번 이기고, 2번 비기고, 3번 졌다.
		50번 계단에서 시작했을 때,
	 	철수는 몇 번째 계단에 있는지 구하시오.
	 	
	 [정답] 
        58
'''
win = 3
lose = 1
miss = 2

curPos = 50

cntWin = 4
cntLose = 2
cntMiss = 3

cur1 = win * cntWin # 12
cur2 = lose * cntLose # 2
cur3 = miss * cntMiss # 6

rs = (curPos + cur1 + cur2) - cur3
print("rs = ", rs)





