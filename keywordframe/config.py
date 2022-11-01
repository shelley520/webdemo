import os

class DirConfig:
    # root dir
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # testcase dir
    testcases_dir = os.path.join(base_dir,"testcases")
    # test report dir
    report_dir = os.path.join(base_dir,"Outputs/report")
    # test data dir
    testdata_dir = os.path.join(base_dir,"testdatas")
    # log dir
    logs_dir = os.path.join(base_dir,"Outputs/logs")
    # screenshot dir
    screen_dir = os.path.join(base_dir,"Outputs/screenshots")
    # excel keywordcol
    keywordcol = 3
    # excel operator colactioncol
    actioncol = 6
    #
    actionTimecol = 7
    # 用例汇总表名称
    casessheetname = '用例汇总'
    # 汇总表是否执行所在列
    caseIsExcuetecol = 5
    # 汇总表中操作步骤名的名称
    caseNamecol = 4
    # 用例测试steps的执行result
    casestepresult = 8
    # 用例执行result
    caseresultcol=7
    # 汇总表用例名称
    casestepnamecol=4

if __name__ == '__main__':
    print(DirConfig.testdata_dir)