

""" 
def Large(li):
    large = 0
    for i in employees:
        for j in range(len(employees[i])):
            if employees[i][j][1] > large:
                large = employees[i][j][1]
                a = employees[i][j]

    return a

employees = {
    "IT": [
        ("teja", 45000),
        ("ravi", 55000),
        ("kiran", 48000)
    ],
    "HR": [
        ("anil", 52000),
        ("suresh", 47000)
    ],
    "Sales": [
        ("mahesh", 60000),
        ("raju", 58000)
    ]
}

res = Large(employees)
print(res)
 """
""" company = {
    "Python": {
        "teja": [80, 85, 90],
        "ravi": [70, 75, 80]
    },
    "Java": {
        "kiran": [90, 95, 92],
        "anil": [60, 70, 65]
    }
}
def Avg(company):
    avg = 0
    for i in company:
        for j  in  company[i]:
            result = 0
            for k in range(len(company[i][j])):
                result += company[i][j][k]
            result1 = result/len(company[i][j])
            if result1 > avg:
                avg = result1 
                
    return avg
res = Avg(company)
print(res) """
""" students = {
    "teja": {
        "Python": 85,
        "Java": 78,
        "SQL": 90
    },
    "ravi": {
        "Python": 92,
        "Java": 88,
        "SQL": 80
    },
    "kiran": {
        "Python": 75,
        "Java": 95,
        "SQL": 85
    },
    "anil": {
        "Python": 88,
        "Java": 82,
        "SQL": 91
    }
}
def Highest(students):
    highest = 0
    for i in students:
        sum1 = 0
        for  j in students[i]:
            sum1+=students[i][j]
            
        if sum1 > highest:
            highest = sum1
            a = i
    return a,highest
res = Highest(students)
print(res)
 """

""" data = {
    "Team1": [
        {"name": "teja", "marks": [80, 90, 85]},
        {"name": "ravi", "marks": [70, 75, 80]}
    ],
    "Team2": [
        {"name": "kiran", "marks": [95, 92, 90]},
        {"name": "anil", "marks": [85, 88, 82]}
    ]
}
high = 0
for team in data:
   
    for  stud in data[team]:
        total = 0
        for mark  in stud["marks"]:
            total = total+mark
        if total > high:
            high = total
            a = stud["name"]
print(a,high)


            """
""" data = {
    "Team1": [
        {"name": "teja", "skills": {"Python", "SQL", "Git"}},
        {"name": "ravi", "skills": {"Java", "SQL", "Git"}}
    ],
    "Team2": [
        {"name": "kiran", "skills": {"Python", "Java", "SQL"}},
        {"name": "anil", "skills": {"Python", "Git"}}
    ]
}


for team in data:
    
    for stud in data[team]:
        if "Python" in stud["skills"] and "SQL" in stud["skills"]:
            print(stud["name"])
 """

""" Write a Python program to Most Frequent Word. Input ["apple","banana","apple","orange","banana","banana"] Output banana """
""" Input =  ["apple","banana","apple","orange","banana","banana"]
large = 0

for i in Input:
    count = 0
    for j in  Input:
        if i == j:
            count +=1
    if count >large:
        a = i
print(i)

         """
""" Seats are booked. If the same seat is booked again, ignore it. bookings = 10,5,8,5,12,8,11,5 Print only successful bookings. """
""" 
Write a Python program to create a new dictionary containing only employees
whose salary is greater than ₹40,000. Input: employees = { "Ravi": 30000, "Anil": 45000, "Kiran": 50000, "Suresh": 35000 } Output: { "Anil": 45000, "Kiran" """
""" employees = { "Ravi": 30000, "Anil": 45000, "Kiran": 50000, "Suresh": 35000 }
high ={}

for i in employees:
    if employees[i] >40000:
        high[i]=employees[i]
print(high) """

""" 
Write a Python program to find the employee who receives the highest salary. Input:"""
""" employees = { "E101": { "name": "Ravi", "salary": 35000 }, "E102": { "name": "Anil", "salary": 50000 }} 
for id in employees:
   if 
     """
""" 
Write a Python program to find the first row containing the maximum number of even elements. 
Input:  """
""" x = [[11, 24, 7, 18],[10, 15, 22, 9],[8, 12, 14, 5],[20, 3, 6, 11]] 
high  = 0
for i in x:
    count = 0
    for j in i:
        if j%2==0:
            count +=1
    if count > high:
        high = count
        li = i
    
print(li,high) """


""" Write a Python program to find all elements that appear exactly once in the entire nested list, 
while maintaining their original order. Input: x = [[10, 20, 30],[20, 40, 50],[30, 60, 70]] 
Output: [10, 40, 50, 60, 70] """

