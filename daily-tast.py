

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

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"name:{self.name}")
        print(f"marks:{self.marks}")
s1 = Student("teja",56)
s1.display()