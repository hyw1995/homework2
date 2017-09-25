#-*- coding: utf-8 -*-
import random
from fractions import Fraction
import sys
import getopt


def Prior(op1, op2):
    if op1 == '*' and op2 == '+' or op1 == '*' and op2 == '-':
        return True
    # if op1 == 'x' and op2 == '-':
    #     return True
    if op1 == '/' and op2 == '+' or op1 == '/' and op2 == '-':
        return True
    # if op1 == '/' and op2 == '-':
    #     return True
    return False


def changeToPostfix(exp):
    stack = []
    postfix = []
    for i in range(len(exp)):
        if type(exp[i]) == int:
            postfix.append(exp[i])
        if type(exp[i]) == str:
            if stack:
                if Prior(exp[i], stack[-1]):
                    stack.append(exp[i])
                else:
                    postfix.append(stack[-1])
                    stack.pop()
                    stack.append(exp[i])
            else:
                stack.append(exp[i])
    if stack:
        stack = stack[::-1]
        postfix.extend(stack)
    return postfix


def CalculatePostfix(exp):
    stack = []
    for i in range(len(exp)):
        if type(exp[i]) == int:
            stack.append(exp[i])
        if type(exp[i]) == str:
            #print exp[i]
            temp = calculate(exp[i], stack[-2], stack[-1])
            stack.pop()
            stack.pop()
            stack.append(temp)
    return stack[0]


def calculate(op, num1, num2):
    if op == '+':
        restmp = Fraction(num1, 1) + Fraction(num2, 1)
    if op == '-':
        restmp = Fraction(num1, 1) - Fraction(num2, 1)
    if op == '*':
        restmp = Fraction(num1, 1) * Fraction(num2, 1)
    if op == '/':
        restmp = Fraction(num1, 1) / Fraction(num2, 1)
    return restmp


quesNums = 0
correct_ans = 0
opers = ['+', '-', '*', '/']
opts, args = getopt.getopt(sys.argv[1:], 'n:')
for opt, value in opts:
    if opt == '-n':
        quesNums = int(value)
eleNums = []
eleOpers = []
for i in range(quesNums):
    for j in range(4):
        eleNums.append(random.randint(1, 100))
    for k in range(3):
        eleOpers.append(opers[random.randint(0, 3)])
    OutputExp = str(eleNums[0]) + eleOpers[0] + str(eleNums[1]) + \
        eleOpers[1] + str(eleNums[2]) + eleOpers[2] + str(eleNums[3])
    CalculateExp = [eleNums[0], eleOpers[0], eleNums[1],
                    eleOpers[1], eleNums[2], eleOpers[2], eleNums[3]]
    print OutputExp + '=',
    usrInput = raw_input()
    PostfixExp = changeToPostfix(CalculateExp)
    res = CalculatePostfix(PostfixExp)
    if(usrInput == str(res)):
        print '正确'.decode('utf-8').encode(sys.getfilesystemencoding())
        correct_ans += 1
    else:
        print '错误,正确答案='.decode('utf-8').encode(sys.getfilesystemencoding()) + str(res)
    eleNums = []
    eleOpers = []
print u'本次得分:' + str(100.0 / quesNums * correct_ans)
