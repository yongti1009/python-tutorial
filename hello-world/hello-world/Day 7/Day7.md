# Day 7：Business EDA & Statistical Thinking（Data Scientist Version）⭐⭐⭐⭐⭐

**預計時間：5～7 小時**

---

# 🎯 今日目標

今天不是學新的函式，而是學會：

* 如何從商業問題開始分析資料
* 如何選擇適合的圖表
* 如何判讀圖表
* 如何決定統計檢定方法
* 如何撰寫分析結論

完成今天後，你將具備：

✅ EDA 分析流程

✅ Visualization Thinking

✅ Statistical Thinking

✅ Business Thinking

---

# Project 1：Titanic Business Case

## Business Question

> 女性真的比較容易生還嗎？

---

## Step 1：提出研究問題

請寫出：

### H₀（虛無假設）

### H₁（對立假設）

並說明：

> 我到底要驗證什麼？

---

## Step 2：思考需要哪些欄位

例如：

* survived
* sex

是否還需要：

* class
* age
* fare

請說明原因。

---

## Step 3：EDA

請自己決定：

哪些圖最適合？

至少畫：

* countplot
* barplot

回答：

* 男女比例？
* 男女生存率？
* 有沒有明顯差異？

---

## Step 4：Group Analysis

完成：

```python
df.groupby("sex")["survived"].mean()

df.groupby(["sex","class"])["survived"].mean()
```

回答：

* 哪一組最高？
* 哪一組最低？

---

## Step 5：Statistical Thinking

請回答：

這是：

* 類別 vs 類別？
* 類別 vs 數值？

應該使用哪種統計檢定？

並說明原因。

---

## Step 6：Business Conclusion

請用主管看得懂的方式寫出結論。

---

# Project 2：Titanic Business Case

## Business Question

> 第一艙真的比較安全嗎？

完成：

---

### 研究問題

---

### EDA

請自己決定：

應該畫：

* barplot？
* countplot？
* heatmap？

並說明理由。

---

### Group Analysis

完成：

```python
df.groupby("class")["survived"].mean()
```

再計算：

```python
df.groupby("class")["survived"].value_counts()
```

回答：

* 每個艙等存活人數
* 每個艙等死亡人數
* 生存率

---

### Conclusion

第一艙真的比較安全嗎？

---

# Project 3：Titanic Business Case

## Business Question

> 小孩真的比較容易生還嗎？

---

## Feature Engineering

建立：

```python
df["age_group"]
```

例如：

* Child
* Adult
* Senior

---

分析：

```python
df.groupby("age_group")["survived"].mean()
```

---

請自己決定：

哪些圖最適合？

並說明原因。

---

# Project 4：Titanic Business Case

## Business Question

> 票價越高的人是否越容易生還？

完成：

---

### Scatterplot

fare vs survived

---

### Boxplot

survived vs fare

---

### Histogram

fare distribution

---

回答：

* fare 是否偏態？
* 有沒有離群值？
* 哪一組 fare 較高？

---

# Project 5：Feature Engineering

建立：

```python
family_size = sibsp + parch + 1
```

新增：

```python
df["family_size"]
```

再建立：

```python
is_alone
```

分析：

```python
df.groupby("is_alone")["survived"].mean()
```

請回答：

> 一個人旅行比較容易生還嗎？

---

# Project 6：Correlation Analysis

建立：

```python
is_female
```

完成：

```python
df.corr(numeric_only=True)
```

畫：

```python
heatmap
```

回答：

* 哪個變數和 survived 最相關？
* fare 和 class 是否相關？
* age 是否重要？

---

# Project 7：Visualization Reading

不要寫程式。

只看圖。

請分析：

* Histogram
* Boxplot
* Scatterplot
* Heatmap

回答：

1. 分布
2. 偏態
3. Outlier
4. Correlation
5. 下一步分析

---

# Project 8：Business Report

請整理成一份 Markdown 報告。

內容包含：

## 1. Business Question

---

## 2. Dataset

---

## 3. EDA

加入：

* 圖片
* 解釋

---

## 4. Statistical Thinking

請回答：

如果：

* 類別 vs 數值

該怎麼辦？

如果：

* 類別 vs 類別

該怎麼辦？

如果：

* 數值 vs 數值

該怎麼辦？

---

## 5. Business Conclusion

最後請用約 300～500 字完成一份完整分析報告。

不要只描述圖表，而是回答：

> 從資料中得到哪些商業洞察？

---

# 🎯 Day 7 完成後能力

你將能夠：

✅ 獨立完成 EDA

✅ 自己選擇適合的圖表

✅ 判讀 Histogram、Boxplot、Heatmap

✅ 使用 Group Analysis 找出 Insight

✅ 建立 Feature Engineering

✅ 判斷適合的統計檢定方法

✅ 撰寫 Business Report

---

# 🚀 Day 8 預告：Statistics for Data Scientists

將正式學習：

* Descriptive Statistics
* Hypothesis Testing
* t-test
* Welch's t-test
* Mann–Whitney U Test
* Chi-square Test
* ANOVA
* Correlation Analysis
* Effect Size
* 如何把統計結果寫成商業報告

完成 Day 8 後，你就能從「會做 EDA」進一步提升到「能用統計方法驗證假設」。
