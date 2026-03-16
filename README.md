Mean-Variance-Standard Deviation Calculator

Overview

The Mean-Variance-Standard Deviation Calculator is a Python-based analytical tool designed to perform multi-axis statistical computations on a 3×3 matrix. Using NumPy, the project transforms a flat list of nine numbers into a structured matrix to compute essential descriptive statistics across rows, columns, and the entire dataset.

This project serves as a demonstration of core data engineering skills: array manipulation, axis-based operations, and robust error handling within a data analysis workflow.

Technical Modules

🛡️ Input Validation
Data Integrity: The function verifies that the input list contains exactly nine numbers.

Exception Handling: Raises a ValueError with the message "List must contain nine numbers." if the requirement is not met, preventing downstream calculation errors.

#📐 Matrix Transformation
NumPy Integration: Leverages the reshape method to convert 1D input lists into 3×3 NumPy arrays.

Memory Efficiency: Uses NumPy’s optimized C-backend for high-speed multi-dimensional calculations.

📊 Statistical Analysis

The tool computes six key metrics across three distinct views:

Axis 0 (Columns): Vertical performance trends.

Axis 1 (Rows): Horizontal performance trends.

Flattened: Global dataset statistics.

Metrics included: Mean, Variance, Standard Deviation, Maximum, Minimum, and Sum.

📋 Output Formatting

Structure: Results are returned in a strictly formatted dictionary compatible with automated testing suites.

Type Conversion: All results are converted from NumPy types back into native Python lists for maximum compatibility with external APIs.

Real-World Application

In a commercial data environment—such as Agricultural Fintech—this logic is fundamental for auditing regional performance. For example, if the matrix represents Loan Repayment Rates across three different Regions (Columns) over three Months (Rows), this tool can instantly identify:

Axis 0: Which region is performing best on average.

Axis 1: Which month saw a dip in repayments across all regions.

Flattened: The overall health of the credit portfolio.

Tech Stack
Language: Python 3.x

Library: NumPy

Environment: Jupyter Notebook 
