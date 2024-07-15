#!/usr/bin/python3




import jk_logging

import jk_json
import jk_jsonmodel





FIRST_FILE_PATH = "merge-1-file.jsonc"
SECOND_FILE_PATH = "merge-2-file.jsonc"





with jk_logging.wrapMain() as log:

	# print()

	jFirst = jk_jsonmodel.loadModelFromFile(FIRST_FILE_PATH)
	# jFirst.dump()

	# print()

	jSecond = jk_jsonmodel.loadModelFromFile(SECOND_FILE_PATH)
	# jSecond.dump()

	print()

	jk_jsonmodel.JMMerger.mergeInfo(jFirst, jSecond)
	jFirst.dump()

	print()

	jk_json.prettyPrint(jFirst.toJSON())




