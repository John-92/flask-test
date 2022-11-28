# -*- coding=utf-8 -*-
# @Time: 2022/11/26 15:42
# @Author: John
# @File: test.py
# @Software: PyCharm
# a= 8 or 1
# b= 8 and 1
# print(b)
def solution(full_text, search_text, allow_overlap=True):
    count = 0
    for i in range(len(full_text)): #i是full_text的序号
        print("i",i)
        for j in range(len(search_text) ):#j是search_text的序号
            print("j", j)
            tem_j=j
            tem_i=i
            while   full_text[tem_i] == search_text[tem_j] :#full_text和search_text的最后一处相等的位置
                print("origin-----》",tem_i,tem_j)
                if tem_j >= len(search_text) -1 or tem_i >= len(full_text) -1:
                    print("while退出")
                    break
                tem_i += 1
                tem_j += 1
            if full_text[tem_i] != search_text[tem_j] :  #如果最后位置的字符不相等，则直接退出search_text的循环
                print("---->break",search_text[tem_j],full_text[tem_i] )
                break
            print("最后检查的位置tem",tem_i,tem_j,full_text[tem_i],search_text[tem_j])
            #if tem_j >= len(search_text) -1 and full_text[tem_i] == search_text[tem_j] and i<=len(full_text)-len(search_text):
            if tem_j >= len(search_text) -1 and i<=len(full_text)-len(search_text):
                #如果j是指向search_text的最后一个位置，且i指向full_text减去search_text长度的差值，则为成功
                count += 1
                print("success----->","i","j",i,j,count)
                break

    if not allow_overlap and count>1 :
        count=1

    return count


# print(solution("aaa_bb_cc_dd_bbbb", "bb",False))
# print(solution("aaa_bb_cc_dd_bbbb", "b"))
# print(solution("bb_", "bb"))
# print(solution("bbb", "bbbb"))
# a="aaa_bb_cc_dd_bbbb"
# print(a[len(a) - 1])
# for i in range(len(a)):
#     print(i,a[i])

class A():
    s='hello'
    # def __str__(self):
    #     s = 'hello'
    #     return s

    def __repr__(self):
        s = 'he'

        return s
    def _test(self):

        pass



# a=A()
# print(str([a,a]))
# print(str(a))
# # a='hello'
# print(repr(1))
#
b=A()
a=[[1,2,[2,3]]]
q=a.pop()
print(callable(b._test))

a=6 and 7
print("a----->",a)
# print(list(q))
# for i in q:
#     print(i)

def flattern(nestedList):
    stack=[nestedList]
    print("--->",stack)
    flattern_list=[]
    while stack:
        top=stack.pop()
        if isinstance(top,list):
            for elem in reversed(top):
            # for elem in top:
                stack.append(elem)

        else:
            flattern_list.append(top)
        print(stack)
    return flattern_list


# print(flattern([1, 2, [3, 4]]))