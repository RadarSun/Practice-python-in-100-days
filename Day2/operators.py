"""
Fuction:测试运算符
Version: 1.0
Author: RadarSun(Sunhonghong)
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0) # flag0 = True
print('flag1 =', flag1) # flag1 = True
print('flag2 =', flag2) # flag2 = False
print('flag3 =', flag3) # flag3 = False
print('flag4 =', flag4) # flag4 = True
print('flag5 =', flag5) # flag5 = False
print(flag1 is True) # True
print(flag2 is not False) # False
#测试 in 和not in
a = [1,2,3]
c = 1 in a
print(c)
d = 4 in a
print(d)
e = 4 not in a
print(e)
#测试 is is not
f = 'kkk'
result = f is 'kk'
print(result)
"""
#测试print的多参数
c=10
print('a','b',c,'\n')
"""