""" x = [[10, 20, 30],[20, 40, 50],[30, 60, 70]]
output = []
for i in x:
    for j in i:
        if j not in output:
            output.append(j)

print(output) """
""" Write a Python program to find the row having the maximum difference between its largest and smallest elements.
Input: x = [[10, 25, 18],[5, 40, 12],[30, 35, 20],[8, 50, 15]] Output: [8, 50, 15] Difference: 42 """
""" 
x = [[10, 25, 18],[5, 40, 12],[30, 35, 20],[8, 50, 15]]
high = 0
for i in x:
    total = 0
    
    for j in range(len(i)-1):
        total +=i[j]-i[j+1]

       
print(total) """
""" 
employees = {
    "E101": {
        "name": "Ravi",
        "skills": {"Python", "SQL", "Git"}
    },
    "E102": {
        "name": "Anil",
        "skills": {"Java", "SQL"}
    },
    "E103": {
        "name": "Teja",
        "skills": {"Python", "Java", "SQL", "Git"}
    },
    "E104": {
        "name": "Kiran",
        "skills": {"Python", "Git"}
    }
}

def fun(employees):
    output = []

    for i in employees:
        if "Python" in employees[i]["skills"] and "SQL" in employees[i]["skills"]:
            output.append((i, employees[i]["name"]))

    return output
res = fun(employees)
print(res) """
""" 
employees = {
    "E101": {
        "name": "Ravi",
        "salary": 45000,
        "skills": {"Python", "SQL"}
    },
    "E102": {
        "name": "Anil",
        "salary": 55000,
        "skills": {"Java", "SQL"}
    },
    "E103": {
        "name": "Teja",
        "salary": 60000,
        "skills": {"Python", "Java", "SQL"}
    },
    "E104": {
        "name": "Kiran",
        "salary": 50000,
        "skills": {"Python", "Git"}
    }
}
def fun(employees):

    high_sal = 0
    li = []
    for i in employees:
        if "Python" in employees[i]["skills"] and "SQL" in employees[i]["skills"]:
            if employees[i]["salary"] >high_sal:
                high_sal = employees[i]["salary"]
                name = employees[i]["name"]
                li.append(name,high_sal)
    return li
res  = fun(employees)
print(res)
 """
""" 
employees = {
    "E101": {
        "name": "Ravi",
        "salary": 45000,
        "skills": {"Python", "SQL", "Git"}
    },
    "E102": {
        "name": "Anil",
        "salary": 55000,
        "skills": {"Java", "SQL"}
    },
    "E103": {
        "name": "Teja",
        "salary": 60000,
        "skills": {"Python", "Java", "SQL"}
    },
    "E104": {
        "name": "Kiran",
        "salary": 50000,
        "skills": {"Python", "Git", "SQL"}
    },
    "E105": {
        "name": "Suresh",
        "salary": 70000,
        "skills": {"Python", "Git"}
    }
}
def fun(employees):
    second = 0
    high = 0

    for i in employees:
        if "Python"  in employees[i]["skills"] and "SQL" in employees[i]["skills"]:
            if employees[i]["salary"] > high:
                second = high
                high = employees[i]["salary"] 
                a = employees[i]["name"]
            elif employees[i]["salary"] >second and employees[i]["salary"]!=high:
                second = employees[i]["salary"]
                a = employees[i]["name"]
    return second,a
res = fun(employees)
print(res)
 """""" 
students = {
    "CSE": [
        {"name": "Teja", "marks": [80, 90, 85], "skills": {"Python", "SQL"}},
        {"name": "Ravi", "marks": [70, 75, 80], "skills": {"Java", "SQL"}}
    ],
    "ECE": [
        {"name": "Kiran", "marks": [95, 92, 90], "skills": {"Python", "Java"}},
        {"name": "Anil", "marks": [85, 88, 82], "skills": {"Python", "SQL"}}
    ]
}
def fun(students):
    avg = 0 
    for i in students:
        
        for j in range(len(students[i])):
            sum1 = 0
            
            if "Python" in students[i][j]["skills"] and "SQL" in students[i][j]["skills"]:
                for k in students[i][j]["marks"]:
                    sum1 +=k
                    
            result = sum1/len(students[i][j]["marks"])
            if result>avg:
                avg = result
                a= students[i][j]["name"]

    return a,avg
res = fun(students)
print(res)
            
 """

""" li = [i for i in range(1,21)]
print(li) """
""" li = [i**2 for i in range(1,11)]
print(li) """
""" 
li  = [i for i in range(1,51) if i%2==0]
print(li) """
""" 
li = [i for i in range(1,31) if i%2!=0]
print(li) """

""" numbers = [10, 15, 20, 25, 30, 35, 40]
li  = [i for i in numbers if i>20]
print(li) """
""" numbers = [1, 2, 3, 4, 5, 6, 7, 8]
li = [i*2 for i in numbers if i%2==0]
print(li) """
""" 
li = ["odd" if i%2!=0 else "even" for i in range(1,21)]
print(li) """

