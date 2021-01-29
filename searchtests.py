import unittest 
from selenium import webdriver
from  pyunitreport import HTMLTestRunner

class SearchTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output="searchtests"))