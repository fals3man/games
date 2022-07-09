import random

class Shape(object):
	shapeNone=0
	shapeI=1
	shapeL=2
	shapeJ=3
	shapeT=4
	shapeO=5
	shapeS=6
	shapeZ=7

	ShapeCoord=(
		((0,0),(0,0),(0,0),(0,0)),
		((0,-1),(0,0),(0,1),(0,2)),
		((0,-1),(0,0),(0,1),(1,1)),
		((0,-1),(0,0),(0,1),(-1,1)),
		((0,-1),(0,0),(0,1),(1,0)),
		((0,0),(0,-1),(1,0),(1,-1)),
		((0,0),(0,-1),(-1,0),(1,-1)),
		((0,0),(0,-1),(1,0),(-1,-1))
	)

	def __init__(self,shape=0):
		self.shape=shape

	def RotateOffsets(self,direction):
		tempCoord=Shape.ShapeCoord[self.shape]
		if (direction==0 or self.shape==Shape.shapeO):
			return((x,y) for x,y in tempCoord)

		if direction==1:
			return((-y,x) for x,y in tempCoord)

		if direction==2:
			if self.shape in (Shape.shapeI, Shape.shapeZ, Shape.shapeS):
				return((x,y) for x,y in tempCoord)
			else:
				return((-x,-y) for x,y in tempCoord)

		if direction==3:
			if self.shape in (Shape.shapeI, Shape.shapeZ, Shape.shapeS):
				return((-y,x) for x,y in tempCoord)
			else:
				return((y,-x) for x,y in tempCoord)

	def getCoord(self,direction,x,y):
		return ((x+x1,y+y1) for x1,y1 in self.RotateOffsets(direction))

	def BoundingOffsets(self,direction):
		tempCoord=self.RotateOffsets(direction)
		minX,maxX,minY,maxY=0,0,0,0
		for x,y in tempCoord:
			if minX > x:
				minX = x
			if maxX < x:
				maxX = x
			if minY > y:
				minY = y
			if maxY < y:
				maxY = y
		return (minX,maxX,minY,maxY)

class BoardData(object):
	width=10
	height=22

	def __init__(self):
		self.backBoard=[0] * BoardData.width * BoardData.height
		self.currDir=0
		self.currX=-1
		self.currY=-1
		self.currShape=Shape()
		self.nextShape=Shape(random.randint(1,7))
		self.stat=[0]*8

	def getData(self):
		return self.backBoard[:]

	def getVal(self,x,y):
		return self.backBoard[x+y* BoardData.width]

	def getCurrShapeCoord(self):
		return self.currShape.getCoord(self.currDir,self.currX,self.currY)

	def createNew(self):
		minX,maxX,minY,maxY=self.nextShape.BoundingOffsets(0)
		res=False
		if self.tryMoveCurr(0,5,-minY):
			self.currX=5
			self.currY=-minY
			self.currDir=0
			self.currShape=self.nextShape
			self.nextShape=Shape(random.randint(1,7))
			res=True
		else:
			self.currDir=0
			self.currX=-1
			self.currY=-1
			self.currShape=Shape()
			res=False
		self.stat[self.currShape.shape] +=1
		return res

	def tryMoveCurr(self,direction,x,y):
		return self.tryMove(self.currShape,direction,x,y)

	def tryMove(self,shape,direction,x,y):
		for x,y in shape.getCoord(direction,x,y):
			if x>=BoardData.width or x<0 or y>=BoardData.height or y<0:
				return False
			if self.backBoard[x+y*BoardData.width]>0:
				return False
		return True

	def moveDown(self):
		l=0
		if self.tryMoveCurr(self.currDir,self.currX,self.currY+1):
			self.currY+=1
		else:
			self.mergePiece()
			l=self.removeFullLines()	
			self.createNew()
		return l

	def drop(self):
		while self.tryMoveCurr(self.currDir,self.currX,self.currY+1):
			self.currY+=1
		self.mergePiece()
		l=self.removeFullLines()	
		self.createNew()
		return l

	def moveRight(self):
		if self.tryMoveCurr(self.currDir,self.currX+1,self.currY):
			self.currX+=1

	def moveLeft(self):
		if self.tryMoveCurr(self.currDir,self.currX-1,self.currY):
			self.currX-=1

	def rotateRight(self):
		if self.tryMoveCurr((self.currDir+1)%4,self.currX,self.currY):
			self.currDir=(self.currDir+1)%4

	def rotateLeft(self):
		if self.tryMoveCurr((self.currDir-1)%4,self.currX,self.currY):
			self.currDir=(self.currDir-1)%4	

	def mergePiece(self):
		for x,y in self.currShape.getCoord(self.currDir,self.currX,self.currY):
			self.backBoard[x+y*BoardData.width]=self.currShape.shape
		self.currDir=0
		self.currX=-1
		self.currY=-1
		self.currShape=Shape()

	def removeFullLines(self):
		newBoard= [0] * BoardData.width *BoardData.height
		tmpY=BoardData.height-1
		l=0
		for y in range(BoardData.height-1,-1,-1):
			blockCnt=sum([1 if self.backBoard[x + y * BoardData.width] > 0 else 0 for x in range(BoardData.width)])
			if blockCnt<BoardData.width:
				for x in range(BoardData.width):
					newBoard[x+tmpY*BoardData.width]=self.backBoard[x+y*BoardData.width]
				tmpY-=1
			else:
				l+=1
		if (l>0):
			self.backBoard=newBoard
		return l
		
	def clr(self):
		self.currDir=0
		self.currX=-1
		self.currY=-1
		self.currShape=Shape()
		self.backBoard=[0]*BoardData.width*BoardData.height

BOARD_DATA=BoardData()		







