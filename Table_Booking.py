import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def insert_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        table_no = table_spinbox.get()
        number_of_people = no_people_spinbox.get()
        day = day_entry.get()
        month = month_entry.get()
        year = year_entry.get()
        deposit = deposit_entry.get()

        # Validate numeric input for number_of_people and deposit
        if not (number_of_people.isdigit() and deposit.replace('.', '', 1).isdigit()):
            tk.messagebox.showwarning(title="Error", message="Invalid input for number of people or deposit.")
            return

        # Connect to your MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="potlepak restaurant"
    )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # SQL query to insert data into the table
        insert_query = "INSERT INTO `table reservation` (Table_Number, Number_of_Customer, Day, Month, Year, Deposit) VALUES (%s, %s, %s, %s, %s, %s)"

        # Execute the query with the data
        mycursor.execute(insert_query, (table_no, number_of_people, day, month, year, deposit))

        # Commit the changes to the database
        mydb.commit()

        mycursor.close()
        mydb.close()

    else:
        tk.messagebox.showwarning(title="Error", message="You have not accepted the terms.")

    messagebox.showinfo("Success", "Data inserted successfully!")

def update_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # Customer Information
        table_number = table_spinbox.get()
        number_of_people = no_people_spinbox.get()

        if table_number and number_of_people:
            day = day_entry.get()
            month = month_entry.get()
            year = year_entry.get()
            deposit = deposit_entry.get()

            # Validate numeric input for number_of_people and deposit
            if not (number_of_people.isdigit() and deposit.replace('.', '', 1).isdigit()):
                tk.messagebox.showwarning(title="Error", message="Invalid input for number of people or deposit.")
                return

            # Connect to your MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="potlepak restaurant"
            )

            # Create a cursor object to execute SQL queries
            mycursor = mydb.cursor()

            # SQL query to update data in the table
            update_query = "UPDATE `table reservation` SET Number_of_Customer=%s, Day=%s, Month=%s, Year=%s, Deposit=%s WHERE Table_Number=%s"

            # Execute the query with the data
            mycursor.execute(update_query, (number_of_people, day, month, year, deposit, table_number))

            # Commit the changes to the database
            mydb.commit()

            mycursor.close()
            mydb.close()

            messagebox.showinfo("Success", "Data updated successfully!")
        else:
            tk.messagebox.showwarning(title="Error", message="Table number and number of people are required.")
    else:
        tk.messagebox.showwarning(title="Error", message="You have not accepted the terms.")

def delete_data():
    table_number = table_spinbox.get()

    # Validate numeric input for table_number
    if not table_number.isdigit():
        tk.messagebox.showwarning(title="Error", message="Invalid input for table number.")
        return

    # Connect to your MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="potlepak restaurant"
    )

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # SQL query to delete data from the table
    delete_query = "DELETE FROM `table reservation` WHERE Table_Number=%s"

    # Execute the query with the data
    mycursor.execute(delete_query, (table_number,))

    # Commit the changes to the database
    mydb.commit()

    mycursor.close()
    mydb.close()

    messagebox.showinfo("Success", "Data deleted successfully!")


# Fixed deposit amount per person
fixed_deposit_per_person = 5

def calculate_cost_per_person():
    try:
        number_of_people = int(no_people_spinbox.get())

        total_deposit = fixed_deposit_per_person * number_of_people

        # Update the deposit entry field with the calculated total deposit
        deposit_entry.delete(0, tk.END)  # Clear the current value
        deposit_entry.insert(0, str(total_deposit))  # Insert the calculated total deposit

        # Display the result in a messagebox
        result_message = f"Fixed Deposit per Person: {fixed_deposit_per_person}\nNumber of People: {number_of_people}\nTotal Deposit Amount: {total_deposit}"
        tk.messagebox.showinfo(title="Calculation Result", message=result_message)

    except ValueError:
        tk.messagebox.showwarning(title="Error", message="Invalid number of people.")


root = tk.Tk() 
root.title("Table Reservation Form")
root.configure(bg="#EEB4B4")

# Table Booking Information
table_info = tk.LabelFrame(root, text="Table Booking Information", font=('Times New Roman', 12,), bg="#EEB4B4")
table_info.grid(row=1, column=0, padx=20, pady=20)

table_number_label = tk.Label(table_info, text="Table Number", font=('Times New Roman', 14), bg="#EEB4B4")
table_spinbox = ttk.Spinbox(table_info, from_=1, to=30, font=('Adlam Display', 12))
table_number_label.grid(row=0, column=0)
table_spinbox.grid(row=1, column=0)

no_people_label = tk.Label(table_info, text="Number of People", font=('Times New Roman', 14), bg="#EEB4B4")
no_people_spinbox = ttk.Spinbox(table_info, from_=1, to=15, font=('Adlam Display', 12))
no_people_label.grid(row=0, column=1)
no_people_spinbox.grid(row=1, column=1)

day_label = tk.Label(table_info, text="Day:", font=('Times New Roman', 14), bg="#EEB4B4")
month_label = tk.Label(table_info, text="Month:", font=('Times New Roman', 14), bg="#EEB4B4")
year_label = tk.Label(table_info, text="Year", font=('Times New Roman', 14), bg="#EEB4B4")
day_label.grid(row=2, column=0)
month_label.grid(row=3, column=0)
year_label.grid(row=4, column=0)

day_entry = tk.Entry(table_info, font=('Adlam Display', 12))
month_entry = tk.Entry(table_info, font=('Adlam Display', 12))
year_entry = tk.Entry(table_info, font=('Adlam Display', 12))
day_entry.grid(row=2, column=1)
month_entry.grid(row=3, column=1)
year_entry.grid(row=4, column=1)

for widget in table_info.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tk.LabelFrame(root, text="Terms and Conditions", bg="#EEB4B4")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Deposit customer paid
deposit_label = tk.Label(root, text="RM (deposit):", font=('Times New Roman', 14), bg="#EEB4B4")
deposit_entry = tk.Entry(root, font=('Adlam Display', 12))
deposit_label.grid(row=3, column=0)
deposit_entry.grid(row=4, column=0)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Deposit", command=calculate_cost_per_person)
calculate_button.grid(row=5, column=0, sticky="n", padx=5, pady=3)

# Insert Data
button = tk.Button(root, text="Insert Data", command=insert_data)
button.grid(row=7, column=0, sticky="n", padx=5, pady=2)

# Update Button
update_button = tk.Button(root, text="Update Data", command=update_data)
update_button.grid(row=8, column=0, sticky="n", padx=5, pady=3)

# Delete Button
delete_button = tk.Button(root, text="Delete Data", command=delete_data)
delete_button.grid(row=9, column=0, sticky="n", padx=5, pady=3)

root.mainloop()