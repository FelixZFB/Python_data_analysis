# 直接赋值，类似于浅拷贝，
# b指向的是a的地址，b和a地址相同
# b改变，实际改变的是b指向的地址,因此a也会发生改变
a = [1, 2, 3]
b = a
print(b)
b[1] = 5
print(b)
print(a)

# Numpy数组：copy和view
# a=b 完全不复制，a和b相互影响
# a = b[:],视图的操作，类似浅拷贝，是一种切片，会创建新的对象a，
# 但是a的数据完全由b保管，他们两个的数据变化是一致的，
# a = b.copy(),复制，a和b互不影响