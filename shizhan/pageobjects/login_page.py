import warnings
from time import sleep
from shizhan.pagelocation.login_page_locs import LoginPageLoc as Locs
from shizhan.base.basepage import BasePage
from shizhan.testdatas import Global_Datas as GlobalData

class LoginPage(BasePage):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self):
        self.driver.close()

    def login(self,page_name,username,password):
        # 实现登陆的步骤
        self.driver.get(GlobalData.login_url)
        # 输入用户名
        self.input(page_name=page_name,loc=Locs.el_username,value=username)
        # 输入password
        self.input(page_name=page_name,loc=Locs.el_password,value=password)
        # 点击登陆
        self.click(page_name=page_name,loc=Locs.el_login)

        sleep(3)


class GoodListPage(BasePage):
    pass