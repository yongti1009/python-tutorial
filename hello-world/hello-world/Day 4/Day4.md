# Day 4：Pandas（最重要）⭐⭐⭐⭐⭐

預計時間：4～6 小時

```python
import pandas as pd
```

---

# Part 1：建立 DataFrame ⭐

建立：

```python
data = {
    "Name": ["Amy", "Bob", "Cindy"],
    "Age": [20, 25, 22],
    "Score": [90, 85, 95]
}

df = pd.DataFrame(data)
```

### 學習

* DataFrame
* columns

---

## Exercise 1 ⭐

建立：

| Name | Age | City      |
| ---- | --- | --------- |
| Tom  | 21  | Taipei    |
| Mary | 23  | Taichung  |
| John | 22  | Kaohsiung |

並印出 DataFrame。

---

## Exercise 2 ⭐

建立：

| Product | Price |
| ------- | ----- |
| Apple   | 30    |
| Banana  | 20    |
| Orange  | 25    |

---

# Part 2：讀取 CSV ⭐

### 學習

```python
pd.read_csv()

head()
```

載入 Titanic：

```python
import seaborn as sns

df = sns.load_dataset("titanic")
```

查看前五筆：

```python
df.head()
```

---

## Exercise 3 ⭐

顯示前 3 筆資料：

```python
df.head(3)
```

---

## Exercise 4 ⭐

顯示前 8 筆資料。

---

## Exercise 5 ⭐

回答：

1. 第一個欄位名稱？
2. 最後一個欄位名稱？
3. 一共有多少欄位？

---

# Part 3：資料結構 ⭐⭐

### 學習

查看欄位：

```python
df.columns
```

查看資料大小：

```python
df.shape
```

例如：

```python
(891, 15)
```

表示：

* 891 筆資料
* 15 個欄位

---

## Exercise 6 ⭐⭐

回答：

1. 幾筆資料？
2. 幾個欄位？

---

## Exercise 7 ⭐⭐

印出所有欄位名稱：

```python
print(df.columns)
```

---

## Exercise 8 ⭐⭐

找出：

* 第一個欄位
* 最後一個欄位

提示：

```python
df.columns[0]

df.columns[-1]
```

---

# Part 4：info() 與 describe() ⭐⭐

### 學習

```python
df.info()

df.describe()
```

---

## Exercise 9 ⭐⭐

回答：

1. age 是否有缺失值？
2. sex 的資料型態？

---

## Exercise 10 ⭐⭐

回答：

1. 平均年齡？
2. 最大年齡？
3. 最小年齡？

---

# Part 5：Series（超重要）⭐⭐⭐

取出一欄：

```python
df["age"]
```

查看型態：

```python
type(df["age"])
```

---

## Exercise 11 ⭐⭐⭐

取出：

```python
df["fare"]
```

並查看：

```python
type(df["fare"])
```

---

## Exercise 12 ⭐⭐⭐

取出：

* sex
* class
* survived

---

# Part 6：基本統計 ⭐⭐⭐

### 學習

平均值：

```python
df["age"].mean()
```

最大值：

```python
df["age"].max()
```

最小值：

```python
df["age"].min()
```

總和：

```python
df["fare"].sum()
```

---

## Exercise 13 ⭐⭐⭐

找出：

平均票價。

---

## Exercise 14 ⭐⭐⭐

找出：

* 最大票價
* 最小票價

---

## Exercise 15 ⭐⭐⭐

找出：

* 平均年齡
* 最大年齡
* 最小年齡

---

# Part 7：loc ⭐⭐⭐

### 學習

```python
df.loc[0]

df.loc[0, "age"]

df.loc[0:4]
```

---

## Exercise 16 ⭐⭐⭐

找：

第 10 位乘客所有資料。

---

## Exercise 17 ⭐⭐⭐

找：

第 20 位乘客的性別。

---

## Exercise 18 ⭐⭐⭐

找：

第 50 位乘客年齡。

---

# Part 8：iloc ⭐⭐⭐

### 學習

```python
df.iloc[0]

df.iloc[0,2]

df.iloc[0:5]
```

---

## Exercise 19 ⭐⭐⭐

找：

第二列。

---

## Exercise 20 ⭐⭐⭐

找：

第十列第五欄。

---

## Exercise 21 ⭐⭐⭐

找：

前二十列。

---

# Part 9：sort_values() ⭐⭐⭐

### 學習

由小到大：

```python
df.sort_values("age")
```

由大到小：

```python
df.sort_values("age", ascending=False)
```

---

## Exercise 22 ⭐⭐⭐

找：

年齡最小的人。

---

## Exercise 23 ⭐⭐⭐

找：

年齡最大的前五人。

---

## Exercise 24 ⭐⭐⭐

找：

票價最高的人。

---

# Part 10：value_counts() ⭐⭐⭐

### 學習

```python
df["sex"].value_counts()
```

---

## Exercise 25 ⭐⭐⭐

統計：

男性與女性的人數。

---

## Exercise 26 ⭐⭐⭐

統計：

```python
df["class"].value_counts()
```

回答：

哪個艙等最多？

---

## Exercise 27 ⭐⭐⭐

統計：

```python
df["survived"].value_counts()
```

回答：

* 生還多少人？
* 死亡多少人？

---

# Project 1：Titanic Dataset Overview ⭐

完成：

1. 載入資料
2. 查看前五筆
3. 查看資料資訊
4. 查看統計量

---

# Project 2：Passenger Search ⭐⭐

找出：

* 第 0 位乘客
* 第 10 位乘客
* 第 100 位乘客

---

# Project 3：loc 練習 ⭐⭐

找出：

* 第 5 位乘客年齡
* 第 30 位乘客性別
* 第 50 位乘客是否生存

---

# Project 4：iloc 練習 ⭐⭐

找出：

* 第一列第三欄
* 第十列第五欄
* 前二十列

---

# Project 5：排序分析 ⭐⭐⭐

找出：

* 年齡最小的人
* 年齡最大的人
* 票價最高的人

---

# Project 6：男女比例分析 ⭐⭐⭐

利用：

```python
df["sex"].value_counts()
```

回答：

1. 男性有幾位？
2. 女性有幾位？
3. 哪個性別較多？

---

# Project 7：艙等分析 ⭐⭐⭐

利用：

```python
df["class"].value_counts()
```

回答：

哪個艙等最多？

---

# Project 8：年齡 Top10 ⭐⭐⭐⭐

找出：

年齡最大的前 10 人。

---

# Project 9：生還率分析 ⭐⭐⭐⭐

統計：

* 生還人數
* 死亡人數

並計算：

生還率 = 生還人數 ÷ 總人數 × 100%

---

# Project 10：Data Scientist Mini Report ⭐⭐⭐⭐⭐

回答：

1. Titanic 有多少筆資料？
2. 有多少欄位？
3. 平均年齡是多少？
4. 平均票價是多少？
5. 男女人數？
6. 哪個艙等最多？
7. 生還率是多少？

---

# Bonus（Day 4+）⭐⭐⭐⭐⭐

## Boolean Indexing

```python
df[df["sex"] == "female"]

df[df["age"] > 60]

df[df["fare"] > 100]
```

## GroupBy（Day 5 前半）

```python
df.groupby("sex")["survived"].mean()
```

完成 Day 4 後，你已經具備初階 Data Analyst 的核心能力。
下一步將進入：

# Day 5：Boolean Indexing + GroupBy + Missing Value

（真正 Data Scientist 的核心）