""" words = ["apple", "banana", "cat", "dog", "elephant"]
li = [i  for i in words if len(i)>4]
print(li) """
""" words = ["python", "java", "sql", "html"]
li = [i.upper() for i in words]
print(li) """

""" numbers = [-5, 10, -2, 8, -1, 20]
li = [i  for i in numbers if i>0]
print(li) """
""" text = "comprehension"

st ={i for i in text if i in "aeiou" }
print(st) """
""" 
dic ={i: "even" if i%2==0 else "odd" for i in range(1,6)}
print(dic)
 """
""" names = ["Teja", "Ravi", "Kiran"]
st = { i: len(i) for i in names}
print(st) """

""" prices = {
    "pen": 10,
    "book": 100,
    "bag": 500
}

dic = {i: prices[i]+((10/100)*prices[i]) for i in prices}
print(dic) """
""" numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
li = [i**2  for i in numbers if i%5==0]  
print(li) """
 
""" numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
li =  [ i for i in numbers if i>20 and i%5==0 ]
print(li) """
""" numbers = [5, 10, 15, 20, 25, 30, 35, 40]
li = [i for i in numbers if i >10 and i%5==0]
print(li) """

""" words = ["python", "java", "sql", "javascript", "html"]
li = [len(i) for i in words if len(i)>3]
print(li) """
""" words = ["apple", "banana", "avocado", "grape", "orange", "kiwi"]
li = [i.upper() for i in words  if  i.startswith("a")  ]
print(li) """
""" words = ["apple", "banana", "avocado", "grape", "orange", "kiwi", "apricot"]
li =  [i.upper() for i in words if i.startswith("a") and len(i)>5]
print(li) """
""" numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
li = [ j   for i in numbers for j in i if j%2==0 ]
print(li) """

""" numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
li = [j**2 for i in numbers for j in i  if j%2==0]
print(li) """
""" 
numbers = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]
li = [j for i in numbers for j in i if j >20 and j%5==0]
print(li) """
"""
company = {
     "IT": {
        "E101": {"name": "Ravi", "salary": 45000},
        "E102": {"name": "Teja", "salary": 60000}
    },
    "HR": {
        "E103": {"name": "Anil", "salary": 50000},
        "E104": {"name": "Kiran", "salary": 55000}
    },
    "Sales": {
        "E105": {"name": "Suresh", "salary": 70000},
        "E106": {"name": "Mahesh", "salary": 48000}
    }
}
def fun(company):
    output= []
    for i in company:
        hight = 0
        for j in company[i]:
            if company[i][j]["salary"]>hight:
                hight  = company[i][j]["salary"]
                brach = i
                name = company[i][j]["name"]
        output.append((name,brach ,hight))

    return output
res = fun(company )
print(res) """

""" 
company = {
    "IT": {
        "E101": {"name": "Ravi", "salary": 45000, "skills": {"Python", "SQL"}},
        "E102": {"name": "Teja", "salary": 60000, "skills": {"Python", "Java"}}
    },
    "HR": {
        "E103": {"name": "Anil", "salary": 50000, "skills": {"Python", "SQL"}},
        "E104": {"name": "Kiran", "salary": 55000, "skills": {"Java", "SQL"}}
    },
    "Sales": {
        "E105": {"name": "Suresh", "salary": 70000, "skills": {"Python", "SQL"}},
        "E106": {"name": "Mahesh", "salary": 48000, "skills": {"Python", "Git"}}
    }
}
output = []
for i in company:
    high = 0
    for j in company[i]:
        if "Python" in company[i][j]["skills"] and "SQL"  in company[i][j]["skills"]:
            if company[i][j]["salary"] >high:
                high = company[i][j]["salary"]
                a = i
                name = company[i][j]["name"]
    output.append((a,name,high))
print(output)
     """

""" 
company = {
    "IT": {
        "E101": {"name": "Ravi", "salary": 45000, "skills": {"Python", "SQL"}},
        "E102": {"name": "Teja", "salary": 60000, "skills": {"Python", "Java", "SQL"}}
    },
    "HR": {
        "E103": {"name": "Anil", "salary": 50000, "skills": {"Python", "SQL"}},
        "E104": {"name": "Kiran", "salary": 55000, "skills": {"Java", "SQL"}}
    },
    "Sales": {
        "E105": {"name": "Suresh", "salary": 70000, "skills": {"Python", "SQL"}},
        "E106": {"name": "Mahesh", "salary": 48000, "skills": {"Python", "Git"}}
    }
}

output = []
for i in company:
    second = 0
    high = 0
    for j in company[i]:
        
        if "Python" in company[i][j]["skills"] and "SQL" in company[i][j]["skills"]:
            if company[i][j]["salary"] >high:
                second = high
                high = company[i][j]["salary"]
                name = company[i][j]["name"]
                a = i
               
            elif company[i][j]["salary"] > second and company[i][j]["salary"]!=high:
                second = company[i][j]["salary"]
                name = company[i][j]["name"]
                a = i
    output.append((a,name,second))      
print(output)

 """
