# 📊 Sales Performance & Revenue Forecast Analytics Dashboard

---

## 🎯 Project Overview

This end-to-end business intelligence solution analyzes **$8.67M in revenue** across **1,986 accounts** to identify growth opportunities, optimize sales performance, and forecast future revenue streams. The project combines advanced Excel analytics with interactive Power BI visualizations to support strategic decision-making.

### Business Problem
- Low overall conversion rate (3.3%) with significant untapped potential ($254.47M)
- Inconsistent sales rep performance requiring optimization
- Need for data-driven geographic expansion strategy
- Requirement for accurate multi-year revenue forecasting

### Solution Delivered
- 6-page interactive Power BI dashboard with drill-down capabilities
- Comprehensive Excel workbook with automated calculations
- 150+ DAX measures and calculated columns
- 4-year revenue projection model with scenario analysis
- Strategic recommendations backed by data insights

---

## ✨ Key Features

### 📈 Advanced Analytics
- **Sales Performance Scoring**: Composite scoring system (Revenue 50%, Efficiency 30%, Customer Count 20%)
- **Quarterly Trend Analysis**: QoQ growth tracking with +65% to -69% range
- **Geographic Intelligence**: Country-level revenue distribution and recommendation scores
- **Growth Segmentation**: High/Medium/No growth potential classification with conversion tracking
- **Revenue Forecasting**: 4-year projection with 29.9% CAGR and scenario planning

### 🎨 Interactive Visualizations
- Dynamic filtering across all dashboard pages
- Drill-through capabilities from summary to detail views
- Waterfall charts showing QoQ revenue changes
- Geographic maps with city-level potential analysis
- Comparative scenario analysis (Pessimistic/Base/Optimistic)

### 🔧 Technical Excellence
- Power Query for automated data transformation
- Custom date table with fiscal calendar support
- Dimension modeling with star schema
- Time intelligence measures (QoQ, YoY, YTD)
- Dynamic measures using DAX variables and SWITCH functions

---

## 📊 Dashboard Pages

### Page 1: Executive Summary
**Purpose**: High-level KPIs and business overview

**Key Metrics**:
- Total Revenue: **$8.68M**
- Total Potential: **$263.14M**
- Untapped Opportunity: **$254.47M** (96.7%)
- Active Customers: **225** (3.3% conversion)
- Average Deal Size: **$38,565**

**Visuals**:
- KPI cards with YoY comparisons
- Revenue by account status (donut chart)
- Monthly revenue trend line
- Top 5 countries by revenue (bar chart)

---

### Page 2: Sales Rep Performance Analysis
**Purpose**: Evaluate and rank sales team effectiveness

**Scoring Methodology**:
```
Final Score = (Revenue Score × 50%) + (Efficiency Score × 30%) + (Customer Score × 20%)
```

**Key Features**:
- Ranked table of all sales representatives
- Performance quadrant analysis (Revenue vs Conversion)
- Individual rep drill-through pages
- Comparison to team averages

**Top Performers**:
1. Rep A - Score: 92.4
2. Rep B - Score: 87.6
3. Rep C - Score: 81.3

---

### Page 3: Quarterly Sales Trends
**Purpose**: Track revenue momentum and seasonality

**Analysis**:
- Quarter-over-quarter growth rates
- Seasonal pattern identification
- Peak performance: **Q4 2022 at $4.3M**
- Significant decline: **-69% in Q1 2023**

**Visuals**:
- Line chart: Quarterly revenue trajectory
- Waterfall chart: QoQ changes with increases/decreases
- Table: Detailed quarterly breakdown with growth %

**Formula Used**:
```excel
QoQ Growth % = (Current Quarter - Previous Quarter) / Previous Quarter × 100
```

---

### Page 4: Geographic Distribution & Country Analysis
**Purpose**: Identify optimal markets for expansion

**Country Breakdown**:
| Country | Revenue | Accounts | Conversion | Recommendation Score |
|---------|---------|----------|------------|---------------------|
| **Germany** | $4.04M (46.5%) | 398 | 25% | 68.1 |
| **Spain** | $1.40M (16.1%) | 658 | 6% | 85.2 |
| **France** | $1.20M (13.8%) | 311 | 8% | 72.4 |

**Strategic Insight**: Spain shows highest recommendation score (85.2) due to:
- Largest account base (658 accounts)
- Strong growth potential (6% → 17% projected conversion)
- Madrid office opportunity: **€36K investment → $1.8M return**

**Visuals**:
- Interactive map with bubble sizes by revenue
- Country comparison matrix
- Top 10 cities by potential
- Quarterly trends by country (heatmap)

---

### Page 5: Growth Segment Analysis
**Purpose**: Prioritize accounts by future potential

**Segment Performance**:

