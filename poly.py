class polygon:
	def getside(self,a,b):
		self.side1=a
		self.side2=b
	def rarea(self):
		self.area=self.side1*self.side2
		print("area of rectangle=",self.area)
	def rperi(self):
		self.peri=(2*(self.side1+self.side2))
		print("perimeter of rectangle=",self.peri)
	def getc(self,r):
		self.rad=r
	def carea(self):
		self.clarea=3.14*self.rad*self.rad
		print("area of circle=",self.clarea)
	def cperi(self):
		self.clperi=2*3.14*self.rad
		print("perimeter of circle=",self.peri)
	def gets(self,s):
		self.side=s
	def sqarea(self):
		self.sarea=self.side*self.side
		print("area of square=",self.sarea)
	def sqperi(self):
		self.speri=4*self.side
		print("perimeter of square=",self.speri)
p=polygon()
s1=int(input("enter the side1="))
s2=int(input("enter the side2="))
p.getside(s1,s2)
p.rarea()
p.rperi()
r1=int(input("enter the radius="))
p.getc(r1)
p.carea()
p.cperi()
q=int(input("enter the side of square="))
p.gets(q)
p.sqarea()
p.sqperi()