""" count = 0 
high = 0
output=[]
li1 = []
li  = [1,2,3,1,2,3,4,5,1,2,3,4,5]
for i in range(len(li)-1):
    if li[i+1]-li[i]==1:
       
       output.append(li[i])
    else:
        output.append(li[i])
        li1.append(output)
        output = []
                     
for i in range(len(li1)):
    if len(li1[i])>high:
        hight = len(li1[i])
        a = li1[i]
        
        

        
    
print(output)
print(li1)
print(a)         """



""" 
Write a Python function to find the maximum sum of any two consecutive elements
in a list and return the elements that produce the maximum sum. Input: [4, 7, 2, 9, 5, 12, 3] Output: [5, 12] """

""" li = [4, 7, 2, 9, 5, 12, 3]
def fun (li):
    high = 0

    for  i in range(len(li)-1):
        sum1 =li[i]+li[i+1]
        if sum1 >high:
            high = sum1
            a = [li[i+1],li[i]]
    return a
res = fun(li)
print(res) """
""" Write a Python function to remove consecutive duplicate characters 
from a string while keeping the first occurrence of each consecutive
 group. Input: "aaabbccdaaee" Output: "abcdae" """
""" 
st = "aaabbccdaaee"

result = ""

for i in range(len(st)):
    if i == 0 or st[i] != st[i - 1]:
        result += st[i]

print(result) """
""" 
Given a tuple of numbers, find the smallest positive number that is
missing from the tuple. Input: (3, 4, -1, 1, 2, 6) Output: 5 """
""" tu = (3, 4, -1, 1, 2, 6) 
li = (sorted(tu))

for i in range(len(li)-1):
    if li[i]>0:
        if li[i+1]-li[i] != 1:
            print(li[i-1]+li[i]//2) """

""" def fun(li):
    start = li
    def fun1():
        nonlocal start
        output = []
        value = [3,7,2,8]
        for i in range(len(value)):
            if i == 0 :
                result = value[i]+start
                output.append(result)
            else:
               result += value[i]
               output.append(result)
        return output
    return fun1()
li = int(input("enter your value"))

res = fun(li)
print(res)
         """

""" li=[1,2,3,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6,7,8]
curr_list=[]
long_list=[]
for i in range(len(li)):
    first=li[i]
    prev=li[i-1]
    if(first>prev):
        curr_list.append(prev)
        curr_list.append(first)
    else:
        curr_list.clear()
    if(len(curr_list)>len(long_list)):
        for j in curr_list:
            if(j not in long_list):
                long_list.append(j)
print(long_list) """
""" 
output=[]
li1 = []
li  = [1,2,3,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6,7,8,9]
for i in range(len(li)):
    if len(li)-1>i:
        if li[i+1]-li[i]==1:
        
            output.append(li[i])
        else:
            output.append(li[i])
            li1.append(output)
            output = []
output.append(li[i])
li1.append(output)
                     
for i in range(len(li1)):
    if len(li1[i])>high:
        hight = len(li1[i])
        a = li1[i]
        
        

        
    
print(output)
print(li1)
print(a) """

""" a = "3[a]2[bc]"
word = ""
output = ""
result = 0
for i in a:
    if ord(i)>=49 and ord(i)<=57:
        result = int(i)
    elif  "a">= i and  i<="z":
        word = word+i
    
        final = word*result
        word = ""
        result = 0
        if final not in output:
            output=output*final """
""" 
def out():
    x = 20
    def inn():
        return (x)
    return inn()
fun = out()
print(fun)
fun() """
""" 
def gen(mul):
    def innterfun(x):
        return x*mul
    return innterfun
res = gen(10)
print(res) """

""" def teja(fun):
    def innter():
        output = fun()
        return output.upper()
    return innter


@teja
def display():
    s = "we are good students"
    return s
res = display()
print(res) """

""" def display (x,y=[]):
    y.append(x)
    print(y)
display(10)
display(20)
display(30) """

""" def deaf(fun):
    def inner():
        fun()
    return inner
@deaf
def welcom():
    print("welcome to python")

welcom() """





""" 






def out(fun):
    def inner():
        print("Before function ")
        fun()
        print("after function")
    return inner






@out
def welcome():
    print("Welcome to Python")


welcome() """





""" def out(check):
    def inner(val):
        if val == "python":
            output= "valid"
        else:
            output = "invalid"
        return output
    return inner
@out
def check(value):
    return value


value  = input("enter the password")
res  =check(value)
print(res)
 """







