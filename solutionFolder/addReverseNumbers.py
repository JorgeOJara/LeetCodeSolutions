class ListNode:
	def __init__(self,listOne,listTwo):
		self.listOne =  listOne;
		self.listTwo = listTwo;
		self.finalValue = []

	def changeOrder(self,val):
		return [ele for ele in reversed(val)]

	def convert(self,content):
		fixContent = self.changeOrder(content)
		print(fixContent)
		s = [str(i) for i in fixContent]
		res = int("".join(s))
		return(res)

	def addContent(self):
		addedValues = self.convert(self.listOne) + self.convert(self.listTwo)
		self.finalValue = self.changeOrder([int(digit) for digit in str(addedValues)])

	def ShowFinalValues(self):
		print(self.finalValue)

l1 = [2,4,3]
l2 = [5,6,4]

done = ListNode(l1,l2)
done.addContent()
done.ShowFinalValues()


