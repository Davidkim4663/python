'''
	[문제] 
	    한번에 500kg까지 운반할 수 있는 승강기가 있다.
	    몸무게가 70kg인 배달원이 이 승강기를 타고 
	    하나의 무게가 30kg인 상자를 운반하려고 할 때,
	    한 번에 최대 몇 상자까지 운반할 수 있는지 알아보자.
	    
	[정답]
		14
  
  maxWeight = 500
  deliveryManWeight = 70
  boxWeight = 30

  useWeight = maxWeight - deliveryManWeight == 430
  maxCnt = useWeight // boxWeight  
'''
maxWeight = 500
deliveryManWeight = 70
boxWeight = 30

print("승강기 중량 = ", maxWeight)
print("배달원 무게 = ", deliveryManWeight)
print("상자 하나 당 무게 = ", boxWeight)

useWeight = maxWeight - deliveryManWeight
maxCnt = useWeight // boxWeight

print("실제 적재중량 = ", useWeight)
print("최대 몇 상자까지? ",maxCnt)