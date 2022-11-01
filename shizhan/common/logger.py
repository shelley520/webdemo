import logging
from shizhan.common.dirconfig import DirConfig as Dir
import os
import time

class FrameLog:

    def getLogger(self):

        # 创建日志器
        logger = logging.getLogger("logger")
        # 日志输出当前级别及以上级别的信息，默认日志输出最低级别是warning
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            # 创建控制台处理器 ---》输出控制台
            SH = logging.StreamHandler()
            # 创建文件处理器 ---》输出文件
            logpath = os.path.join(Dir.logs_dir,f"log_{time.strftime('%Y%m%d%H%M%S',time.localtime())}.txt")
            FH = logging.FileHandler(logpath,encoding='utf-8')
            # 日志包含哪些内容 时间 文件 日志级别：事件描述/问题描述
            formatter = logging.Formatter(fmt="[%(asctime)s] [%(filename)s] %(levelname)s :%(message)s",
                                          datefmt='%Y/%m/%d %H:%M:%S')
            logger.addHandler(SH)
            logger.addHandler(FH)
            SH.setFormatter(formatter)
            FH.setFormatter(formatter)
        return logger

    def sum(self,a,b):
        sum = a+b
        self.getLogger().info(f"实现求和：{sum}")
        return sum

if __name__ == '__main__':
    FrameLog().sum(1,2)