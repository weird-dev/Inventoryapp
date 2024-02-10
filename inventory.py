# %%
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('inventory.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create a table to store product information
c.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )''')

# Function to add a new product to the database
def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    c.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    print("Product added successfully!")

# Function to display the menu
def display_menu():
    print("\nInventory Management System Menu:")
    print("1. Add Product")
    print("2. Exit")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':

            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()



# %%



