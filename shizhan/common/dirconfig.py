import os

class DirConfig:
    # root dir
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
    print(base_dir)