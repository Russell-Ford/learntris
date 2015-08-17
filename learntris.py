#I'm putting a comment at the top of this so I can learn how to github

gameState = 1

matrix = [[0 for x in range(10)] for x in range(22)] 

def clearMatrix():
	for row in range(0, 22):
		for column in range(0, 10):
			matrix[row][column] = "."
		
def printMatrix():
	for row in range(0, 22):
			for column in range(0, 9):
				print(matrix[row][column]),
			print(matrix[row][9])
			
clearMatrix()

while(gameState == 1):
	input = raw_input()
	if(input == "q"):
		gameState = 0
	elif(input == "p"):
		printMatrix()
	elif(input == "g"):
		for row in range(0, 22):
			line = raw_input()
			lineLength = len(line)
			x = 0
			while(x < lineLength):
				if(line[x] == " "):
					line = line[:x] + line[x+1:lineLength]
					lineLength -= 1
				else:
					x += 1
			for column in range(0, 10):
				matrix[row][column] = line[column]
	elif(input == "c"):
		clearMatrix()