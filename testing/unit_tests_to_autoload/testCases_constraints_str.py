

from jk_testing import *

import jk_json
import jk_jsonmodel




DATA = jk_jsonmodel.loadModel("""{
	"aStr": "abc",
}""")




@TestCase()
def test_minLength_1(ctx:TestContext):
	v = DATA.getStrE("aStr", jk_jsonmodel.minLength(1))
#

@TestCase(
	RaisesException(Exception),
)
def test_minLength_1e(ctx:TestContext):
	v = DATA.getStrE("aStr", jk_jsonmodel.minLength(123))
#

@TestCase()
def test_maxLength_1(ctx:TestContext):
	v = DATA.getStrE("aStr", jk_jsonmodel.maxLength(123))
#

@TestCase(
	RaisesException(Exception),
)
def test_maxLength_1e(ctx:TestContext):
	v = DATA.getStrE("aStr", jk_jsonmodel.maxLength(1))
#

@TestCase()
def test_regex_1(ctx:TestContext):
	v = DATA.getStrE("aStr", jk_jsonmodel.matchRegEx("a.+"))
#

@TestCase(
	RaisesException(Exception),
)
def test_regex_1e(ctx:TestContext):
	v = DATA.getStrE("aStr", jk_jsonmodel.matchRegEx("x.+"))
#










