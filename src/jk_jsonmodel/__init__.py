


__author__ = "Jürgen Knauth"
__version__ = "0.2023.2.20"



import bz2
import gzip
import chardet
import typing

import jk_json



from .JsonParserRelaxedModel import JsonParserRelaxedModel as _JsonParserRelaxedModel
from .jclasses import AbstractJMElement, JMDict, JMValue, JMList





__tokenizerRelaxed = jk_json.TokenizerRelaxed()

__parserRelaxedModel = _JsonParserRelaxedModel()





#
# Deserialize a JSON string: Reconstruct a python data structure from the specified JSON string.
#
# @param	str textToParse		The JSON to parse in binary or string representation. If binary data is specified a simple UTF-8 decoding is performed
#								to get to a string which is then parsed.
# @param	bool bStrict		If ```True``` this parser sticks strictly to the JSON standard. If ```False``` C-style comments
#								are allowed and strings can be specified with single quotes and double quotes.
#								Furthermore NaN, positive and negative infinitiy is supported.
#
def loadModel(
		textToParse:str,
		bDebugging:bool = False,
		allowDuplicatePropertyNames:bool = False,
		sourceID:str = None,
	) -> typing.Union[JMDict,JMList]:

	assert isinstance(textToParse, str)
	assert isinstance(bDebugging, bool)
	assert isinstance(allowDuplicatePropertyNames, bool)
	if sourceID is not None:
		assert isinstance(sourceID, str)

	# ----

	if isinstance(textToParse, (bytes, bytearray)):
		textToParse = textToParse.decode("utf-8")
	elif not isinstance(textToParse, str):
		raise Exception("Can't decode JSON data from a non-string or non-binary value!")

	tokenizer = __tokenizerRelaxed
	parser = __parserRelaxedModel

	ret = parser.parse(tokenizer.tokenize(textToParse, sourceID), bDebugging, allowDuplicatePropertyNames)
	assert isinstance(ret, (JMDict,JMList))
	return ret
#



#
# Deserialize a JSON string: Reconstruct a python data structure reading data from the specified JSON file.
#
# @param	str filePath		The path of the file to load.
# @param	bool bStrict		If ```True``` this parser sticks strictly to the JSON standard. If ```False``` C-style comments
#								are allowed and strings can be specified with single quotes and double quotes.
#								Furthermore NaN, positive and negative infinitiy is supported.
#
def loadModelFromFile(
		filePath:str,
		bDebugging:bool = False,
		encoding:str = None,
		autoDetectEncoding:bool = True,
		errPrintFunc = None,
		allowDuplicatePropertyNames:bool = False
	) -> typing.Union[JMDict,JMList]:

	assert isinstance(filePath, str)
	assert isinstance(bDebugging, bool)

	# ----

	if filePath.endswith(".bz2"):
		with bz2.open(filePath, "rb") as f:
			rawData = f.read()
	elif filePath.endswith(".gz"):
		with gzip.open(filePath, "rb") as f:
			rawData = f.read()
	else:
		with open(filePath, "rb") as f:
			rawData = f.read()

	textData = None

	if encoding is None:
		if autoDetectEncoding:
			try:
				if rawData.startswith(b"\xef\xbb\xbf"):		# utf-8 byte order mark
					rawData = rawData[3:]

				textData = rawData.decode("utf-8")

			except:
				encoding = chardet.detect(rawData)["encoding"]
				if encoding is None:
					encoding = "utf-8"

		else:
			encoding = "utf-8"

	if textData is None:
		textData = rawData.decode(encoding)

	if errPrintFunc and callable(errPrintFunc):
		try:
			return loadModel(textData, bDebugging = bDebugging, allowDuplicatePropertyNames = allowDuplicatePropertyNames)
		except jk_json.ParserErrorException as ee:
			s = filePath if len(filePath) < 40 else ("..." + filePath[-40:])
			prefix = "{}:{} ".format(s, ee.location.lineNo + 1)
			errPrintFunc(prefix + ee.textLine.replace("\t", " "))
			errPrintFunc(" " * (len(prefix) + ee.location.charPos + 1) + "ᐃ")
			errPrintFunc(" " * (len(prefix) + ee.location.charPos + 1 - 6) + "╌╌╍╍━━┛")
			raise
	else:
		return loadModel(
			textData,
			bDebugging = bDebugging,
			allowDuplicatePropertyNames = allowDuplicatePropertyNames,
			sourceID = filePath,
		)
#

def loadListModelFromFile(
		filePath:str,
		bDebugging:bool = False,
		encoding:str = None,
		autoDetectEncoding:bool = True,
		errPrintFunc = None,
		allowDuplicatePropertyNames:bool = False
	) -> JMList:

	ret = loadModelFromFile(filePath, bDebugging, encoding, autoDetectEncoding, errPrintFunc, allowDuplicatePropertyNames)
	assert isinstance(ret, JMList)
	return ret
#

def loadDictModelFromFile(
		filePath:str,
		bDebugging:bool = False,
		encoding:str = None,
		autoDetectEncoding:bool = True,
		errPrintFunc = None,
		allowDuplicatePropertyNames:bool = False
	) -> JMDict:

	ret = loadModelFromFile(filePath, bDebugging, encoding, autoDetectEncoding, errPrintFunc, allowDuplicatePropertyNames)
	assert isinstance(ret, JMDict)
	return ret
#

