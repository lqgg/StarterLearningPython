#! /usr/bin/env python
#coding:utf-8
	
print("请输入任意一个整数数字：")
	
number = int(input())

if number == 10:#如果数字等于10
    print("您输入的数字是：{}".format(number))#打印的结果为你输出的数字为10
    print("You are SMART.")#你太小了
elif number > 10:
    print("您输入的数字是：{}".format(number))
    print("This number is more than 10.")#这个数字大于10
elif number < 10:
    print("您输入的数字是：{}".format(number))
    print("This number is less than 10.")#这个数字小于10
else:
    print("Are you a human?")#你是一个男人
    
