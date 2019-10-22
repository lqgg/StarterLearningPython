#!/usr/bin/env python
# coding=utf-8

name = raw_input("What is your name?")#你的名字是什么

age = raw_input("How old are you?")#你现在多大啦

print "Your name is:", name#打印出你输入的你的名字
print "You are " + age + " years old."#打印出你输入的你的年龄

after_ten = int(age) + 10#十年之后
print "You will be " + str(after_ten) + " years old after ten years."#打印出你的十年之后是多少岁
