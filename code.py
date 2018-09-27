class Coba():
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.arg = arg

	def wkwk(self):
		print("Ko gitu", self.arg)


b = Coba('sih')
b.wkwk()

print("="*30)

nama = "Ersya Dharmawan"
umur = 20

print("Nama saya {} dan \numur saya {}".format(nama, umur))

print("="*30)

nomor = 1

while nomor < 10:
	a = 0
	while a < nomor:
		a += 1
		print("*", end=" ")
	print(" ")
	nomor += 1

print("="*30)

x = 1
y = 1

while (x <= 10):
	print ("--- Perkalian {} ---".format(x))
	while (y <= 10):
		print("{} X {} = {}".format(x,y, (x*y)))
		y += 1
	y = 1
	x += 1

print("="*30)

#while True:
#	s = input("masukkan nama: ")
#	if s == 'ersya':
#		print ("ok")
#		break
#	else:
#		print("salah")
#else:
#	print("Gak ok")

print("="*30)

x = "Django and Python"

def sayHello():
	global x
	print(x)

sayHello()

print("="*30)

x = "Python Function"

def sayHello(x):
	return(x)

print(sayHello(x))

print("="*30)

def sayHello(*arg1, **arg2):
	'''Cara menggunakan args dan kwargs'''
	print(arg1, arg2)

sayHello(1,2,3, nama='ersya')
print(sayHello.__doc__)

print("="*30)

lst = ['a', 'b', 'c', 'd', 'e']

for x in lst:
	print(x)

print("="*30)

tpl = ('cow', 'ant', 'elephant', 'deer')

print("I like animal {}".format(tpl[3][0:]))

print("="*30)

dct = {'nama': 'ersya', 'umur': 21, 'jurusan': 'TI'}

for i in dct:
	print(dct[i])

print("="*30)

st = set(['Pizza', 'Solaria', 'MCD', 'ChatTime'])

print (st)

st1 = st.copy()
st1.add("J\'CO")
print(st1)

print ('Ayam Go' in st1)

st2 = set(['1','2','3','4','5'])
st3 = set(['6','7','2','9','10'])

#Set intersection
print(st2 & st3)

#Set union
print(st2 | st3)

print("="*30)

# OOP
# Base Overloading Methods
# __init__ ( self [,args...] ) -> Constructor (with any optional arguments) -> Sample Call : obj = className(args)
# __del__( self ) -> Destructor, deletes an object -> Sample Call : del obj
# __repr__( self ) -> Evaluable string representation -> Sample Call : repr(obj)
# __str__( self ) -> Printable string representation -> Sample Call : str(obj)
# __cmp__ ( self, x ) -> Object comparison -> Sample Call : cmp(obj, x)

class Test:
	"""docstring for ClassName"""
	def __init__(self, nama, kelas):
		self.nama = nama
		self.kelas = kelas

	def intro(self):
		print("Nama saya {} dan kelas {}".format(self.nama, self.kelas))

class Test1(Test):
	"""docstring for Inheritance ClassName"""
	def __init__(self, nama, kelas, jurusan):
		Test.__init__(self, nama, kelas)
		self.jurusan = jurusan

	def intro1(self):
		print("Nama saya {}, kelas {} dan jurusan {}".format(self.nama, self.kelas, self.jurusan))
		

x = Test("Ersya", "3IA16")
x.intro()

print("="*30)

x = Test1("Dharmawan", "3IA16", "TI")
x.intro1()

print("="*30)

#normal statements to access attributes
#hasattr(emp1, 'age')    > Returns true if 'age' attribute exists
#getattr(emp1, 'age')    > Returns value of 'age' attribute
#setattr(emp1, 'age', 8) > Set attribute 'age' at 8
#delattr(empl, 'age')    > Delete attribute 'age'

print(hasattr(x, 'nama'))
print(getattr(x, 'nama'))

# Built in class atrributes
#__dict__ − Dictionary containing the class's namespace.
#__doc__ − Class documentation string or none, if undefined.
#__name__ − Class name.
#__module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.
#__bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

print("="*30)

print(Test.__dict__)
print(Test.__doc__)
print(Test.__name__)
print(Test.__module__)
print(Test.__bases__)

print("="*30)

class Persegi:
	"""Rumus untuk menghitung luas pada persegi"""
	def setLuas(self, s1, s2):
		self.s1 = s1
		self.s2 = s2

	def getLuas(self):
		print("Hasilnya adalah {}".format(self.s1 * self.s2))

coba = Persegi()
coba.setLuas(4, 5)
coba.getLuas()

print(Persegi.__doc__)


print("="*30)

# open file
# operasi file
'''	
r = Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
rb = Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
r+ = Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
rb+ = Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
w = Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
wb = Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
w+ = Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
wb+ = Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
a = Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
ab = Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
a+ = Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
ab+ = Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
'''
fileHandle = open("try.txt", "w")

txt = "Hello World"
fileHandle.write(txt)
