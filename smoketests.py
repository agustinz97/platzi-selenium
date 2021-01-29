from unittest import TestLoader, TestSuite
from  pyunitreport import HTMLTestRunner
from assertions import AssertionsTests
from searchtests import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_test])

runner = HTMLTestRunner(output='smoke-tests')
runner.run(smoke_test)