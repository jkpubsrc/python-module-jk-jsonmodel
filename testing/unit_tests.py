#!/usr/bin/env python3


import jk_logging

from jk_testing import *






with jk_logging.wrapMain() as log:

	testCaseCollection = TestCaseCollection2()
	testCaseCollection.loadTestsFromDirectory("unit_tests_to_autoload", log=log)
	#testCaseCollection.dump()

	#orderedTestCaseCollection = OrderedTestCaseCollection.buildFromCollection(testCaseCollection)
	#orderedTestCaseCollection.dump()

	TestDriver = TestDriver()
	result = TestDriver.runTests(testCaseCollection, log)

	# result.dump()

#










