# -*- coding: utf-8 -*-
from questionProcessing.question_read import read_ques
from questionProcessing.ans_read import one_line,two_line,four_line,one_line2,two_line2,four_line2
# from questionProcessing.write_db import write_que_bank

questions = open("./QUESTION_BANK.txt","r")
qid = 1
adots = ("A.","A、","A:","A．","A：")
status = 0
s_dot = 0

for line in questions:
    # print(status)
    if line.startswith("\n"):
        continue
    question = line.lstrip()
    if question.startswith("1."):
        read_ques(question,qid)
        # write_que_bank(qid)
        qid += 1
        status = 0
        s_dot = 0
        continue
        # seq = question.lsplit(pre.group())
        # seqq = seq.split()
        # qbsql = """INSERT INTO SJD_QUESTION_BANK (ID) VALUES(%s)"""
        # mcsql = """INSERT INTO SJD_MULTI_CHOICE (QID,QUESTION,ANSWER)
        #             VALUES (%s,)"""
    if status == 4 or s_dot == 4:
        continue
    if question.startswith(adots, status):
        # print(question)
        try:
            one_line(question)
            status += 4
            # print(chos)
        except AttributeError:
            try:
                two_line(question)
                status += 2
            except AttributeError:
                four_line(question)
                status += 1
                s_dot = 5
        continue
    if s_dot == 5:
        four_line(question)
        status += 1
        continue
    if s_dot != 5 and status == 2:
        try:
            two_line(question)
            status += 2
            continue
        except AttributeError:
            four_line(question)
            status += 1
            s_dot = 5

    if question.startswith("A"):
        # print(question)
        try:
            one_line2(question)
            s_dot += 4
            # print(chos)
        except AttributeError:
            try:
                two_line2(question)
                s_dot += 2
            except AttributeError:
                four_line2(question)
                s_dot += 1
                status = 5
    if status == 5:
        four_line2(question)
        s_dot += 1
    if status != 5 and s_dot == 2:
        try:
            two_line2(question)
            s_dot += 2
            continue
        except AttributeError:
            four_line2(question)
            s_dot += 1
            status = 5

        continue

# db.close()
