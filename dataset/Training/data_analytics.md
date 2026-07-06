# TechNova Solutions Pvt. Ltd.

# Data Analytics Training Manual

**Training Version:** 1.0
**Department:** Learning & Development (L&D), Business Intelligence, and Data Analytics
**Duration:** 8 Weeks
**Target Audience:** Data Analysts, Business Analysts, Data Scientists, BI Developers, Interns, and Freshers

---

# 1. Introduction to Data Analytics

Data Analytics is the process of collecting, processing, analyzing, and interpreting data to support business decision-making.

Benefits of data analytics:

* Better decision making
* Increased operational efficiency
* Improved customer experience
* Risk management
* Revenue optimization
* Business forecasting

---

# 2. Types of Analytics

Organizations use four major types of analytics:

| Analytics Type         | Purpose            |
| ---------------------- | ------------------ |
| Descriptive Analytics  | What happened?     |
| Diagnostic Analytics   | Why did it happen? |
| Predictive Analytics   | What will happen?  |
| Prescriptive Analytics | What should we do? |

---

# 3. Data Analytics Workflow

Typical analytics workflow:

```text
Business Problem
       ↓
Data Collection
       ↓
Data Cleaning
       ↓
Data Analysis
       ↓
Visualization
       ↓
Insights
       ↓
Decision Making
```

---

# 4. Data Sources

Common data sources include:

* Excel files
* CSV files
* SQL databases
* APIs
* Cloud storage
* CRM systems
* ERP systems
* Web analytics

---

# 5. Microsoft Excel for Data Analytics

Excel remains one of the most widely used analytics tools.

Applications:

* Reporting
* Dashboard creation
* Financial analysis
* Data cleaning
* Business analysis

---

# 6. Excel Functions

Common functions:

```excel
SUM()
AVERAGE()
COUNT()
MAX()
MIN()
IF()
VLOOKUP()
XLOOKUP()
```

Example:

```excel
=SUM(A1:A10)
```

---

# 7. Lookup Functions

Example:

```excel
=VLOOKUP(A2,B:E,3,FALSE)
```

Modern lookup:

```excel
=XLOOKUP(A2,B:B,E:E)
```

Applications:

* Employee lookup
* Product lookup
* Sales analysis

---

# 8. Pivot Tables

Pivot tables summarize large datasets.

Example applications:

* Sales analysis
* HR reporting
* Customer analytics
* Financial reporting

Benefits:

* Fast aggregation
* Interactive reporting
* Easy filtering

---

# 9. Data Cleaning in Excel

Tasks include:

* Remove duplicates
* Handle blanks
* Text formatting
* Date formatting
* Error correction

Example:

```excel
Data → Remove Duplicates
```

---

# 10. Introduction to SQL

SQL (Structured Query Language) is used to manage and analyze relational databases.

Applications:

* Data retrieval
* Reporting
* Analytics
* Data transformation

---

# 11. SQL Databases

Popular databases:

| Database   | Usage                 |
| ---------- | --------------------- |
| MySQL      | Web applications      |
| PostgreSQL | Enterprise            |
| SQL Server | Business intelligence |
| Oracle     | Enterprise systems    |
| SQLite     | Local applications    |

---

# 12. SELECT Statement

Example:

```sql
SELECT *
FROM employees;
```

Retrieve specific columns:

```sql
SELECT name, salary
FROM employees;
```

---

# 13. Filtering Data

Example:

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

Operators:

* =
* >
* <
* > =
* <=
* LIKE
* IN
* BETWEEN

---

# 14. Sorting Data

Example:

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

Options:

* ASC
* DESC

---

# 15. Aggregate Functions

Functions include:

```sql
COUNT()
SUM()
AVG()
MIN()
MAX()
```

Example:

```sql
SELECT AVG(salary)
FROM employees;
```

---

# 16. GROUP BY

Example:

```sql
SELECT department,
       AVG(salary)
FROM employees
GROUP BY department;
```

Applications:

* Department analysis
* Customer segmentation
* Revenue analysis

---

# 17. HAVING Clause

Example:

```sql
SELECT department,
       COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
```

---

# 18. SQL JOINs

Types of joins:

* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* FULL JOIN

Example:

```sql
SELECT e.name,
       d.department
FROM employees e
INNER JOIN departments d
ON e.dept_id=d.id;
```

