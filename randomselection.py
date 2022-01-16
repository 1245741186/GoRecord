import random
st_num=eval(input('请输入班级人数：'))
ls=[]
for i in range(1,st_num+1):
    ls.append(i)
random.shuffle(ls)
print(ls)
