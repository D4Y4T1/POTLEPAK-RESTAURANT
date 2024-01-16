import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def insert_data(employee_data, accept_var):
    accepted = accept_var.get()

    if accepted == "Accepted":
        first_name = employee_data.get("first_name")
        last_name = employee_data.get("last_name")
        number_phone = employee_data.get("number_phone")
        gender = employee_data.get("gender")
        age = employee_data.get("age")
        email = employee_data.get("email")

        #Connect to your MySQL database
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "potlepak restaurant"

        )

        #Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        #SQL query to insert data into the table
        insert_query = "INSERT INTO employee (first_name, last_name, number_phone, gender, age, email) VALUES (%s, %s, %s, %s, %s, %s)"

        #Execute the query with the data
        mycursor.execute(insert_query, (first_name, last_name, number_phone, gender, age, email))

        #Commit the changes to the database
        mydb.commit()

        mycursor.close()
        mydb.close()

        messagebox.showinfo("Success", "Data inserted successfully")

    else :
        tk.messagebok.showwarning(title = "Error", message = "You have not accepted the terms")

def clear_entries():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    number_phone_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def employee_registration():
    while True:
        root = tk.Tk()
        root.title("Employee Detail")
        root.geometry("400x500")

        employee_info = tk.LabelFrame(root, text="Employee Registration", font=('Times New Roman', 12))
        employee_info.grid(row=1, column=0, padx=20, pady=10)


def update_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # Employee Information
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        age = age_entry.get()
        email = email_entry.get()

        if first_name and last_name:
            email = email_entry.get()

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
            update_query = "UPDATE employee SET age = %s, email = %s WHERE first_name = %s AND last_name = %s"

            # Execute the query with the data
            mycursor.execute(update_query, (age, email, first_name, last_name))

            # Commit the changes to the database
            mydb.commit()

            mycursor.close()
            mydb.close()

            messagebox.showinfo("Success", "Data updated successfully")
        else:
            tk.messagebox.showwarning(title="Error", message="First Name and Last Name are required")
    else:
        tk.messagebox.showwarning(title="Error", message="You have not accepted the terms")

def delete_data():
    email = email_entry.get()

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
    delete_query = "DELETE FROM employee WHERE email = %s"

    # Execute the query with the data
    mycursor.execute(delete_query, (email,))

    # Commit the changes to the database
    mydb.commit()

    mycursor.close()
    mydb.close()

    messagebox.showinfo("Success", "Data deleted successfully")

    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    number_phone_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Employee Detail")
root.geometry("400x500")
root.configure(bg="#CD9B9B")

employee_info = tk.LabelFrame(root, text="Employee Registration", font=('Times New Roman', 12), bg="#CD9B9B")
employee_info.grid(row=1, column=0, padx=20, pady=10)

first_name_label = tk.Label(employee_info, text="First Name :", font=('Times New Roman', 14), bg="#CD9B9B")
first_name_entry = tk.Entry(employee_info, font=('Adlam Display', 12))
first_name_label.grid(row=0, column=0)
first_name_entry.grid(row=0, column=1)

last_name_label = tk.Label(employee_info, text="Last Name :", font=('Times New Roman', 14), bg="#CD9B9B")
last_name_entry = tk.Entry(employee_info, font=('Adlam Display', 12))
last_name_label.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

number_phone_label = tk.Label(employee_info, text="Phone Number :", font=('Times New Roman', 14), bg="#CD9B9B")
number_phone_entry = tk.Entry(employee_info, font=('Adlam Display', 12))
number_phone_label.grid(row=2, column=0)
number_phone_entry.grid(row=2, column=1)

gender_label = tk.Label(employee_info, text="Gender :", font=('Times New Roman', 14), bg="#CD9B9B")
gender_entry = tk.Entry(employee_info, font=('Adlam Display', 12))
gender_label.grid(row=3, column=0)
gender_entry.grid(row=3, column=1)

age_label = tk.Label(employee_info, text="Age :", font=('Times New Roman', 14), bg="#CD9B9B")
age_entry = tk.Entry(employee_info, font=('Adlam Display', 12))
age_label.grid(row=4, column=0)
age_entry.grid(row=4, column=1)

email_label = tk.Label(employee_info, text="Email :", font=('Times New Roman', 14), bg="#CD9B9B")
email_entry = tk.Entry(employee_info, font=('Adlam Display', 12))
email_label.grid(row=5, column=0)
email_entry.grid(row=5, column=1)

for widget in employee_info.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

#Accept terms
terms_frame = tk.LabelFrame(root, text = "Terms and Conditions", bg="#CD9B9B")
terms_frame.grid(row = 6, column = 0, sticky = "news", padx =20, pady = 20)

accept_var = tk.StringVar(value = "Not Value")
terms_check = tk.Checkbutton(terms_frame, text = "I accept the terms and conditions", variable = accept_var, onvalue = "Accepted", offvalue = "Not Accepted")
terms_check.grid(row = 0, column = 0)

# Insert Data
button = tk.Button(root, text="Insert Data", command=lambda: insert_data({
    "first_name": first_name_entry.get(),
    "last_name": last_name_entry.get(),
    "number_phone": number_phone_entry.get(),
    "gender": gender_entry.get(),
    "age": age_entry.get(),
    "email": email_entry.get()
}, accept_var))
button.grid(row=7, column=0, sticky="n", padx=5, pady=3)

#Update Button
update_button = tk.Button(root, text = "Update Data", command = update_data)
update_button.grid(row = 8, column = 0, sticky = "n", padx = 5, pady = 3)

#Delete Button
delete_button = tk.Button(root, text = "Delete Data", command = delete_data)
delete_button.grid(row = 10, column = 0, sticky = "n", padx = 5, pady = 3)

# Clear Entries Button
clear_button = tk.Button(root, text="Clear Entries", command=clear_entries)
clear_button.grid(row=9, column=0, sticky="n", padx=5, pady=3)

# Break the loop and exit the window when the user closes it
root.protocol("WM_DELETE_WINDOW", root.destroy)

root.mainloop()

