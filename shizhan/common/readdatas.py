import os
import yaml
from shizhan.common.dirconfig import DirConfig
import jsonpath

class Data:
    def __init__(self,key=None,filename="login.yaml"):
        filepath = os.path.join(DirConfig.testdata_dir, filename)
        print(filepath)
        with open(filepath) as yaml_file:
            self.datas = yaml.load(yaml_file, Loader=yaml.FullLoader)
            # 获取字典某个key的value datas.get(key) 等同 data[key]
            if key != None:
                self.data = jsonpath.jsonpath(self.datas,f"$..{key}")



def readYaml(key,filename="testdatas.yaml"):
    filepath = os.path.join(DirConfig.testdata_dir,filename)
    with open(filepath) as yaml_file:
        datas = yaml.load(yaml_file,Loader=yaml.FullLoader)
        # 获取字典某个key的value datas.get(key) 等同 data[key]
        data = datas.get(key)
    return data

if __name__ == '__main__':

    data = Data().datas
    print(*data)