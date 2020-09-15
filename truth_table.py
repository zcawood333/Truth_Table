# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 00:44:57 2020

@author: zcawo
"""
#imports
from sys import argv

#classes
class Literal():
    def __init__(self,letter):
        self.letter = letter
        self.val = 0
    def __str__(self):
        return f"{self.letter}: {self.val}"
    def __repr__(self):
        return self.__str__()

def main(input_exp = None):
    #acquire expression
    if input_exp != None:
        exp = input_exp
    elif len(argv) > 1:
        if len(argv) == 2:
            exp = argv[1]
        else:
            raise Exception('Incorrect number of arguments; \nmake sure there are no spaces in the expression or surround it with double quotes')
    else:
        exp = input("Expression to create truth table for: ")
    exp = exp.upper() 
    exp = exp.replace(" ","")
    
    #converting exp to python exp and collecting variables
    variables = []
    not_done = True
    while not_done:
        not_done = False
        pars = []
        for idx, char in enumerate(exp):
            if char == "(":
                pars.append(idx)
            elif char == ")":
                if  idx < len(exp) - 1 and exp[idx + 1] == "'":
                    start = pars.pop()
                    end = idx
                    not_statement = f"(not {exp[start:end+1]})"
                    exp = exp[:start] + not_statement + exp[end+2:]
                    not_done = True
                    break
                else:
                    pars.pop()      
            elif idx < len(exp) - 1 and exp[idx + 1] == "'":
                not_statement = f"(not {exp[idx]})"
                exp = exp[:idx] + not_statement + exp[idx + 2:]
                not_done = True
                break
            elif char == "*":
                statement = " and "
                exp = exp[:idx] + statement + exp[idx + 1:]
                not_done = True
                break
            elif char == "+":
                statement = " or "
                exp = exp[:idx] + statement + exp[idx + 1:]
                not_done = True
                break
            elif char.isalpha and char.isupper():
                if char not in [literal.letter for literal in variables]:
                    variables.append(Literal(char))
                    
    #sort variables list alphabetically for nicer output
    variables.sort(key=lambda literal: literal.letter)
    
    #develop output values
    output = []
    variable_vals = [[] for i in variables]
    #loop through all combinations of 1 and 0
    num_variables = len(variables)
    for num in range(2**num_variables):
        curr_num = num
        for i in range(num_variables):
            base = (2**(num_variables - (i + 1)))
            variables[i].val = curr_num//base
            curr_num = curr_num%base
        #replace variables in python expression and evaluate
        curr_exp = exp
        for idx, literal in enumerate(variables):
            variable_vals[idx].append(literal.val)
            curr_exp = curr_exp.replace(literal.letter,"True" if literal.val == 1 else "False")
        output.append(1 if eval(curr_exp) else 0)
    
    #display output
    for literal in variables:
        print(f'|    {literal.letter}    |',end='')
    print('|   OUT   |')
    print("-"*(11*(num_variables+1)))
    for i in range(2**num_variables):
        for idx in range(num_variables):
            print(f'|    {variable_vals[idx][i]}    |',end='')
        print(f'|    {output[i]}    |')
        print("-"*(11*(num_variables+1)))
        
if __name__ == '__main__':
    main()