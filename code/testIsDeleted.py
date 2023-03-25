import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_isDeleted(self):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        self.assertEqual(judgeWhetherBeDeleted(driver, "駿清清"),
                         False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
