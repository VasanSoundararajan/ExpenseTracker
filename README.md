# ExpenseTracker
Build a simple expense tracker application to manage your finances. The application should allow users to add, delete, and view their expenses. The application should also provide a summary of the expenses.

# Requirements
Application should run from the command line and should have the following features:

Users can add an expense with a description and amount.
Users can update an expense.
Users can delete an expense.
Users can view all expenses.
Users can view a summary of all expenses.
Users can view a summary of expenses for a specific month (of current year).

# add 
To add to the list of expenses we can use the keyword add

sample usage

... \ExpenseTracker> python mian.py add -d lunch -a 10
Added expense: 1

# delete
To delete an expense from the list of expenses we can use the keyword delete

sample usage

... \ExpenseTracker> python mian.py delete -id 1
Deleted expense with ID: 1

# List 
To list all expenses done we can use the keyword list 

sample usage

... \ExpenseTracker> python mian.py list        
Your current expenses:
2 | lunch | 2024-09-25 | 12.0

Total expenses : 12.0

if you want to list specific month expenses you can use -m with the list command

sample usage

... \ExpenseTracker> python mian.py list -m 9    
Your current expenses for month 9: 
2 | lunch | 2024-09-25 | 12.0

Total expenses for month 9: 12.0

# summary 
To summary all the expense we can use the keyword summary

sample usage

... \ExpenseTracker> python mian.py summary
Total expenses: 12.0

if you need to calculate for a single month you can use the optional parmeter -m with summary

sample usage 

... \ExpenseTracker> python mian.py summary -m 9
Total expenses: 12.0

# Profiles links
Linkedin www.linkedin.com/in/vasan-s-624b34253

Leetcode @VasanS2004

if you have any queries contact me vasansoundararajan.21@gmail.com

# Project url
https://roadmap.sh/projects/expense-tracker
