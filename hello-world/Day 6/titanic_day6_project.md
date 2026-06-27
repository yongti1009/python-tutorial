# 🚢 Titanic Survival Insights Project (Day 6 EDA Project)

## 🎯 1. Project Goal

This project aims to explore the Titanic dataset and answer the following questions:

1. Which variables are most related to survival?
2. Do gender, age, and passenger class affect survival?
3. Does socioeconomic status influence survival?
4. Are single variables enough to explain survival outcomes?

---

## 📦 2. Dataset

```python
import seaborn as sns
df = sns.load_dataset("titanic")
```

---

## 🧹 3. Data Preprocessing

### 3.1 Basic Cleaning

```python
df = df.dropna(subset=["age", "embarked"])
```

---

### 3.2 Feature Engineering

```python
df["is_female"] = (df["sex"] == "female").astype(int)
df["is_alone"] = ((df["sibsp"] + df["parch"]) == 0).astype(int)
df["is_child"] = (df["age"] < 18).astype(int)
```

---

### 3.3 Age Grouping

```python
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 12, 18, 30, 45, 60, 100],
    labels=["child","teen","young_adult","adult","middle","senior"]
)
```

---

## 📊 4. Exploratory Data Analysis (EDA)

### 4.1 Correlation Heatmap

```python
import seaborn as sns
import matplotlib.pyplot as plt

df_corr = df[["survived", "age", "fare", "pclass", "sibsp", "parch", "is_female", "is_alone"]].corr()

sns.heatmap(df_corr, annot=True, cmap="coolwarm")
plt.show()
```

---

### Key Insight:
- Identify variables most correlated with survival

---

### 4.2 Survival by Group

#### Sex vs Survival

```python
df.groupby("sex")["survived"].mean()
```

#### Class vs Survival

```python
df.groupby("pclass")["survived"].mean()
```

#### Age Group vs Survival

```python
df.groupby("age_group")["survived"].mean()
```

---

## 📉 5. Visualization

### Survival Distribution

```python
sns.countplot(x="survived", data=df)
```

### Sex vs Survival

```python
sns.barplot(x="sex", y="survived", data=df)
```

### Class vs Survival

```python
sns.barplot(x="pclass", y="survived", data=df)
```

### Age vs Survival

```python
sns.boxplot(x="survived", y="age", data=df)
```

---

## 🔥 6. Interaction Analysis

### Sex + Class

```python
sns.barplot(x="pclass", y="survived", hue="sex", data=df)
```

### Age + Survival by Sex

```python
sns.boxplot(x="sex", y="age", hue="survived", data=df)
```

---

## 🧠 7. Key Findings

- Gender is the strongest predictor of survival
- Passenger class shows strong negative correlation with survival
- Fare is positively correlated with survival
- Age has weak direct influence on survival
- Survival is multi-factorial, not explained by a single variable

---

## 📌 8. Conclusion

Survival on the Titanic was influenced by multiple factors, especially gender and passenger class.  
This suggests that social hierarchy and demographic structure played a key role in survival outcomes.

---