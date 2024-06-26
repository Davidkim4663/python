'''
	[문제]
		철수는 집에서 학교까지 버스를 타고 다닌다.
		철수의 버스비는 1200원이다. 
  
		철수는 학교가 끝나면 바로 학원에 간다.
	
 	학원에 갈 때는 지하철을 이용한다.
		지하철 요금은 1100원이다.
  
		철수가 학원에서 집으로 바로 올 때는 1300원의 차비가 든다.
		철수가 학교에서 집으로 바로 올 때는 1200원의 차비가 든다.
츠
		학교는 월화수목금 매일 다닌다.
		학원은 월수금에만 다닌다.
		이번 달에 철수는 4주 동안 학교와 학원에 다녔다.
		이번 달 필요한 총차비를 구하시오.
		
	[정답] 
		62400

	====================
    버스요금 -> 1200원 (학교 갈 때)
		지하철 요금 -> 1100원 (학원 갈 때)
    학원 -> 집 : 1300원 (지하철) 주 3일 (월, 수, 금)
    학교 -> 집 : 1200원 (버스) 주 5일(월 ~ 금) 
    
    학원 가는 날  총 3회 (1회 : 3600원) * 3 => 10,800원
      집 ->(버스 : 1200원) 학교 ->(1100원) 학원 ->(1300원) 집  3600원 (    

    학원 안 가는 날 총 2회 (1회 : 2400원) * 2 => 4800원
      집->(버스 : 1200원) 학교 ->(버스 : 1200원) 집 / 1회 : 2400원
      
    철수가 1주 동안 쓴 교통비 : 15,600원 
    철수가 4주 동안 쓴 교통비 : 15,600원  * 4 => 62,400원
    
'''
bus_fee = 1200
subway_free = 1100
학원_집 = 1300; # 
학교_집 = 1200; # 
print("버스 요금 : ", bus_fee)
print("지하철 요금 : ", subway_free)

이동경로1_요금 = 1300 # 지하철(학원 -> 집)
이동경로2_요금 = 1200 # 버스(학교 -> 집)

학원_가는날 = bus_fee + subway_free + 학원_집

#주 3회
_1주_학원 = 학원_가는날 * 3
print("학원 가는 날 3회 요금 ",_1주_학원,"원")

학원_안_가는_날 = bus_fee + 학교_집
print("학원_안_가는_날 1회 요금 = ", 학원_안_가는_날,"원")

#주1회_학원ㄴㄴ
_1주_노학원 = 학원_안_가는_날 * 2
print("학원 안 가는 날 2회 요금", _1주_노학원,"원")

#주 1회 교통비
_1stWeek = _1주_학원 + _1주_노학원
print("1주일 교통비",_1stWeek,"원")
  
_4thWeek = _1stWeek * 4
print("4주 교통비",_4thWeek,"원")
