'''
 	[문제]
		철수네 반 학생은 31명이다.
		이 중에서 남학생은 3명, 
		여학생은 남학생의 3배의 학생이 봉사활동을 하였다.
		철수네 반에서 봉사활동을 하지 않은 학생과 
		봉사활동 한 학생의 차이는 얼마인지 구하시오.
	    
	[정답] 
		7
'''

unit = 31
male = 3
female = male * 3 #9

volunteer = male + female # 12
unvolunteer = unit - volunteer

difference = unvolunteer - volunteer
print("rs = ", difference)