""" 
Write a Python program using a closure where the outer function takes a number n and
the inner function takes another number x and returns n + x. Input: n = 10 x = 5 Output: 15 """

""" def out(n):
    def innter(x):
        return n+x
    return innter
res = out(5)
res1 = res(10)
print(res1) """


""" Create a closure counter() that maintains a count. Every time the inner function is called,
it should increase the count by 1 and return the updated count. Input: c = counter() print(c()) print(c()) print(c()) Output: 1 2 3

 """
""" def counter():
    count = 0
    def innerfun():
        nonlocal count
        count+=1
        return count
    return innerfun
c = counter()
print(c())
print(c())
print(c())
 """

""" def outter():
    count  =10
    def inner(x):
        nonlocal count
        count +=x
        return count
    return inner
res = outter()
print(res(5))
print(res(3))
print(res(7)) """


""" def outer(fun):
    def inner(x,y):
        import time 
        start = time.time()
        z = fun(x,y)
        end = time.time()
        print('time taken is ',end-start)
        return z
    return inner


def isprimie(num):
    
    for i in range(2,(num//2)+1):
        if num%i == 0:
            return False
    else:
        return True
        
@outer
def range1(s,e):
    for i in range(s,e+1):
        if isprimie(i):
            print(i)


range1(1,20) """


""" 
x = [1,2,3,4,5,6,7,8]
it = iter(x)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it)) """

""" it = (i for i in range(1,10) if i%2==0)
print(next(it)) """


""" square = (lambda  *args:sum(args))(1,2,3,4,5,6)
print(square) """
""" numbers = [10, 20, 30, 40, 50]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
 """
""" x = (i for i in range(1,7+1))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x)) """

""" def fun(n):
    for i in range(1 ,n+1):
        if i%2==0:
            yield i
res = fun(10)
print(res)
 """
""" x = (i for i in range(1,10))
for i in x:
    print(i) """

""" squ = (lambda num:num**2)(10)
print(squ)
 """
""" numbers = [1, 2, 3, 4, 5]
res = (map(lambda num:num**2,numbers))
for i in res:
    print(i)
 """
""" x = [10, 15, 20, 25, 30, 35, 40]
res = list(filter(lambda num :num%2==0,x))
print(res) """
""" from functools import reduce
x = [1, 2, 3, 4, 5]
res = reduce(lambda a,b:a*b,x)
print(res) """
""" x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list(map(lambda n:n**2,list(filter(lambda n:n%2==0 ,x))))
print(res)
 """
""" from functools import reduce
x= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res =reduce(lambda a,b:a+b ,list(map(lambda n:n**2, list(filter(lambda n:n%2==0,x)))))
print(res) """
""" 
def fun(n):
    m = (i**2 for i in range(1,n+1) if i%2==0)
       
    yield from  m
res = fun(20)
for i in res:
    print(i) """

""" numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def fun(n):
    res = list(map(lambda n:n**2 ,list(filter(lambda n:n%2==0 , n))))
    yield from res
res = fun(numbers)
for i in res:
    print(i) """
""" from functools import reduce
x = [3, 7, 2, 9, 4, 12, 5, 8]
def fun(x):
    result =list(reduce(lambda a,b:a+b ,list(map(lambda n: n**2,list(filter(lambda n : n>5 ,x))))))
    return result
res =fun(x)
print(res)
 """
""" def fact(x = 5):
    
    if x == 1:
        return 1
    return x+fact(x-1)
   
print(fact()) """

""" def fun(n):
    result = n%10
    s= 0 
    if result%2 ==0:
        s+=result
    if n <10:
        return s
    else:
        return s+ fun(n//10)
print(fun(583624)) """

""" 
def fun(n):
    


    print(n)
    if n == :
        return n
    return  fun(n//10)
print(fun(48291))
 """

""" def fun(n):
    print(n)
    if 6 ==6:
        return 6
    return fun(n+1)
print(fun(0)) """

""" def fun(n):

    # 1. What should I do?
    if n % 2 == 0:
        print(n)

    # 2. When should I stop?
    if n == 1:
        return

    # 3. What is the next recursive call?
    return fun(n-1)
print(fun(6)) """

""" def fun(n): """
"""     if n%2!=0: """
"""         print(n) """
"""     if n == 1: """
"""         return  """
"""     return fun(n-1) """
""" print(fun(6)) """
""" def even_count(n): """
"""  """
"""     if n == 1: """
"""         return 0 """
"""  """
"""     count = 0 """
"""  """
"""     if n % 2 = 0: """
"""         count = 1 """
"""  """
"""     return count + even_count(n - 1) """
"""  """
"""  """
""" print(even_count(6)) """
"""  """

