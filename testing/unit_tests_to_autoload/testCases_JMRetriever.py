

from jk_testing import *

import jk_jsonmodel




DATA = jk_jsonmodel.loadModelFromStr("""{

	"foo": {
		"bar": {
			"vStr": "abc",
		},
	},

}""")










@TestCase(
	RaisesException(Exception),
)
def test_getStrE_refPath_invalid(ctx:TestContext):
	isinstance(DATA, jk_jsonmodel.JMDict)

	v = jk_jsonmodel.JMRetriever.getStrE(DATA, refPath="foo.bar. vStr")
#






@TestCase()
def test_getStrE_keySequence(ctx:TestContext):
	isinstance(DATA, jk_jsonmodel.JMDict)

	v = jk_jsonmodel.JMRetriever.getStrE(DATA, "foo", "bar", "vStr")
	Assert.isInstance(v, str)
	Assert.isEqual(v, "abc")
#

@TestCase()
def test_getStrE_refPath(ctx:TestContext):
	isinstance(DATA, jk_jsonmodel.JMDict)

	v = jk_jsonmodel.JMRetriever.getStrE(DATA, refPath="foo.bar.vStr")
	Assert.isInstance(v, str)
	Assert.isEqual(v, "abc")
#



@TestCase()
def test_getStrN_keySequence(ctx:TestContext):
	isinstance(DATA, jk_jsonmodel.JMDict)

	v = jk_jsonmodel.JMRetriever.getStrN(DATA, "foo", "bar", "vStr")
	Assert.isInstance(v, str)
	Assert.isEqual(v, "abc")
#

@TestCase()
def test_getStrN_refPath(ctx:TestContext):
	isinstance(DATA, jk_jsonmodel.JMDict)

	v = jk_jsonmodel.JMRetriever.getStrN(DATA, refPath="foo.bar.vStr")
	Assert.isInstance(v, str)
	Assert.isEqual(v, "abc")
#



@TestCase(
	RaisesException(Exception),
)
def test_getStrE_keySequence_error(ctx:TestContext):
	isinstance(DATA, jk_jsonmodel.JMDict)

	v = jk_jsonmodel.JMRetriever.getStrE(DATA, "foo", "bar", "vStrXYZ")
#

@TestCase()
def test_getStrN_refPath_error(ctx:TestContext):
	isinstance(DATA, jk_jsonmodel.JMDict)

	v = jk_jsonmodel.JMRetriever.getStrN(DATA, "foo", "bar", "vStrXYZ")
	Assert.isEqual(v, None)
#



