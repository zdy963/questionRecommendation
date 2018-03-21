# -*- coding: utf-8 -*-
import pymysql
from questionReading.question_read import read_ques
from questionReading.ans_read import one_line,two_line,four_line,one_line2,two_line2,four_line2
from questionReading.write_db import write_que_bank, write_multi_choice

questions = open("../question1.txt","r")
qid = 186
adots = ("A.","A、","A:","A．","A：")
cho_a = ("(A", "（A")
num = ("1","2","3","4","5","6","7","8","9")
status = 0
s_dot = 0
que_dict = {qid:["ImQue","ImAns"]}                          # 存储题干和正确选项的字典
cho_dict = {qid:["ImChoA","ImChoB","ImChoC","ImChoD"]}   # 存储选项的字典
unfinished = []

db = pymysql.connect(host = "127.0.0.1",user = "root", passwd = "admin",db =  "question", charset = "utf8")
cursor = db.cursor()

for line in questions:
    # 若本行为空
    if line.startswith("\n"):
        continue
    question = line.lstrip()
    # 若本行以题号格式开头，则读取题干和答案
    if question.startswith(num):
        if status == 4 or s_dot == 4:
            print(qid, "Done")
        else:
            print("【UNFINISHED】")
            unfinished.append(qid)
        qid += 1
        que_dict = read_ques(question, qid, que_dict)
        # write_que_bank(qid,cursor)
        # print(qid)
        status = 0
        s_dot = 0
        continue

    # 若4个选项已经读完
    if status == 4 or s_dot == 4:
        # print("Skip")
        continue
    # 若选项后有标点分隔
    if question.startswith(adots, status):
        # print(question)
        try:
            cho_dict = one_line(question, qid, cho_dict)
            status += 4
            # print(chos)
        except AttributeError:
            try:
                cho_dict = two_line(question, qid, cho_dict)
                status += 2
            except AttributeError:
                cho_dict = four_line(question, qid, cho_dict)
                status += 1
                s_dot = 5
        continue
    # 若上一行有两个选项
    if s_dot == 5:
        cho_dict = four_line(question, qid, cho_dict)
        status += 1
        continue
    # 若上一行有两个选项
    if s_dot != 5 and status == 2:
        try:
            cho_dict = two_line(question, qid, cho_dict)
            status += 2
            continue
        except AttributeError:
            cho_dict = four_line(question, qid, cho_dict)
            status += 1
            s_dot = 5

    # 若选项后无标点分隔
    if question.startswith("A"):
        # print(question)
        try:
            cho_dict = one_line2(question, qid, cho_dict)
            s_dot += 4
            # print(chos)
        except AttributeError:
            try:
                cho_dict = two_line2(question, qid, cho_dict)
                s_dot += 2
            except AttributeError:
                cho_dict = four_line2(question, qid, cho_dict)
                s_dot += 1
                status = 5
        continue
    if status == 5:
        cho_dict = four_line2(question, qid, cho_dict)
        s_dot += 1
    if status != 5 and s_dot == 2:
        try:
            cho_dict = two_line2(question, qid, cho_dict)
            s_dot += 2
            continue
        except AttributeError:
            cho_dict = four_line2(question, qid, cho_dict)
            s_dot += 1
            status = 5

        continue


questions.close()

# print(unfinished)


# 写入数据库

for i in range(187,qid):
    # print("【题目", i,  "】【答案", que_dict[i][1], "】")
    # print(que_dict[i][0])
    # print(cho_dict[i])
    # print("")
    write_que_bank(i, cursor)
    write_multi_choice(i, que_dict,cho_dict, cursor)


db.commit()
cursor.close()
db.close()