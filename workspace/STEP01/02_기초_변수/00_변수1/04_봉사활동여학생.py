'''
	[문제]
    철수네 반 학생은 30명이다.
    남학생은 16명이다.
    이 중에서 남학생은 3명 , 
    여학생은 남학생의 3배의 학생이 봉사활동을 하였다.
    봉사활동을 하지 않은 여학생은 몇 명인지 구하시오.
    
[정답] 
    5
'''

unit = 30
male_stu = 16
female_stu = unit - male_stu

print(female_stu)

male_volunteer = 3
female_volunteer = male_volunteer * 3 # 9

female_non_volunteer = female_stu - female_volunteer # 5
print("봉사활동을 하지 않은 여학생은 몇 명인가 ", female_non_volunteer ,"명 입니다.") 