| Segment | Accounts | Revenue | Conversion | Distribution |
|---------|----------|---------|------------|--------------|
| **High Growth** | 151 | $5.40M | 96.7% | 7.6% |
| **Medium Growth** | 99 | $2.79M | 67.7% | 5.0% |
| **No Growth** | 1,736 | $488K | 0.7% | 87.4% |

**Critical Finding**: 87.4% of accounts classified as "No Growth Potential" - represents major optimization opportunity

**Country Distribution**:
- Spain has **89.06%** of accounts in "No Growth" segment
- Indicates need for better prospect qualification

**Visuals**:
- Segment revenue breakdown (stacked bar)
- Conversion funnel by segment
- Country-segment matrix
- Account distribution pie chart

---

### Page 6: 4-Year Revenue Forecast
**Purpose**: Project future revenue with scenario planning

**Base Case Assumptions**:
- **New Customers**: 2% annual conversion of untapped potential = $4.73M/year
- **High Growth**: +30% YoY compound growth
- **Medium Growth**: +10% YoY compound growth
- **No Growth**: Flat ($488K maintained)

**Forecast Results**:
| Year | New | High Growth | Medium Growth | No Growth | **Total** |
|------|-----|-------------|---------------|-----------|----------|
| 2022 (Actual) | - | $5.40M | $2.79M | $488K | **$8.68M** |
| 2023 | $4.73M | $7.02M | $3.07M | $488K | **$15.31M** |
| 2024 | $4.73M | $9.13M | $3.37M | $488K | **$17.72M** |
| 2025 | $4.73M | $11.87M | $3.71M | $488K | **$20.80M** |
| 2026 | $4.73M | $15.43M | $4.08M | $488K | **$24.73M** |

**Key Metrics**:
- **CAGR**: 29.9% over 4 years
- **Total Growth**: 185% from 2022 to 2026
- **Revenue by 2026**: $24.73M

**Scenario Analysis**:

| Scenario | 2026 Revenue | vs Base Case | Key Assumptions |
|----------|--------------|--------------|-----------------|
| **Pessimistic** | $16.3M | -34% | 1% conversion, +20% high growth, +5% medium |
| **Base Case** | $24.7M | - | 2% conversion, +30% high growth, +10% medium |
| **Optimistic** | $32.0M | +30% | 5% conversion, +40% high growth, +15% medium |

**Sensitivity Analysis**:
- +1% new customer conversion = +$2.4M by 2026
- +10% high growth rate = +$5.2M additional revenue
- +5% medium growth rate = +$800K additional revenue

**Visuals**:
- Stacked column chart: Forecast by segment over time
- Line chart: Total revenue trajectory with confidence bands
- Scenario comparison: Side-by-side columns
- Waterfall chart: 2022 to 2026 bridge analysis

---

## 🏗️ Technical Architecture

### Data Model Structure
```
Star Schema Design:

FACT TABLE:
├── Sales_Data (Main fact table)
    ├── Account_Name
    ├── Revenue_Amount
    ├── Potential_Business
    ├── Opportunity_Close_Date
    ├── Account_Status
    └── Future_Growth_Potential

DIMENSION TABLES:
├── Date_Table (Date dimension)
│   ├── Date (PK)
│   ├── Year, Quarter, Month
│   ├── Year_Quarter
│   └── Weekday, Week_Number
│
├── Account_Owner_Dim (Sales rep dimension)
│   └── Account_Owner (PK)
│
├── Country_Dim (Geographic dimension)
│   └── Primary_Country (PK)
│
└── Growth_Segment_Dim (Segment dimension)
    └── Segment (PK)

RELATIONSHIPS:
Sales_Data[Opportunity_Close_Date] → Date_Table[Date] (Many-to-One)
Sales_Data[Account_Owner] → Account_Owner_Dim[Account_Owner] (Many-to-One)
Sales_Data[Primary_Country] → Country_Dim[Primary_Country] (Many-to-One)
Sales_Data[Future_Growth_Potential] → Growth_Segment_Dim[Segment] (Many-to-One)
```

---

## 🧮 Calculations & Formulas

### Core DAX Measures

#### Revenue Metrics
```dax
Total_Revenue = 
CALCULATE(
    SUM('Sales Data'[Revenue_Amount]),
    'Sales Data'[Account_Status] = "Active Customer"
)

Untapped_Opportunity = 
[Total_Potential] - [Total_Revenue]

Conversion_Rate = 
DIVIDE([Total_Revenue], [Total_Potential], 0)
```

