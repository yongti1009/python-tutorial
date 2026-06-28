# Day 5：Pandas 進階（Data Scientist 核心）⭐⭐⭐⭐⭐

預計時間：4～6 小時

```python
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
```

這一天非常重要。

學會後，你就可以開始做真正的資料分析（EDA）。

---

# Part 1：groupby() ⭐⭐⭐⭐⭐

groupby 是 Data Scientist 最常用的功能之一。

## 學習

依照性別分組：

```python
df.groupby("sex")
```

計算平均年齡：

```python
df.groupby("sex")["age"].mean()
```

可能得到：

```
sex
female    27.9
male      30.7
```

依照艙等分組：

```python
df.groupby("class")["fare"].mean()
```

---

## Exercise 1 ⭐⭐⭐

找出：

不同性別的平均年齡。

---

## Exercise 2 ⭐⭐⭐

找出：

不同艙等的平均票價。

---

## Exercise 3 ⭐⭐⭐

找出：

不同性別的生還率。

提示：

```python
df.groupby("sex")["survived"].mean()
```

---

## Exercise 4 ⭐⭐⭐⭐

找出：

不同艙等的平均年齡。

---

## Exercise 5 ⭐⭐⭐⭐

找出：

不同 embark_town 的平均票價。

---

# Part 2：多個 groupby ⭐⭐⭐⭐⭐

可以同時依照兩個欄位分組。

## 學習

```python
df.groupby(["sex","class"])["survived"].mean()
```

可能得到：

```
female First     0.97
female Second    0.92
male Third       0.14
```

---

## Exercise 6 ⭐⭐⭐⭐

找出：

不同性別 × 艙等的平均年齡。

---

## Exercise 7 ⭐⭐⭐⭐⭐

找出：

不同性別 × 艙等的生還率。

---

# Part 3：pivot_table() ⭐⭐⭐⭐⭐

pivot table 可以把 groupby 的結果變成表格。

## 學習

```python
pd.pivot_table(
    df,
    values="survived",
    index="sex",
    columns="class"
)
```

輸出：

```
class      First   Second   Third
sex
female      0.97    0.92     0.50
male        0.36    0.15     0.14
```

---

## Exercise 8 ⭐⭐⭐⭐

建立：

不同性別 × 艙等的平均年齡表。

提示：

```python
values="age"
```

---

## Exercise 9 ⭐⭐⭐⭐⭐

建立：

不同性別 × 艙等的平均票價表。

---

## Exercise 10 ⭐⭐⭐⭐⭐

建立：

不同 embark_town × class 的平均生還率。

---

# Part 4：缺失值（Missing Value）⭐⭐⭐⭐⭐

先查看缺失值：

```python
df.isnull()
```

統計缺失值數量：

```python
df.isnull().sum()
```

可能得到：

```
age            177
deck           688
embark_town      2
```

---

## Exercise 11 ⭐⭐⭐

找出：

每個欄位缺失值數量。

---

## Exercise 12 ⭐⭐⭐⭐

哪個欄位缺失值最多？

提示：

觀察：

```python
df.isnull().sum()
```

---

# Part 5：dropna() ⭐⭐⭐⭐⭐

刪除缺失值：

```python
df.dropna()
```

刪除 age 缺失值：

```python
df.dropna(subset=["age"])
```

---

## Exercise 13 ⭐⭐⭐⭐

建立：

沒有 age 缺失值的新 DataFrame。

```python
df2 = df.dropna(subset=["age"])
```

---

## Exercise 14 ⭐⭐⭐⭐

比較：

```python
len(df)
```

與

```python
len(df2)
```

少了多少筆資料？

---

# Part 6：fillna() ⭐⭐⭐⭐⭐

使用平均值填補：

```python
df["age"].fillna(
    df["age"].mean()
)
```

建立新欄位：

```python
df["age_fill"] = df["age"].fillna(
    df["age"].mean()
)
```

---

## Exercise 15 ⭐⭐⭐⭐

建立：

```python
fare_fill
```

利用平均票價填補缺失值。

---

## Exercise 16 ⭐⭐⭐⭐⭐

建立：

```python
age_fill
```

利用平均年齡填補缺失值。

---

## Exercise 17 ⭐⭐⭐⭐⭐

確認：

```python
df["age_fill"].isnull().sum()
```

應該得到：

```
0
```

---

# Part 7：merge() ⭐⭐⭐⭐⭐

Data Scientist 幾乎每天都在合併資料。

建立：

```python
student = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Amy","Bob","Cindy"]
})

score = pd.DataFrame({
    "ID":[1,2,3],
    "Score":[90,80,95]
})
```

合併：

```python
pd.merge(student, score)
```

得到：

```
ID Name Score
1 Amy 90
2 Bob 80
3 Cindy 95
```

---

## Exercise 18 ⭐⭐⭐⭐

建立：

### product

```python
ID Product
1 Apple
2 Banana
3 Orange
```

### price

```python
ID Price
1 30
2 20
3 25
```

使用 merge 合併。

---

## Exercise 19 ⭐⭐⭐⭐⭐

建立：

### employee

```python
ID Name
101 Tom
102 Mary
103 John
```

### department

```python
ID Department
101 HR
102 Finance
103 IT
```

合併成：

```
ID Name Department
101 Tom HR
102 Mary Finance
103 John IT
```

---

# Mini Project 1 ⭐⭐⭐⭐

分析：

不同性別的平均年齡與生還率。

提示：

```python
df.groupby("sex")[["age","survived"]].mean()
```

---

# Mini Project 2 ⭐⭐⭐⭐⭐

分析：

不同艙等的：

* 平均年齡
* 平均票價
* 生還率

提示：

```python
df.groupby("class")[["age","fare","survived"]].mean()
```

---

# Mini Project 3 ⭐⭐⭐⭐⭐

建立 Pivot Table：

列：

* sex

欄：

* class

數值：

* survived

觀察：

「哪一群人最容易生還？」

---

# Bonus Project ⭐⭐⭐⭐⭐

回答：

### 「女性是否比男性更容易生還？」

### 「First Class 是否比 Third Class 更容易生還？」

利用：

```python
groupby()

pivot_table()

sort_values()
```

完成一份簡單的 Data Analysis 報告。

---

# Day 5 完成後能力

你將能：

✅ groupby()

✅ 多重 groupby

✅ pivot_table()

✅ dropna()

✅ fillna()

✅ merge()

✅ Missing Value 處理

✅ 基礎 EDA（Exploratory Data Analysis）

---

# 下一步：Day 6

真正的 Data Cleaning ⭐⭐⭐⭐⭐

學習：

```python
unique()

nunique()

duplicated()

drop_duplicates()

replace()

astype()

apply()

lambda
```

Day 6 結束後，你就會進入接近 Junior Data Analyst 的能力範圍。
