__author__ = 'inna'
 
import unittest
import os
import wta
import HtmlTestRunner
 
class WTATestSuite(unittest.TestCase):
 
    def test_all_cases_with_report(self):
 
        test_with_report = unittest.TestSuite()
        test_with_report.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(wta.wta),
        ])
        current_directory = os.getcwd()
        output_file = open(current_directory + "\HTML_Test_Runner_ReportTest.html", "w")
        html_runner = HtmlTestRunner.HTMLTestRunner(
        stream=output_file,
        report_title='HTML Reporting for WTA with Selenium',
        descriptions='HTML Reporting using PyUnit & HTMLTestRunner'
        ) 
        html_runner.run(test_with_report)
if __name__ == '__main__':
    unittest.main()