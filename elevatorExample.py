def goUpfloor(current, target):
	floorList = list(range(current, target+1,1))
	for floor in floorList:
		print("현재 층은 ", floor, "입니다.")
		if(floor == target):
			print(floor, " 층에 도착하였습니다. 안녕히 가세요.")

def goDownfloor(current, target):
	floorList = list(range(target, current+1))
	floorList = list(reversed(floorList))
	for floor in floorList:
		print("현재 층은 ", floor," 입니다.")
		if(floor == target):
			print(floor, " 층에 도착하였습니다. 안녕히 가세요.")

currentFloor = 1

while True:
	targetFloor = int(input('가고자하는 층을 입력하세요(운행정지는 -100을 입력): '))
	if targetFloor == -100:
		break
	elif targetFloor == currentFloor:
		print("다른 층을 눌러주세요.")
	else:
		if targetFloor >= currentFloor:
			goUpfloor(currentFloor, targetFloor)
			currentFloor = targetFloor
		else:
			goDownfloor(currentFloor, targetFloor)
			currentFloor = targetFloor