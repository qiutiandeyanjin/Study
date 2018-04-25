# !/usr/bin/python3

"""
FileName    : run_test.py
Author      : ken
Date        : 2018-04-22
Describe    : use the unittest and HTMLTestRunner, run all test case
"""
import os
import time
import unittest

from commonFile import getDir
from commonFile.HTMLTestReportCN import HTMLTestRunner

proDir = getDir.proDir
now = time.strftime("%Y_%m_%d")

if __name__ == "__main__":
    # setting report dir
    ReportDir = os.path.join(proDir, "testReport")

    # setting case dir
    CaseDir = os.path.join(proDir, "testCase")

    # search test case
    discover = unittest.defaultTestLoader.discover(start_dir=CaseDir, pattern="test_*.py")

    # setting report fileName
    fileName = "parameterTest_%s.html" % now
    fp = open(os.path.join(ReportDir, fileName), 'wb')

    runner = HTMLTestRunner(stream=fp,
                            title="ParameterTest",
                            description="use case execution: ",
                            tester="ken",
                            verbosity=2)

    runner.run(discover)
