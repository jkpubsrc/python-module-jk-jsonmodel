#!/usr/bin/python3




import jk_logging

import jk_jsonmodel





FILE_PATH = "SomeJSONFile.jsonc"





with jk_logging.wrapMain() as log:

	jRaw = jk_jsonmodel.loadModelFromFile(FILE_PATH)
	jRaw.dump()


