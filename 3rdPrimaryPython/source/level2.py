"""解码指定的凯撒密码"""

# 位移值应当为9，结果为"can you finish level3?"


def get_new_ord(sec_ord, num):
    """对输入的字母对应的ASCII列表进行指定的位移。参数：字符串对应的ASCII列表,位移值"""
    new_ord = []
    for item in sec_ord:
        if item in range(65, 91):
            add_num = item + num
            if add_num <= 90:
                new_num = add_num
            else:
                new_num = add_num - 90 + 64
            new_ord.append(new_num)
        elif item in range(97, 123):
            add_num = item + num
            if add_num <= 122:
                new_num = add_num
            else:
                new_num = add_num - 122 + 96
            new_ord.append(new_num)
        else:
            new_ord.append(item)
            continue
    return new_ord


def decrype(sec_str, num):
    """解密凯撒密码并输出结果。参数：加密的字符串,位移数(若为0则输出全部结果)"""
    sec_list = list(sec_str)
    sec_ord = []

    for item in sec_list:
        sec_ord.append(ord(item))

    if num != 0:
        new_list = []
        new_ord = get_new_ord(sec_ord, num)
        for item in new_ord:
            new_list.append(chr(item))
        print("".join(new_list))
    else:
        for i in range(1, 27):
            new_list = []
            new_ord = get_new_ord(sec_ord, i)
            for item in new_ord:
                new_list.append(chr(item))
            print("".join(new_list))


if __name__ == "__main__":
    sec_str = "tre pfl wzezjy cvmvc3?"
    print("\n凯撒密码解密程序")
    print("准备解密字符串：")
    print(sec_str + "\n")
    while True:
        num = input("输入位移值(要打印全部结果请输入0)：")
        try:
            num = int(num)
            decrype(sec_str, num)
        except ValueError:
            print("输入错误！")

