def TripleStepHelper(curPos, maxPos):
	if curPos == maxPos:
		return 1
	if curPos > maxPos:
		return 0
	return TripleStepHelper(curPos + 1, maxPos) + TripleStepHelper(curPos + 2, maxPos) + TripleStepHelper(curPos + 3, maxPos)

def TripleStep(n):
	return TripleStepHelper(0, n)


def TripleStep_ThieuKhang(n):
	waysToStepLst = [0] * (n + 1)
	waysToStepLst[0] = 1
	waysToStepLst[1] = 1
	waysToStepLst[2] = 2

	for i in range(3, n + 1):
		waysToStepLst[i] = waysToStepLst[i - 1] + waysToStepLst[i - 2] + waysToStepLst[i - 3]

	print(waysToStepLst)
	return waysToStepLst[-1]


def RobotInGridHelper(curX, curY, maxX, maxY, offLimitLst):
	if curX == maxX and curY == maxY:
		return 1
	if (curX, curY) in offLimitLst:
		return 0
	if curX > maxX or curY > maxY:
		return 0

	return RobotInGridHelper(curX + 1, curY, maxX, maxY, offLimitLst) + RobotInGridHelper(curX + 1, curY + 1, maxX, maxY, offLimitLst) + RobotInGridHelper(curX, curY + 1, maxX, maxY, offLimitLst)

def RobotInGrid(maxX, maxY, offLimitLst):
	return RobotInGridHelper(0, 0, maxX, maxY, offLimitLst)



if __name__ == '__main__':
	pass
