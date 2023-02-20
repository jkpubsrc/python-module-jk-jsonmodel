#!/usr/bin/python3



import typing

import jk_jsonmodel
import jk_prettyprintobj





class BirthdayRecord(jk_prettyprintobj.DumpMixin):

	def __init__(self, jData:jk_jsonmodel.JMDict):
		assert isinstance(jData, jk_jsonmodel.JMDict)

		self.month = jData.getIntE("month")
		self.day = jData.getIntE("day")
		self.year = jData.getIntN("year")
	#

	def _dumpVarNames(self) -> typing.List[str]:
		return [
			"month",
			"day",
			"year",
		]
	#

#

class PhoneNumberRecord(jk_prettyprintobj.DumpMixin):

	def __init__(self, key:str, phoneNumber:jk_jsonmodel.JMValue):
		assert isinstance(key, str)
		assert isinstance(phoneNumber, jk_jsonmodel.JMValue)

		self.key = key
		self.phoneNumber = phoneNumber.vStrN()
	#

	def _dumpVarNames(self) -> typing.List[str]:
		return [
			"key",
			"phoneNumber",
		]
	#

#

class ContactDataRecord(jk_prettyprintobj.DumpMixin):

	def __init__(self, jData:jk_jsonmodel.JMDict):
		assert isinstance(jData, jk_jsonmodel.JMDict)

		self.name = jData.getStrE("name")
		self.surename = jData.getStrE("surename")
		self.birthday = BirthdayRecord(jData.getDictE("birthday")) if "birthday" in jData else None
		self.phoneNumbers = {}
		for k, v in jData.getDictE("phoneNumbers").items():
			self.phoneNumbers[k] = PhoneNumberRecord(k, v)
	#

	def _dumpVarNames(self) -> typing.List[str]:
		return [
			"name",
			"surename",
			"birthday",
			"phoneNumbers",
		]
	#

#



jData = jk_jsonmodel.loadDictModelFromFile("somedata.json")
theModel = ContactDataRecord(jData)
theModel.dump()