""" 
def large(n,i=0):
    if n[i] == len(n)-1:
        return larger
    larger = 0 
    if  n[i] >larger :
        larger = n[i]
    return  large(n,i=i+1)




print(large([3, 7, 2, 9, 4])) """

""" def fun(n):
    return n**2
print(fun(5))
print(10%5) """
""" n = 98765
while True:
    sum = 0
    while 0<n:
        digit = n%10
        sum += digit
        n//=10
    if sum <=9:
        print(sum)
        break
    else:
        n = sum
 """

""" 
def fun(n):
    total = 0 
    while  0<n:
        digit = n%10
        total +=digit
        n//=10
    if total <=9:
        return total
    return fun(total)
print(fun(98765)) """

""" def fun(n, rev= 0):
    if n == 0:
        return  rev
    rev = rev*10+n%10
    return  fun(n//10,rev)
print(fun(12345))
 """
""" lst = [1, [2, 3], [4, [5, 6]], 7]

def fun(li,output = []):
    
    for i in li:
        if type(i)==list:
            fun(i)
        else:
            output.append(i)
    return output
res = fun(lst)
print(res) """


""" lst =  [ [2, [3, 4]], [5, [6, [7]]]] 
def fun(li,sum = 0):
    for i in li:
        if type(i) == list:
            fun(i)
        else:
            sum +=i
    return sum
res = fun(lst)
print(res) """

""" def fun(n,result = 1):  
    
    if n == 0 :
        return result
    result *=n%10
    return fun(n//10,result)
print(fun(2345)) """

""" def fun (n,count= 0):
    result = n%10
    if result%2==0:
        count +=1
    if n == 1:
        return count
    return fun(n//10,count)
print(fun(123456)) """



""" 

def out(fun):
    def inner():
        print("="*30)
        fun()
        print("="*30)
    return inner




@out
def display():
    print("welcom to python")

display()
 """
""" def out(fun):
    def inner():
        res =fun()
        print("before")
        print(res)
        print("after")
    return inner
@out
def display():
    return 10+20
display() """
""" def out(fun):
    def inner(a,b):
        print("before")
        res = fun(a,b)
        print(res)
        print("after")
    return inner
@out
def add(a,b):
    return a+b
add(2,4) """


""" def out(n,large = 0):
    result = n%10
    if result > large:
        large  = result
    if n == 0:
        return large
    return out(n//10,large)
print(out(58329)) """



""" def out(fun):
    def inner(name):
        print("starting")
        fun(name)
        print("ending")
    return inner

@out
def display(name):
    print("hello",name)
na = input("enter your name")
display(na)
 """

""" def out(n):
    if n == 0:
        return 0

    digit = n % 10
    result = out(n // 10)
    
    if digit % 2 == 0:
        return digit + result

    return result
print(out(123456)) """




""" def out(fun):
    def inner(a,b):
        print("staring")
        res = fun(a,b)
        print(res)
        print("ending")
    return inner
@out
def display(a,b):
    return a+b
display(10,30) """



""" def fun(n):
    if n == 0:
        return  0
    digit = n%10
    result = fun(n//10)
    if digit > result:
        return digit
    return result



print(fun(58329)) """

""" class Car:
    def __init__(self,brand ,model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print(self.brand,self.model,self.price)
s1 = Car("tata","tare",344566)
s1.display() """


""" class Emploree:
    def __init__(self, name, employee, salary):
        self.name = name
        self.employee = employee
        self.salary = salary
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.employee)
s1 = Emploree("teja",1,50000)
s2 = Emploree("ram",2,60000)

s2.display()
s1.display() """

""" lst = [2,4,6,8,10]
res = list(map(lambda n:n**2,lst))
print(res) """
""" 
lst = [10, 15, 20, 30, 45, 50, 60, 72] 
res = list(filter(lambda n:n%3==0 and n%5==0,lst))
print(res) """
""" from functools import reduce
lst = [2, 3, 4, 5]
res = reduce(lambda a,b:a*b,lst)
print(res) """
""" lst = [1, 2, 3, 4, 5, 6, 7, 8]
res =list(map(lambda n:n**3 ,filter(lambda n:n%2==0,lst)))
print(res) """
""" 
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"name:{self.name}")
        print(f"marks:{self.marks}")
s1 = Student("teja",56)
s1.display() """

""" class Bank:
    def __init__(self,name):
        self.name = name
    def deposit(self,n):
        return n
    def withdrwa(m):
        return m - deposit(n)
    def display(n):
        return self.name ,withdrwa()

s1 = Bank("teja")
s1.deposit(10000) """
""" 
class Stud:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no =roll_no
        self.marks = marks
    def display(self):
        print("Name :",self.name)
        print("ROll_no :",self.roll_no)
        print("Marks :",self.marks)
s1 = Stud("teja",101,85)
s1.display() """

