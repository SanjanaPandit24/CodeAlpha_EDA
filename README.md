# Task 2 - Exploratory Data Analysis (EDA) | Titanic Dataset | CodeAlpha

## 🎯 Objective
Ask meaningful questions about Titanic dataset and explore data structure, trends, patterns and anomalies.

## 📂 Dataset
- File: titanic.csv
- Rows: 891, Columns: 12
- Source: Kaggle

## 🛠️ Tools Used
- Python, Pandas
- Matplotlib, Seaborn
- VS Code

## 🔎 Steps Performed
1. **Load Data:** df.head(), df.shape, df.isnull().sum()
2. **Data Cleaning:** 
   - Age -> filled with median
   - Embarked -> filled with mode
   - Cabin -> dropped (77% missing)
3. **Feature Engineering:** FamilySize = SibSp + Parch + 1

## ❓ Questions Asked
- Q1: How many survived?
- Q2: Does Gender affect survival?
- Q3: Does Pclass affect survival?
- Q4: What is Age distribution?
- Q5: Does Fare affect survival?
- Q6: What is correlation between variables?
- Q7: Does FamilySize affect survival?

## 📈 Visualizations (7 Graphs)
- 1_survival_count.png - Survival count (0=No, 1=Yes)
- 2_gender_survival.png - Female 74% vs Male 19% survived
- 3_class_survival.png - Pclass 1 has highest survival
- 4_age_dist.png - Age distribution with KDE
- 5_fare_survival.png - Fare vs Survival (Boxplot)
- 6_correlation.png - Correlation heatmap
- 7_family_survival.png - Survival by FamilySize

## 💡 Key Insights
- Female passengers had 4x higher survival rate than Male.
- Pclass 1 passengers survived more than Pclass 3.
- Age group 20-35 was maximum on ship.
- Higher Fare = Higher survival chance.
- FamilySize 2-4 had best survival rate.

## 🚀 How to Run
pip install pandas matplotlib seaborn
python titanic_eda.py

## 👩‍💻 Author
CodeAlpha Data Analytics Intern - Task 2