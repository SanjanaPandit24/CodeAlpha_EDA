import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic.csv')

# Cleaning
df.drop('Cabin', axis=1, inplace=True)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Feature Engineering - Yahi pehle banana tha
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# 1
plt.figure()
sns.countplot(x='Survived', data=df)
plt.title('1. Survival Count')
plt.savefig('1_survival_count.png')
plt.show()

# 2
plt.figure()
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('2. Survival by Pclass')
plt.savefig('2_pclass_survival.png')
plt.show()

# 3
plt.figure()
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('3. Survival by Sex')
plt.savefig('3_sex_survival.png')
plt.show()

# 4
plt.figure()
sns.histplot(df['Age'], kde=True)
plt.title('4. Age Distribution')
plt.savefig('4_age_distribution.png')
plt.show()

# 5
plt.figure()
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('5. Fare vs Survival')
plt.savefig('5_fare_survival.png')
plt.show()

# 6
plt.figure(figsize=(8,6))
numeric_df = df[['Survived','Pclass','Age','SibSp','Parch','Fare']]
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('6. Correlation Heatmap')
plt.savefig('6_correlation.png')
plt.show()

# 7
plt.figure(figsize=(7,4))
sns.countplot(x='FamilySize', hue='Survived', data=df)
plt.title('7. Survival by Family Size')
plt.savefig('7_family_survival.png')
plt.show()

print("EDA Done - All 7 graphs saved!")