#### Sales Rep Performance
```dax
Final_Rep_Score = 
VAR RevenueScore = DIVIDE([Rep_Total_Revenue], [Max_Revenue_All_Reps], 0) * 50
VAR EfficiencyScore = DIVIDE([Rep_Total_Revenue], [Rep_Total_Potential], 0) * 30
VAR CustomerScore = DIVIDE([Rep_Active_Customers], [Max_Customers_All_Reps], 0) * 20
RETURN
    RevenueScore + EfficiencyScore + CustomerScore
```

#### Time Intelligence
```dax
QoQ_Growth_% = 
VAR CurrentQuarter = [Total_Revenue]
VAR PreviousQuarter = 
    CALCULATE(
        [Total_Revenue],
        DATEADD(Date_Table[Date], -1, QUARTER)
    )
RETURN
    DIVIDE(CurrentQuarter - PreviousQuarter, PreviousQuarter, 0)
```

#### Geographic Analysis
```dax
Country_Recommendation_Score = 
VAR RevenueWeight = [Country_Revenue_Share] * 0.4
VAR ConversionWeight = [Conversion_Rate] * 0.3
VAR AccountWeight = 
    DIVIDE(
        DISTINCTCOUNT('Sales Data'[Account_Name]),
        CALCULATE(
            DISTINCTCOUNT('Sales Data'[Account_Name]), 
            ALL('Sales Data'[Primary_Country])
        ),
        0
    ) * 0.3
RETURN
    RevenueWeight + ConversionWeight + AccountWeight
```

#### Forecasting
```dax
High_Growth_Forecast = 
VAR BaseValue = [High_Growth_Revenue]
VAR YearsFromBase = YEAR(MAX('Calendar'[Date])) - 2022
RETURN
    IF(
        YearsFromBase >= 0,
        BaseValue * POWER(1.30, YearsFromBase),
        BLANK()
    )

Total_Forecast = 
[Forecast_New_Customers] + 
[Forecast_High_Growth] + 
[Forecast_Medium_Growth] + 
[Forecast_No_Growth]
```

### Excel Formulas

#### Quarterly Analysis
```excel
// Quarter Column
=TEXT(J2,"YYYY") & " Q" & ROUNDUP(MONTH(J2)/3,0)

// QoQ Growth
=(Current_Quarter - Previous_Quarter) / Previous_Quarter * 100
```

#### Country Scoring
```excel
=( (Spain_Revenue/Total_Revenue)*40 ) +
  ( (Spain_Conversion/AVG_Conversion)*30 ) +
  ( (Spain_Accounts/MAX_Accounts)*30 )
```

#### Forecast Calculations
```excel
// Year 2023 High Growth
=2022_High_Growth * 1.30

// Total Forecast 2023
=New_Customer_Revenue + High_Growth_Y1 + Medium_Growth_Y1 + No_Growth
```

#### CAGR
```excel
=((2026_Total/2022_Total)^(1/4))-1
// Result: 29.9%
```

---

## 🚀 Installation & Setup

### Prerequisites
- **Microsoft Excel** 2016 or later (with Power Query)
- **Power BI Desktop** (Latest version recommended)
- **DAX Studio** (Optional, for formula testing)

### Step-by-Step Setup

#### 1. Clone Repository
```bash
git clone https://github.com/yourusername/sales-analytics-dashboard.git
cd sales-analytics-dashboard
```

#### 2. Excel Workbook Setup
1. Open `Sales_Analytics.xlsx`
2. Enable macros if prompted
3. Refresh all pivot tables: `Data > Refresh All`
4. Verify calculated columns in Sheet: `Sales_Data`

#### 3. Power BI Dashboard Setup
1. Open `Sales_Dashboard.pbix` in Power BI Desktop
2. If data source prompts appear:
   - Click `Transform Data`
   - Update file path to your local `Sales_Data.xlsx`
   - Click `Close & Apply`
3. Refresh all visuals: `Home > Refresh`

#### 4. Data Refresh Process
```powerquery
// Power Query - Update Source Path
let
    Source = Excel.Workbook(
        File.Contents("YOUR_PATH_HERE/Sales_Data.xlsx"), 
        null, 
        true
    ),
    Sales_Data = Source{[Name="Sales_Data"]}[Data]
in
    Sales_Data
```

#### 5. Verify Setup
- Check Date Table relationship: `Model View > Manage Relationships`
- Validate measures: `Home > Manage Measures`
- Test filters and slicers on all pages
- Confirm forecast calculations display correctly

---

## 💡 Key Insights & Recommendations

### 🎯 Strategic Recommendations

#### 1. **Immediate Actions (0-3 months)**
- **Spain Office Expansion**
  - Investment: €36,000 (€24K rent + €12K sales rep)
  - Expected Return: $1.8M annually
  - Payback Period: 3 months
  - Target: Madrid (10.2% of Spanish potential)

- **Sales Rep Optimization**
  - Focus training on bottom 30% performers (Score < 45)
  - Implement best practices from top 3 reps
  - Estimated impact: +15% overall conversion

