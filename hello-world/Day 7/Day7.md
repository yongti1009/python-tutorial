# Day 7：Mini Project（Titanic EDA 完整分析）⭐⭐⭐⭐⭐

⏱️ 時間：4～6 小時
🎯 目標：完成第一份 Data Scientist 等級的 EDA 報告

---

# 0. 專案目標

你要完成：

✅ Titanic 資料探索（EDA）
✅ 男女生存率分析
✅ groupby 統計
✅ 基本視覺化（histogram / boxplot）
✅ 結論整理（像報告）

---

# 1. 載入資料

```python id="load1"
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
```

---

# 2. 基本資料探索（EDA 基礎）

## head()

```python id="head1"
df.head()
```

---

## info()

```python id="info1"
df.info()
```

---

## describe()

```python id="desc1"
df.describe()
```

---

## 🎯 Exercise 1

請回答：

1. 資料有幾筆？
2. 有哪些欄位？
3. age 是否有缺失值？

---

# 3. 資料理解（重要）

## 欄位觀察

```python id="col1"
df.columns
```

---

## 🎯 Exercise 2

回答：

* 哪些欄位是數值？
* 哪些欄位是類別？

---

# 4. 男女生存率分析（核心）

## groupby（最重要）

```python id="grp1"
df.groupby("sex")["survived"].mean()
```

---

## 🎯 Exercise 3

請回答：

* 女性生存率是多少？
* 男性生存率是多少？
* 哪個比較高？

---

## 進階 groupby

```python id="grp2"
df.groupby(["sex", "class"])["survived"].mean()
```

---

## 🎯 Exercise 4

回答：

* 哪一群（sex + class）生存率最高？
* 哪一群最低？

---

# 5. 視覺化分析（Data Insight）

---

# 5-1 Histogram（分布）

## 年齡分布

```python id="hist1"
plt.hist(df["age"].dropna(), bins=20)
plt.title("Age Distribution")
plt.show()
```

---

## 🎯 Exercise 5

畫出：

* fare 分布圖

並回答：

👉 大部分票價集中在哪裡？

---

# 5-2 Boxplot（分布 + 比較）

## 性別 vs 年齡

```python id="box1"
sns.boxplot(x="sex", y="age", data=df)
plt.title("Age vs Sex")
plt.show()
```

---

## 🎯 Exercise 6

畫：

* class vs fare boxplot

並回答：

👉 哪一個艙等票價最高？

---

## 生存 vs 年齡

```python id="box2"
sns.boxplot(x="survived", y="age", data=df)
plt.title("Survival vs Age")
plt.show()
```

---

## 🎯 Exercise 7

回答：

👉 生還者是否比較年輕？

---

# 6. 綜合分析（Data Insight）

## Step 1：生存率

```python id="final1"
df["survived"].value_counts(normalize=True)
```

---

## Step 2：男女差異

```python id="final2"
df.groupby("sex")["survived"].mean()
```

---

## Step 3：艙等影響

```python id="final3"
df.groupby("class")["survived"].mean()
```

---

## 🎯 Exercise 8

請回答：

1. 哪個因素影響生存率最大？

   * sex？
   * class？
   * age？

---

# 7. Final Conclusion（一定要寫）

請寫出你的結論（可以用中文）：

---

## ✍️ 範例（可直接改）

```text
從 Titanic 資料分析中可以觀察到：

1. 女性生存率明顯高於男性
2. 第一艙等生存率高於第三艙等
3. 年齡較低的乘客生存率稍高
4. 票價較高的乘客生存率較高

因此可以推測：
性別與艙等是影響生存的重要因素。
```

---

# 8. Colab Notebook 要求（重要）

請整理成 Google Colab：

## 必須包含：

✔ 程式碼
✔ 圖表
✔ markdown 說明
✔ conclusion

---

# 🎯 Day 7 完成後能力

你已經可以：

✔ 做完整 EDA
✔ 用 groupby 找 insight
✔ 畫基本統計圖
✔ 解釋資料
✔ 寫分析報告

---

# 🚀 下一步（非常重要）

如果你完成 Day 7，你已經接近：

> Junior Data Analyst Level

下一步建議：

## Day 8：完整 Data Analysis Project（進階）

* 加入 feature engineering
* missing value strategy
* deeper insight
* storytelling report

---

如果你要，我可以幫你做：

👉「完整 Titanic EDA 範例（像 Kaggle 等級）」
👉「Colab 模板直接給你」
👉「面試用 Data Analyst Portfolio 版本」

只要說一聲就可以。
