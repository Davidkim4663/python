'''
	[문제] 
	철수네 반은 학생이 40명이다.
	철수, 영희, 민수는 반장선거에 나갔다.
	민수는 득표를 40%를 획득했고, 
	영희는 9표를 얻었다.
	나머지는 철수가 득표했다.
	철수의 득표수를 구하시오.
	
    [정답]
    15

철수네 반 = 40명
민수 득표 : 40% (16명)
영희 득표 : 9표
철수 득표 : 

40명 : 100% = n명 : 40%
100n = 1600
n = 16명

철수득표 = 철수네반 - (민수득표 + 영희득표 )
'''
all_student = 40
percent = 100
yeonghee = 9
print("영희 득표 수 = ",yeonghee)

minsu_vote_percent = 40
minsu_vote = (all_student * minsu_vote_percent) // percent
print("민수 득표 수 = ",minsu_vote)

cheolsu_vote = all_student-(minsu_vote + yeonghee)
print("철수 득표 수 = ", cheolsu_vote)