# -*- coding: UTF-8 -*-
# @Project ：Self_use_module
# @File    ：get_data.py
# Author   ：0xsdeo
# Date     ：2024/8/9 上午9:38

def generate_data(file_name):
    """

    :param file_name: 传入文件名
    :return: 以数组形式返回数据
    """
    with open(file_name, 'r', encoding='utf-8') as _:
        data = _.readlines()

    index = 0
    for i in data:
        data[index] = i.replace("\n", "")
        index += 1

    count = data.count('')

    while count:  # 清除空字符
        index = data.index('')
        del data[index]
        count -= 1

    return data

