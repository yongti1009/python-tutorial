# Day 6：Matplotlib + Seaborn（資料視覺化）⭐⭐⭐⭐⭐

⏱️ 時間：3～4 小時
🎯 目標：能畫出 Data Scientist 最常用的四種圖

```python id="init1"
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
```

---

# Part 1：Histogram（直方圖）⭐⭐⭐⭐⭐

用來看「分布」

## 學習

```python id="hist1"
plt.hist(df["age"].dropna())
plt.show()
```

👉 觀察：

* 年齡分布
* 哪個年齡最多

---

## Exercise 1 ⭐

畫出：

* fare（票價）的分布圖

```python
plt.hist(df["fare"].dropna())
plt.show()
```

---

## Exercise 2 ⭐

畫出：

* age 分布圖
* 並觀察是否有偏態（skewed）

---

## Exercise 3 ⭐⭐

調整 bins：

```python id="hist2"
plt.hist(df["age"].dropna(), bins=20)
plt.show()
```

👉 試試：

* bins = 10
* bins = 30

觀察差異

---

# Part 2：Scatter Plot（散點圖）⭐⭐⭐⭐⭐

用來看「關係」

## 學習

```python id="sc1"
plt.scatter(df["age"], df["fare"])
plt.show()
```

---

## Exercise 4 ⭐

畫出：

* age vs fare

---

## Exercise 5 ⭐⭐

畫出：

* age vs survived

觀察：

👉 年齡會影響生還嗎？

---

## Exercise 6 ⭐⭐

改變透明度：

```python id="sc2"
plt.scatter(df["age"], df["fare"], alpha=0.3)
plt.show()
```

👉 觀察：

* 是否更容易看出密集區

---

# Part 3：Boxplot（箱型圖）⭐⭐⭐⭐⭐

用來看：

* 中位數
* 分布
* 離群值

---

## 學習

```python id="bx1"
sns.boxplot(x=df["age"])
plt.show()
```

---

## Exercise 7 ⭐

畫出：

* fare 的 boxplot

---

## Exercise 8 ⭐⭐

比較：

```python id="bx2"
sns.boxplot(x="sex", y="age", data=df)
plt.show()
```

👉 看：

* 男女性年齡分布差異

---

## Exercise 9 ⭐⭐⭐

比較：

* class vs fare

```python
sns.boxplot(x="class", y="fare", data=df)
plt.show()
```

---

# Part 4：Heatmap（熱力圖）⭐⭐⭐⭐⭐

用來看「相關性（correlation）」

---

## 學習

先做 correlation matrix：

```python id="hm1"
corr = df.corr(numeric_only=True)
```

畫 heatmap：

```python id="hm2"
sns.heatmap(corr, annot=True)
plt.show()
```

---

## Exercise 10 ⭐⭐

畫 correlation heatmap

---

## Exercise 11 ⭐⭐⭐

觀察：

👉 哪兩個變數關係最強？

---

## Exercise 12 ⭐⭐⭐⭐

嘗試：

```python id="hm3"
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()
```

👉 比較顏色差異

---

# Mini Project 1 ⭐⭐⭐⭐

### 分析年齡是否影響生還

做三件事：

1. histogram（age）
2. scatter（age vs survived）
3. boxplot（age vs survived）

---

# Mini Project 2 ⭐⭐⭐⭐⭐

### 分析票價是否影響生還

做三件事：

1. histogram（fare）
2. boxplot（class vs fare）
3. scatter（age vs fare）

---

# Mini Project 3 ⭐⭐⭐⭐⭐

### Titanic 相關性分析

用 heatmap 回答：

* 哪個變數和 survived 最相關？
* fare 和 class 是否相關？
* age 是否重要？

---

# Bonus（進階思維）⭐⭐⭐⭐⭐

嘗試：

```python id="bx3"
sns.boxplot(x="survived", y="age", data=df)
plt.show()
```

👉 問自己：

* 生還者比較年輕嗎？

---

# Day 6 完成後能力

你會具備：

✅ Histogram（分布）

✅ Scatter plot（關係）

✅ Boxplot（分布+離群值）

✅ Heatmap（相關性）

---

# 🎯 Data Scientist 能力升級

完成 Day 6 後，你已經可以：

✔ 做 EDA（探索式資料分析）

✔ 判斷變數關係

✔ 找出重要特徵

✔ 做基礎 Data Insight

---

# 🚀 下一步建議（Day 7）

如果你要繼續，我建議：

### Day 7：EDA Project（真正專案級）

* Titanic 完整分析報告
* 5~10 張圖
* 結論輸出
* 像面試作品

---
