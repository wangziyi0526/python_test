# 自定义函数1
def fn (n, ary):
  if n == 1:
    n = 2
  for item in ary:
    # return item == n
    if item == n:
      return item
    else:
      return "早晚得分手哈哈哈"

arr = [1]
b = int(input('请输入数字判断你和她的会不会分手:'))
a = fn(b,arr)
print(a)

# 自定义函数2  简直惨绝人寰为所欲为啊

def func (a,b,c,d):
    while a > 0:
      ok = input(b)
      if ok in ('y','ye','yes'):
        a = a - 1
        print(c)
      else:
        a = a - 1
        print(d)
num = 10
tishi = '请输入 yes or no 测试她是否爱你:'
zhaxin = '放弃吧她不爱你'
waner = '系统故障,再来一次'
func(num,tishi,zhaxin,waner)