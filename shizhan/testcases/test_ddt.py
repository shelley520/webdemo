import unittest

import os
from selenium import webdriver
# from shizhan.common.readdatas import readYaml
from shizhan.common.dirconfig import DirConfig
from shizhan.common.readdatas import Data
from shizhan.pageobjects.login_page import LoginPage
from ddt import ddt,data,unpack,file_data

@ddt
class TestLogin(unittest.TestCase):

    # 元组
    # 单组元素
    @unittest.skip('慧')
    @data(('login page','516463257@qq.com','chris520h'))
    def test_tuple_01(self,data):
        driver = webdriver.Chrome()
        loginpage= LoginPage(driver=driver)
        loginpage.login(*data)

    # 多组元素未unpack
    @unittest.skip('hui')
    @data(('login page', '516463257@qq.com', 'chris520h'),('login page','bonnie_c520@yahoo.com','12345678'))
    def test_tuple_02(self, data):
        driver = webdriver.Chrome()
        loginpage = LoginPage(driver=driver)
        loginpage.login(*data)

    # 多组元素unpack
    @unittest.skip('bonnie')
    @data(('login page', '516463257@qq.com', 'chris520h'), ('login page', 'bonnie_c520@yahoo.com', '12345678'))
    @unpack
    def test_tuple_03(self, a,b,c):
        driver = webdriver.Chrome()
        loginpage = LoginPage(driver=driver)
        loginpage.login(a,b,c)

    # 列表,不适用
    # 单组元素
    @unittest.skip('慧')
    @data(['login page', '516463257@qq.com', 'chris520h'])
    def test_list_01(self, data):
        driver = webdriver.Chrome()
        loginpage = LoginPage(driver=driver)
        loginpage.login(*data)

    # 多组元素未unpack
    @unittest.skip('hui')
    @data(*[{'page_name':'login page','username': '516463257@qq.com','password': 'chris520h'}, {'page_name':'login page','username': 'bonnie_c520@yahoo.com', 'password':'12345678'}])
    def test_list_02(self, data):
        print(*data)
        driver = webdriver.Chrome()
        loginpage = LoginPage(driver=driver)
        loginpage.login(**data)

    # 多组元素unpack
    @unittest.skip('bonnie')
    @data(*[{'page_name':'login page','username': '516463257@qq.com', 'password':'chris520h'}, {'page_name':'login page', 'username':'bonnie_c520@yahoo.com','password': '12345678'}])
    @unpack
    def test_list_03(self,page_name,username,password):
        print(page_name,username,password)
        # driver = webdriver.Chrome()
        # loginpage = LoginPage(driver=driver)
        # loginpage.login(**data)

    # 字典
    # 单组元素
    @unittest.skip('慧')
    @data({'page_name':'login page','username': '516463257@qq.com','password': 'chris520h'})
    def test_dict_01(self, data):
        driver = webdriver.Chrome()
        loginpage = LoginPage(driver=driver)
        loginpage.login(**data)

    # 多组元素未unpack
    @unittest.skip('hui')
    @data({'page_name': 'login page', 'username': '516463257@qq.com', 'password': 'chris520h'},
           {'page_name': 'login page', 'username': 'bonnie_c520@yahoo.com', 'password': '12345678'})
    def test_dict_02(self, data):
        print(data)
        driver = webdriver.Chrome()
        loginpage = LoginPage(driver=driver)
        loginpage.login(**data)

    # 多组元素unpack
    @unittest.skip('bonnie')
    @data({'page_name': 'login page', 'username': '516463257@qq.com', 'password': 'chris520h'},
           {'page_name': 'login page', 'username': 'bonnie_c520@yahoo.com', 'password': '12345678'})
    @unpack
    def test_dict_03(self, page_name, username,password):
        driver = webdriver.Chrome()
        loginpage = LoginPage(driver=driver)
        loginpage.login(page_name,username,password)

    # 文件
    @unittest.skip("hui")
    @data(*Data(filename='login.yaml').datas)
    @unpack
    def test_file(self,a,b,c):
        print(a,b,c)
        driver = webdriver.Chrome()
        loginpage = LoginPage(driver=driver)
        loginpage.login(a, b, c)

    @file_data(os.path.join(DirConfig.testdata_dir, 'login.yaml'))
    @unpack
    def test_file(self, data):
        driver = webdriver.Chrome()
        loginpage = LoginPage(driver=driver)
        loginpage.login(*data)