""" class Rect:
    def __init__(self,len,breadth):
        self.len = len
        self.breadth = breadth
    def length(self):
        return self.len*self.breadth
    def Per(self):
        return 2*(self.len+self.breadth)
s1 = Rect(10,5)
res = s1.length()
print(res)
res2 = s1.Per()
print(res2) """
""" 
class Emp:
    def __init__(self,name,id,salary,):
        self.name = name
        self.id = id
        self.salary = salary
        self.m = 0
    def sal(self,n):
        self.m = n
    def display(self):
        print(self.name)
        print(self.id)
        print(self.n)
        print(self.salary+self.m)

s1 = Emp("surya",101,40000)
s1.sal(5000)
s1.display()
"""
        

""" 
class Mobile:
    def __init__(self,brand,model,prince):
        self.brand = brand
        self.model = model
        self.prince = prince
    def display(self):
        print("brand",self.brand)
        print("price",self.prince)
        print("model",self.model)
obj = Mobile("samsung","s24",70000)
obj.display()

obj1 = Mobile("redmi","redmi13",15000)
obj1.display()
 """
""" 
class Stud:
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks
    def display(self):
        if  self.marks > 40:
            print(self.name,"pass")
        else:
            print(self.name,"fali")
s1 = Stud("teja",45)
s2  = Stud("ravi",39)
s1.display()
s2.display() """

""" class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
   
    def dispay(self):
        print(self.name)
        print(self.price*self.quantity)
        print(self.quantity)
s1 = Product("teja",1000,2)
s1.dispay() """

""" class Cir:
    def __init__(self,radius):
        self.radius =radius
    def display(self):
        print("area",3.14*(self.radius*self.radius))
s1 = Cir(5)
s1.display()
 """
""" class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def withdraw(self,n):
        if self.balance > n:
            self.balance = self.balance - n
    def disposite(self,m):
        self.balance = self.balance+m
    def display(self):
        print("name : " ,self.name)
        print("balance",self.balance)
c1 = Bank("ravi",5000)
c1.display()
c1.disposite(1400)
c1.display()
c1.withdraw(4000)
c1.display() """

""" 
class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def discount(self,percent):
        self.price = self.price - ((percent/100)*self.price) 
    def display(self):
        print(self.price)

c1 = Mobile("samsung",50000)
c1.discount(10)
c1.display() """

""" class Mobile:
    def __init__(self,brand,price):
        self.price = price
    def display(self):
        print(self.brand)
        print(self.price)

c1 = Mobile("lg",3456)
print(c1.brand) """

""" class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def display(self):
        print(self.__balance)
print(self.__balance) """


""" class Stud:
    def __init__(self,name):
        self.__name = name
    def get_balance(self):
        return self.__name
c1 = Stud("teja")
print(c1.get_balance()) """

""" class Mobile:
    def __init__(self, price):
        self.__price = price

    def  access(self):
        return self.__price
c1 = Mobile(4500)
print(c1.access()) """

""" class Mobile:
    def __init__(self, price):
        self.__price = price
    def  access(self):
        return self.__price
    def set_price(self, price):
        self.__price = price
c1 = Mobile(4500)
c1.set_price(2300)
print(c1.access()) """

""" class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.__balance  = balance
    def deposit(self,m):
        self.__balance = self.__balance+m
    def withdraw(self,w):
        if self.__balance > w:
            self.__balance = self.__balance - w
    def  display(self):
        return self.name,self.__balance
s1 = Bank("teja",5000)
s1.withdraw(2000)
s1.deposit(5000)
res = s1.display()
print(res) """
""" 
class Emp:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    @property    
    def getter(self):
        return self.name,self.__salary
    @getter.setter
    def getter(self,m):
        self.__salary = m
c1 = Emp("teja",5000)
res = c1.getter
print(res)
c1.setter = 6000
res = c1.getter
print(res) """
""" 
 """
""" 
class Tem:
    def __init__(self,tempareture):
        self.__tempareture = tempareture
    @property
    def xyz(self):
        result = f"tempareture   {self.__tempareture}"
        return result
    @xyz.setter
    def xyz(self,m):
        self.__tempareture = m
c1 = Tem(39)
res = c1.xyz
print(res)
c1.xyz = 60
res = c1.xyz
print(res)
 """
""" 
class Student :
    def __init_(self ,name,age,m1,m2):
        self.name = name
        self.age = age
        self.m1= m1
        self.m2 = m2
    def display(self):
        print(self.name,self.age)
    def ava(self):
        return (self.m1+self.m2)//2
    def grade(self):
        avg = self.ava()
        if avg >= 70:
            grade = "A"
        elif avg >=50:
            grade = "B"
        else:
            grade = "c"
        msg = f"{self.name},grade{grade}"
class Mgmt:
    def __init__(self):
        self.student = []
    def join(self,std):
        self.student.append(std)
    def display_students(self):
        for  std in self.student:
            std.dispay()


    
 """
