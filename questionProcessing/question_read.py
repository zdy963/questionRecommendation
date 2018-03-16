import re



# 读问题的函数
def read_ques(question,qid):
    try:
        ques1(question, qid)
    except AttributeError:
        try:
            ques2(question, qid)
        except AttributeError:
            no_ans(question, qid)


# 答案在（）__中 或 答案在句末
def ques1(question,qid):
    que = re.match('\S*?\s(.*?)([_（【(＿]+)\s?.?\s?([＿)】）_]+)(.*?)[ABCD]?\n', question)
    # que = re.match('\S*?\s(.*?)[（\t]?[ABCD]?[）\t]?(.*?)[ABCD]?\n', question)
    # print(que)
    ans = re.match('.*?[_（【(＿]?\s?([ABCD])\s?[＿)】）_\n]+.*?', question)
    rm_blank = que.group(1).lstrip()


    # print(" ")
    # print(qid, ".", rm_blank + que.group(2), "QAQ", que.group(3) + que.group(4), end="")
    # print("【", ans.group(1),"】")


# 答案前后只有空格
def ques2(question,qid):
    que = re.match('\S*?\s(.*?)\s+[ABCD]\s+(.*?)\n', question)
    # que = re.match('\S*?\s(.*?)[（\t]?[ABCD]?[）\t]?(.*?)[ABCD]?\n', question)
    # print(que)
    print(" ")
    print(qid, ".", que.group(1), "QAQ", que.group(2), end="")
    ans = re.match('.*?\s+([ABCD])\s+?.*?', question)
    print("【", ans.group(1),"】")
    print(que,"ques2")


# 没有答案
def no_ans(question, qid):
    # try:
    #     que = re.match('\S*?\s?(\S*?)\s?[ABCD]\s?')
    que = re.match('\S*?\s(.*?)\n', question)
    print(" ")
    print(qid, ".", que.group(1), "【无答案】")
    print(que)