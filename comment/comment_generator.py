import os


def traverse_files(dir_path):
    if dir_path.startswith("."):
        dir_path = os.path.abspath(dir_path)
    re = []
    files = os.listdir(dir_path)
    for file in files:
        if file.startswith("__pycache__") or file.startswith("."):
            continue
        full_path = os.path.join(dir_path, file)
        if os.path.isdir(full_path) and not file.startswith('.'):
            re.append(full_path)
            re.append(traverse_files(full_path))
        elif not file.startswith('.'):
            re.append(full_path)
    return re


import os
import time

import os
import time


def create_obsidian_page(name, content):
    """创建一个Obsidian页面"""
    # 检查文件夹是否存在,不存在则创建
    folder_path = os.environ.get("OBVAULTPATH","/Users/bytedance/Documents/Obsidian Vault")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 构造文件名和文件路径
    filename = name + ".md"
    file_path = os.path.join(folder_path, filename)

    # 打开文件,如果不存在则创建,存在则追加写
    flags = "a"
    with open(file_path, flags, encoding='utf-8') as f:
        # 添加时间戳
        timestamp = "\n\n" + time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(timestamp)

        # 添加内容
        f.write("\n\n" + content)

    print("页面更新成功!")


def create_hook(file_path,):
    pass

if __name__ == '__main__':
    import time
    create_obsidian_page("thisIsTest","aaa")
    time.sleep(2)
    create_obsidian_page("thisIsTest","bbb")