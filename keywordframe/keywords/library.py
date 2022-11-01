import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from keywordframe.common.logger import FrameLog

class Library:

    logger = FrameLog().getLogger()

    def open_browser(self,browser):
        browser = browser.capitalize()
        # webdriver.Chrome()
        try:
            self.driver = getattr(webdriver,browser)()
            self.logger.info(f"打开{browser}浏览器")
        except:
            self.logger.error(f"无法打开{browser}浏览器")
        # if browser == 'chrome':
        #     self.driver = webdriver.Chrome()
        # elif browser == 'ie':
        #     self.driver = webdriver.Ie()
        # elif browser == 'firefox':
        #     self.driver = webdriver.Firefox()

    def load_url(self,url):
        try:
            self.driver.get(url)
            self.logger.info(f"加载项目地址{url}")
        except:
            self.logger.error(f"无法加载项目地址{url}")

    def sleep(self,s):
        time.sleep(s)

    def locator(self,type,express):
        try:
            el = self.driver.find_element(type,express)
            self.logger.info(f"查找元素{type,express}成功")
            return el
        except:
            self.logger.error(f"无法查找元素{type,express}")


    def input(self,type,express,value):
        try:
            self.locator(type,express).send_keys(value)
            self.logger.info(f"操作元素{type,express}成功，输入{value}正确")
        except:
            self.logger.error(f"操作元素{type,express}不成功，输入{value}错误")

    def click(self,type,express):
        try:
            self.locator(type,express).click()
            self.logger.info(f"点击元素{type,express}成功")
        except:
            self.logger.error(f"点击元素{type,express}未成功")

    def move_element(self,type,express):
        try:

            el=self.locator(type,express)
            ActionChains(self.driver).move_to_element(el).perform()
            self.logger.info(f"移到元素{type,express}成功")
        except:
            self.logger.error(f"移到元素{type,express}未成功")

    def run(self,keyword,*args):
        # 基于反射调用关键字函数
        getattr(self,keyword)(*args)

    def assertEqual(self,type,express,expect):
        el = self.locator(type,express)
        fact = el.text
        if fact != expect:
            raise Exception(f'assertText:{fact}!={expect}')
        else:
            pass


if __name__ == '__main__':
    hui = Library()
    hui.run("open_browser","chrome")