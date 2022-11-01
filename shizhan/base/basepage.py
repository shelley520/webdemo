import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from shizhan.common.dirconfig import DirConfig as Dir
from shizhan.common.logger import FrameLog as log


class BasePage:

    """
    BasePage: 每个页面的相同属性和方法
    相同属性：获取浏览器驱动对象
    相同方法：元素查询，点击，输入...等操作
    """


    def __init__(self,driver:webdriver):
        self.driver = driver

    def locator(self,page_name,loc):
        # loc = (By.LINK_TEXT,"登陆")
        try:
            el = self.driver.find_element(*loc)
            log().getLogger().info(f"在[{page_name}],找到元素{loc}")
        except:
            log().getLogger().error(f"在[{page_name}],未找到元素{loc}")
            self.save_page_shot(page_name)
            raise
        return self.driver.find_element(*loc)

    # 等待元素可见
    def wait_ele_visibility(self,page_name,loc,timeout=15,poll_fre=0.5):
        try:
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.visibility_of_all_elements_located(loc))
            log().getLogger().info(f"在[{page_name}],元素{loc}可见")
        except:
            log().getLogger().error(f"在[{page_name}],元素{loc}不可见")
            raise

    # 等待元素存在
    def wait_ele_presence(self, page_name,loc,timeout=15,poll_fre=0.5):
        try:
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.presence_of_all_elements_located(loc))
            log().getLogger().info(f"在[{page_name}],找到元素{loc}")
        except:
            log().getLogger().error(f"在[{page_name}],找不到元素{loc}")
            raise

    # 等待元素可点击
    # def wait_ele_clickable(self,loc,timeout=15,poll_fre=0.5):
    #     WebDriverWait(self.driver,timeout,poll_fre).until(EC.element_to_be_clickable(loc))

    def input(self,page_name,loc,value):
        # 等待元素可见
        try:
            self.wait_ele_visibility(page_name,loc)
            self.locator(page_name,loc).send_keys(value)
            log().getLogger().info(f"在[{page_name}],元素{loc}输入成功")
        except:
            log().getLogger().error(f"在[{page_name}],元素{loc}输入不成功")
            self.save_page_shot(page_name)
            raise

    def click(self,page_name,loc):
        try:
            self.wait_ele_visibility(page_name,loc)
            self.locator(page_name,loc).click()
            log().getLogger().info(f"在[{page_name}],元素{loc}点击成功")
        except:
            log().getLogger().error(f"在[{page_name}],元素{loc}点击不成功")
            self.save_page_shot(page_name)
            raise

    def sleep(self,s):
        time.sleep(s)

    def move_element(self,page_name,loc):
        try:
            self.wait_ele_visibility(page_name,loc)
            ActionChains(self.driver).move_to_element(self.locator(page_name,loc)).perform()
            log().getLogger().info(f"在[{page_name}],移动到元素{loc}成功")
        except:
            log().getLogger().error(f"在[{page_name}],移动到元素{loc}不成功")
            self.save_page_shot(page_name)
            raise

    def save_page_shot(self,img_name):
        filename = os.path.join(Dir.screen_dir,img_name+'.png')
        self.driver.save_screenshot(filename)
        log().getLogger().info(f"执行错误，截图当前页面，存储的路径：{filename}")