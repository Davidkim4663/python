'''
  	[문제]
  		과일 상점에 과일 250개가 있다. 
  		그중에 오전에 120개가 팔렸고 오후에는 80개가 팔렸다.
  		남은 과일은 전체 과일의 몇 퍼센트인지 구하시오.
  		
  	[정답] 
  		20
    
    전체 과일 수 = 250개
    오전 판매량 = 120개
    오후 판매량 = 80개
    
    전체 판매량 = 200개
    잔여량 = 50개
    
    
    250개 : 100% = 50개 : n%
    
    250n = 5000
    n = 20
    
'''
total = 250
noon = 120
afternoon = 80
percent = 100

print("전체 과일 수 = ", total,"\n")
print("오전 판매량 = ", noon,"\n")
print("오후 판매량 = ", afternoon,"\n")

total_sales = noon + afternoon
print("전체 판매량 = ", total_sales,"\n")

잔여량 = total - total_sales
print("잔여량 = ",잔여량,"\n")

잔여량_퍼센트 = percent * 잔여량 // total
print("남은 과일은 전체 과일의",잔여량_퍼센트,"% 입니다.") 