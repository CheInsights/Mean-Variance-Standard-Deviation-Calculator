Mean-Variance-Standard Deviation Calculator
Overview
The Mean-Variance-Standard Deviation Calculator is a Python project designed to perform statistical analysis on a 3×3 matrix of numbers using NumPy. This focused tool takes a flat list of exactly nine numbers, reshapes it into a matrix, and computes essential descriptive statistics — mean, variance, standard deviation, maximum, minimum, and sum — across rows, columns, and the entire flattened dataset. It serves as an excellent demonstration of array manipulation, axis-based operations, and statistical computation in data analysis workflows.

Features
1. Input Validation Module
Data Validation: Ensures the input list contains exactly nine numbers; raises a clear ValueError with the message "List must contain nine numbers." if the requirement is not met.

2. Matrix Transformation Module
NumPy Integration: Converts the input list of nine numbers into a clean 3×3 NumPy array using reshape for efficient multi-dimensional calculations.

3. Statistical Analysis Module
Comprehensive Calculations: Computes six key statistics (mean, variance, standard deviation, max, min, sum) along three views:
- Rows (axis=1)
- Columns (axis=0)
- Flattened matrix (overall)
Returns results in a structured dictionary with plain Python lists and scalar values.

4. Output Formatting Module
Dictionary Structure: Organizes results in the precise format required, with row statistics first, followed by column statistics, followed by the flattened value — ensuring compatibility with automated testing suites.

Why Mean-Variance-Standard Deviation Calculator?
This project aims to showcase proficiency in NumPy and fundamental data analysis techniques commonly used in scientific computing and statistics. By handling matrix reshaping, axis-specific operations, type conversion, and exception handling, it demonstrates clean, reliable code for numerical analysis tasks encountered in data science, research, and certification assessments.

Special Note
The Mean-Variance-Standard Deviation Calculator is not only a functional statistical tool but also a clear illustration of the power of NumPy in simplifying complex array-based computations. The combination of input validation, precise axis handling, and structured output adds a layer of robustness and professionalism to numerical data processing workflows.

Feel free to explore the function, test it with different datasets, and adapt the code for your specific analytical needs.
