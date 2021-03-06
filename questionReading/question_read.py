import re


# 读问题的函数
def read_ques(question,qid,que_dict):
    try:
        que_dict = ques1(question, qid,que_dict)
    except AttributeError:
        try:
            que_dict = ques2(question, qid,que_dict)
        except AttributeError:
            que_dict = no_ans(question, qid,que_dict)
    return que_dict


# 答案在（）__中 或 答案在句末
def ques1(question,qid,que_dict):
    que = re.match('\d*\S\s*?(.*?)([_（【(＿]+)\s?.?\s?([＿)】）_]+)(.*?)[ABCD]?\n', question)
    # que = re.match('\S*?\s(.*?)[（\t]?[ABCD]?[）\t]?(.*?)[ABCD]?\n', question)
    # print(que)
    ans = re.match('.*?[_（【(＿]?\s?([ABCD])\s?[＿)】）_\n]+.*?', question)
    rm_blank = que.group(1).lstrip()
    que_wri = rm_blank + que.group(2) + que.group(3) + que.group(4)
    ans_wri = ans.group(1)
    # print(" ")
    # print(qid, ".", que_wri, end="")
    # print("【", ans_wri,"】")
    que_dict[qid] = [que_wri, cho_replace(ans_wri)]
    return que_dict


# 答案前后只有空格
def ques2(question,qid,que_dict):
    que = re.match('\d*\S\s*?(.*?)\s+[ABCD]\s+(.*?)\n', question)
    # que = re.match('\S*?\s(.*?)[（\t]?[ABCD]?[）\t]?(.*?)[ABCD]?\n', question)
    ans = re.match('.*?\s+([ABCD])\s+?.*?', question)
    # print(que)
    # print(" ")
    rm_blank = que.group(1).lstrip()
    que_wri = rm_blank + que.group(2)
    ans_wri = ans.group(1)
    # print(qid, ".", que_wri, end="")
    # print("【", ans_wri,"】")
    # print(que,"ques2")
    que_dict[qid] = [que_wri, cho_replace(ans_wri)]
    return que_dict


# 没有答案
def no_ans(question, qid, que_dict):
    # try:
    #     que = re.match('\S*?\s?(\S*?)\s?[ABCD]\s?')
    que = re.match('\d*\S\s*?(.*?)\n', question)
    # print(" ")
    que_wri = que.group(1).lstrip()
    ans_wri = "None"
    # print(qid, ".", que_wri, "【无答案】")
    # print(que)
    que_dict[qid] = [que_wri, cho_replace(ans_wri)]
    return que_dict


# 用数字替换字母选项
def cho_replace(choice):
    if choice == 'A': return 1
    if choice == 'B': return 2
    if choice == 'C': return 3
    if choice == 'D': return 4
    if choice == 'None': return 0


# 去除开头带有数字的情况