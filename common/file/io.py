import yaml
""""
    io 工具类
"""


def load_yml(path=""):
    """"
    @path  文件路径
    """
    data = {}
    with open(path, mode="r", encoding="utf-8") as f:
        data = yaml.load(f)
    return data
