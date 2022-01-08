import re

Str = """
apple! and peer!
ndioasdsa
eqwre3213_-+=
xszcv*&
312123!
"""
pattern = r"(apple).*(peer!)"
# 获取第一个分组
print(re.search(pattern,Str).group(1))
# 获取第二个分组
print(re.search(pattern,Str).group(2))

