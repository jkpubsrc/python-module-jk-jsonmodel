#!/usr/bin/env python3


import jk_logging

from jk_testing import *






with jk_logging.wrapMain() as log:

	temp = []
	TestCaseFileLoader.loadTestsFromDirectory("unit_tests_to_autoload", collection=temp, log=log)
	testCaseCollection = TestCaseCollection2()
	testCaseCollection.appendAll(temp, log)

	#orderedTestCaseCollection = OrderedTestCaseCollection.buildFromCollection(testCaseCollection)
	#orderedTestCaseCollection.dump()

	TestDriver = TestDriver()
	result = TestDriver.runTests(testCaseCollection, log)

	# result.dump()

#










