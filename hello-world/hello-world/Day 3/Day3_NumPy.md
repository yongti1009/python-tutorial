# Day 3：NumPy（約 3~4 小時）

先安裝：

```python
import numpy as np
```

---

# Part 1：建立 NumPy array（30 分鐘）

NumPy array 就像升級版的 list，可以讓電腦更快進行數值計算。

建立：

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
```

輸出：

```python
[1 2 3 4 5]
```

查看型態：

```python
print(type(numbers))
```

輸出：

```python
<class 'numpy.ndarray'>
```

---

## 練習 1

建立：

```python
scores = np.array([80, 90, 75, 88, 95])
```

印出：

```python
print(scores)
```

應得到：

```python
[80 90 75 88 95]
```

---

# Part 2：sum()（20 分鐘）

sum() 可以計算總和。

建立：

```python
scores = np.array([80, 90, 75, 88, 95])
```

計算：

```python
print(scores.sum())
```

輸出：

```python
428
```

---

## 練習 2

建立：

```python
sales = np.array([100, 150, 120, 180])
```

印出總銷售額。

---

# Part 3：mean()（平均值）（20 分鐘）

建立：

```python
scores = np.array([80, 90, 75, 88, 95])
```

計算平均：

```python
print(scores.mean())
```

輸出：

```python
85.6
```

---

## 練習 3

建立：

```python
temperature = np.array([25, 27, 28, 26, 30])
```

求平均溫度。

---

# Part 4：max()、min()（20 分鐘）

建立：

```python
scores = np.array([80, 90, 75, 88, 95])
```

最高分：

```python
print(scores.max())
```

最低分：

```python
print(scores.min())
```

輸出：

```python
95
75
```

---

## 練習 4

建立：

```python
height = np.array([165, 172, 180, 168, 175])
```

找出：

* 最高身高
* 最低身高

---

# Part 5：std()（標準差）（30 分鐘）

標準差代表資料的分散程度。

建立：

```python
scores = np.array([80, 90, 75, 88, 95])
```

計算：

```python
print(scores.std())
```

輸出：

```python
6.88
```

（數值可能有小數差異）

---

## 練習 5

建立：

```python
weight = np.array([60, 62, 58, 65, 61])
```

求：

```python
weight.std()
```

---

# Part 6：reshape()（40 分鐘）

reshape 可以改變資料形狀。

建立：

```python
numbers = np.array([1,2,3,4,5,6])
```

變成 2×3：

```python
print(numbers.reshape(2,3))
```

輸出：

```python
[[1 2 3]
 [4 5 6]]
```

變成 3×2：

```python
print(numbers.reshape(3,2))
```

輸出：

```python
[[1 2]
 [3 4]
 [5 6]]
```

---

## 練習 6

建立：

```python
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
```

將它：

* reshape 成 3×4
* reshape 成 4×3

---

# Part 7：NumPy array 和 list 的差別（30 分鐘）

Python list：

```python
a = [1,2,3]
b = [4,5,6]

print(a+b)
```

輸出：

```python
[1,2,3,4,5,6]
```

是「合併」。

---

NumPy：

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
```

輸出：

```python
[5 7 9]
```

是「逐個元素相加」。

---

## 練習 7

觀察：

```python
list1 = [1,2,3]
list2 = [4,5,6]

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(list1+list2)
print(arr1+arr2)

print(list1*2)
print(arr1*2)
```

並回答：

1. `list + list` 的結果是什麼？
2. `array + array` 的結果是什麼？
3. `list * 2` 和 `array * 2` 有什麼不同？

---
# Day 3：NumPy 專案練習
# ⭐ Project 1：成績分析器（Day 3 專題）

建立：

```python
scores = np.array([78,85,90,92,88,76,95])
```

輸出：

```text
平均分數：
最高分：
最低分：
總分：
標準差：
```

---

# Project 2：BMI 分析器 ★

建立：

```python
import numpy as np

height = np.array([170, 165, 180, 175])
weight = np.array([65, 55, 80, 70])
```

完成：

BMI = 體重 / (身高(m)^2)

輸出：

```text
BMI：
[22.49 20.20 24.69 22.86]

平均 BMI：
最高 BMI：
最低 BMI：
```

學習重點：

* array 運算
* mean()
* max()
* min()

