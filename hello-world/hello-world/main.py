print("hello world!")
print("我是小松露")

#建立資料列表，求數值個數(len)、最大值(max)、最小值(min)、總和(sum)、平均值(平均值 = 總和 / 個數)
weights = [ 45, 50, 65, 60, 73, 43, 54, 35, 67]
print(len(weights))
print(max(weights))
print(min(weights))
print(sum(weights))
print(sum(weights) / len(weights))

#Part 1：Variable（變數)
#變數就是「儲存資料的盒子」
name = "Sophie"
age = 21
height = 161
school = "NTU"
grade = 3.2

#查看內容
print(name)
print(age)
print(height)
print(school)

print("My name is " + name + "." + " I study at " + school + ".")

#若想印出分兩行的效果
#1.使用\n換行符號
print("My name is " + name + ".\nI study at " + school + ".")
 
#2.分成兩個print()
#3.使用 f-string（推薦，以後會大量使用的字串格式化方式：f"文字 {變數} 文字"）
print(f"My name is {name}.\nI study at {school}.")

#4.三引號字串
print(f"""My name is {name}.
I study at {school}.""")

#Part 2 Data Type（資料型態）
age = 21 #int 整數 
weight = 51.2 #float 浮點數
name = "Sophie" #str 字串
is_student = True #bool 布林值（True/False）

#查看型態 print(type(age))
print(type(age))
print(type(weight))
print(type(name))
print(type(is_student))

#練習2
temperature = 36.5
city = "Taipei"
is_raining = False
print(type(temperature))
print(type(city))
print(type(is_raining))
print(f'The temperature in {city} is {temperature} degrees.')

#Part 3：List（串列）
#串列是一種可以儲存多個資料的資料型態，使用中括號 [] 表示，資料之間用逗號分隔。
scores = [65, 79, 88 ,90]
print(scores[0]) #印出第一個元素（索引從0開始）
print(scores[1]) #印出第二個元素

#append()方法：在串列末尾添加元素，新增資料
scores.append(100)
print(scores)
print(len(scores)) #len()函數：計算串列中元素的個數
print(sum(scores)) #sum()函數：計算串列中元素的總和
print(max(scores)) #max()函數：計算串列中元素的最大值
print(min(scores)) #min()函數：計算串列中元素的最小值
print(sum(scores) / len(scores)) #計算平均值

#練習3
prices = [20, 45, 65, 79, 40, 23, 55]
prices.append(64)
print(len(prices))
print(sum(prices))
print(max(prices))
print(min(prices))
print(sum(prices) / len(prices))

#Part 4：Dictionary（字典）
#字典是一種以鍵值對（key-value pair）形式儲存資料
student = {
    "name": "Sophie",
    "age": 21,
    "height": 161,
    "school": "NTU",
    "grade": 3.2
}
#取出資料
print(student["name"])
print(student["age"])
print(student["height"])
print(student["school"])
print(student["grade"])

#新增資料
student["major"] = "Life Science"
print(student)

#練習4
book = {
    "Title" : "Python", 
    "Price" : 500
}
book["Author"] = "Eric Matthes"
print(book)

#Part 5：If statement（條件判斷）
#if條件成立就執行縮排的程式碼
score = 85
if score >= 60:
    print("Pass")
#if條件不成立就執行else縮排的程式碼
score = 50
if score >= 60:
    print("Pass")
else:
    print("Fail")

#練習5
temperature = 37.2
if temperature >= 28: 
    print("It's hot today.")
else:
    print("It's cool today.")

#Part 6：For loop（迴圈）
#for迴圈可以重複執行一段程式碼，直到達到指定的次數或條件。
#使用for迴圈印出串列中的每個元素
scores = [65, 79, 88 ,90]
for score in scores:
    print(score)

#求總和
scores = [65, 79, 88 ,90]
total = 0
for score in scores:
    total = total + score
print(total)

#練習6
numbers = [2,3,4,5,6]
total = 0
for number in numbers:
    total = total + number
print(total)

#Part 7 : Function（函式）
#函式是一段可以重複使用的程式碼，使用def關鍵字定義，函式名稱後面跟著括號和冒號。
def greet():
    print("Hello!")
greet() #呼叫函式
#帶參數的函式
def square(x):
    return x * x
result = square(5) #呼叫函式並傳入參數
print(result)

#練習7
def add(a,b):
    return a + b
result = add(9,12)
print(result)

#Project: BMI Calculator（BMI計算器）
def BMI (weight, height):
    return weight / (height/100) **2
result = BMI(65, 170)
print(f"Your BMI is {result: .1f}.")

#進階版：加入條件判斷，根據BMI值判斷體重狀況
weight = float(input("請輸入體重(kg): "))
height = float(input("請輸入身高(cm): "))

BMI = weight / (height/100) **2
print(f"你的BMI是 {BMI:.1f}.") #:.1f表示保留小數點後一位
if BMI < 18.5:
    print("體重過輕")   
elif BMI < 24:
    print("體重正常")
elif BMI < 27:
    print("體重過重")
else:
    print("肥胖")

#Project: 成績平均

