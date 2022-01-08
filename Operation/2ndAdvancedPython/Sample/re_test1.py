import re
 
# 目标:想匹配到Cats和smarter
line = """
****
Cats are smarter than dogs
"""

"""
调用方式: match(pattern,string)
         search(pattern,string)
"""
# 正则表达式
pattern = r'(C.*) are (.*) .*'  # 原始字符串:python就不会解析里面的\n之类的东西
# 进行搜索
searchObj = re.search(pattern,line)

# 对搜索结果进行获取与判断
if searchObj:
    # 使用.group(n)来返回匹配到的内容
    print("group(): ", searchObj.group()) # 不加数字或n=0表示返回全部匹配
    print("group(1)", searchObj.group(1)) # 加字母表示匹配正则中()里的内容
    print("group(2)", searchObj.group(2))
    print("span",searchObj.span())
else:
    print("Nothing found!!")