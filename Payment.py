from random import randint
import re

class Payment:
	'''
	Abstract Class for different payment methods
	'''
	def __init__(self):
		pass
	@staticmethod  
	def processpayment():
		'''
		function to be overrided for different gateways
		'''
		pass

class CheapGateway(Payment):
	def processpayment():
		print('Trying using Cheap gateway')
		try:
			rno = randint(0,1)
			if rno == 0:
				return '200 OK'
			else:
				raise Exception
		except Exception as e:
			return('500 Internal Server Error')

class ExpensiveGateway(Payment):
	def processpayment():
		print('Trying using Expensive Gateway')
		try:
			rno = randint(0,1)
			if rno == 0:
				return '200 OK'
			else:
				raise Exception
		except Exception as e:
			return CheapGateway.processpayment()
class PremiumGateway(Payment):
	def processpayment():
		for _ in range(3):
			try:
				print('Trying using PremiumGateway')
				rno = randint(0,1)
				if rno == 0:
					return '200 OK'
				else:
					raise Exception
			except Exception as e:
				pass
		return '500 Internal Server Error'


class PaymentGateway:
	def __init__(self,cardno,name,expdate,seccode=None,amount = 0):
		'''
		constructor for initialising the class
		args:
		cardno -> integer(must be 16 digits)
		name -> cardholder name string
		expdate -> string of the format mm/yy
		seccode -> security code or cvv(3 digits) integer
		amount -> amount 
		special variable:
		flag -> 
		        0 - normally
		        1 - if any arg is passed in invalid format

		'''
		self.flag = 0
		self.__cardno = cardno
		self.__name = name
		self.__expdate = expdate
		self.__seccode = seccode
		self.amount = amount
		if len(self.__cardno)!=16 or not self.__cardno.isdigit():
			self.flag = 1
		if type(self.__name)!=str:
			self.flag = 1
		expdate_pattern = re.compile("^(0[1-9]|1[0-2])\/?(([0-9]{4}|[0-9]{2})$)")
		expdate_match = re.match(expdate_pattern,self.__expdate)
		if expdate_match is None:
			self.flag = 1
		if type(self.amount) !=int or self.amount < 1:
			self.flag = 1
	def process(self):
		'''
		Method for processing the payment
		args:
		None
		returns:
		response 
		 - 200 OK if processed
		 - 400 Bad Request incase of invalid attributes
		 - 500 Internal Server Error incase of bugs/errors
		'''

		if self.flag == 0:
			print('hereeeeeee')
			try:
				if self.amount < 20:
					return CheapGateway.processpayment()
				elif self.amount > 21 and self.amount < 500:
					return ExpensiveGateway.processpayment()
				elif self.amount > 501:
					return PremiumGateway.processpayment()
			except Exception as e:
				print(e)
				return '500 Internal Server Error'
		else:
			return '400 Bad Gateway'