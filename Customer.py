import tkinter as tk
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
        user="root",
        password="",
        database="potlepak restaurant"   
)

mycursor = mydb.cursor()

# Function to insert data into the table
def insert_data():
    Cus_Name = name_entry.get()
    Cus_Phone = phonenumber_entry.get()
    Cus_ID = id_entry.get()
    Birth_day = dayField.get()
    Birth_Month = monthField.get()
    Birth_year = yearField.get() 
    Cus_Age = age_year_entry.get()


    # Corrected the INSERT INTO syntax and removed quotes from the data variable
    insert_query = "INSERT INTO customer (Cus_Name, Cus_Phone, Cus_ID, Birth_Day, Birth_Month, Birth_Year, Cus_Age) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (Cus_Name, Cus_Phone, Cus_ID, Birth_day, Birth_Month, Birth_year, Cus_Age)

    # Execute the query with the data
    mycursor.execute(insert_query, data)

    # Commit the changes to the database
    mydb.commit()

    mycursor.close()
    mydb.close()

    messagebox.showinfo("Success", "Data inserted successfully!")

	
def calculate_age():
    # Extract values from the respective entry boxes
    birth_day = int(dayField.get())
    birth_month = int(monthField.get())
    birth_year = int(yearField.get())

    given_day = int(current_day.get())
    given_month = int(current_month.get())
    given_year = int(current_year.get())

    # If birth date is greater than given birth_month, adjust the values
    if birth_day > given_day:
        given_month -= 1
        given_day += 30  # Assuming a 30-day month to simplify

    if birth_month > given_month:
        given_year -= 1
        given_month += 12

    # Calculate day, month, year
    calculated_year = given_year - birth_year

    # Insert the calculated year into the entry box
    age_year_entry.insert(10, str(calculated_year))

def clear_entry_fields():
    name_entry.delete(0, tk.END)
    phonenumber_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    dayField.delete(0, tk.END)
    monthField.delete(0, tk.END)
    yearField.delete(0, tk.END)
    age_year_entry.delete(0, tk.END)

# Function to update data in the table
def update_data():
    Cus_Name = name_entry.get()
    Cus_Phone = phonenumber_entry.get()
    Cus_ID = id_entry.get()
    Birth_day = dayField.get()
    Birth_Month = monthField.get()
    Birth_year = yearField.get() 
    Cus_Age = age_year_entry.get()

    if Cus_Name and Cus_ID:
        try:
            with mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="potlepak restaurant"
            ) as mydb:
                with mydb.cursor() as mycursor:
                    update_query = "UPDATE customer SET Cus_Name = %s, Cus_Phone = %s, Birth_Day = %s, Birth_Month = %s, Birth_Year = %s, Cus_Age = %s WHERE Cus_ID = %s"
                    mycursor.execute(update_query, (Cus_Name, Cus_Phone, Birth_day, Birth_Month, Birth_year, Cus_Age, Cus_ID))
                    mydb.commit()

            messagebox.showinfo("Success", "Data updated successfully")
        except mysql.connector.Error as err:
            tk.messagebox.showerror("Error", f"Error: {err}")
    else:
        tk.messagebox.showwarning(title="Error", message="Name and ID are required.")

# Function to delete data from the table
def delete_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="potlepak restaurant"
    )
    cursor = conn.cursor()

    delete_query = "DELETE FROM customer WHERE Cus_ID=%s"
    data = (id_entry.get(),)

    cursor.execute(delete_query, data)

    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data deleted successfully")

# Tkinter GUI
root = tk.Tk()
root.title("Customer Registration")
root.configure(bg="#BC8F8F")

label_name = tk.Label(root, text="Name:", font=('Times New Roman', 12), bg="#BC8F8F")
label_name.grid(row=0, column=0)
name_entry = tk.Entry(root, font=('Adlam Display', 12))
name_entry.grid(row=0, column=1)

label_phonenumber = tk.Label(root, text="Phone number:",font=('Times New Roman', 12), bg="#BC8F8F")
label_phonenumber.grid(row=1, column=0)
phonenumber_entry = tk.Entry(root, font=('Adlam Display', 12))
phonenumber_entry.grid(row=1, column=1)

label_id = tk.Label(root, text="Id:", font=('Times New Roman', 12), bg="#BC8F8F")
label_id.grid(row=2, column=0)
id_entry = tk.Entry(root, font=('Adlam Display', 12))
id_entry.grid(row=2, column=1)

# Date of birth
birth_date = tk.Label(root, text="Birth Day", font=('Times New Roman', 12), bg="#BC8F8F")
birth_date.grid(row=3, column=0)
birth_month = tk.Label(root, text="Birth Month", font=('Times New Roman', 12), bg="#BC8F8F")
birth_month.grid(row=3, column=1)
birth_year = tk.Label(root, text="Birth Year", font=('Times New Roman', 12), bg="#BC8F8F")
birth_year.grid(row=3, column=2)

# Create a text entry box for filling or typing the information(dob). 
dayField = tk.Entry(root, font=('Adlam Display', 12))
dayField.grid(row=4, column=0)
monthField = tk.Entry(root, font=('Adlam Display', 12))
monthField.grid(row=4, column=1)
yearField = tk.Entry(root, font=('Adlam Display', 12))
yearField.grid(row=4, column=2)

# Current Year
curr_day = tk.Label(root, text= "Current Day", font=('Times New Roman',12), bg="#BC8F8F")
curr_day.grid(row=5,column=0)
curr_month = tk.Label(root, text= "Current Month", font=('Times New Roman',12), bg="#BC8F8F")
curr_month.grid(row=5, column=1)
curr_year = tk.Label(root, text= "Current Year", font=('Times New Roman',12), bg="#BC8F8F")
curr_year.grid(row=5, column=2)

# Create a text entry box for filling or typing the information(current year). 
current_day = tk.Entry(root, font=('Adlam Display', 12))
current_day.grid(row=6, column=0)
current_month = tk.Entry(root, font=('Adlam Display', 12))
current_month.grid(row=6, column=1)
current_year = tk.Entry(root, font=('Adlam Display', 12))
current_year.grid(row=6, column=2)	

# Age results
resultantAge = tk.Button(root, text = "Age", command = calculate_age, padx=25, pady=5)
resultantAge.grid(row=8, column=1, sticky= "news")

age_year = tk.Label(root, text= "Age:", font=('Times New Roman',12), bg="#BC8F8F")
age_year.grid(row=7, column=0)
age_year_entry = tk.Entry(root, font=('Adlam Display', 12))
age_year_entry.grid(row=7, column=1)

for widget in root.winfo_children():
    widget.grid(padx=10, pady=5)

insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.grid(row=9, column=1, sticky="news")

# Update and Delete buttons
update_button = tk.Button(root, text="Update Data", command=update_data)
update_button.grid(row=10, column=0, sticky="news")

delete_button = tk.Button(root, text="Delete Data", command=delete_data)
delete_button.grid(row=10, column=2, sticky="news")  

root.mainloop()