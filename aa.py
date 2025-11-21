import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from scipy import stats
from datetime import datetime

warnings.filterwarnings('ignore')

# Set visualization style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

########################################################################################################

def load_and_explore_data(file_path):
    """Load data and perform initial exploration"""
    print("="*80)
    print("SALES ANALYTICS - EXPLORATORY DATA ANALYSIS")
    print("="*80)
    
    # Load Excel file
    df = pd.read_excel(file_path, engine='openpyxl')
    
    print("\n1. DATASET OVERVIEW")
    print("-"*80)
    print(f"Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\nColumn Names:\n{df.columns.tolist()}")
    
    print("\n2. DATA TYPES")
    print("-"*80)
    print(df.dtypes)
    
    print("\n3. FIRST 5 ROWS")
    print("-"*80)
    print(df.head())
    
    print("\n4. STATISTICAL SUMMARY")
    print("-"*80)
    print(df.describe())
    
    print("\n5. MISSING VALUES ANALYSIS")
    print("-"*80)
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing_Count': missing,
        'Missing_Percentage': missing_pct
    }).sort_values('Missing_Count', ascending=False)
    print(missing_df[missing_df['Missing_Count'] > 0])
    
    return df

########################################################################################################

def clean_data(df):
    print("\n6. DATA CLEANING")
    print("-"*80)
    
    df_clean = df.copy()
    
    # Convert date columns
    date_columns = [col for col in df_clean.columns if 'date' in col.lower()]
    for col in date_columns:
        df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')
    
    # Replace missing text values
    text_columns = ['account_owner', 'primary_country', 'primary_city']
    for col in text_columns:
        if col in df_clean.columns:
            df_clean[col].fillna('Unknown', inplace=True)
    
    # Revenue & potential
    if 'revenue_amount' in df_clean.columns:
        df_clean['revenue_amount'] = df_clean['revenue_amount'].fillna(0)

    if 'potential_business' in df_clean.columns:
        df_clean['potential_business'] = df_clean['potential_business'].fillna(0)

    if 'revenue_amount' in df_clean.columns and 'potential_business' in df_clean.columns:
        df_clean['untapped_potential'] = df_clean['potential_business'] - df_clean['revenue_amount']
    
    # Date-based features
    if 'opportunity_close_date' in df_clean.columns:
        df_clean['year'] = df_clean['opportunity_close_date'].dt.year
        df_clean['quarter'] = df_clean['opportunity_close_date'].dt.quarter
        df_clean['month'] = df_clean['opportunity_close_date'].dt.month
        df_clean['year_quarter'] = df_clean['year'].astype(str) + ' Q' + df_clean['quarter'].astype(str)
    
    print("✓ Data cleaned successfully")
    print(f"Clean dataset shape: {df_clean.shape}")
    
    return df_clean

########################################################################################################

def univariate_analysis(df):
    """Perform univariate analysis on key variables"""
    print("\n7. UNIVARIATE ANALYSIS")
    print("-"*80)
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Univariate Analysis - Distribution Plots', fontsize=16, fontweight='bold')
    
    # Revenue distribution
    if 'revenue_amount' in df.columns:
        axes[0, 0].hist(df[df['revenue_amount'] > 0]['revenue_amount'], bins=50, color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Revenue Amount Distribution')
        axes[0, 0].set_xlabel('Revenue ($)')
        axes[0, 0].set_ylabel('Frequency')
        axes[0, 0].axvline(df['revenue_amount'].mean(), color='red', linestyle='--', label='Mean')
        axes[0, 0].legend()
    
    # Potential
    if 'potential_business' in df.columns:
        axes[0, 1].hist(df[df['potential_business'] > 0]['potential_business'], bins=50,
                        color='lightgreen', edgecolor='black')
        axes[0, 1].set_title('Potential Business Distribution')
    
    # Account status
    if 'account_status' in df.columns:
        status_counts = df['account_status'].value_counts()
        axes[0, 2].bar(status_counts.index, status_counts.values,
                       color=['#FF9999', '#66B2FF', '#99FF99'])
        axes[0, 2].set_title('Account Status Distribution')
        axes[0, 2].tick_params(axis='x', rotation=45)
    
    # Growth potential pie
    if 'future_growth_potential' in df.columns:
        growth_counts = df['future_growth_potential'].value_counts()
        axes[1, 0].pie(growth_counts.values, labels=growth_counts.index,
                       autopct='%1.1f%%', startangle=90)
        axes[1, 0].set_title('Growth Potential Distribution')
    
    # Country
    if 'primary_country' in df.columns:
        top_countries = df['primary_country'].value_counts().head(10)
        axes[1, 1].barh(top_countries.index, top_countries.values, color='coral')
        axes[1, 1].set_title('Top 10 Countries')
    
    # Owners
    if 'account_owner' in df.columns:
        top_owners = df['account_owner'].value_counts().head(10)
        axes[1, 2].barh(top_owners.index, top_owners.values, color='mediumpurple')
        axes[1, 2].set_title('Top 10 Account Owners')
    
    plt.tight_layout()
    plt.savefig('univariate_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Univariate analysis saved")
    plt.show()


########################################################################################################

def main():
    file_path = "/kaggle/input/aabbccdd/Excel.xlsx"   
    
    try:
        df = load_and_explore_data(file_path)
        df_clean = clean_data(df)
        univariate_analysis(df_clean)
        bivariate_analysis(df_clean)
        time_series_analysis(df_clean)
        correlation_analysis(df_clean)
        outlier_detection(df_clean)
        metrics = calculate_business_metrics(df_clean)
        segment_performance(df_clean)
        generate_eda_report(df_clean, metrics)

        print("\n✓ EDA COMPLETED SUCCESSFULLY!")
    
    except FileNotFoundError:
        print(f"\n❌ File not found: {file_path}")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
