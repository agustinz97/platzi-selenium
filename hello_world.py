import unittest 
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(5)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output="reports", report_name="hello_world_report"))
