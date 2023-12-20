#!/usr/bin/env python3
# coding=utf-8


import argparse
import subprocess
from datetime import date
import os

def git_push(commit_message):
    # Git add
    subprocess.run(['git', 'add', '.'])

    # Git commit
    subprocess.run(['git', 'commit', '-m', commit_message])

    # Git push
    subprocess.run(['git', 'push'])

def main():
    parser = argparse.ArgumentParser(description="A python script that eases your git push.")

    # 添加命令行参数
    parser.add_argument('commit_message', nargs='?', default=None, help='Commit message (optional)')

    args = parser.parse_args()

    # 获取当前日期
    current_date = date.today().strftime("%y.%m.%d")

    # 设置默认提交信息
    default_commit_message = f"update {current_date}"

    # 如果有命令行参数传递，使用参数作为提交信息，否则使用默认信息
    commit_message = args.commit_message if args.commit_message else default_commit_message

    # 获取当前工作目录
    current_directory = os.getcwd()

    # 切换到当前目录下的 Git 仓库
    os.chdir(current_directory)

    # 执行 Git 操作
    git_push(commit_message)

if __name__ == "__main__":
    main()
   
