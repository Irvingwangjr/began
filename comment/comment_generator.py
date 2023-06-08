import os
import time
from tqdm import tqdm
from claude.claude import ClaudeClient
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)

client = ClaudeClient()


def _default_file_function(file_path):
    print(f"size of file {file_path}: {os.path.getsize(file_path)}")


def _default_dir_function(dir_path):
    # print(f"size of dir {dir_path}: {os.stat(dir_path).st_size}")
    pass

def traverse_files(dir_path, file_function, dir_function):
    if file_function is None:
        file_function = _default_file_function
    if dir_function is None:
        dir_function = _default_dir_function
    print(dir_path)
    if dir_path.startswith("."):
        dir_path = os.path.abspath(dir_path)
    re = []
    if not os.path.isdir(dir_path):
        file_function(dir_path)
        return re

    files = os.listdir(dir_path)
    for file in tqdm(files):
        if file.startswith("__pycache__") or file.startswith(".") or file.startswith("target"):
            continue
        full_path = os.path.join(dir_path, file)
        if os.path.isdir(full_path) and not file.startswith('.'):
            dir_function(full_path)
            traverse_files(full_path,file_function,dir_function)
        elif not file.startswith('.'):
            file_function(full_path)
    return re


def create_obsidian_page(name, content):
    """创建一个Obsidian页面"""
    # 检查文件夹是否存在,不存在则创建
    folder_path = os.environ.get("OBVAULTPATH", "/Users/bytedance/Documents/test_for_ob/test_for_llm")
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


def create_hook(file_path, ):
    pass


language_mapper = {
    "cpp": Language.CPP,
    "go": Language.GO,
    "java": Language.JAVA,
    "js": Language.JS,
    "php": Language.PHP,
    "proto": Language.PROTO,
    "python": Language.PYTHON,
    "rst": Language.RST,
    "ruby": Language.RUBY,
    "rust": Language.RUST,
    "scala": Language.SCALA,
    "swift": Language.SWIFT,
    "latex": Language.LATEX,
    "html": Language.HTML
}


def fake_file_function_code_explain(file_path: os.path):
    prompt = "解释上述代码，并用markdown格式输出"
    file_type = os.path.splitext(file_path)[1][1:]
    file_type_lang = language_mapper.get(file_type)
    if file_type_lang is None:
        return
    else:
        print(file_path)


def file_function_code_explain(file_path: os.path):
    prompt = "解释上述代码，并用markdown格式输出"
    file_type = os.path.splitext(file_path)[1][1:]
    file_type_lang = language_mapper.get(file_type)
    if file_type_lang is None:
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

        code_splitter = RecursiveCharacterTextSplitter.from_language(
            language=file_type_lang, chunk_size=7000, chunk_overlap=1000
        )
        code_doc = code_splitter.create_documents([content])
        content = []
        for code_block in code_doc:
            result = client.chat(code_block.page_content + "\n" + prompt)
            parse_result = result.replace("\\n", "\n")
            content.append(parse_result[1: -1])
        print(f"finish for file {file_path}\n")
        file_result = "\n\n\n".join(content)
        obsidian_name = file_path.split("/")[-1]
        create_obsidian_page(obsidian_name, file_result)


if __name__ == '__main__':
    traverse_files("/Users/bytedance/workspace/src/cromwell_bd/cromwell/common/src/main/scala/common", file_function=file_function_code_explain,
                   dir_function=_default_dir_function)
