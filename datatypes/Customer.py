import random
from datetime import datetime
from DataTypeBase import DataTypeBase

class Customer(DataTypeBase):
	def __init__(self, fake, useSystemDate=False):
		self.ID = Customer.ID
		Customer.ID += 1
		self.first_name = fake.first_name()
		self.last_name = fake.last_name()
		self.credit_card_number = fake.credit_card_number()
		self.billing_address = fake.address().replace('\n', ' ')
		self.phone_number = fake.phone_number()
		self.date_joined = str(datetime.now()) if useSystemDate else str(fake.date_time_this_century())

	@staticmethod
	def get_headers(self, delimiter="|"):
		return  "customer id" + delimiter + \
				"first name" + delimiter + \
				"last name" + delimiter + \
				"credit card number" + delimiter + \
				"billing address" + delimiter + \
				"phone number" + delimiter + "date joined"

	def to_record(self, delimiter="|"):
		return  str(self.ID) + delimiter + \
				self.first_name + delimiter + \
				self.last_name + delimiter + \
				self.credit_card_number + delimiter + \
				self.billing_address + delimiter + \
				self.phone_number + delimiter + \
				str(self.date_joined)