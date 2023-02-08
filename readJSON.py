# -*- coding: utf-8 -*-
# @Author: Admin
# @Date:   2023-2-7
# @Last Modified by:   Admin
# @Last Modified time: 2023-2-7


# 读取json文件
def read_json(fileName=""):
    import json
    if fileName!='':
        strList = fileName.split(".")
        if strList[len(strList)-1].lower() == "json":
            with open(fileName,mode='r',encoding="utf-8") as file:
                return json.loads(file.read())
