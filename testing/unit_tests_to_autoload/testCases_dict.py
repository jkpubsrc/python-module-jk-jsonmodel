

from jk_testing import *

import jk_json
import jk_jsonmodel




_strDATA = """{
	"aNull": null,
	"anEmptyDict": {},
	"aDict": {
		"foo": 123,
		"bar": 456,
	},
}"""
DATA = jk_jsonmodel.loadModelFromStr(_strDATA)
# DATA.dump()

_strDATA2 = """{
	"aNull": null,
	"anInt": 123,
	"aStr": "abc",
}"""
DATA2json = jk_json.loads(_strDATA2)
DATA2 = jk_jsonmodel.loadModelFromStr(_strDATA2)
# DATA2.dump()




@TestCase()
def test_getDictN_null(ctx:TestContext):
	v = DATA.getDictN("aNull")
	Assert.isNone(v)
#

@TestCase()
def test_getDictE_empty(ctx:TestContext):
	v = DATA.getDictE("anEmptyDict")
	Assert.isInstance(v, jk_jsonmodel.JMDict)
	Assert.isEqual(len(v), 0)
#

@TestCase()
def test_getDictE_notEmpty(ctx:TestContext):
	v = DATA.getDictE("aDict")
	Assert.isInstance(v, jk_jsonmodel.JMDict)
	Assert.isEqual(len(v), 2)
	Assert.isEqual(v.getIntE("foo"), 123)
	Assert.isEqual(v.getIntE("bar"), 456)
#

@TestCase()
def test_indexed_notEmpty(ctx:TestContext):
	v = DATA["aDict"]
	Assert.isInstance(v, jk_jsonmodel.JMDict)
	Assert.isEqual(len(v), 2)
	Assert.isEqual(v.getIntE("foo"), 123)
	Assert.isEqual(v.getIntE("bar"), 456)
#

@TestCase()
def test_getDictN_nonExistent1(ctx:TestContext):
	v = DATA.getDictN("aDictXXXX")
	Assert.isNone(v)
#

@TestCase()
def test_getDictN_nonExistent2(ctx:TestContext):
	v = DATA.get("aDictXXXX")
	Assert.isNone(v)
#

@TestCase(
	RaisesException(Exception),
)
def test_indexed_nonExistent(ctx:TestContext):
	v = DATA["aDictXXXX"]
	Assert.isNone(v)
#

@TestCase()
def test_getDictE_withCtx1(ctx:TestContext):
	with DATA as d:
		v = d.getDictE("aDict")
		Assert.isInstance(v, jk_jsonmodel.JMDict)
#

@TestCase()
def test_getDictE_withCtx2(ctx:TestContext):
	with DATA as d:
		v = d["aDict"]
		Assert.isInstance(v, jk_jsonmodel.JMDict)
#

@TestCase()
def test_keys(ctx:TestContext):
	allKeys = set()
	nCount = 0
	for k in DATA2.keys():
		assert isinstance(k, str)
		allKeys.add(k)
		nCount += 1
	Assert.isEqual(nCount, 3)
	Assert.isEqual(allKeys, set(DATA2.keys()))
	Assert.isEqual(allKeys, set(DATA2json.keys()))
#

@TestCase()
def test_values(ctx:TestContext):
	allValues = set([
		DATA2json[k] for k in DATA2.keys()
	])
	nCount = 0
	for v in DATA2.values():
		Assert.isInstance(v, jk_jsonmodel.JMValue)
		if v.data not in allValues:
			raise AssertionException(repr(v) + " seems not to be in " + repr(allValues))
		nCount += 1
	Assert.isEqual(nCount, 3)
#

@TestCase()
def test_valuesv(ctx:TestContext):
	allValues = set([
		DATA2json[k] for k in DATA2.keys()
	])
	nCount = 0
	for v in DATA2.valuesv():
		if v is not None:
			Assert.isInstance(v, (int,str,float,bool,jk_jsonmodel.JMList,jk_jsonmodel.JMDict))
		if v not in allValues:
			raise AssertionException(repr(v) + " seems not to be in " + repr(allValues))
		nCount += 1
	Assert.isEqual(nCount, 3)
#

@TestCase()
def test_itemsv(ctx:TestContext):
	nCount = 0
	allKeys = set()
	for k, v in DATA2.itemsv():
		if k not in DATA2json:
			raise AssertionException(repr(k) + ":" + repr(v) + " seems not to be in " + repr(DATA2json))
		Assert.isEqual(v, DATA2json[k])
		allKeys.add(k)
		nCount += 1
	Assert.isEqual(allKeys, set(DATA2json.keys()))
	Assert.isEqual(nCount, 3)
#

@TestCase()
def test_items(ctx:TestContext):
	nCount = 0
	allKeys = set()
	for k, v in DATA2.items():
		if k not in DATA2json:
			raise AssertionException(repr(k) + ":" + repr(v) + " seems not to be in " + repr(DATA2json))
		Assert.isInstance(v, jk_jsonmodel.JMValue)
		Assert.isEqual(v.data, DATA2json[k])
		allKeys.add(k)
		nCount += 1
	Assert.isEqual(allKeys, set(DATA2json.keys()))
	Assert.isEqual(nCount, 3)
#

@TestCase()
def test_in_1(ctx:TestContext):
	x = "anInt" in DATA2
	Assert.isInstance(x, bool)
	Assert.isTrue(x)
#

@TestCase()
def test_in_2(ctx:TestContext):
	x = "fooBarXXXXXXXXXX" in DATA2
	Assert.isInstance(x, bool)
	Assert.isFalse(x)
#










