import click
import csv
import os
from datetime import datetime

@click.command()
@click.argument("method", default="list")
@click.option('--description', '-d', default="", help="Description of the expense")
@click.option('--amount', '-a', default=0.0, type=float, help="The expense amount")
@click.option('-id', type=int, help="ID of the expense to delete")
@click.option('-m', type=int, help="Month to filter expenses for the summary")

def main(method, description="", amount=0.0, id=None, m=None):
    # Read the existing data from CSV
    if os.path.exists('expense.csv'):
        with open('expense.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            data = list(reader)
    else:
        data = []

    # Handle "add" method
    if method == "add":
        if description and amount:
            # Generate a unique ID based on the current data size
            new_id = len(data) + 1  # ID starts from 1
            
            # Add new row with ID, description, date, and amount (as float)
            data.append([new_id, description, str(datetime.now().date()), float(amount)])
            
            # Write data back to CSV file
            with open('expense.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(["ID", "Description", "Date", "Amount"])
                # Write all data rows
                writer.writerows(data)
            
            print(f"Added expense: {new_id}")
        else:
            print("Please provide both description and amount.")

    # Handle "list" method to display the current expenses
    elif method == "list":
        if data:
            try:
                total = 0
                if m:
                    # Filter expenses by the given month
                    print("Your current expenses for month {}: ".format(m))
                    for row in data:
                        if datetime.strptime(row[2], '%Y-%m-%d').month == m:
                            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
                            total += float(row[3])
                    print("Total expenses for month {}: {}".format(m, total))
                else:
                    # Summarize all expenses
                    print("Your current expenses:")
                    for row in data:
                        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
                        total += float(row[3])
                    print(f"Total expenses: {total}")
            except ValueError:
                print("Error processing dates.")
        else:
            print("No expenses found.")

    # Handle "delete" method
    elif method == "delete":
        if data and id is not None:
            try:
                # Find the row with the matching ID and delete it
                data = [row for row in data if int(row[0]) != id]
                
                # Write updated data back to CSV
                with open('expense.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Description", "Date", "Amount"])
                    writer.writerows(data)
                
                print(f"Deleted expense with ID: {id}")
            except ValueError:
                print("Invalid ID format.")
        else:
            print("No valid ID provided or no expenses found.")

    # Handle "summary" method
    elif method == 'summary':
        if data:
            try:
                total = 0
                if m:
                    # Filter expenses by the given month
                    total = sum(float(row[3]) for row in data if datetime.strptime(row[2], '%Y-%m-%d').month == m)
                else:
                    # Summarize all expenses
                    total = sum(float(row[3]) for row in data)
                print(f"Total expenses: {total}")
            except ValueError:
                print("Error processing dates.")
        else:
            print("No expenses to summarize.")
            
if __name__ == '__main__':
    main()
