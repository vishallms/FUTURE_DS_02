# Task 2: Customer Retention & Churn Analysis

## Overview
This project analyzes customer churn patterns in the Telecommunications domain to identify key churn drivers, evaluate retention strategies, and recommend targeted business interventions.

## Key Insights
- **Overall Churn Rate:** 26.54% (1,869 churned out of 7,043 total customers).
- **Contract Impact:** Customers on **Month-to-month** contracts show the highest churn volume (1,655 users), whereas **Two-year** contracts have the highest retention rate (only 48 churned users).
- **Financial Drivers:** High monthly charges correlate strongly with increased churn probability.
- **Tenure Risk:** Most churn occurs during the initial 1–12 months of customer subscription.

## Tools Used
- **Python 3.13**
- **Pandas** for data cleaning & aggregation
- **Matplotlib & Seaborn** for statistical charts

## How to Run
1. Place `Telco-Customer-Churn.csv` in the root folder.
2. Run the script:
   ```bash
   py task2_churn_analysis.py
