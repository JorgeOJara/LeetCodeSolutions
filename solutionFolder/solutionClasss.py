class Solution:
	def __init__(self,CompleteList,target):
		self.CompleteList = CompleteList;
		self.target = target;
		self.finalDEAL = []
		self.indexValues = []

		#count if values its found
		self.counter = 0;


	def findSumsofTarget(self):
		for x in self.CompleteList:
			for y in range(len(self.CompleteList)):
				if(x + self.CompleteList[y] == self.target and self.counter == 0):
					#if values are same to target try to collect....
					if(self.CompleteList.index(x) != self.CompleteList.index(self.CompleteList[y])):
						#if values are in the same index on array ignore....false positive
						self.finalDEAL.append(x)
						self.finalDEAL.append(self.CompleteList[y])
						self.indexFinder(x,self.CompleteList[y])
						self.counter = 1;

	def indexFinder(self,one,two):
		self.indexValues.append(self.CompleteList.index(one))
		self.indexValues.append(self.CompleteList.index(two))



	def showFinalANswer(self):
		print(self.finalDEAL)


	def showIndexOfContent(self):
		print(self.indexValues)


#variables
nums = [2,7,11,15];
#nums  = [3,2,4]

target  = 9;
#target = 6;

done = Solution(nums,target)
done.findSumsofTarget()
done.showFinalANswer()
done.showIndexOfContent()