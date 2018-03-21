import re


# 答案在同一行且选项后有标点
def one_line(question, qid, cho_dict):
    chos = re.match('[(（]?([ABCD])\s?[.、:．：）)]\s?(.*?)\s?'
                    '[(（]?([ABCD])\s?[.、:．：）)]\s?(.*?)\s'
                    '[(（]?([ABCD])\s?[.、:．：）)]\s?(.*?)\s'
                    '[(（]?([ABCD])\s?[.、:．：）)]\s?(.*?)\n', question)
    # print(chos,"way1.1")
    # print(chos.group(1), ":", chos.group(2))
    # print(chos.group(3), ":", chos.group(4))
    # print(chos.group(5), ":", chos.group(6))
    # print(chos.group(7), ":", chos.group(8))
    cho_dict[qid] = [chos.group(2).strip(),chos.group(4).strip(),chos.group(6).strip(),chos.group(8).strip()]
    return cho_dict


# 答案分成两行且选项后有标点
def two_line(question,qid,cho_dict):
    chos = re.match('([ABCD])\s?[.、:．：）)]\s?(.*?)\s*'
                    '([ABCD])\s?[.、:．：）)]\s?(.*?)\n', question)
    # print(chos,"way1.2")
    # print(chos.group(1), ":", chos.group(2))
    # print(chos.group(3), ":", chos.group(4))
    if chos.group(1) == 'A':
        cho_dict[qid] = [chos.group(2).strip(), chos.group(4).strip()]
    else:
        cho_dict[qid].extend([chos.group(2).strip(),chos.group(4).strip()])
    return cho_dict


# 答案分成四行且选项后有标点
def four_line(question,qid,cho_dict):
    chos = re.match('([ABCD])\s?[.、:．：）)]\s?(.*?)\n', question)
    # print(chos,"way1.3")
    # print(chos.group(1), ":", chos.group(2))
    if chos.group(1) == 'A':
        cho_dict[qid] = [chos.group(2).strip()]
    else:
        cho_dict[qid].append(chos.group(2).strip())
    return cho_dict


# 答案在同一行2且无标点
def one_line2(question,qid,cho_dict):
    chos = re.match('([ABCD])\s?(.*?)\s?'
                    '([ABCD])\s?(.*?)\s'
                    '([ABCD])\s?(.*?)\s'
                    '([ABCD])\s?(.*?)\n', question)
    # print(chos,"way2.1")
    # print(chos.group(1), ":", chos.group(2))
    # print(chos.group(3), ":", chos.group(4))
    # print(chos.group(5), ":", chos.group(6))
    # print(chos.group(7), ":", chos.group(8))
    cho_dict[qid] = [chos.group(2).strip(),chos.group(4).strip(),chos.group(6).strip(),chos.group(8).strip()]
    return cho_dict


# 答案分成两行2且无标点
def two_line2(question,qid,cho_dict):
    chos = re.match('([ABCD])\s?(.*?)\s*'
                    '([ABCD])\s?(.*?)\n', question)
    # print(chos, "way2.2")
    # print(chos.group(1), ":", chos.group(2))
    # print(chos.group(3), ":", chos.group(4))
    if chos.group(1) == 'A':
        cho_dict[qid] = [chos.group(2).strip(), chos.group(4).strip()]
    else:
        cho_dict[qid].extend([chos.group(2).strip(),chos.group(4).strip()])
    return cho_dict


# 答案分成四行2且无标点
def four_line2(question,qid,cho_dict):
    chos = re.match('([ABCD])\s?(.*?)\n', question)
    # print(chos, "way2.3")
    # print(chos.group(1), ":", chos.group(2))
    if chos.group(1) == 'A':
        cho_dict[qid] = [chos.group(2).strip()]
    else:
        cho_dict[qid].append(chos.group(2).strip())
    return cho_dict