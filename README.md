Mean-Variance-Standard Deviation Calculator
Overview
Super straightforward NumPy mini-project: feed it a list of exactly 9 numbers → it turns them into a 3×3 matrix → spits out mean, variance, std, max, min and sum for rows, columns and the whole thing flattened.

Perfect little exercise if you're learning NumPy axes, reshaping, or doing freeCodeCamp's Data Analysis with Python cert.

Features
1. Input check
Only accepts lists with exactly 9 numbers. Otherwise → ValueError("List must contain nine numbers.")

2. Matrix magic
Turns your flat list into a proper 3×3 NumPy array with .reshape(3, 3)

3. Stats party
Calculates six stats (mean, var, std, max, min, sum) in three different ways:
- per row (axis=1)
- per column (axis=0)
- overall (flattened)

4. Clean output
Returns a nice dictionary — rows first, then columns, then total. All plain Python lists/numbers (no ugly numpy types).

Why bother with this project?
It's a great way to really understand NumPy axes (which confuse almost everyone at first) and practice writing robust little functions that real data analysis code is built on.

Special Note
NumPy makes matrix math feel almost too easy once you get the hang of it. This tiny project shows how much power you get from just reshape + axis arguments + good input validation.

Go ahead — throw some random lists at it, break it, fix it, make it yours. Have fun! 🚀
