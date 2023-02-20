

import os
import typing

import jk_prettyprintobj



from .JMLocation import JMLocation






AbstractJMElement = typing.NewType("AbstractJElement", object)
JMDict = typing.NewType("JMDict", AbstractJMElement)
JMList = typing.NewType("JMList", AbstractJMElement)
JMValue = typing.NewType("JMValue", AbstractJMElement)







class AbstractJMElement(jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def location(self) -> JMLocation:
		raise NotImplementedError()
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dumpVarNames(self) -> typing.List[str]:
		raise NotImplementedError()
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def ensureIsDictE(self) -> JMDict:
		raise NotImplementedError()
	#

	def ensureIsListE(self) -> JMList:
		raise NotImplementedError()
	#

	def ensureIsValueE(self) -> JMValue:
		raise NotImplementedError()
	#

#





class JMValue(AbstractJMElement, jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self,
			location:JMLocation,
			data:typing.Union[int,str,bool,float,None] = None,
		):

		self._location = location

		self._data = data
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def location(self) -> JMLocation:
		return self._location
	#

	@property
	def data(self):
		return self._data
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dumpVarNames(self) -> typing.List[str]:
		return [
			"location",
			"data",
		]
	#

	def _buildErrorTypeMismatch(self, typeStr:str) -> Exception:
		if typeStr[0] in "aeiou":
			typeStr = "an " + typeStr
		else:
			typeStr = "a " + typeStr

		return Exception("Expecting value at {} to be {} ({}:{}:{})".format(
			repr(self._location.jsonPath),
			typeStr,
			self._location.sourceID,
			self._location.lineNo,
			self._location.charPos
		))
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __str__(self) -> str:
		s = repr(self._data)
		return self.__class__.__name__ + "<(" + s[1:-1] + ")>"
	#

	def __repr__(self) -> str:
		s = repr(self._data)
		return self.__class__.__name__ + "<(" + s[1:-1] + ")>"
	#

	def ensureIsDictE(self):
		raise self._buildErrorTypeMismatch("object")
	#

	def ensureIsListE(self):
		raise self._buildErrorTypeMismatch("list")
	#

	def ensureIsValueE(self):
		return self
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vIntN(self) -> typing.Union[int,None]:
		if (self._data is None) or isinstance(self._data, int):
			return self._data
		raise self._buildErrorTypeMismatch("integer")
	#

	def vIntE(self) -> int:
		if (self._data is None) or (not isinstance(self._data, int)):
			raise self._buildErrorTypeMismatch("integer")
		return self._data
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vFloatN(self) -> typing.Union[float,None]:
		if (self._data is None) or isinstance(self._data, float):
			return self._data
		raise self._buildErrorTypeMismatch("float")
	#

	def vFloatE(self) -> float:
		if (self._data is None) or (not isinstance(self._data, float)):
			raise self._buildErrorTypeMismatch("float")
		return self._data
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vBoolN(self) -> typing.Union[bool,None]:
		if (self._data is None) or isinstance(self._data, bool):
			return self._data
		raise self._buildErrorTypeMismatch("boolean")
	#

	def vBoolE(self) -> bool:
		if (self._data is None) or (not isinstance(self._data, bool)):
			raise self._buildErrorTypeMismatch("boolean")
		return self._data
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vStrN(self) -> typing.Union[str,None]:
		if (self._data is None) or isinstance(self._data, str):
			return self._data
		raise self._buildErrorTypeMismatch("string")
	#

	def vStrE(self) -> str:
		if (self._data is None) or (not isinstance(self._data, str)):
			raise self._buildErrorTypeMismatch("string")
		return self._data
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vPimitiveN(self) -> typing.Union[str,int,float,bool,None]:
		if (self._data is None) or isinstance(self._data, (int,float,bool,str)):
			return self._data
		raise self._buildErrorTypeMismatch("primitive")
	#

	def vPimitiveE(self) -> typing.Union[str,int,float,bool]:
		if (self._data is not None) and isinstance(self._data, (int,float,bool,str)):
			return self._data
		raise self._buildErrorTypeMismatch("primitive")
	#

#



#
# This class is used internally only.
#
class _JMProperty(jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self,
			location:JMLocation,
			key:str,
			value,
		):

		self._location = location

		self._key = key
		self._data = value
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def location(self) -> JMLocation:
		return self._location
	#

	@property
	def data(self):
		return self._data
	#

	@property
	def key(self):
		return self._key
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dumpVarNames(self) -> typing.List[str]:
		return [
			"location",
			"key",
			"data",
		]
	#

	def _buildErrorTypeMismatch(self, typeStr:str) -> Exception:
		if typeStr[0] in "aeiou":
			typeStr = "an " + typeStr
		else:
			typeStr = "a " + typeStr

		return Exception("Expecting value at {} to be {} ({}:{}:{})".format(
			repr(self._location.jsonPath),
			typeStr,
			self._location.sourceID,
			self._location.lineNo,
			self._location.charPos
		))
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def vDictE(self) -> JMDict:
		if (self._data is None) or (self._data.__class__.__name__ != "JMDict"):
			raise self._buildErrorTypeMismatch("object")
		return self._data
	#

	def vDictN(self) -> typing.Union[JMDict,None]:
		if self._data is None:
			return None
		if self._data._data is None:
			return None
		if self._data.__class__.__name__ != "JMDict":
			raise self._buildErrorTypeMismatch("object")
		return self._data
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vListE(self) -> typing.Union[JMList,None]:
		if (self._data is None) or (self._data.__class__.__name__ != "JMList"):
			raise self._buildErrorTypeMismatch("list")
		return self._data
	#

	def vListN(self) -> typing.Union[JMList,None]:
		if self._data is None:
			return None
		if self._data._data is None:
			return None
		if self._data.__class__.__name__ != "JMList":
			raise self._buildErrorTypeMismatch("list")
		return self._data
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vStrE(self) -> str:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("string")
		if isinstance(self._data._data, str):
			return self._data._data
		raise self._buildErrorTypeMismatch("string")
	#

	def vStrN(self) -> typing.Union[str,None]:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("string")
		if self._data._data is None:
			return None
		if isinstance(self._data._data, str):
			return self._data._data
		raise self._buildErrorTypeMismatch("string")
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vIntE(self) -> int:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("integer")
		if isinstance(self._data._data, int):
			return self._data._data
		raise self._buildErrorTypeMismatch("integer")
	#

	def vIntN(self) -> typing.Union[int,None]:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("integer")
		if self._data._data is None:
			return None
		if isinstance(self._data._data, int):
			return self._data._data
		raise self._buildErrorTypeMismatch("integer")
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vFloatE(self) -> float:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("float")
		if isinstance(self._data._data, float):
			return self._data._data
		raise self._buildErrorTypeMismatch("float")
	#

	def vFloatN(self) -> typing.Union[float,None]:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("float")
		if self._data._data is None:
			return None
		if isinstance(self._data._data, float):
			return self._data._data
		raise self._buildErrorTypeMismatch("float")
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vBoolE(self) -> bool:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("boolean")
		if isinstance(self._data._data, bool):
			return self._data._data
		raise self._buildErrorTypeMismatch("boolean")
	#

	def vBoolN(self) -> typing.Union[bool,None]:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("boolean")
		if self._data._data is None:
			return None
		if isinstance(self._data._data, bool):
			return self._data._data
		raise self._buildErrorTypeMismatch("boolean")
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vPrimitiveE(self) -> typing.Union[bool,int,float,str]:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("primitive")
		if isinstance(self._data._data, (int,float,str,bool)):
			return self._data._data
		raise self._buildErrorTypeMismatch("primitive")
	#

	def vPrimitiveN(self) -> typing.Union[bool,int,float,str,None]:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("primitive")
		if self._data._data is None:
			return None
		if isinstance(self._data._data, (int,float,str,bool)):
			return self._data._data
		raise self._buildErrorTypeMismatch("primitive")
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def vValueE(self) -> JMValue:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("value")
		return self._data
	#

	def vValueN(self) -> typing.Union[JMValue,None]:
		if (self._data is None) or (self._data.__class__.__name__ != "JMValue"):
			raise self._buildErrorTypeMismatch("value")
		if self._data._data is None:
			return None
		return self._data
	#

#




class JMList(AbstractJMElement, jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self,
			location:JMLocation,
			data:list,
		):

		self._location = location

		self._data = data
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def location(self) -> JMLocation:
		return self._location
	#

	@property
	def data(self):
		return self._data
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dumpVarNames(self) -> typing.List[str]:
		return [
			"location",
			"data",
		]
	#

	def _buildErrorTypeMismatch(self, typeStr:str) -> Exception:
		if typeStr[0] in "aeiou":
			typeStr = "an " + typeStr
		else:
			typeStr = "a " + typeStr

		return Exception("Expecting value at {} to be {} ({}:{}:{})".format(
			repr(self._location.jsonPath),
			typeStr,
			self._location.sourceID,
			self._location.lineNo,
			self._location.charPos
		))
	#

	def _buildErrorTypeMismatchIndexed(self, i:int, typeStr:str) -> Exception:
		if typeStr[0] in "aeiou":
			typeStr = "an " + typeStr
		else:
			typeStr = "a " + typeStr

		return Exception("Expecting value at {}[{}] to be {} ({}:{}:{})".format(
			repr(self._location.jsonPath),
			i,
			typeStr,
			self._location.sourceID,
			self._location.lineNo,
			self._location.charPos
		))
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __str__(self) -> str:
		s = self._data.__str__()
		return self.__class__.__name__ + "<(" + s[1:-1] + ")>"
	#

	def __repr__(self) -> str:
		s = self._data.__str__()
		return self.__class__.__name__ + "<(" + s[1:-1] + ")>"
	#

	def ensureIsDictE(self) -> JMDict:
		raise self._buildErrorTypeMismatch("object")
	#

	def ensureIsListE(self) -> JMList:
		return self
	#

	def ensureIsValueE(self) -> JMValue:
		raise self._buildErrorTypeMismatch("value")
	#

	def __getitem__(self, index:int) -> typing.Union[None,int,float,bool,str,JMList,JMDict]:
		if not isinstance(index, int):
			raise TypeError("A list index must be of type 'int'!")

		ret = self._data[index]
		if isinstance(ret, JMValue):
			return ret._data
		assert isinstance(ret, (JMList,JMDict))
		return ret
	#

	def __setitem__(self, index, value):
		raise Exception(self.__class__.__name__ + " classes are read only!")
	#

	def __delitem__(self, index):
		raise Exception(self.__class__.__name__ + " classes are read only!")
	#

	def __len__(self) -> int:
		return self._data.__len__()
	#

	def __contains__(self, value) -> bool:
		return value in self._data
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def toStrList(self, bAllowNull:bool = False) -> typing.List[str]:
		ret = []
		if bAllowNull:
			for i, v in enumerate(self._data):
				if isinstance(v, JMValue):
					ret.append(v.vStrN())
				else:
					raise self._buildErrorTypeMismatchIndexed(i, "str")
		else:
			for i, v in enumerate(self._data):
				if isinstance(v, JMValue):
					ret.append(v.vStrE())
				else:
					raise self._buildErrorTypeMismatchIndexed(i, "str")
		return ret
	#

#



class JMDict(AbstractJMElement, jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self,
			location:JMLocation,
			data:dict,
		):

		self._location = location

		self._data:typing.Dict[str,_JMProperty] = data
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def location(self) -> JMLocation:
		return self._location
	#

	@property
	def data(self):
		return self._data
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dumpVarNames(self) -> typing.List[str]:
		return [
			"location",
			"data",
		]
	#

	def _buildErrorMissingKey(self, key:str) -> Exception:
		return Exception("Expecting key {} at {} ({}:{}:{})".format(
			repr(key),
			self._location.jsonPath,
			self._location.sourceID,
			self._location.lineNo,
			self._location.charPos
		))
	#

	def _buildErrorTypeMismatch(self, typeStr:str) -> Exception:
		if typeStr[0] in "aeiou":
			typeStr = "an " + typeStr
		else:
			typeStr = "a " + typeStr

		return Exception("Expecting value at {} to be {} ({}:{}:{})".format(
			repr(self._location.jsonPath),
			typeStr,
			self._location.sourceID,
			self._location.lineNo,
			self._location.charPos
		))
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __str__(self) -> str:
		s = {
			k:v for k,v in self.itemsv()
		}.__str__()
		return self.__class__.__name__ + "<(" + s[1:-1] + ")>"
	#

	def __repr__(self) -> str:
		s = {
			k:v for k,v in self.itemsv()
		}.__str__()
		return self.__class__.__name__ + "<(" + s[1:-1] + ")>"
	#

	def ensureIsDictE(self) -> JMDict:
		return self
	#

	def ensureIsListE(self) -> JMList:
		raise self._buildErrorTypeMismatch("object")
	#

	def ensureIsValueE(self) -> JMValue:
		raise self._buildErrorTypeMismatch("value")
	#

	def __enter__(self) -> JMDict:
		return self
	#

	def __exit__(self, exception_type, exception_value, exception_traceback):
		pass
	#

	def __len__(self) -> int:
		return self._data.__len__()
	#

	def valuesv(self) -> typing.Iterable[typing.Union[int,float,str,bool,None,JMList,JMDict]]:
		for prop in self._data.values():
			assert isinstance(prop, _JMProperty)
			if isinstance(prop._data, JMValue):
				yield prop._data._data
			else:
				yield prop._data
	#

	def values(self) -> typing.Iterable[typing.Union[JMValue,JMList,JMDict]]:
		for prop in self._data.values():
			assert isinstance(prop, _JMProperty)
			yield prop._data
	#

	def keys(self) -> typing.Iterable[str]:
		yield from self._data.keys()
	#

	def itemsv(self) -> typing.Iterable[typing.Tuple[str,typing.Union[int,float,str,bool,None,JMList,JMDict]]]:
		for key, prop in self._data.items():
			assert isinstance(prop, _JMProperty)
			if isinstance(prop._data, JMValue):
				yield key, prop._data._data
			else:
				yield key, prop._data
	#

	def items(self) -> typing.Iterable[typing.Tuple[str,typing.Union[JMValue,JMList,JMDict]]]:
		for key, prop in self._data.items():
			assert isinstance(prop, _JMProperty)
			yield key, prop._data
	#

	def __getitem__(self, key:str) -> typing.Union[JMValue,JMList,JMDict]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			ret = self._data[key]
			assert isinstance(ret, _JMProperty)
			return ret._data
		raise self._buildErrorMissingKey(key)
	#

	def get(self, key:str) -> typing.Union[JMValue,JMList,JMDict]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			assert isinstance(prop, _JMProperty)
			return prop._data
		return None
	#

	def getv(self, key:str) -> typing.Union[int,float,str,bool,None,JMList,JMDict]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			assert isinstance(prop, _JMProperty)
			if isinstance(prop._data, JMValue):
				return prop._data._data
			else:
				return prop._data
		return None
	#

	def __setitem__(self, key, value):
		raise Exception(self.__class__.__name__ + " classes are read only!")
	#

	def __delitem__(self, x):
		raise Exception(self.__class__.__name__ + " classes are read only!")
	#

	def __contains__(self, key:str) -> bool:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		return key in self._data
	#

	def hasNonNull(self, key:str) -> bool:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		v = self._data.get(key)
		if v is None:
			return False
		if isinstance(v, JMValue):
			return v._data is not None
		return True
	#

	################################################################################################################################

	def getDictE(self, key:str) -> JMDict:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vDictE()
		raise self._buildErrorMissingKey(key)
	#

	def getDictN(self, key:str) -> typing.Union[JMDict,None]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			assert isinstance(prop, _JMProperty)
			return prop.vDictN()
		return None
	#

	################################################################################################################################

	def getListE(self, key:str) -> JMList:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vListE()
		raise self._buildErrorMissingKey(key)
	#

	def getListN(self, key:str) -> typing.Union[JMList,None]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vListN()
		return None
	#

	################################################################################################################################

	def getStrE(self, key:str) -> str:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vStrE()
		raise self._buildErrorMissingKey(key)
	#

	def getStrN(self, key:str) -> typing.Union[str,None]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vStrN()			# there is a key but its value might be null
		return None						# no such key
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def getIntE(self, key:str) -> int:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vIntE()
		raise self._buildErrorMissingKey(key)
	#

	def getIntN(self, key:str) -> typing.Union[int,None]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vIntN()			# there is a key but its value might be null
		return None						# no such key
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def getFloatE(self, key:str) -> float:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vFloatE()
		raise self._buildErrorMissingKey(key)
	#

	def getFloatN(self, key:str) -> typing.Union[float,None]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vFloatN()		# there is a key but its value might be null
		return None						# no such key
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def getBoolE(self, key:str) -> bool:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vBoolE()
		raise self._buildErrorMissingKey(key)
	#

	def getBoolN(self, key:str) -> typing.Union[bool,None]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vBoolN()		# there is a key but its value might be null
		return None						# no such key
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def getPrimitiveE(self, key:str) -> typing.Union[str,int,float,bool]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vPrimitiveE()
		raise self._buildErrorMissingKey(key)
	#

	def getPrimitiveN(self, key:str) -> typing.Union[str,int,float,bool,None]:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vPrimitiveN()		# there is a key but its value might be null
		return None							# no such key
	#

	# --------------------------------------------------------------------------------------------------------------------------------

	def getValueE(self, key:str) -> JMValue:
		if not isinstance(key, str):
			raise TypeError("A specified key is of type {} but it must be of type 'str'!".format(type(key)))

		if key in self._data:
			prop = self._data[key]
			return prop.vValueE()
		raise self._buildErrorMissingKey(key)
	#

#


