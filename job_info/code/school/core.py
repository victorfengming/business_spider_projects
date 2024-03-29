#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

from usual_spider import *
from info_dict import *


def get_main_page_title_and_link(curr_college,url):
    '''
    获取主页标题和链接
    传当前学校进来,返回标题列表和链接列表
    :param curr_college:
    :return:
    '''
    # print("-"*80)
    # print("一共有", len(college_info),"个学校 :")
    # 实例化主页信息类对象
    # print("当前是--->",curr_college)
    # print(college_info[curr_college]["base_url"])
    # print("-"*80)
    info = college_info[curr_college]
    # 2.    调用主页对象中的获取标题和连接的方法
    # 返回的结果为    标题数组和    链接数组
    # 要是url有,就用url
    # 要是没有,就是原来的
    if url:
        # TODO 这里用下一页的url
        mpi = MainPageInfo(url, info["base_url"], info["find_pattern_dict"])
    else:
        mpi = MainPageInfo(info["url"], info["base_url"], info["find_pattern_dict"])
    # 标题列表
    title_list = mpi.get_every_title()
    # print("-" * 80)
    # print("标题获取成功")
    # print("一共有：",len(title_list),"个标题")
    # print("-" * 80)
    # for i in title_list:
    # print(i)

    # 链接列表
    link_list = mpi.get_single_page_link()
    # print("-"*80)
    # print("链接获取成功")
    # print("一共有：",len(link_list),"个链接")
    # print("-"*80)

    # for i in link_list:
    # print(i)
    next_link = mpi.get_next_link()
    print('-'*80)
    print("下一个链接是:")
    print(next_link)
    print('-'*80)
    return title_list, link_list, next_link


def download_single_collage_info(curr_college):

    # 先定义好数据列表
    data_list = []
    url = ''

    while True:
        # 在里面是通过每个学校的名字实例化主页信息对象
        main_info_list = get_main_page_title_and_link(curr_college,url)
        # 返回两个为元组类型数据,再进行数据的拆分
        title_list = main_info_list[0]
        link_list = main_info_list[1]
        next_link = main_info_list[2]

        # 5. 构造data数据,字典格式,key为序号,value为当前行数据的内容列表
        #     其中包括标题信息和手机号电话号列表
        data = {

        }

        # 3.    写一个总循环, 同步循环标题和链接
        for i in range(0, len(link_list)):
            # 实例化一个rf对象，
            rf = ReFind(link_list[i])
            # 4.  调用refind对象中的匹配手机号方法,
            mobile_list = rf.get_mobile_num()
            # 4.  调用refind对象中的匹配座机号方法,
            tel_list = rf.get_tel_num()
            # 4.2.  调用refind对象中的匹配邮箱方法,
            email_list = rf.get_email()
            # 定义当前行数据,先等于一个标题再说
            curr_row = [title_list[i]]
            # 遍历移动手机号码,每一条数据(单元格)是一个号码
            for mobile in mobile_list:
                if len(curr_row) >= 2:
                    break
                curr_row.append(mobile)

            # 遍历座机号码,每一条数据(单元格)是一个号码
            for tel in tel_list:
                if len(curr_row) >= 2:
                    break
                curr_row.append(tel)
                # 保证有两个电话号

            # 要是数据不够长,就追加值
            if len(curr_row) == 1:
                curr_row.append('')
            #     curr_row.append('')
            #     curr_row.append('')
            # if len(curr_row) == 2:
            #     curr_row.append('')
            #     curr_row.append('')
            # if len(curr_row) == 3:
            #     curr_row.append('')
            # 遍历座机号码,每一条数据(单元格)是一个邮箱
            for email in email_list:
                curr_row.append(email)
                # 限制数据量
                if len(curr_row) >= 3:
                    break
            # print("-" * 80)
            # print("当前数据为")
            # print(curr_row)
            # print("-" * 80)
            data[i + 1] = curr_row
            # 实例数据格式:
            # data = {
            #     1:['首都医学院','13930206059','13567542345','400-88884839','400-56781235']
            # }
            # print("-" * 80)
            # print("成功准备第", i, "条数据")
            # print("-" * 80)

        # 6. 学校名称作为文件名filename, data作为代保存数据
        file_name = curr_college
        # print("-" * 80)
        # print("-----------------------------------数据为-------------------------------")
        # print(data)
        # print("-" * 80)

        # 保存数据
        data_list.append(data)

        # 判断下一个链接,要是有,循环回去
        if next_link:
            url = next_link
        else:
            break

    save_data_to_xls(file_name, data_list)

    # 暂时就循环一次,用于测试
    # break


if __name__ == '__main__':
    '''
    思路规划
    1. 循环所有的学校信息
    在里面是通过每个学校的名字实例化主页信息对象
    2.调用主页对象中的获取标题和连接的方法
    返回的结果为 标题数组 和 链接数组
    3. 写一个总循环,同步循环标题和链接
    4. 实例化一个rf对象，调用refind对象中的匹配手机号方法,
    其中,链接列表的内容作为参数,    返回移动电话号列表和座机号列表
    5. 构造data数据,字典格式,key为序号,value为当前行数据的内容列表
    其中包括标题信息和手机号电话号列表
    6. 学校名称作为文件名filename,data作为代保存数据
    7. 调用save_data_to_xls方法, 将构造的数据保存到表格文档中
    '''
    # 1. 循环所有的学校信息
    # for curr_college in college_info.keys():
    #     try:
    #         download_single_collage_info(curr_college)
    #     except:
    #         print('-'*80)
    #         print("网站响应异常:"+curr_college)
    #         print('-'*80)
    # download_single_collage_info('赣南医学院')
    #
    #

    while True:
        # print('-'*50)
        i = 0
        print('-' * 80)
        for curr_college in college_info.keys():
            i += 1
            print('|', i, '\t|', curr_college.ljust(20, ' '))
        print('-' * 80)
        choice_num = input('请选择学校(序号) :')
        if choice_num.isdigit():
            choice_num = int(choice_num)
        else:
            print("输入有误,请输入数字!")
            continue

        if choice_num in range(1, len(college_info.keys()) + 1):
            pass
        else:
            print("输入序号不在范围,请重新输入!")
            continue

        choice_college = list(college_info.keys())[choice_num - 1]
        # print('-'*80)
        # if choice_college == '0':
        #     print('掰掰┏(＾0＾)┛')
        #     break
        # elif choice_college in college_info.keys():
        #     try:
        #         print('正在抓取,请稍后...')
        #         download_single_collage_info(choice_college)
        #     except:
        #         print('-' * 80)
        #         print("网站响应异常:" + choice_college + "\t抓取数据失败!")
        #         print('-' * 80)
        # else:
        #     print('-' * 80)
        #     print('您输入的序号不正确,请重新输入!')
        #     print('-' * 80)
        try:
            print('正在抓取,请稍后...')
            download_single_collage_info(choice_college)
        except:
            print('-' * 80)
            print("网站响应异常:" + choice_college + "\t抓取数据失败!")
            print('-' * 80)

    # download_single_collage_info('安徽医科大学')
    # print(len(college_info.keys()))
