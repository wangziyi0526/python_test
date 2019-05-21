# range() 函数
#  如果你确实需要遍历一个数字序列，内置函数 range() 会派上用场。它生成算术级数:


# part1-1   在range()函数中传递一个参数的情况下
lists = []
for i in range(5):
  lists.append(i)
  print(lists) # 根据for循环把 利用range()内置函数生成的序列依次 push(append)进lists 列表中
print(lists)

# part1-2   在range()函数中传递两个参数的情况下 
arry = []
for i in range(5,8):
  arry.append(i)
  print(arry)
print(arry)

# part1-3
ary = []
for i in range(1,10,3):
   ary.append(i)
   print(ary)
print(ary)

#  个人理解
# 传递一个参数的情况下默认区间是从0开始到传进的参数之间的值  但是不包含传进去的参数的值
# 传递两个参数的情况下第一个参数是区间开始的值，第二个参数是区间结束的值
# 传递三个参数的情况下前两个参数的意思见上一条， 第三个参数的意义 是在前两个参数区间内，以第三个参数的值
# 作为增长数值

# range() 函数 可以与len()函数进行配合使用

name = ['kobe', 'jordan', 'james', 'lakers']
for item in range(len(name)):
  print(item, name[item])

# list()

array = list(range(5))
print(array)

for n in range(2,10):
  print('开始')
  print(n)
  for x in range(2,n):
    print(x)
    if n%x == 0:
      print("这是啥")
      break
  else:
    print(n, '这又是啥')   

