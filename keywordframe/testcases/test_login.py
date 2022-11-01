import unittest
from ddt import ddt,data
from keywordframe.common.excel_operater import Excel_Operator
from keywordframe.config import DirConfig
from keywordframe.keywords.library import Library

@ddt
class TestLogin(unittest.TestCase):
    excel = Excel_Operator()

    casedata = excel.get_casesdata()
    @data(*casedata)
    def test_login_03(self,casedata):
        stepdatas = casedata["stepdata"]
        casename = casedata["casename"]
        print(stepdatas)
        print(casename)
        lib = Library()
        for index,stepdata in enumerate(stepdatas):
            print('*************')
            print(index,stepdata)
            print(type(index))
            try:
                lib.run(*stepdata)
                # 写入测试step执行的时间
                self.excel.write_step_time(casename,index+2)
                # 写入测试steps的result为pass，工作表名称，行
                # write_step_result() sheet.cell(行=8).value=pass
                self.excel.write_step_result(sheetname=casename,row=index+2,col=DirConfig.casestepresult,result="PASS")
            except Exception as error:
                # write_step_result() sheet.cell(行=8).value=value
                self.excel.write_step_result(sheetname=casename, row=index+2, col=DirConfig.casestepresult, result="FALSE")
        # 把测试result写入汇总表
        self.excel.write_case_result()

    # @unittest.skip('hui')
    # def test_login_01(self):
    #     """
    #     基于关键字
    #     :return:
    #     """
    #     he = Library()
    #     he.open_browser('chrome')
    #     he.load_url(url='')
    #     he.input(loc='',value='')
    #     he.input(loc='', value='')
    #     he.click(loc='')
    #
    # @unittest.skip('慧')
    # def test_login_02(self):
    #     el_username=()
    #     el_password=()
    #     el_login=()
    #     lib = Library()
    #     lib.run()
    #     lib.run()
    #     lib.run()
    #     lib.run()
    #     lib.run()
