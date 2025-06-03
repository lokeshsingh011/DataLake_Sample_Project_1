import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load your transformed CSV
csv_path = r'c:\Users\lkmah\Downloads\Data-Lake-Project\data_lake\transformed\sample.csv'
df = pd.read_csv(csv_path)

# Show basic info
print("\n📋 Dataset Overview:")
print(df.info())
print("\n📊 Descriptive Statistics:")
print(df.describe())
print("\n🧪 Sample Data:")
print(df.head())

# Create a directory for saving plots
output_dir = os.path.join(os.path.dirname(csv_path), 'visualizations')
os.makedirs(output_dir, exist_ok=True)

# 🎯 1. Survival Rate by Class
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Pclass', y='SurvivalRate', palette='Blues_d')
plt.title('Average Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'survival_rate_by_class.png'))
plt.show()

# 🎯 2. Fare by Class
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Pclass', y='Fare', palette='Greens_d')
plt.title('Average Fare by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'fare_by_class.png'))
plt.show()

# 🎯 3. Survival Rate by Embarkation Port
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Embarked', y='SurvivalRate', palette='Purples_d')
plt.title('Survival Rate by Embarkation Port')
plt.xlabel('Embarked From')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'survival_rate_by_embarked.png'))
plt.show()

# 🎯 4. Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df[['SurvivalRate', 'Fare']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
plt.show()

print(f"\n✅ Visualizations saved to: {output_dir}")
# This script visualizes the data from the transformed layer of the data lake project.