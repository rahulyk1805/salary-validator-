# Salary Validation Tool

## Overview

The Salary Validation Tool is a Python-based desktop web application developed using Streamlit to automate the validation of salary Excel files. Organizations often maintain salary records in Excel workbooks where employee data is grouped into multiple sections or blocks, and each block contains a summary row representing the total values for various salary components. Manual verification of these totals is time-consuming, error-prone, and inefficient, especially when dealing with large datasets and multiple worksheets.

This tool automates the entire validation process by identifying salary blocks using formatting rules, calculating column-wise totals from employee records, comparing them with the corresponding summary values, and generating a detailed validation report highlighting mismatches. The application significantly reduces manual effort and improves data accuracy in payroll auditing and financial verification processes.

---

# Problem Statement

In salary workbooks, data is often organized into multiple employee groups where:

* A bold row represents the block header containing summary totals.
* Multiple employee records exist beneath the header.
* The next bold row marks the beginning of a new block and the end of the previous block.
* Totals in the header row must match the sum of employee records below it.

Manually verifying these calculations across multiple sheets can be labor-intensive and prone to errors.

The Salary Validation Tool solves this problem by automatically performing block-wise and column-wise validation.

---

# Project Objectives

* Automate salary data verification.
* Reduce manual auditing efforts.
* Improve payroll accuracy.
* Detect mismatches instantly.
* Generate structured validation reports.
* Support multiple worksheets within a workbook.
* Create a scalable framework for future financial data validation projects.

---

# System Workflow

## Step 1: Upload Salary File

The user uploads an Excel file (.xlsx) containing salary information through the Streamlit interface.

↓

## Step 2: Detect Salary Blocks

The application scans each worksheet and identifies bold rows.

* First bold row → Block Start
* Next bold row → Block End for previous block and Start for next block

↓

## Step 3: Extract Summary Values

The tool extracts the values present in the block header row.

↓

## Step 4: Calculate Employee Totals

All rows between two consecutive bold rows are processed.

For each numeric column:

* Values are summed independently.
* Calculations are performed column-wise.

↓

## Step 5: Validation

The calculated totals are compared with the values present in the block header.

↓

## Step 6: Mismatch Detection

Any discrepancy is recorded along with:

* Sheet Name
* Block Name
* Column Name
* Expected Value
* Actual Value
* Difference
* Status

↓

## Step 7: Report Generation

A new worksheet named:

Validation_Report

is automatically generated inside the output workbook.

↓

## Step 8: Download Processed File

The user downloads the validated workbook with the generated report.

---

# Features

### Automated Block Detection

* Detects salary blocks using bold formatting.
* No manual configuration required.

### Multi-Sheet Processing

* Automatically validates all worksheets in a workbook.

### Column-Wise Validation

* Each numeric column is validated independently.

### Mismatch Reporting

* Generates a dedicated Validation_Report sheet.

### User-Friendly Interface

* Simple and interactive Streamlit dashboard.

### Downloadable Output

* Processed files can be downloaded instantly.

### Scalable Architecture

* Designed to support additional financial document types in the future.

---

# Technologies Used

## Frontend

* Streamlit

## Backend

* Python

## Excel Processing

* OpenPyXL
* Pandas

## Data Handling

* NumPy

## Version Control

* Git
* GitHub

---

# Validation Logic

For every block:

Header Total

must equal

Sum(Employee Records)

for each numeric column.

Example:

Salary Header Total = Sum of Employee Salary Values

PF Header Total = Sum of Employee PF Values

ESIC Header Total = Sum of Employee ESIC Values

Net Salary Header Total = Sum of Employee Net Salary Values

Each column is validated independently.

---

# Output Format

The generated Validation_Report sheet contains:

| Sheet Name | Block Name | Column | Expected Value | Actual Sum | Difference | Status |
| ---------- | ---------- | ------ | -------------- | ---------- | ---------- | ------ |

Only mismatches are reported, making it easier to identify problematic records quickly.

---

# Business Applications

This solution can be used in:

* Payroll Management
* Internal Audits
* Financial Reconciliation
* HR Operations
* Accounting Departments
* Salary Verification Processes
* Compliance Checks
* Employee Remuneration Validation

---

# Benefits

* Eliminates manual calculations.
* Saves auditing time.
* Improves payroll accuracy.
* Reduces human error.
* Enhances operational efficiency.
* Provides transparent validation reports.
* Supports large datasets.

---

# Future Scope

The project is designed to be extended beyond salary validation.

Future enhancements may include:

### Additional File Types

* Sales Validation
* Purchase Validation
* Stock Validation
* Journal Voucher Validation
* Sundry Creditors Validation

### AI-Based Validation

* Intelligent anomaly detection.
* Pattern recognition.
* Outlier identification.

### Dashboard Analytics

* Interactive charts.
* Summary statistics.
* Validation trends.

### Cloud Deployment

* Web-hosted validation platform.
* Multi-user access.

### Role-Based Access Control

* Admin
* Auditor
* HR Manager

### Database Integration

* MySQL
* PostgreSQL
* SQL Server

### Automated Email Reports

* Scheduled validation reports.
* Alert notifications for mismatches.

---

# Repository Structure

```text
salary-validator/
│
├── app.py
├── cleaner.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

```bash
git clone https://github.com/rahulyk1805/salary-validator-.git

cd salary-validator

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

# Author

**Rahul Yerunkar**
