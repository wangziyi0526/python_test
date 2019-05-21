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

#part 2
# \n 换行符  
message = 'Kobe \nBryant'
print(message)

path = 'C:\name'
print(path)
print(r'C:\name')

# 字符串拼接
a = 'vue'
print(a * 3 + '.js')

# 根据字符串的索引去查找相应的值
b = 'abcdefg'
print(b[0]) # a
print(b[1]) # b
print(b[2]) # c
print(b[3]) # d
print(b[4]) # e
print(b[5]) # f
# 索引为负数的为倒序查找
print(b[-1])# g
# 切片
print(b[2:4]) # cd
print(b[0:3]) #abc
print(b[:2])  #ab
print(b[2:])  #cdefg
print(b[:])   #abcdefg

print(b[-2:]) #fg
print(b[:-2]) #abcde

print(b[2:] + b[:-2])  #cdefgabcde
print(b[-3:] + b[:-3]) #efgabcd

# length
# 字符串的长度
c = "abcdefghijklmn"
print(len(c)) # 14 



# 关于字符串这一块算是按照文档过了一遍 此时此刻我只想说一句python操作字符串太特么舒服了
# 比JavaScript 骚气多了 哈哈哈当然JavaScript也很牛逼



