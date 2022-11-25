#push() , pop() , isEmpty(). isFull()


num=[]
num.append(2) #use to enetr new item
 num.append(6)
 num.append(5)
num.append(3)
print(num)
print (num.pop())
print(num)'''

'''def push (num,n):
    num.append(n)
    return num
def pop (num):
    if isEmpty(num):
        print("stack is empty")
        return False
    else:
        num.pop()
        return num
def isEmpty(num):
    if not num:
        return True
    else:
            return False
num=[]
push (num,2)
push (num,3)
push (num,4)
print(num)
pop(num)
pop(num)
pop(num)
pop(num)
print(num)

def p (num, a):
    a.append(num)
    return a
a=[]
p (4,a)
print(a)  
def pop(a):
    if isEmpty(a):
        return False
    else:
            a.pop()
            return a'''

def isEmpty(num):
    if not num:
        return True
    else:
        return False

num=[]
isEmpty(num)
