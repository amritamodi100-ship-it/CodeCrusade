'''Scholarship Evaluator: A student gets a scholarship if their GPA is greater than 3.5 AND
they have no disciplinary records. They ALSO get it if their GPA is exactly 4.0,regardless of records. 
Create variables for gpa (float) and has_record (Boolean).Write a complex logical expression using parentheses, comparisons,
and logical operators (and, or, not) to print whether they get the scholarship (True/False).'''


# has_record = bool(input("Enter disciplinary records : "))
# gpa = float(input("Enter your GPA : "))
gpa = 9.0
has_record = False

get_scholar = ((gpa > 3.5 and not has_record ) or (gpa == 4.0 ))
print("can you get scholarship ",get_scholar)