---

# 19. Subqueries

Example:

```sql
SELECT name
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
);
```

---

# 20. Common Table Expressions (CTE)

Example:

```sql
WITH employee_cte AS
(
    SELECT *
    FROM employees
)
SELECT *
FROM employee_cte;
```

Benefits:

* Cleaner queries
* Better readability

---

# 21. Window Functions

Examples:

```sql
ROW_NUMBER()
RANK()
DENSE_RANK()
LAG()
LEAD()
```

Example:

```sql
SELECT
ROW_NUMBER() OVER(
PARTITION BY department)
FROM employees;
```

---

# 22. Introduction to Python for Analytics

Python is widely used for:

* Data cleaning
* Data analysis
* Visualization
* Machine learning

Popular libraries:

* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

# 23. Pandas Library

Import:

```python
import pandas as pd
```

Load data:

```python
df = pd.read_csv("sales.csv")
```

Common functions:

```python
df.head()
df.tail()
df.info()
df.describe()
```

---

# 24. Data Cleaning using Pandas

Example:

```python
df.drop_duplicates()
df.fillna(0)
df.isnull().sum()
```

Tasks:

* Missing value handling
* Duplicate removal
* Data conversion
* Outlier detection

---

# 25. Data Filtering

Example:

```python
df[df["salary"] > 50000]
```

Multiple conditions:

```python
df[
    (df["salary"] > 50000)
    &
    (df["age"] > 25)
]
```

---

# 26. GroupBy Operations

Example:

```python
df.groupby(
    "department"
).mean()
```

Applications:

* Revenue analysis
* Customer analysis
* Employee analysis

---

# 27. Merging Data

Example:

```python
pd.merge(
    employee,
    department,
    on="id"
)
```

Types:

* Inner join
* Left join
* Right join
* Outer join

---

# 28. NumPy Library

Example:

```python
import numpy as np

arr = np.array([1,2,3])
```

Applications:

* Statistics
* Matrix operations
* Scientific computing

---

# 29. Statistics for Analytics

Important concepts:

* Mean
* Median
* Mode
* Variance
* Standard deviation
* Correlation
* Covariance

---

# 30. Data Visualization

Visualization helps communicate insights.

Popular libraries:

* Matplotlib
* Plotly
* Power BI
* Tableau

---

# 31. Charts and Graphs

Common visualizations:

* Bar chart
* Line chart
* Pie chart
* Scatter plot
* Histogram
* Box plot

Applications:

* Trend analysis
* Distribution analysis
* Comparison analysis

---

# 32. Correlation Analysis

Correlation measures relationships between variables.

Values:

```text
-1  = Negative correlation
 0  = No correlation
+1  = Positive correlation
```

Applications:

* Financial analysis
* Customer behavior
* Sales forecasting

---

# 33. Regression Analysis

Regression predicts future values.

Applications:

* Sales prediction
* Revenue forecasting
* Risk analysis

Example:

```python
from sklearn.linear_model import LinearRegression
```

---

# 34. Introduction to Power BI

Power BI is Microsoft's business intelligence platform.

Features:

* Dashboard creation
* Interactive reports
* Data modeling
* Data visualization

---

# 35. Power Query

Power Query performs ETL operations.

Tasks:

* Extract
* Transform
* Load

Applications:

* Data cleaning
* Data transformation
* Automation

---

# 36. Data Modeling in Power BI

Relationships:

* One-to-one
* One-to-many
* Many-to-many

Benefits:

* Better reporting
* Faster analysis

---

# 37. DAX (Data Analysis Expressions)

Example:

```DAX
TotalSales =
SUM(Sales[Amount])
```

Common DAX functions:

* SUM
* COUNT
* AVERAGE
* CALCULATE
* FILTER

---

# 38. Dashboard Development

A good dashboard should provide:

* KPIs
* Trends
* Comparisons
* Filters
* Drill-down capabilities

Examples:

* Sales dashboard
* HR dashboard
* Banking dashboard
* Finance dashboard

---

# 39. Business KPIs

Common KPIs include:

| Domain     | KPI             |
| ---------- | --------------- |
| Sales      | Revenue         |
| HR         | Attrition Rate  |
| Finance    | Profit Margin   |
| Marketing  | Conversion Rate |
| Operations | Efficiency      |

