import logging
import time

# 笔记 https://www.cnblogs.com/WG11/p/17409858.html
# 参考 https://blog.csdn.net/Daningliu/article/details/119684778


# 配置日志记录器
# logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.basicConfig(filename='app.log',format="[%(asctime)s] [%(levelname)s]  %(message)s [%(filename)s %(lineno)s]",
                    datefmt="%Y-%m-%d %H:%M:%S %z", level=logging.DEBUG)

# 记录调试信息
logging.debug('This is a debug message')

# 记录错误信息
try:
    a = 1 / 0
except Exception as e:
    logging.error(f'Error: {e}')

# 记录访问信息
logging.info('User "John" accessed page "/home"')

# 记录性能信息
start_time = time.time()
# 执行一些操作
end_time = time.time()
duration = end_time - start_time
logging.debug(f'Time spent in operation: {duration}s')

# 记录系统信息
import psutil
cpu_percent = psutil.cpu_percent()
memory_usage = psutil.virtual_memory().percent
# logging.debug(f'System info: CPU usage {cpu_percent}%, Memory usage {memory_usage}%')