#### 2. **Medium-Term Initiatives (3-12 months)**
- **Account Segmentation Refinement**
  - Re-qualify 1,736 "No Growth" accounts
  - Focus resources on High Growth segment (96.7% conversion)
  - Potential to move 200 accounts to Medium Growth = +$5.5M

- **Geographic Diversification**
  - Reduce Germany dependency (currently 46.5% of revenue)
  - Expand in France (+300% Q3→Q4 growth momentum)
  - Target Romania & Slovakia (recommendation scores: 15)

#### 3. **Long-Term Strategy (1-4 years)**
- **New Customer Acquisition**
  - Current: 2% conversion of untapped potential
  - Target: 5% conversion = +$2.4M per 1% improvement
  - Initiative: Digital marketing + inside sales team

- **Revenue Diversification**
  - Current forecast: 29.9% CAGR
  - Optimistic scenario: 40% CAGR possible with aggressive expansion
  - Focus: High Growth accounts (30% YoY growth sustained)

---

### 📊 Critical Findings

#### ⚠️ Risks Identified
1. **High Revenue Concentration**
   - 46.5% revenue from Germany (single country risk)
   - Q4 2022 spike followed by -69% decline (volatility)
   
2. **Low Overall Conversion**
   - 3.3% conversion rate vs. industry benchmark 8-12%
   - 87.4% of accounts in "No Growth" category

3. **Sales Rep Disparity**
   - Top rep: 18% conversion
   - Bottom rep: 0.5% conversion
   - Indicates training/process gaps

#### ✅ Opportunities Identified
1. **Untapped Potential: $254.47M**
   - Even 2% conversion = $5.09M additional revenue
   - Focus on 1,761 "Not a Customer" accounts

2. **High Growth Segment Excellence**
   - 96.7% conversion rate (nearly perfect)
   - Blueprint for account management best practices

3. **Spain Market Opportunity**
   - 658 accounts (highest volume)
   - 6% → 17% conversion potential with local presence
   - Strong ROI (3-month payback)

---

## 🛠️ Technologies Used

### Core Technologies
| Technology | Purpose | Version |
|------------|---------|---------|
| **Power BI Desktop** | Dashboard & Visualizations | Latest |
| **Microsoft Excel** | Data Analysis & Calculations | 2016+ |
| **Power Query (M)** | Data Transformation | Built-in |
| **DAX** | Calculated Measures & Columns | Latest |

### Advanced Features Utilized
- ✅ DAX Variables (VAR/RETURN)
- ✅ Time Intelligence Functions (DATEADD, TOTALYTD, SAMEPERIODLASTYEAR)
- ✅ Context Transition (CALCULATE, FILTER)
- ✅ Iterator Functions (SUMX, MAXX, RANKX)
- ✅ Dynamic Measures (SWITCH, SELECTEDVALUE)
- ✅ Star Schema Data Modeling
- ✅ Power Query Custom Functions
- ✅ Conditional Formatting & Drill-through

---

## 📁 Project Structure

```
sales-analytics-dashboard/
│
├── 📊 Power BI Files/
│   ├── Sales_Dashboard.pbix          # Main Power BI dashboard (6 pages)
│   └── Sales_Dashboard_Template.pbit  # Template for reuse
│
├── 📁 Excel Files/
│   ├── Sales_Analytics.xlsx          # Master workbook with calculations
│   ├── Sales_Data_Raw.xlsx          # Original raw data
│   └── Forecast_Model.xlsx          # Separate forecast calculator
│
├── 📝 Documentation/
│   ├── calculations.pdf             # All Excel & DAX formulas explained
│   ├── DAX_all_formulas.pdf        # Complete DAX measure library
│   ├── DAX_all_formulas.docx       # Editable formula documentation
│   └── DATA_PREPARATION_STEPS.pdf   # Power Query transformation guide
│
├── 🖼️ Screenshots/
│   ├── executive_summary.png
│   ├── sales_rep_performance.png
│   ├── quarterly_trends.png
│   ├── geographic_analysis.png
│   ├── growth_segments.png
│   └── revenue_forecast.png
│
├── 📊 Data Files/
│   └── sample_data.csv              # Anonymized sample data for testing
│
├── 🔧 Scripts/
│   ├── power_query_transformations.txt  # M code snippets
│   └── dax_measures_library.txt         # Copy-paste DAX measures
│
├── README.md                        # This file
├── LICENSE                          # MIT License
└── .gitignore                      # Git ignore rules
```
## 🌟 Acknowledgments

Special thanks to:
- Power BI Community for DAX optimization tips
- SQLBI for time intelligence best practices
- Excel Power Query documentation team
- Beta testers who provided valuable feedback
