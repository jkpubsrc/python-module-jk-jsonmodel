

from jk_testing import *

import jk_jsonmodel




DATA = jk_jsonmodel.loadModel("""{
	"aNull": null,
	"anEmptyList": [],
	"anIntList": [ 123, 456 ],
}""")




@TestCase()
def test_getListN_null(ctx:TestContext):
	v = DATA.getListN("aNull")
	Assert.isNone(v)
#

@TestCase()
def test_getListE_empty(ctx:TestContext):
	v = DATA.getListE("anEmptyList")
	Assert.isInstance(v, jk_jsonmodel.JMList)
	Assert.isEqual(len(v), 0)
#

@TestCase()
def test_getListE_intList(ctx:TestContext):
	v = DATA.getListE("anIntList")
	Assert.isInstance(v, jk_jsonmodel.JMList)
	Assert.isEqual(len(v), 2)
	Assert.isEqual(v[0], 123)
	Assert.isEqual(v[1], 456)
#

@TestCase(
	RaisesException(IndexError),
	RunAfter("test_getListE_intList"),
)
def test_getListE_intList_indexTooLarge(ctx:TestContext):
	v = DATA.getListE("anIntList")
	Assert.isInstance(v, jk_jsonmodel.JMList)
	Assert.isEqual(len(v), 2)
	x = v[2]
#

@TestCase()
def test_getListN_nonExistent(ctx:TestContext):
	v = DATA.getListN("anIntListXXXX")
	Assert.isNone(v)
#

@TestCase()
def test_getListN_intList(ctx:TestContext):
	v = DATA.getListN("anIntList")
	Assert.isInstance(v, jk_jsonmodel.JMList)
	Assert.isEqual(len(v), 2)
	Assert.isEqual(v[0], 123)
	Assert.isEqual(v[1], 456)
#