""" 
class A:
    def __init__(self,vehicle):
        self.vehicle = vehicle
    def display(self):
        print(self.vehicle)
class B(A):
    def __init__(self,model):
        self.model = model
    def display(self):
        super().display()
        print(self.model)

c1 = A("toyota")
c2 = B("innova")
c2.display()
     """


""" class User:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name)
class Salary(User):
    def __init__(self,salary):
        self.salary = salary
    def display(self):
        super().display()
        print(self.salary)

c2 = Salary(2500,"tjea")
c2.display()
 """


""" 
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle started")
        print(self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print("Car is driving")
        print(self.model)


c1 = Car("Toyota", "Innova")

c1.start()
c1.drive()
 """ """
class Parent:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name)
class Student(Parent):
    def __init__(self,name,mark):
        super().__init__(name)
        self.mark = mark
    def display1(self):
        print(self.mark)
c1 = Student("teja",85)
c1.display()
c1.display1()
 """
""" class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
c1 = Dog()
c1.sound()
 """
""" class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("employee")
class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def display(self):
        print("Manager")
c1  = Manager("teja",40550)
c1.display() """

""" class Vehicle:
    def start(self):
        print("vehicle starts")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick")
b1  = Bike()
b1.start() """

""" 
class Per:
    def __init_(self,name):
       self.name = name
    def display(self):
        print(self.name)
class Salary(Per):
    def __init__(self,name,salary):
        super().__init(name)
        self.salary = salary
    def display_salayr(self):
        print(self.salary)
class Department(Salary)
    def __init__(self,name,salary,department):
        super().__init__(salary,name)
    def name  """




""" class Emp:
    def __init__(self,name,salary):
        self.name =name
        self.salary = salary
    def display(self):
        print(self.name)
        print(self.salary)
class Manager(Emp):
    def __init__(self,name ,salary,dept):
        super().__init__(name,salary)
        self.dept  = dept
    def display(self):
        super().display()
        print(self.dept)
c1 = Manager("teja",45000,"IT")
c1.display()
 """
""" class Mobile():
    def Power_on(self):
        print("Mobile Powered on")
class SmartPhone(Mobile):
    def use_app(self):
        print("using Instager")
c1 = SmartPhone()
c1.Power_on()
c1.use_app() """

""" class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name)
class Marks(Student):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks = marks
    def display(self):
        super().display()
        if self.marks >40:
            print("pass")
        else:
            print("fail")
class Result(Marks):
    pass
c1 = Result("teja",60)
c1.display() """


""" class Company:
    def display(self):
        print("teja techs")
class Dev(Company):
    def display1(self):
        
        print("develop the software")
class Test(Company):
    def display(self):
        super().display()
        print("test the software")

c1 = Dev()
c2 = Test()
c2.display()
c1.display()
c1.display1() """

""" class A:
    def sound(self):
        print("hello")
class B:
    def sound(self):
        print("world")
class C:
    def sound(self):
        print("teja")
obj = [A(),B(),C()]
for i in obj:
    i.sound()
def  fun(n):
    n.sound()
fun(A())
fun(B())
fun(C())
 """
""" class Vehicle:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def display(self):
        print(self.brand)
        print(self.price)
class car(Vehicle):
    def __init__(self,fuel,brand,price):
        super().__init__(brand,price)
        self.fuel = fuel
    def display(self):
        super().display()
        print(self.fuel)
obj = car("petrol","toyota",300000)
obj.display() """

""" class Vehicle:
    def strat(self):
        print("vehicle is starting")
class Car(Vehicle):
    def strat(self):
        print("car started with a key")
c1= Car()
c1.strat() """
""" 
class Dog:
    def sound(self):
        print("dog barks ")
class Cat:
    def sound(self):
        print("car meows")
obj = [Dog(),Cat()]
for i in obj:
    i.sound() """
""" 
class Bike:
    def move(self):
        print("bike moves on two wheels")
class  Car:
    def move(self):
        print("car moves on four wheels")
def fun(obj):
    obj.move()
fun(Bike())
fun(Car()) """
""" 
class Emp:
    def salary(self):
        print("basic salary")
class Developer(Emp):
    def salary(self):
        print("Developer Salary: 50000")
class Tester(Emp):
    def salary(self):
        print("Tester Salary: 40000")

c1 = Tester()
c1.salary()
c2=Developer()
c2.salary() """
class Shape:
    def  area(self):
        print("Area of Shape")
class Circle(Shape):
    def area(self):
        print("Circle Area")
class Rect(Shape):
    def area(self):
        print("rectangle area")

obj  = [Circle(),Rect()]
for i in obj:
    i.area()

""""""