---

# Project 3：一週氣溫分析 ★

建立：

```python
temperature = np.array([30, 32, 29, 28, 33, 35, 31])
```

求：

* 平均溫度
* 最高溫
* 最低溫
* 溫度標準差

輸出：

```text
平均：
最高：
最低：
標準差：
```

學習重點：

```python
mean()
max()
min()
std()
```

---

# Project 4：公司銷售分析 ★★

建立：

```python
sales = np.array([120,150,180,200,170,220,250])
```

輸出：

```text
總銷售：
平均銷售：
最高銷售：
最低銷售：
```

再輸出：

```text
高於平均值的銷售：

[180 200 220 250]
```

提示：

```python
sales > sales.mean()
```

以及：

```python
sales[sales > sales.mean()]
```

學習重點：

Boolean Indexing

---

# Project 5：考試成績分析 ★★

建立：

```python
scores = np.array([78,85,92,60,55,88,95,70])
```

求：

全班平均：

```python
scores.mean()
```

不及格成績：

```python
scores[scores < 60]
```

不及格人數：

```python
len(scores[scores < 60])
```

輸出：

```text
不及格成績：

[55]

不及格人數：

1
```

---

# Project 6：找出高收入者 ★★★

建立：

```python
salary = np.array([
40000,
55000,
70000,
45000,
90000,
60000
])
```

找出：

收入 > 60000

輸出：

```text
高收入者：

[70000 90000]
```

求：

* 平均收入
* 最高收入
* 最低收入

---

# Project 7：股票價格分析 ★★★

建立：

```python
stock = np.array([
100,
105,
98,
110,
108,
115,
120
])
```

求：

```text
平均價格：
最高價格：
最低價格：
價格波動（std）：
```

再找出：

價格 > 平均值

---

# Project 8：矩陣製作器 ★★★

建立：

```python
numbers = np.array([
1,2,3,4,5,6,
7,8,9,10,11,12
])
```

完成：

### 3 × 4

```python
numbers.reshape(3,4)
```

### 4 × 3

```python
numbers.reshape(4,3)
```

### 2 × 6

```python
numbers.reshape(2,6)
```

### 6 × 2

```python
numbers.reshape(6,2)
```

---

# Project 9：班級身高分析 ★★★★

建立：

```python
height = np.array([
165,170,172,168,
180,175,178,160,
162,169
])
```

輸出：

```text
平均身高：
最高身高：
最低身高：
標準差：
```

找出：

```text
高於平均的人：

[170 172 180 175 178]
```

---

# Project 10：每天步數分析 ★★★★

建立：

```python
steps = np.array([
5000,
7000,
8000,
6000,
10000,
12000,
9000
])
```

求：

```text
總步數：
平均步數：
最高步數：
最低步數：
```

再找：

```text
超過 8000 步：

[10000 12000 9000]
```

---

# Project 11：電商訂單分析 ★★★★★

建立：

```python
orders = np.array([
150,
200,
120,
300,
180,
250,
400,
350
])
```

求：

```text
總營收：
平均訂單金額：
最高訂單：
最低訂單：
標準差：
```

找出：

大於平均訂單的金額

輸出：

```text
高價訂單：

[300 250 400 350]
```

---

# Project 12：迷你 Data Scientist 專案 ★★★★★

某商店一週銷售量：

```python
sales = np.array([
120,150,180,200,170,220,250
])
```

請輸出：

```text
===== Sales Report =====

總銷售量：
平均銷售量：
最高銷售量：
最低銷售量：
標準差：

高於平均值：

低於平均值：

共有幾天高於平均：
共有幾天低於平均：
```

---

# Project 13：學生成績排行榜 ★★★★★

建立：

```python
students = np.array([
85,92,78,96,88,75,90
])
```

請找出：

### 90 分以上

```python
[92 96 90]
```

### 不及格（<60）

### 平均分數

### 標準差

### 最高分

### 最低分

---

# Day 3 學習目標

熟悉：

* np.array()
* sum()
* mean()
* std()
* max()
* min()
* reshape()
* Boolean Indexing

完成後即可進入：

# Day 4：Pandas

學習：

* Series
* DataFrame
* read_csv()
* head()
* shape
* columns
* describe()

正式進入 Data Scientist 的資料分析流程。


