
'''
	[문제]
    총 3과목의 시험을 보았다.
    국어는 84 점 수학 23점 과학은 53 점을 받았다.
    평균을 구하시오. 
    소수점 두자리까지 구하시오. 
    
	[정답] 
    53.3

'''
kor = 84;
math = 23;
science = 53;

total = kor + math + science;

avg = total / 3;

print("total = ", total)
print("avg = ", round(avg, 2))