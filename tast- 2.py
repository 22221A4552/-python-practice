""" 
Given a list of integers, display the elements whose indexes are both prime numbers and Fibonacci numbers. 
Input: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] Output: 20 30 50 """


""" li  = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(len(li))
def fun(n):
    li = []
    for  i  in range(0,len(n)+1):
    
        count = 0
        for j in range(1,i+1):
            if i%j == 0:
                count +=1
        if count == 2:
            li.append(n[i])
    return li
 """
""" li  = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
def fun(li):

    li2 = []
    for i in range(len(li)):
        count = 0
        for j  in range(1,i+1):
            if i%j ==0:
                count +=1
        if count ==2:
            li2.append(i)
    return li2
print(fun(li))
def fib(n)               
    a = 0
    b = 1
    i =  1
    while i < 10:
        c = a+b 
        a = b
        b = c
        if  c in n:
            print()
        i +=1 
 """
""" 
def fun(n,m):
    count = 0
    sum = 0
    str = ""
    for i in n:
        sum += i
        count +=1
    result = sum/count
    for  i in range(0,len(n)):
        if n[i]>result:
            str = str + m[i]
            str= str + " "
    return str



def fun2(n,m):
    lowest  = max(n)
    for i in range(0,len(n)): 
        if  lowest > n[i]:
            lowest  = n[i]
            value  = i

    return f"the lowest value salary is {m[value]} {lowest}"

def fun1(n,m):
    large = 0
    for i in range(0,len(n)):
        if n[i] > large:
            large = n[i]
            value  = i
    return f"the highest salary is  {m[value]} {large} "
salary = [35000,42000,28000,50000]
name = ["ravi","priya","Arun","sneha"]
print(fun1(salary,name))
print(fun2(salary,name))
print(fun(salary,name))

 """
""" def fun(n):
    count = 0
    value = n
    res = 0
    while 0<value:
        value = value//10
        count +=1
    half =count//2
    org = n
    i = 1
    while i<=half:
        digit  = org//10
        res= res*10+digit
       
        i +=1
    
    return count,res ,half
print(fun(123456))
 """
""" org = 123456
divisor = 100000
i = 1

while divisor > 0:
    digit = org // divisor
    print(digit)

    org = org % divisor
    print(org)
    divisor //= 10 """

""" a = int(input("enter your value "))
n  = a
b = a
count = 0
sum  = 0
while n>0:
    n=n//10
    count+=1
while b > 0:
    digit = b%10
    sum += digit**count
    b//=10
if sum == a:
    print("strong number")
else:
    print("not a strong number") """

""" Strong Number
1! + 4! + 5!
= 1 + 24 + 120
= 145 """
""" 
a = 145
b = a
sum = 0
while b > 0 :
    digit = b%10
    i = 1
    product = 1
    while i <= digit:
        product = product*i
        i +=1
    sum += product
    b//=10
if sum == a:
    print("strong number")
else:
    print("not strong")
 """

""" a = 28
b= a
sum = 0
i = 1
while i < 28:
    if a%i==0:
        
        sum +=i
    i+=1
if sum ==a:
    print("perfect number")
else:
    print("not perfect number")
 """
""" class employee:
    def __init__(self,name,salary, exp):
        self.name = name
        self.salary = salary
        self.exp = exp
class B(employee):
    def display(self):
        if self.exp>=2 and self.exp <=4:
            result = self.salary +(10/100)*self.salary
            return f" the employee{self.name} after hicking salaryr{result}"
        elif self.exp >= 5 and self.exp <=7:
            result = self.salary +(20/100)*self.salary
            return f" the employee{self.name} after hicking salaryr{result}"
        elif self.exp >7 :
            result = self.salary +(30/100)*self.salary
            return f" the employee{self.name} after hicking salaryr{result}"
        else:
            return f" the employee{self.name} salaryr{result}"

obj = B("teja",21000,3)
obj1 = B("ravi",21000,8)
print(obj.display())
print(obj1.display()) """

""" def factorial(num):
    if num == 1:
        return 1
   return num*factorial(num-1) """

""" def fun(n):
    result = n%10
    if n == 0:
        return 0
    return result+fun(n//10)
print(fun(5832))
 """

""" def fun(n,res =0):
    result = n%10
    
    if n == 0:
        return res
    res = res*10+result
    return fun(n//10,res)
print(fun(5832)) """

""" def fun(n):
    if n == 0:
        return 0
    fun(n-2)
    print(n)
    
fun(48) """

""" def fun(n,m,k):
    result = n&m
    result2  = m&k
    result3 = k&n
    res = result|result2|result3
    return res
s2 = {20, 30, 60, 70}
s1 = {10, 20, 30, 40, 50}
s3 = {30, 40, 80, 90} 
print(fun(s2,s1,s3)) """