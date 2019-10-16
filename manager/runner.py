import setting
import re
from importlib import import_module


def runner(path=None,):

    if path:
        spider_name = re.search("([0-9a-zA-Z]+)\.py", path).group(1)
        setting.spider_name = spider_name
    else:
        raise ValueError("必须指定路径！")

    if path and path.endswith(".py"):
        path = path.replace("\\", '/')
        path = "spider." + path.replace("/", '.').strip(".py")

        spider_cls = import_module(path, "MySpider")
        spider = spider_cls.MySpider()
        spider.init()
        if hasattr(spider, "early"):
            spider.early()
        spider.start()


if __name__ == '__main__':
    runner("text.py")