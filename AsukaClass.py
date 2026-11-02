from os import getlogin, system
from InquirerPy import inquirer


obj = None
obj1 = None


class Langley:
	NAME = "Asuka Langley"
	
	
class Asuka(Langley):
	__NAME = Langley.NAME[:5]
	__ORD = sum(ord(x) for x in __NAME)
	
			
	def __init__(self, string:str="a"):
		self.__name = str(self.__class__.__name__) + "_obj"
		self.__string = string
		self.__ord = sum(ord(x) for x in self.__string)
	
	@classmethod
	def __checkObj(cls, other):
		if not isinstance(other, (str, Asuka)):
			raise TypeError("Not expected type u fool")
		if isinstance(other, str):
			string = other
		
		else:
			string = other.__string
		
		return string
	
	
	@property
	def ord(self):
		return self.__ord
		
		
	@property
	def name(self):
		return self.__name
		
		
	@property
	def string(self):
		return self.__string
	
	@string.setter	
	def string(self, val):
		self.__string = val
	
	
	def __lt__(self, other):
		string = self.__checkObj(other)
		
		if len(string) == len(self.__string):
			self_ord = sum(ord(x) for x in self.__string)
			str_ord = sum(ord(x) for x in string)
			return True if abs(self_ord - self.__ORD) > abs(str_ord - self.__ORD) else False
			
		elif len(string) > len(self.__string):
			return True
		elif len(string) < len(self.__string):
			return False
	
	
	def __eq__(self, other):
		string = self.__checkObj(other)
		if len(string) != len(self.__string):
			return False
			#raise ValueError(f"These strings aren't equal, baka {getlogin()}")
		if len(string) == len(self.__string):
			self_ord = sum(ord(x) for x in self.__string)
			str_ord = sum(ord(x) for x in string)
		return True if abs(self_ord - self.__ORD) == abs(str_ord - self.__ORD) else False
	
	
	def __gt__(self, other):
		return not(self.__lt__(other))
		
		
	def __le__(self, other):
		raise TypeError("Anta baka?! Only strict inequalities are allowed! CHOOSE!!!1")
		
	
	def __ge__(self, other):
		return self.__le__(other)
	
	
	def __str__(self):
		return f"\nname: {self.__name}\nvalue: {self.__string}\nord: {self.__ord}\nclass: {self.__NAME}\n"
	
	
class Sorhyu():
	def __call__(self):
		choice = input("Sorhyu or Shikinami?: ").strip()
		
		match choice:
			case "Sorhyu":
				print("Good choice\n")
			case "Shikinami":
				raise ValueError(f"{getlogin()}, u r fuckin looser")
			case other:
				print(f"Wotta \"{other}\", dumb?! U can't write \"Sorhyu\"?! ")
				exit()
			

def calculate(expression:str = "0"):
	expression = expression.strip()
	if expression == "0":
		return 0
	for i in range(len(expression)):
		ord_e = ord(expression[i])
		
		if ord_e == 61 or ord_e == 33:
			math_symb_indx1 = i-1
			math_symb_indx2 = i
		elif ord_e == 60 or ord_e == 62:
			math_symb_indx1 = i
			math_symb_indx2 = i	
	global obj, obj1	
	obj = Asuka(expression[:math_symb_indx1].strip())
	math_symb = expression[math_symb_indx1:math_symb_indx2 + 1].strip()
	saveOn = input("Wanna save it, foolish?(yes/no)\n")
	match saveOn:
		case "yes":
			obj1 = Asuka(expression[math_symb_indx2+1:].strip())
		case "no" | "":
			obj1 = expression[math_symb_indx2+1:].strip()
		case other:
			raise ValueError(f"{other} isn't answer GOOONER")
	print()
	match math_symb:
		case "==":
			return "Strings are equal!!" if obj == obj1 else "Strings aren't equal.."
		case "!=":
			return "Strings aren't equal.." if obj != obj1 else "Strings aren't inequal!!"
		case ">":
			return f"{obj.string} is bigger than {obj1.string if isinstance(obj1, Asuka) else obj1}))" if obj > obj1 else f"{obj.string} isn't bigger than {obj1.string if isinstance(obj1, Asuka) else obj1}(("
		case "<":
			return f"{obj.string} is smaller than {obj1.string if isinstance(obj1, Asuka) else obj1}))" if obj < obj1 else f"{obj.string} isn't smaller than {obj1.string if isinstance(obj1, Asuka) else obj1}(("
		case ">=":
			return obj >= obj1
		case "<=":
			return obj <= obj1
		case _:
			return f"bad bad bad expression\nfuck u {getlogin()}!!!"
			exit()					
	
system("cls")
s = Sorhyu()
s()

while True:
	print("Commands(4 — my fav<3)")
	print("1 - Compare strings")
	print("2 - Show str info(name, ord, class, value n bla bla bla...)")
	print("3 - About rules of equations(for nerdss....)")
	print("4 - Exit<3<3<3(please!!)")
	cmd = input()
	match cmd:
		case "1":
			expres = input("\nEnter ur expression, idiot!!:\n")
			print(calculate(expres))
			input("\nPRESS <<ENTER>> STUPIDD")
			system("cls")
		case "2":
			if not isinstance(obj, (Asuka, str)) and not isinstance(obj1,(Asuka, str)):
				raise ValueError("strings not exists \nCOMPARE THE STRINGS FIRST STUPID")
			elif obj and isinstance(obj1, Asuka):
				# u_str = input(f"\nPick a damn string: \n{obj.string}\n{obj1.string if isinstance(obj1, Asuka) else obj1}\n")
				u_str = inquirer.select(message="\nPick a damn string:", choices=[obj.string, obj1.string if isinstance(obj1, Asuka) else obj1]).execute()
				match u_str:
					case obj.string:
						print(obj)
					case obj1.string:
						print(obj1)
					case other:
						raise ValueError(f"{other} isnt in the list, baka {getlogin()}")
				input("PRESS <<ENTER>> STUPIDD")
				system("cls")
			elif obj:
				print(obj)
				input("PRESS <<ENTER>> STUPIDD")
				system("cls")
		case "3":
			print("Comming soon")
			input("\nPRESS <<ENTER>> STUPIDD")
			system("cls")
		case "4":
			print("bye idiot))")
			exit()