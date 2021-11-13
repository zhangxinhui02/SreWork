"""转换字符串为hello redrock"""
longstr = "vimlnello redrockhtml"

#转换为列表
longstr = list(longstr)

#替换前4个字符为空格
for i in range(0, 4):
    longstr[i] = ' '

#替换第5个字符为'h'
longstr[4] = 'h'

#替换后四个字符为空格
for i in range(-1, -5, -1):
    longstr[i] = ' '

#转换为字符串
newstr = "".join(longstr)

print(newstr.strip())