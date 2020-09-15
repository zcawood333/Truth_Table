# Truth_Table
Contains one .py file that creates a truth table based on boolean inputs.

Input can be a command line argument or, if not provided, will be asked for.

Argument expression must use single-letter variables, is case insensitive, must have no spaces(or be wrapped in ""), and requires the correct operators(see below).

There is no guarantee for correct output if formatting of input is incorrect. Made on windows, not tested on other platforms.

Correct operators:
\* = AND 
+ = OR 
' = NOT(INVERSION) 

ex. for command line: python truth_table.py "(a*b')+(a'*b)"

