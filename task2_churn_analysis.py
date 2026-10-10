import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

def load_and_prep_data(file_path):
    print("Loading Customer Churn dataset...")
    df = pd.read_csv(file_path)
    
    # Handle TotalCharges missing/whitespace values
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].str.strip(), errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
    
    print(f"Data Loaded Successfully! Total Records: {len(df):,}\n")
    return df

def analyze_churn(df):
    print("==========================================")
    print("     CUSTOMER CHURN ANALYSIS REPORT       ")
    print("==========================================")
    
    # Calculate Churn Rate
    churn_counts = df['Churn'].value_counts()
    churn_rate = (churn_counts.get('Yes', 0) / len(df)) * 100
    
    print(f"Total Customers:  {len(df):,}")
    print(f"Retained:         {churn_counts.get('No', 0):,}")
    print(f"Churned:          {churn_counts.get('Yes', 0):,}")
    print(f"Overall Churn Rate: {churn_rate:.2f}%\n")
    
    os.makedirs("output_charts", exist_ok=True)
    
    # 1. Churn Distribution (Pie Chart)
    plt.figure(figsize=(6, 6))
    plt.pie(churn_counts, labels=['Retained', 'Churned'], autopct='%1.1f%%', colors=['#2ecc71', '#e74c3c'], startangle=90, explode=(0, 0.1))
    plt.title('Overall Customer Churn Distribution', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('output_charts/churn_distribution.png', dpi=300)
    plt.close()

    # 2. Churn by Contract Type
    contract_churn = df.groupby(['Contract', 'Churn']).size().unstack()
    print("--- Churn Count by Contract Type ---")
    print(contract_churn.to_string(), "\n")
    
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='Contract', hue='Churn', palette=['#2ecc71', '#e74c3c'])
    plt.title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
    plt.xlabel('Contract Type')
    plt.ylabel('Customer Count')
    plt.tight_layout()
    plt.savefig('output_charts/churn_by_contract.png', dpi=300)
    plt.close()

    # 3. Monthly Charges vs Churn
    plt.figure(figsize=(9, 5))
    sns.kdeplot(data=df, x='MonthlyCharges', hue='Churn', common_norm=False, palette=['#2ecc71', '#e74c3c'], fill=True)
    plt.title('Monthly Charges Distribution by Churn Status', fontsize=14, fontweight='bold')
    plt.xlabel('Monthly Charges ($)')
    plt.ylabel('Density')
    plt.tight_layout()
    plt.savefig('output_charts/monthly_charges_churn.png', dpi=300)
    plt.close()

    # 4. Tenure vs Churn
    plt.figure(figsize=(9, 5))
    sns.histplot(data=df, x='tenure', hue='Churn', multiple='stack', palette=['#2ecc71', '#e74c3c'], bins=30)
    plt.title('Customer Churn vs Tenure (Months)', fontsize=14, fontweight='bold')
    plt.xlabel('Tenure (Months)')
    plt.ylabel('Customer Count')
    plt.tight_layout()
    plt.savefig('output_charts/tenure_vs_churn.png', dpi=300)
    plt.close()

    print("Analysis complete! All charts saved in 'output_charts/' folder.")

if __name__ == "__main__":
    file_name = "Telco-Customer-Churn.csv"
    if os.path.exists(file_name):
        df_churn = load_and_prep_data(file_name)
        analyze_churn(df_churn)
    else:
        print(f"Error: {file_name} not found.")