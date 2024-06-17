'''
	[문제]
 		철수네 반은 학생이 40명이다.
 	 	철수, 영희, 민수 이렇게 세 학생은 반장선거에 출마했다.
 	 	민수는 득표를 전체 중 40%를 획득했고, 
 	 	영희는 9표를 획득했다.
 	 	나머지는 철수가 득표했다.
 	 	철수의 전체 득표는 몇 퍼센트 인지 구하시오. 	
 	 	
    [정답] 
        37.50
        
    철수네반 = 40명
    민수 = 40% (16표)
    영희 = 9표 (22.5%)
    철수 = 15표
    
    40명 : 100% = 9명 : n%
    100n = 1600
    n = 16표
    
    철수득표 = 철수네반 - (민수 + 영희) 15표
   
    철수 득표 퍼센트 = 100 - (민수 득표율 + 철수 득표율)62.5
    37.5%

     
'''
total_stu = 40
minsu_vote_per = 40
percent = 100
youngHee_vote = 9

print("민수 득표율 = ", minsu_vote_per)

youngHee_vote_per = round((youngHee_vote * percent) / total_stu, 2)
print("영희 득표율 = ", youngHee_vote_per)

cheolsu_vote_per = 100 - (minsu_vote_per + youngHee_vote_per)
print("철수 득표율 = ",cheolsu_vote_per)
