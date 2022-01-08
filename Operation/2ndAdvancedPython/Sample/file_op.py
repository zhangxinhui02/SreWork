"""
open(file=,mode=,encoding=)
"""

# 以字节为单位读写
with open("./testfile/test.txt",mode="ab+") as f:
    # 对文件的操作
    print(f.read())
    # f.write("\nhahahha".encode("utf-8"))

# 以字符为单位读写
# with open("./testfile/test.txt",mode="a+",encoding="utf-8") as f:
#     print(f.read())
    # f.write("\n112233")
    