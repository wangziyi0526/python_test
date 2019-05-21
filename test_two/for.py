# for 循环  循环遍历数据

#part1

NBASuperStar = ['bryant','jordan','james','allen']
# 分别打出了 每一项item 以及每一项item的length的长度

for item in NBASuperStar:
  print(item, len(item))

# bryant 6
# jordan 6
# james 5
# allen 5

for item in NBASuperStar[:]:
  if len(item)>5:
    NBASuperStar.insert(0,item)
print(NBASuperStar)  #  ['jordan', 'bryant', 'bryant', 'jordan', 'james', 'allen']