---

# 40. Data Storytelling

Effective storytelling includes:

* Context
* Visualization
* Insights
* Recommendations

Goal:

```text
Data → Insight → Action
```

---

# 41. Business Analytics Use Cases

Applications:

* Customer analytics
* Banking analytics
* Fraud detection
* Sales forecasting
* HR analytics
* Supply chain analytics

---

# 42. Data Governance

Organizations should ensure:

* Data quality
* Data privacy
* Security
* Compliance
* Accessibility

---

# 43. Analytics Project Lifecycle

Project workflow:

```text
Business Understanding
         ↓
Data Collection
         ↓
Data Preparation
         ↓
Analysis
         ↓
Visualization
         ↓
Deployment
```

---

# 44. Recommended Projects

Students should complete:

* Sales Analytics Dashboard
* HR Analytics Dashboard
* Banking Transaction Analytics
* Customer Churn Analysis
* Financial Analytics Dashboard
* Healthcare Analytics
* Supply Chain Analytics
* Retail Analytics Dashboard

---

# 45. Tools Used in Industry

| Tool     | Category        |
| -------- | --------------- |
| Excel    | Spreadsheet     |
| SQL      | Database        |
| Python   | Analytics       |
| Power BI | BI Tool         |
| Tableau  | Visualization   |
| Jupyter  | Development     |
| Git      | Version Control |

---

# 46. Assessment

| Component   | Weightage |
| ----------- | --------- |
| Assignments | 20%       |
| Labs        | 30%       |
| Project     | 40%       |
| Viva        | 10%       |

Minimum passing score:

```text
70%
```

---

# 47. Frequently Asked Questions

### Q1. Is SQL mandatory for data analysts?

Yes.

### Q2. Is Excel still used in industry?

Yes.

### Q3. Is Python required?

Yes.

### Q4. Is Power BI important?

Yes.

### Q5. Are projects mandatory?

Yes.

---

# 48. Training Ownership

This Data Analytics Training Manual is maintained jointly by the Learning & Development Department, Business Intelligence Team, and Data Analytics Department of TechNova Solutions Pvt. Ltd.
# TechNova Solutions Pvt. Ltd.

# Data Analytics Training Manual

**Training Version:** 1.0
**Department:** Learning & Development (L&D), Business Intelligence, and Data Analytics
**Duration:** 8 Weeks
**Target Audience:** Data Analysts, Business Analysts, Data Scientists, BI Developers, Interns, and Freshers

---

# 1. Introduction to Data Analytics

Data Analytics is the process of collecting, processing, analyzing, and interpreting data to support business decision-making.

Benefits of data analytics:

* Better decision making
* Increased operational efficiency
* Improved customer experience
* Risk management
* Revenue optimization
* Business forecasting

---

# 2. Types of Analytics

Organizations use four major types of analytics:

| Analytics Type         | Purpose            |
| ---------------------- | ------------------ |
| Descriptive Analytics  | What happened?     |
| Diagnostic Analytics   | Why did it happen? |
| Predictive Analytics   | What will happen?  |
| Prescriptive Analytics | What should we do? |

---

# 3. Data Analytics Workflow

Typical analytics workflow:

```text
Business Problem
       ↓
Data Collection
       ↓
Data Cleaning
       ↓
Data Analysis
       ↓
Visualization
       ↓
Insights
       ↓
Decision Making
```

---

# 4. Data Sources

Common data sources include:

* Excel files
* CSV files
* SQL databases
* APIs
* Cloud storage
* CRM systems
* ERP systems
* Web analytics

---

# 5. Microsoft Excel for Data Analytics

Excel remains one of the most widely used analytics tools.

Applications:

* Reporting
* Dashboard creation
* Financial analysis
* Data cleaning
* Business analysis

---

# 6. Excel Functions

Common functions:

```excel
SUM()
AVERAGE()
COUNT()
MAX()
MIN()
IF()
VLOOKUP()
XLOOKUP()
```

Example:

```excel
=SUM(A1:A10)
```

---

# 7. Lookup Functions

Example:

```excel
=VLOOKUP(A2,B:E,3,FALSE)
```

Modern lookup:

```excel
=XLOOKUP(A2,B:B,E:E)
```

