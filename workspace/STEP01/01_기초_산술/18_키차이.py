'''
	[문제]
  		민수는 키가 184cm이고,
  		철수는 키가 165cm이고,
  		영희는 키가 160cm이다.
  		세학생의 키의 평균에서 키가 가장작은 학생의 차이를 구하시오.
  		수소점 두자리까지 구하시오.
		
	[정답] 
		9.67
'''

minsu_height = 184;
cheolsu_height = 165;
yeoughee_height = 160;

total = minsu_height + cheolsu_height + yeoughee_height
print("총합: " , total,"cm")

avg = round(total / 3, 2)
print("평균: " , avg,"cm")

heightDifference = round(avg - yeoughee_height, 2)
print("rs = ", heightDifference,"cm")