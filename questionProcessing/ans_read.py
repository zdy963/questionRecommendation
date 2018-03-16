import re


# 答案在同一行
def one_line(question):
    chos = re.match('([ABCD])[.、:．：）)]\s?(.*?)\s?'
                    '([ABCD])[.、:．：）)]\s?(.*?)\s'
                    '([ABCD])[.、:．：）)]\s?(.*?)\s'
                    '([ABCD])[.、:．：）)]\s?(.*?)\n', question)
    # print(chos)
    print(chos.group(1), ":", chos.group(2))
    print(chos.group(3), ":", chos.group(4))
    print(chos.group(5), ":", chos.group(6))
    print(chos.group(7), ":", chos.group(8))


# 答案分成两行
def two_line(question):
    chos = re.match('([AC])[.、:．：）)]\s?(.*?)\s*'
                    '([BD])[.、:．：）)]\s?(.*?)\n', question)
    # print(chos)
    print(chos.group(1), ":", chos.group(2))
    print(chos.group(3), ":", chos.group(4))


# 答案分成四行
def four_line(question):
    chos = re.match('([ABCD])[.、:．：）)]\s?(.*?)\n', question)
    print(chos.group(1), ":", chos.group(2))


# 答案在同一行2
def one_line2(question,):
    chos = re.match('([ABCD])\s?(.*?)\s?'
                    '([ABCD])\s?(.*?)\s'
                    '([ABCD])\s?(.*?)\s'
                    '([ABCD])\s?(.*?)\n', question)
    # print(chos)
    print(chos.group(1), ":", chos.group(2))
    print(chos.group(3), ":", chos.group(4))
    print(chos.group(5), ":", chos.group(6))
    print(chos.group(7), ":", chos.group(8))


# 答案分成两行2
def two_line2(question):
    chos = re.match('([AC])\s?(.*?)\s*'
                    '([BD])\s?(.*?)\n', question)
    # print(chos)
    print(chos.group(1), ":", chos.group(2))
    print(chos.group(3), ":", chos.group(4))


# 答案分成四行2
def four_line2(question,):
    chos = re.match('([ABCD])\s?(.*?)\n', question)
    print(chos.group(1), ":", chos.group(2))