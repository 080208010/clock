import datetime
import time

def run_clock():
    while True:
        # 获取当前时间
        now = datetime.datetime.now()
        
        # 格式化时间字符串
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        
        # 清除屏幕
        print('\033c', end='')
        
        # 输出当前时间
        print("当前时间：", current_time)
        
        # 休眠1秒
        time.sleep(1)

# 运行时钟程序
run_clock()
