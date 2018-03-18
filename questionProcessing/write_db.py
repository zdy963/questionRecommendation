import pymysql
import time

cur_time = time.strftime("%Y-%m-%d", time.localtime())

def write_que_bank(qid, cursor):
    sql = """INSERT INTO SJD_QUESTION_BANK (ID, CREATE_TIME) VALUES (%d, %s)""" % (qid, cur_time)
    cursor.execute(sql)


def write_question(qid,cursor,question):
    sql = "INSERT INTO SJD_MULTI_CHOICE (QID, QUESTION) VALUES (%d, %s)"% (qid,question)
    cursor.execute(sql)


def write_choices(qid,cursor,ans_num, ans):
    sql = "INSERT INTO SJD_MULTI_CHOICE(SELECTION_%s) VALUES (%s) WHERE QID = %d" % (ans_num, ans,qid)
    cursor.execute(sql)


def write_ans(qid,cursor,ans):
