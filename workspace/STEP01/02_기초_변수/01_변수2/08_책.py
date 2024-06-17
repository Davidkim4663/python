'''		
	[문제]
        책이 총 78page이다. 
        [1] 철수는 책을 64page 읽었다. 몇 퍼센트 읽은 것인가?	
            소수점 두 자리까지 구하시오.		
        [2] 철수는 책을 30퍼센트 읽었다. 현재 페이지는 몇인가?		
    [정답]
        [1] 82.05
        [2] 23.4
        
       78p : 100% = 64p : n%
       6400 = 78n
       n = 82.0%
       
       78p : 100% = np : 30%
       100n = 2,340
       n = 23.4페이지
        
'''
total_page = 78
cur_page = 30
cur_per = 64
percent = 100

# 1
rs_percent = round((cur_per * percent) / total_page, 2)
print("현재 퍼센트 = ",rs_percent,"%")

#2
rs_page = round((total_page * cur_page) / percent, 2)
print("현재 페이지 = ", rs_page,"페이지")