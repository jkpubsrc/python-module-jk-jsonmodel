

from jk_testing import *

import jk_jsonmodel




DATA = jk_jsonmodel.loadModel("""{
	"aFloat": 1.234,
	"anInt": 1234,
	"aBool": true,
	"aStr": "abc",
	"aNull": null,
}""")




@TestCase()
def test_isTypeJMyDict(ctx:TestContext):
	isinstance(DATA, jk_jsonmodel.JMDict)
#

# ----

@TestCase()
def test_getFloatE_1(ctx:TestContext):
	v = DATA.getFloatE("aFloat")
	Assert.isInstance(v, float)
	Assert.isEqual(v, 1.234)
#

@TestCase()
def test_getFloatN_1(ctx:TestContext):
	v = DATA.getFloatN("aFloatXXX")
	Assert.isNone(v)
#

# ----

@TestCase()
def test_getIntE_1(ctx:TestContext):
	v = DATA.getIntE("anInt")
	Assert.isInstance(v, int)
	Assert.isEqual(v, 1234)
#

@TestCase()
def test_getIntN_1(ctx:TestContext):
	v = DATA.getIntN("anIntXXX")
	Assert.isNone(v)
#

# ----

@TestCase()
def test_getBoolE_1(ctx:TestContext):
	v = DATA.getBoolE("aBool")
	Assert.isInstance(v, bool)
	Assert.isTrue(v)
#

@TestCase()
def test_getBoolN_1(ctx:TestContext):
	v = DATA.getBoolN("aBoolXXX")
	Assert.isNone(v)
#

# ----

@TestCase()
def test_getStrE_1(ctx:TestContext):
	v = DATA.getStrE("aStr")
	Assert.isInstance(v, str)
	Assert.isEqual(v, "abc")
#

@TestCase()
def test_getStrN_1(ctx:TestContext):
	v = DATA.getStrN("aStrXXX")
	Assert.isNone(v)
#

# ----

@TestCase(
	RaisesException(Exception),
)
def test_getNullE_1(ctx:TestContext):
	v = DATA.getPrimitiveE("aNull")
	Assert.isNone(v)
#

@TestCase()
def test_getNullN_1(ctx:TestContext):
	v = DATA.getPrimitiveN("aNullXXX")
	Assert.isNone(v)
#



