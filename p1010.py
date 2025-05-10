# 10월 10일 수업자료

import random



class TestClass:
        aaa= 3000
        _bb = 100
        def __init__(self):
            self.result = 0
        def classPrint(self):
            print(self.result, self.aaa)
    
def strFn():
    str1 = "문자열 \" 큰 따옴표 넣기 \""
    print(f"큰 따옴표 출력 연습 : (str1)")
    str2 = "test"*3
    print(f"문자열 곱하기 : (str2)")
    
    l1 = [1, 2, 3]
    l1.append(4)
    print(l1)




def tupleEx():
    return 1, 2, 3
    

def dictFn():
    d1 = {'a' : 'apple' , 'b' : 'banana'}
    print(d1)
    print(d1.keys())
    print(d1.values())
    print(d1.items())
    
    for item in d1.items():
        print(item)
        
    for i in d1:
        print(i, d1[i])
        
    d1['c'] = 'coco'
    print(d1)
    d1['a'] = 'apple2'
    print(d1)
    
    # if 'c' in d1 : print(d1(c))
    
    
# def setFn():
    # tmp1 = []
    # for i in l1:
        # if i not in tmpl1:
            # tmpl1.append(i)
    
    
    # tmpl1 = list(set(i))
    
def muiumFn():
    a = 3
    print(id(3))
    a = 5 
    b = a
    print(id(a), id(b))
    
    l1 = [1,2,3]
    print(id(l1))
    l1.append(4)
    l1[2] = 200
    print(id(l1), l1)
    
    t1 = (1, 2)
    print(id(t1))
    t1 = (3, 4)
    print(id(t1))
    

# def ifFn():
    # score = 80
    
    # 조건: 80점 이상이면 "Success" 아니면 "Fail"
    # if score 
    
def removeFn():
    l1 = list(range(1, 10))
    remove_set = (3, 5)
    result = list()    
    for i in l1:
        if i not in remove_set:
            result.append(i)
    print(result)
    
    
    
def iterFn():
    l1 = [1, 2, 3, 4, 5]
    print(hasattr(l1, "__iter__"))
    print(iter(l1))
    # for i in l1
    

def oddevenSumFn():
    data1 = list() #data1 = []
    for _ in range(10):
        data1.append(random.randint(1,9))
    # print(data1)
    
    # # random.randint
    
    
    # data1 = [random.randint(1,9)*10]
    
    # print(data1)
     
     
    # eSum = 0; oSum= 0
    
    # for i in range(len(range)):
    #     if data1[i] % 2 == 0 :
    #         eSum += data1[i]
    #     else :
    #         oSum += data1[i]
    # print(f"c style : 짝수합 : {eSum} , 홀수합 : {oSum}")
    
    
    
    # 2. python
    
    # eSum = 0 ; oSum = 0
    # for i in data1:
    #     if i % 2 == 0 :
    #         eSum += i
    #     else:
    #         oSum += i
    # print(f"python :  짝수합 : {eSum}, 홀수합 : {oSum}")
    

    # 3. python list
    
    eSum = sum([i for i in data1 if i %2 == 0])
    oSum = sum([i for i in data1 if i %2 == 0])
    print(f"list : 짝수합 : {eSum}, 홀수합 : {oSum}")
    
    
    def f1(*args):
        print(type(args) , args)
    
    def f2(*args, **kwargs):
        print(type(args), args)
        print(type(kwargs), kwargs)
        
    def f3(a=0, b=0, c=0, d=0, e=0):
        print(a,b,c,d,e)
        
    def f4(a=0, b=0, c=0):
        print(a,b,c)

    def f5(b,a):
        print(a,b)
        return a, b    
    
    
   
    
    
    
if __name__ == "__main__":
    
    
    print("10월 10일")
    
    
strFn()
t1 = tupleEx()
print(type(t1))
# dictFN()
# setFn()
muiumFn()
removeFn()
iterFn()
oddevenSumFn()
# f1(1,2,3,4,5)
# f2(1,2,3,4,5, a=1, b=2, c=3)
# f3(1,2, 100)
# f4(1,2,3)
# f5(a=1, b=100)

instancel = TestClass()
instancel.classPrint()
print(instancel.aaa)
print(instancel.result)
print(instancel._bb)