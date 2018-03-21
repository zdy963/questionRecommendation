# -*- coding: utf-8 -*-
import time


def write_que_bank(qid, cursor):
    cur_time = "%s" % time.strftime("%Y-%m-%d", time.localtime())
    sql = "INSERT INTO SJD_QUESTION_BANK (ID, CREATE_TIME) VALUES (%d, str_to_date(%s,'%%Y-%%m-%%d'))" % (qid, cur_time)
    cursor.execute(sql)


def write_multi_choice(qid, que_dict, cho_dict, cursor):
    sql = "INSERT INTO SJD_MULTI_CHOICE VALUES (%d, '%s', '%s', '%s', '%s', '%s',NULL,NULL,%d)"\
          % (qid,que_dict[qid][0],cho_dict[qid][0],cho_dict[qid][1],cho_dict[qid][2],cho_dict[qid][3], que_dict[qid][1])
    cursor.execute(sql)