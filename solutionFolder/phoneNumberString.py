class SolutionforDigits():
	def __init__(self,digits):
		self.digits = digits;
		self.spliter = None;
		self.ArrayContainer = []
		self.finalList = []
		self.abc = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

	def split(self,word):
		return [char for char in word]

	def checkForPosibleInputsErrors(self):
		if(self.digits  == "" or self.digits == 1):
			return []
		else:
			self.makeSpliterIfNeeded()

	def makeSpliterIfNeeded(self):
		if(len(self.digits) > 1):
			self.spliter = self.split(self.digits)
			self.GetlettersForSolution()
		else:
			# return content for single number
			self.finalList = self.split(self.abc[int(self.digits) - 2])

	def GetlettersForSolution(self):
		for x in range(len(self.spliter)):
			self.ArrayContainer.append(self.split(self.abc[int(self.spliter[x]) - 2]))
		self.finalStepMakeArrayWithAllPosibleCombinations()

	def finalStepMakeArrayWithAllPosibleCombinations(self):
		for x in self.ArrayContainer[0]:
			for y in self.ArrayContainer[1]:
				self.finalList.append(x+y)
			
	def showFinalData(self):
		print(self.finalList)


done = SolutionforDigits("2")
done.checkForPosibleInputsErrors()
done.showFinalData()

