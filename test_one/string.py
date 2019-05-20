# part 1
#  python 也可以操作字符串 单引号(' ... '), 双引号 (" ... "),都可以获得相同的结果
#  反斜杠  \  可以用来转义


name = 'Kobe Bryant'
print(name)

# answer = "doesn't like it !"
# 那如果是一下的情况呢？ 在英文中会有一些 ' 这个符号在字符串中
# 会报错
# answer = 'doesn't like it!' 
# 我们可以这样
answer = 'doesn\'t like it !'
print(answer)  # 利用 '\' 反斜杠来进行转义


