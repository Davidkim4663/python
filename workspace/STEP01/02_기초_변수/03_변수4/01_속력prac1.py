'''
	[ 속력 문제 ]		
		[1] 철수는 시속 3km 의 속도로 37분간 걸어갔다. 
			철수가 간거리는 몇km 인가?
			철수가 간거리는 몇m 인가?

			60분 : 3km = 37분 : nkm
			60 x n = 3 x 37
			n = 3km x 37 / 60 
			n = 3000m x 37 / 60
   
			    
            60분 : 3000m = 37분 : nkm
            60n =  111,000
            n = 
       
       
       
		[2] 철수는 870미터를 40분간 걸어갔다. 
			철수의 시속은 얼마인가?
			철수의 분속은 얼마인가?

			40분 / 60 : 870m = 1시간 : nM
			n x (40 / 60) = 870 x 1
			n = 870 / (40 / 60)
			n = 870 / 40
'''
표준시간 = 60 #60분
_km = 3
_m = _km * 1000
이동시간 = 37

이동거리_km = round(이동시간 * _km / 표준시간, 2)
print("철수 이동거리 km = ", 이동거리_km,"km")

이동거리_m = round(이동시간 * _m / 표준시간, 2)
print("철수 이동거리 m = ", 이동거리_m,"m")