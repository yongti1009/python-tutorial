# 🍎 Mac Data Scientist 開發環境完整安裝指南（2026 版）

適用對象：

* MacBook Air / Pro（Intel 或 Apple Silicon）
* VS Code
* Python Data Scientist
* Jupyter Notebook
* Machine Learning
* Kaggle

---

# Step 1：安裝 Homebrew（Mac 必備）

Homebrew 是 macOS 最常用的套件管理工具。

打開 Terminal：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

確認是否成功：

```bash
brew --version
```

例如：

```text
Homebrew 4.x.x
```

---

# Step 2：安裝 Git

```bash
brew install git
```

確認：

```bash
git --version
```

---

# Step 3：安裝 Python（建議使用 Homebrew）

> 不建議使用 macOS 內建 Python。

```bash
brew install python
```

確認：

```bash
python3 --version
```

例如：

```text
Python 3.12.x
```

---

# Step 4：更新 pip

```bash
python3 -m pip install --upgrade pip
```

確認：

```bash
pip3 --version
```

---

# Step 5：建立 Data Scientist 專案資料夾

例如：

```text
~/Documents/DataScience
```

Terminal：

```bash
mkdir ~/Documents/DataScience
cd ~/Documents/DataScience
```

---

# Step 6：建立 Python 虛擬環境（推薦）

建立：

```bash
python3 -m venv ds-env
```

啟動：

```bash
source ds-env/bin/activate
```

成功後 Terminal 前面會看到：

```text
(ds-env)
```

以後每次開始學習都先啟動：

```bash
source ~/Documents/DataScience/ds-env/bin/activate
```

---

# Step 7：安裝 Data Scientist 必備套件

```bash
pip install \
numpy \
pandas \
matplotlib \
seaborn \
scipy \
scikit-learn \
jupyter \
notebook \
ipykernel \
plotly \
openpyxl \
xlsxwriter \
statsmodels \
missingno
```

---

# Step 8：註冊 Jupyter Kernel

讓 VS Code 能辨識你的虛擬環境：

```bash
python -m ipykernel install --user --name=ds-env --display-name "Python (ds-env)"
```

---

# Step 9：安裝 VS Code 擴充套件

建議安裝：

* Python
* Jupyter
* Pylance
* GitHub Copilot（可選）
* Markdown All in One
* Rainbow CSV（可選）

---

# Step 10：VS Code 選擇 Kernel

打開 Notebook：

右上角：

```
Select Kernel
```

選：

```
Python (ds-env)
```

---

# Step 11：測試環境

建立 Notebook：

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Matplotlib:", plt.matplotlib.__version__)
print("Seaborn:", sns.__version__)
print("Scikit-learn:", sklearn.__version__)
```

沒有任何錯誤代表成功。

---

# Step 12：測試 Titanic Dataset

```python
import seaborn as sns

df = sns.load_dataset("titanic")

df.head()
```

若正常顯示資料代表：

* Pandas
* Seaborn
* Jupyter

全部正常。

---

# Step 13：建立專案結構（推薦）

```
DataScience/
│
├── ds-env/
│
├── Python/
│   ├── Day01
│   ├── Day02
│   ├── Day03
│   ├── Day04
│   ├── Day05
│   ├── Day06
│   └── Day07
│
├── SQL/
│
├── MachineLearning/
│
├── Portfolio/
│
└── Datasets/
```

---

# Step 14：安裝 Machine Learning 套件（未來）

```bash
pip install \
xgboost \
lightgbm \
catboost
```

---

# Step 15：確認所有套件

```bash
pip list
```

至少應該看到：

```
numpy
pandas
matplotlib
seaborn
scikit-learn
scipy
plotly
jupyter
ipykernel
openpyxl
statsmodels
missingno
```

---

# Data Scientist 學習階段

## 第 1 階段（目前）

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn

## 第 2 階段

* SQL
* Git
* EDA
* Statistics

## 第 3 階段

* Scikit-learn
* Machine Learning
* Feature Engineering

## 第 4 階段

* XGBoost
* LightGBM
* Kaggle
* Portfolio

---

# 每次開始學習的流程

開啟 Terminal：

```bash
cd ~/Documents/DataScience
source ds-env/bin/activate
code .
```

接著在 VS Code 開啟 Notebook，確認 Kernel 為：

```
Python (ds-env)
```

即可開始學習。

---

# 完成後你將擁有

✅ 完整 Python 開發環境

✅ Jupyter Notebook

✅ VS Code

✅ Git

✅ Data Scientist 所需套件

✅ Machine Learning 環境

✅ 可直接開始 Kaggle、EDA、AI 專案

之後只需要專注於學習，不必再花時間處理環境問題。
