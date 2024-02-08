#library fine calculator
book_id = input("Enter book ID: ")
due_date = input("Enter due date (format: dd/mm/yyyy): ")
return_date = input("Enter return date (format: dd/mm/yyyy): ")

# Calculate days overdue
due_date_split = due_date.split("/")
return_date_split = return_date.split("/")
due_day = int(due_date_split[0])
due_month = int(due_date_split[1])
due_year = int(due_date_split[2])
return_day = int(return_date_split[0])
return_month = int(return_date_split[1])
return_year = int(return_date_split[2])

days_overdue = (return_year - due_year) * 365 + (return_month - due_month) * 30 + (return_day - due_day)

# Determine fine rate
if days_overdue <= 7:
    fine_rate = 20
elif days_overdue <= 14:
    fine_rate = 50
else:
    fine_rate = 100

# Calculate fine amount
fine_amount = days_overdue * fine_rate

# Display results
print("Book ID:", book_id)
print("Due date:", due_date)
print("Return date:", return_date)
print("Days overdue:", days_overdue)
print("Fine rate:", fine_rate)
print("Fine amount:", fine_amount)
