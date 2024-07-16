#!/usr/bin/env python3

import os

def rename_files_with_start(directory):
    """重命名目录下所有文件，加上文件开头的内容"""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            title, _ = os.path.splitext(file_path)
            title = title[4:]
            with open(file_path, 'r+', encoding='utf-8') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(f"{title}\n\n{content}")

# 替换成你的目录路径
directory_path = 'tmp/'

rename_files_with_start(directory_path)
