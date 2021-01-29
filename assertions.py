import unittest 
from selenium import webdriver
from  pyunitreport import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except:
            return False
        return True

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output="assertions"))