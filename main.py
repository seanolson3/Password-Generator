import tkinter as tk
import tkinter.messagebox as msgbox
import secrets
import string

# Open the file in append mode ('a') with write permissions
pass_file = open("Passwords.txt", 'a')


def generate_password():
    characters = string.ascii_letters + string.digits
    groups = []

    for _ in range(3):
        group = ''
        has_number = False

        for _ in range(5):
            char = secrets.choice(characters)
            group += char
            if char.isdigit():
                has_number = True

        if not has_number:
            group = group[:-1] + secrets.choice(string.digits)

        groups.append(group)

    password = ':'.join(groups)
    return password


#  Create the main window
root = tk.Tk()
root.title("Password Generator")

root.geometry("400x200")
root.configure(bg="#333333")

# Create a label to display the generated password
password_label = tk.Label(root, text="", font=("Arial", 12), bg="light grey", width=30, pady=10)
password_label.pack(pady=10)  # Add padding above the label

# Variable to store the currently displayed password
current_password = ""


# Function to update the password label
def update_password_label():
    global current_password
    current_password = generate_password()  # Generate a new password
    password_label.config(text=current_password)  # Update the password label


# Function to save the current password to file and show message box
def save_password():
    global current_password
    pass_file.write(current_password + "\n")  # Write current password to file with newline
    pass_file.flush()  # Flush the buffer to ensure the write is immediate

    # Show message box
    msgbox.showinfo("Password Saved", "Password saved successfully!")


# Create a button to generate password
generate_button = tk.Button(root, text="Generate Password", command=update_password_label, bg="#146eb4", fg="white",
                            font=("Arial", 14, "bold"))
generate_button.pack(pady=10)  # Add padding below the button

# Create a button to save password
save_button = tk.Button(root, text="Save Password", command=save_password, bg="#146eb4", fg="white",
                        font=("Arial", 14, "bold"))
save_button.pack(pady=10)  # Add padding below the button

# Run the Tkinter main loop
root.mainloop()

# Close the file after the program is done
pass_file.close()
