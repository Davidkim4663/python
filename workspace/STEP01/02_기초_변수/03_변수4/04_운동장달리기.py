'''
	[문제]  
	 	철수는 일정한 빠르기로 운동장을 25바퀴 도는데 
	 	1시간 15분 20초 걸렸습니다. 		 
	  	67바퀴를 도는 데 걸리는 시간을 초로 출력하시오.
	  	
	[정답] 
		12113.6
  
 25바퀴 : 4,520초 = 1바퀴 : n초
 25n = 4520
 n =  180초 (1바퀴)
 
'''

철수_이동횟수 = 25
철수_이동시간 = 4520 # 1시간 = 3600초, 15분 = 900초 , 20초
철수_1바퀴_소요시간 = 철수_이동시간 / 철수_이동횟수

print("철수_1바퀴_소요시간 = ", 철수_1바퀴_소요시간)

철수_67바퀴_소요시간 = 철수_1바퀴_소요시간 * 67
print("철수_67바퀴_소요시간 = ", 철수_67바퀴_소요시간)
