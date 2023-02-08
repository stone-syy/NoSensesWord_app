#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author: Mr.shi
# version: 1.0
# description: 废话文学生成APP，请勿当真

import os
import random
import sys
import readJSON
from time import strftime
from tkinter import messagebox, Button, Label, Entry, Tk


# 资源文件目录访问
def source_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 修改当前工作目录，使得资源文件可以被正确访问
cd = source_path('')
os.chdir(cd)

# 读取json文件
data = readJSON.read_json("data.json")
famous_word = data["famous"]  # a代表after_word，b代表before_word
after_word = data["before"]  # 在famous_word前面弄点useless_word
before_word = data['after']  # 在famous_word后面弄点useless_word
useless_word = data['bosh']  # 代表文章主要useless_word来源
repetition_times = 1


def detect_cycle(word_list):
    """
    循环遍历data.json文件,生成器
    """
    global repetition_times
    pond = list(word_list) * repetition_times
    while True:
        random.shuffle(pond)
        for content in pond:
            yield content


next_useless_word = detect_cycle(useless_word)
next_famous_word = detect_cycle(famous_word)


def add_famous_word():
    """
    添加点名人名言
    """
    global next_famous_word
    words = next(next_famous_word)
    words = words.replace("a", random.choice(after_word))
    words = words.replace("b", random.choice(before_word))
    return words


def else_paragraph():
    """
    开启下一段函数
    """
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx


def context_make():
    """
    文章生成函数
    """
    context_subject = content_input.get()
    if context_subject == '':
        messagebox.showinfo(title='提示', message="请输入文章主题")
        pass
    else:
        for word in context_subject:
            context = str()
            while (len(context)) < 5000:
                random_number = random.randint(0, 100)
                if random_number < 10:
                    context += else_paragraph()
                elif random_number < 50:
                    context += add_famous_word()
                else:
                    context += next(next_useless_word)
            context = context.replace("x", context_subject)
            # print(context)
            return context


# 主函数+持久化输出到TXT文档
def main():
    """
    输出文章到TXT文档，路径为EXE文件同级目录下
    """
    try:
        file_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        with open(file_path+'/'+content_input.get()+'.txt', 'w+',
                  encoding='utf-8', newline='') as file:
            if file.write(context_make()):
                messagebox.showinfo(title='信息', message='文章输出成功，路径:%s' % file_path)
    except Exception as e:
        messagebox.showerror(title='报错', message="Error \t\n Reason: %s" % e)


# 退出功能函数
def exits():
    sys.exit(0)


# 重置功能函数
def reset():
    if content_input.get() == '':
        pass
    else:
        content_input.delete(first=0, last=1000)


# 打印时间函数
def print_time():
    """
    打印时间函数，每一秒刷新一次
    """
    clock.config(text=strftime("%Y-%m-%d %H:%M:%S"))
    clock.after(1000, print_time)


# GUI界面配置
window = Tk()
window.title('废话文学生成器V1.0')
window.geometry("300x200+600+300")
window.iconbitmap('happy_icon.ico')
window.resizable(False, False)
input_label = Label(window, text='请在下边输入文章主题:', font=('仿宋体', 12, 'bold'))
content_input = Entry(window, width=35, font=('仿宋体', 12))
welcome = Label(window, text='欢迎你: %s' % os.getlogin(), font=('仿宋体', 15))
clock = Label(window, font=('Arial black', 15))
start_button = Button(window, text='开始运行', font=('仿宋体', 12, 'bold'), command=main)
reset_button = Button(window, text='重置内容', font=('仿宋体', 12, 'bold'), command=reset)
exit_button = Button(window, text='退出程序', font=('仿宋体', 12, 'bold'), command=exits)
# 窗口布局
input_label.pack()
content_input.pack()
start_button.place(x=5, y=65)
reset_button.place(x=110, y=65)
exit_button.place(x=215, y=65)
welcome.place(x=80, y=120)
clock.place(x=55, y=150)
print_time()
window.mainloop()
