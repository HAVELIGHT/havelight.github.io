# from __future__ import division
# # coding=utf-8
# from pychecker import checker
#
# i = ' '.join(['a', 'b', 'c'])
# print i
# list = '\n'.join(['\t'.join(['%d * %d' % (x, y) for x in range(1, 10) if x <= y]) for y in range(1, 10)])
# print list
#
# print 9 / 2
# set = set('1' + '2' + '2')
# print set
# from itertools import permutations
#
# for i in permutations([1, 2, 3, 4], 3):
#     print i
#
# 运算符重载
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d,%d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# v3 = Vector(3, 2)
# print v1 + v2 + v3
#
#
# class B(object):
#     def name(self):
#         print('name is cat')
#
#
# class A(object):
#     def name(self):
#         print('name is xiaoming')
#         super(A, self).name()
#
#
# class C(A, B):
#     def name(self):
#         print('name is wang')
#         super(C, self).name()
#
#
# if __name__ == '__main__':
#     a = A()
#     print a.__class__.__mro__
#     c = C()
#     print(c.__class__.__mro__)
#     c.name()
#
#
# class Fib:
#     def __init__(self):
#         self.prev = 0
#         self.curr = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         value = self.curr
#         self.curr += self.prev
#         self.prev = value
#         return value
#
#
# def gener():
#     result = []
#     for i in range(10):
#         result.append(i)
#     return result
#
#
# def gen():
#     for i in range(10):
#         yield i
#
#
# res = gener()
# print res
# g = gen()
# print list(g)
# a = (x ** 2 for x in range(10))
# print list(a)
#
#
# def index_words(text):
#     result = []
#     if text:
#         result.append(0)
#     for index, letter in enumerate(text, 1):
#         if letter == ' ':
#             result.append(index)
#     return result
#
#
# r = index_words('h an l ei ')
# print r
# a = [1, 2]
#
#
# def fo():
#     a = [3, 4]
#     print a
#     print id(a)
#
#
# fo()
# print a
# print id(a)
#
#
# def outer():
#     x = 1
#
#     def inner():
#         print x
#
#     return inner
#
#
# foo = outer()
# print foo.func_closure
# print outer
#
#
# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return "Coord: " + str(self.__dict__)
#
#
# def wrapper(func):
#     def checker(a, b):
#         if a < 0 or b < 0:
#             a = a if a > 0 else 0
#             b = b if b > 0 else 0
#         result = func(a, b)
#         return result
#
#     return checker
#
#
# @wrapper
# def add(a, b):
#     return a + b
#
#
# a = add(-1, -2)
#
# print a
#
#
# def one(*a):
#     print a
#
#
# i = one(1, 2, 3)
# print type(i)
#
#
# def test(*args, **kwargs):
#     print args
#     print type(args)
#     print kwargs
#
#
# test(1, 2, 'a', x=1, y=2, z=3)
#
# print checker.warn.Warning

# def foo():
#     for i in range(50) :
#         if i % 2==0:
#             yield i
#
# print foo().next()


# import sys
# import time
# from collections import deque
# fancy_loading = deque('>>>--------------------------------------------------')
# while True:
#     print '\r%s' % ''.join(fancy_loading),
#     fancy_loading.rotate(1)
#     #sys.stdout.flush()
#     time.sleep(0.1)

# l=[1,2,3,4]
# for i,j in enumerate(l):
#     print '%d,%s' % (i,j)
#
# print [i*2 for i in l if i%2==0]
# l2=l[::-1]
# print l2

# 列表插入一个元素
# a=[2,3]
# a.insert(1,'a')
# print a
# #列表插入多个元素使用切片
# b=[2,3]
# b[1:1]=['a','b']
# print b

# import copy
#
# a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
#
# b = a  # 赋值，传对象的引用
# c = copy.copy(a)  # 对象拷贝，浅拷贝
# d = copy.deepcopy(a)  # 对象拷贝，深拷贝
#
# a.append(5)  # 修改对象a
# a[4].append('c')  # 修改对象a中的['a', 'b']数组对象
#
# print id(a),a
# print id(b),b
# print id(c),c
# print id(d),d
## import copy
# a=['a']
# b=copy.copy(a)
# print a is b
# print b

# l=['a','b','c']
# l1=['(%d,%s)' % (i,j) for i,j in enumerate(l)]
# print l1

# class myIterator():
#     def __init__(self, step):
#         self.step = step
#
#     def next(self):
#         if self.step == 0:
#             raise StopIteration
#         self.step -= 1
#         return self.step
#
#     def __iter__(self):
#         return self
# myit=myIterator(5)
# class fi():
#     def __init__(self):
#         self.a=1
#         self.b=0
#
#     def __repr__(self):
#         return str(self.a)
#
#     def calc(self):
#         print myit.next()
#
# a=fi()
# a.calc()
# print myit.next()
#
# a=1
# print id(a)
# def test():
#     global a
#     a=2
#     print a,id(a)
#
# test()

# def test():
#     for i in range(10):
#         yield i
#
#
# res=test()
# for i in range(10):
#     print res.next()

#生成器
import math
import time
# def is_prime(number):
#     if number > 1:
#         if number == 2:
#             return True
#         if number % 2 == 0:
#             return False
#         for current in range(3, int(math.sqrt(number) + 1), 2):
#             if number % current == 0:
#                 return False
#         return True
#     return False
#
# def get_primes(number):
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1
#
# def get_primes(number):
#     while True:
#         if is_prime(number):
#             number=yield number
#         number+=1
#
# def print_successive_primes(iterarions,base=10):
#     prime_generator=get_primes(base)


# def solve_number_10():
#     # She *is* working on Project
#     total = 2
#     for next_prime in get_primes(3):
#         if next_prime < 2000000:
#             total += next_prime
#         else:
#             print(total)
#             return
# t=get_primes(2)
# print t.next()
# time.sleep(3)
# print t.next()
# time.sleep(3)
# print t.next()
# # print t.next()
#
# class test():
#     def __init__(self,age):
#         self.age=age
#
#     # def __str__(self):
#     #     return 'str %d' % self.age
#
#     def __repr__(self):
#         return 'repr %d' % self.age
#
# t=test(10)
# print t

#生成器实现裴波那契数列
# def fibonacci():
#     a,b=0,1
#     while True:
#         yield b
#         a,b=b,a+b
#
# fib=fibonacci()
# print [fib.next() for i in range(10)],type(fib)
# i=0
# for value in fib:
#     print type(value)
#     i+=1
#     if i==10:
        #break

def psychologist():
    print 'Please tell me your problem.'
    while True:
        answer=(yield)
        if answer.endswith('?'):
            print("Don't ask yourself so many quewtions")
        if 'good' in answer:
            print "A that's good. go on"
# psychologist()
# free=psychologist()
# free.send(None)
# #free.next()
# free.send('i am good')
# free.send('you are good')



