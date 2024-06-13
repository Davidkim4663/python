'''
	[문제] 
		철수와 영희는 50000원을 가지고 있다. 
		철수와 영희는 같이 영화 1편을 관람했다.
		간식은 팝콘 1개와 콜라 2개를 사 먹었다.
		아래 힌트를 참고하여 남은 돈은 얼마인지 구하시오. 
		[힌트] 
			(1) 콜라 1개는 팝콘 1개보다 4000원 싸다.
			(2) 영화 1편의 가격은 12000원이다.
			(3) 팝콘의 가격은 영화의 6/10 가격이다.  
			
	[정답]
		12400
  
  cash = 50000원
  movie = 12000원 (2인 -> 24000원)
  popcorn = 7200원
  coke = 3200원 (2인 -> 6400원)
  
'''
cash = 50000

movie_single = 12000
movie_couple = movie_single * 2

popcorn = (movie_single / 10) * 6 # 7200
coke = popcorn - 4000
coke_couple = coke * 2 # 6400

useMoney = movie_couple + popcorn + coke_couple
print("사용한 금액 = ", useMoney)

restMoney = cash - useMoney
print("잔돈 = ", restMoney)