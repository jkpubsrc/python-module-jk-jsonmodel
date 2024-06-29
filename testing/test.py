#!/usr/bin/python3




import jk_logging

import jk_jsonmodel





FILE_PATH = "SomeJSONFile.jsonc"





with jk_logging.wrapMain() as log:

	jRaw = jk_jsonmodel.loadDictModelFromFile(FILE_PATH)
	#jRaw.dump()

	with jRaw.getDictE("magic") as jMagic:
		_s = jMagic.getStrE("magic")
		assert isinstance(_s, str)
		_i = jMagic.getIntE("version")
		assert isinstance(_i, int)

	with jRaw.getDictE("foo") as jFoo:
		jFoo.getBoolE("bar")

	with jRaw.getDictN("foo") as jFoo:
		_f = jFoo.getFloatE("baz")
		assert isinstance(_f, float)

	# with jRaw.getDictN("xxxxxx") as jFoo:
	# 	if jFoo is not None:
	# 		_y = jFoo.getBoolE("yyyyyy")
	# 		raise Exception("This code line should not be executed!")

	_x = jRaw.getDictE("foo").getListN("fooList")
	assert isinstance(_x, jk_jsonmodel.JMList)

	_x = jRaw.getDictE("foo").getListN("xxxxxxxx")
	assert _x is None


