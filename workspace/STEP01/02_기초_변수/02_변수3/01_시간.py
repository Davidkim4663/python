'''
 * 시간 테스트 
		1시간 = 60분 = 3600초(60분 * 60초)
		1분   = 60초
		1초

		[1]
<<<<<<< Updated upstream
		  4 000 초를 시간만 출력하시오.		  
		  4000 초를 시간을 제외하고 분만 출력하시오.
		  4000 초를 시간을 제외하고 초만 출력하시오.
		  
		  시간 = 4000 // 3600 = 1시간
		  분 = (4000 % 3600) // 60 = 6분
		  초 = 4000 % 60 = 40초
=======
		4000 초를 시간만 출력하시오.		  
		4000 초를 시간을 제외하고 분만 출력하시오.
		4000 초를 시간을 제외하고 초만 출력하시오.
	
		시간 = 4000 // 3600 = 1시간
		분 = (4000 % 3600) // 60 = 6분
		초 = 4000 % 60 = 40초
>>>>>>> Stashed changes

		[2]
		123123 초를 시간만 출력하시오.		  
		123123 초를 시간을 제외하고 분만 출력하시오.
		123123 초를 시간을 제외하고 초만 출력하시오.
'''

print("[문제1]")
print(4000 // 3600 , "시간")
print(4000 % 3600 // 60 , "분")
print(4000 % 60, "초")


print("[문제2]")
print(123123 // 3600 , "시간")
print(123123 % 3600 // 60 , "분")
print(123123 % 60, "초")