Applications:

* Employee lookup
* Product lookup
* Sales analysis

---

# 8. Pivot Tables

Pivot tables summarize large datasets.

Example applications:

* Sales analysis
* HR reporting
* Customer analytics
* Financial reporting

Benefits:

* Fast aggregation
* Interactive reporting
* Easy filtering

---

# 9. Data Cleaning in Excel

Tasks include:

* Remove duplicates
* Handle blanks
* Text formatting
* Date formatting
* Error correction

Example:

```excel
Data → Remove Duplicates
```

---

# 10. Introduction to SQL

SQL (Structured Query Language) is used to manage and analyze relational databases.

Applications:

* Data retrieval
* Reporting
* Analytics
* Data transformation

---

# 11. SQL Databases

Popular databases:

| Database   | Usage                 |
| ---------- | --------------------- |
| MySQL      | Web applications      |
| PostgreSQL | Enterprise            |
| SQL Server | Business intelligence |
| Oracle     | Enterprise systems    |
| SQLite     | Local applications    |

---

# 12. SELECT Statement

Example:

```sql
SELECT *
FROM employees;
```

Retrieve specific columns:

```sql
SELECT name, salary
FROM employees;
```

---

# 13. Filtering Data

Example:

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

Operators:

* =
* >
* <
* > =
* <=
* LIKE
* IN
* BETWEEN

---

# 14. Sorting Data

Example:

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

Options:

* ASC
* DESC

---

# 15. Aggregate Functions

Functions include:

```sql
COUNT()
SUM()
AVG()
MIN()
MAX()
```

Example:

```sql
SELECT AVG(salary)
FROM employees;
```

---

# 16. GROUP BY

Example:

```sql
SELECT department,
       AVG(salary)
FROM employees
GROUP BY department;
```

Applications:

* Department analysis
* Customer segmentation
* Revenue analysis

---

# 17. HAVING Clause

Example:

```sql
SELECT department,
       COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
```

---

# 18. SQL JOINs

Types of joins:

* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* FULL JOIN

Example:

```sql
SELECT e.name,
       d.department
FROM employees e
INNER JOIN departments d
ON e.dept_id=d.id;
```

---

# 19. Subqueries

Example:

```sql
SELECT name
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
);
```

---

# 20. Common Table Expressions (CTE)

Example:

```sql
WITH employee_cte AS
(
    SELECT *
    FROM employees
)
SELECT *
FROM employee_cte;
```

Benefits:

* Cleaner queries
* Better readability

---

# 21. Window Functions

Examples:

```sql
ROW_NUMBER()
RANK()
DENSE_RANK()
LAG()
LEAD()
```

Example:

```sql
SELECT
ROW_NUMBER() OVER(
PARTITION BY department)
FROM employees;
```

---

# 22. Introduction to Python for Analytics

Python is widely used for:

* Data cleaning
* Data analysis
* Visualization
* Machine learning

Popular libraries:

* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

# 23. Pandas Library

Import:

```python
import pandas as pd
```

Load data:

```python
df = pd.read_csv("sales.csv")
```

Common functions:

```python
df.head()
df.tail()
df.info()
df.describe()
```

---

# 24. Data Cleaning using Pandas

Example:

```python
df.drop_duplicates()
df.fillna(0)
df.isnull().sum()
```

Tasks:

* Missing value handling
* Duplicate removal
* Data conversion
* Outlier detection

---

# 25. Data Filtering

Example:

```python
df[df["salary"] > 50000]
```

Multiple conditions:

```python
df[
    (df["salary"] > 50000)
    &
    (df["age"] > 25)
]
```

---

# 26. GroupBy Operations

Example:

```python
df.groupby(
    "department"
).mean()
```

Applications:

* Revenue analysis
* Customer analysis
* Employee analysis

---

# 27. Merging Data

Example:

```python
pd.merge(
    employee,
    department,
    on="id"
)
```

Types:

* Inner join
* Left join
* Right join
* Outer join

---

# 28. NumPy Library

Example:

```python
import numpy as np

arr = np.array([1,2,3])
```

Applications:

* Statistics
* Matrix operations
* Scientific computing

---

# 29. Statistics for Analytics

Important concepts:

* Mean
* Median
* Mode
* Variance
* Standard deviation
* Correlation
* Covariance

