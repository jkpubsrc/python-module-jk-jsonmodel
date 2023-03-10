

from jk_testing import *

import jk_json
import jk_jsonmodel




DATA = jk_jsonmodel.loadModel("""{
	"aFloat": 1.234,
}""")




@TestCase()
def test_minValue_1(ctx:TestContext):
	v = DATA.getFloatE("aFloat", jk_jsonmodel.minValue(1))
#

@TestCase(
	RaisesException(Exception),
)
def test_minValue_1e(ctx:TestContext):
	v = DATA.getFloatE("aFloat", jk_jsonmodel.minValue(12345))
#

@TestCase()
def test_maxValue_1(ctx:TestContext):
	v = DATA.getFloatE("aFloat", jk_jsonmodel.maxValue(12345))
#

@TestCase(
	RaisesException(Exception),
)
def test_maxValue_1e(ctx:TestContext):
	v = DATA.getFloatE("aFloat", jk_jsonmodel.maxValue(1))
#











