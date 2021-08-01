import copy

class Solution:
	def __init__(self,AccountInfo):
		self.AccountInfo =  AccountInfo;
		self.cleanData =  copy.copy(AccountInfo)
		self.finalContent = None;
		self.once = 0;

	def startResearch(self):
		for x in self.AccountInfo:
			for z in self.AccountInfo:
				if x == z:
					self.checkforEmailOne(x);
				else:
					return False;

	def checkforEmailOne(self,content):
		for x in self.AccountInfo:
			if x[1] == content[1]:
				self.cleanData.remove(x)
				self.lastCheck(x)

	def lastCheck(self,content):
		for x in self.AccountInfo:
			try:
				if x[2] != content[2]:
					if(self.once == 0):
						self.finalContent = x;
						self.finalContent.append(content[2])
						self.once = 1;	
			except:
				return False;

	def reFormatContent(self):
		self.cleanData.insert(0,self.finalContent)


	def showContent(self):
		for x in self.cleanData:
			print(x)



done = Solution([["John","johnsmith@mail.com","john_newyork@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"],["John","johnsmith@mail.com","john00@mail.com"]])
done.startResearch()
done.reFormatContent()
done.showContent()