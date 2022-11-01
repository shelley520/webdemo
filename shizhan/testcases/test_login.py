import unittest
from selenium import webdriver
from shizhan.common.readdatas import readYaml
from shizhan.pageobjects.login_page import LoginPage
from ddt import ddt,data,unpack,file_data

# @ddt
class TestLogin(unittest.TestCase):

    # @data()
    def test_login(self):
        driver = webdriver.Chrome()
        loginpage= LoginPage(driver=driver)
        page_name = readYaml(key="login").get("success")[0]
        username = readYaml(key="login").get("success")[1]
        password = readYaml(key="login").get("success")[2]
        loginpage.login(page_name,username,password)
        # self.assertIn()