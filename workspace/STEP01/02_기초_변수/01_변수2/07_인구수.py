'''
	[문제] 
	  	어느 도시에 전체 인구가 400000명이다. 
	    그중 나이가 19세 이하 인구는 35%이다.
	    그리고 나이가 40세 이상 인구는 25%이다.	      
	 	위 도시의 19세 이하 인구에서 40세 이상 인구수를 뺀 인구수를 구하시오.		 
	[정답] 
		40000
  
  전체인구 : 400000명
  19세 이하 : 35%
  40세 이상 = 25%
  
  19세 이하 인구에서 40세 이상 인구수를 뺀 인구수 = 35% - 25% = 10%
  
  400000명 : 100% = n명 : 10%
  4000000 = 100n
  n = 40000명
  
'''
전체인구 = 400000
_19세이하 = 35
_40세이상 = 25
percentage = 100

# 19세 이하 인구에서 40세 이상 인구수를 뺀 인구수
인구수차이 = 35 - 25 #10%

rs = (전체인구 * 인구수차이) // percentage
print("rs = ", rs,"명") 