---

# 30. Data Visualization

Visualization helps communicate insights.

Popular libraries:

* Matplotlib
* Plotly
* Power BI
* Tableau

---

# 31. Charts and Graphs

Common visualizations:

* Bar chart
* Line chart
* Pie chart
* Scatter plot
* Histogram
* Box plot

Applications:

* Trend analysis
* Distribution analysis
* Comparison analysis

---

# 32. Correlation Analysis

Correlation measures relationships between variables.

Values:

```text
-1  = Negative correlation
 0  = No correlation
+1  = Positive correlation
```

Applications:

* Financial analysis
* Customer behavior
* Sales forecasting

---

# 33. Regression Analysis

Regression predicts future values.

Applications:

* Sales prediction
* Revenue forecasting
* Risk analysis

Example:

```python
from sklearn.linear_model import LinearRegression
```

---

# 34. Introduction to Power BI

Power BI is Microsoft's business intelligence platform.

Features:

* Dashboard creation
* Interactive reports
* Data modeling
* Data visualization

---

# 35. Power Query

Power Query performs ETL operations.

Tasks:

* Extract
* Transform
* Load

Applications:

* Data cleaning
* Data transformation
* Automation

---

# 36. Data Modeling in Power BI

Relationships:

* One-to-one
* One-to-many
* Many-to-many

Benefits:

* Better reporting
* Faster analysis

---

# 37. DAX (Data Analysis Expressions)

Example:

```DAX
TotalSales =
SUM(Sales[Amount])
```

Common DAX functions:

* SUM
* COUNT
* AVERAGE
* CALCULATE
* FILTER

---

# 38. Dashboard Development

A good dashboard should provide:

* KPIs
* Trends
* Comparisons
* Filters
* Drill-down capabilities

Examples:

* Sales dashboard
* HR dashboard
* Banking dashboard
* Finance dashboard

---

# 39. Business KPIs

Common KPIs include:

| Domain     | KPI             |
| ---------- | --------------- |
| Sales      | Revenue         |
| HR         | Attrition Rate  |
| Finance    | Profit Margin   |
| Marketing  | Conversion Rate |
| Operations | Efficiency      |

---

# 40. Data Storytelling

Effective storytelling includes:

* Context
* Visualization
* Insights
* Recommendations

Goal:

```text
Data → Insight → Action
```

---

# 41. Business Analytics Use Cases

Applications:

* Customer analytics
* Banking analytics
* Fraud detection
* Sales forecasting
* HR analytics
* Supply chain analytics

---

# 42. Data Governance

Organizations should ensure:

* Data quality
* Data privacy
* Security
* Compliance
* Accessibility

---

# 43. Analytics Project Lifecycle

Project workflow:

```text
Business Understanding
         ↓
Data Collection
         ↓
Data Preparation
         ↓
Analysis
         ↓
Visualization
         ↓
Deployment
```

---

# 44. Recommended Projects

Students should complete:

* Sales Analytics Dashboard
* HR Analytics Dashboard
* Banking Transaction Analytics
* Customer Churn Analysis
* Financial Analytics Dashboard
* Healthcare Analytics
* Supply Chain Analytics
* Retail Analytics Dashboard

---

# 45. Tools Used in Industry

| Tool     | Category        |
| -------- | --------------- |
| Excel    | Spreadsheet     |
| SQL      | Database        |
| Python   | Analytics       |
| Power BI | BI Tool         |
| Tableau  | Visualization   |
| Jupyter  | Development     |
| Git      | Version Control |

---

# 46. Assessment

| Component   | Weightage |
| ----------- | --------- |
| Assignments | 20%       |
| Labs        | 30%       |
| Project     | 40%       |
| Viva        | 10%       |

Minimum passing score:

```text
70%
```

---

# 47. Frequently Asked Questions

### Q1. Is SQL mandatory for data analysts?

Yes.

### Q2. Is Excel still used in industry?

Yes.

### Q3. Is Python required?

Yes.

### Q4. Is Power BI important?

Yes.

### Q5. Are projects mandatory?

Yes.

---

# 48. Training Ownership

This Data Analytics Training Manual is maintained jointly by the Learning & Development Department, Business Intelligence Team, and Data Analytics Department of TechNova Solutions Pvt. Ltd.
