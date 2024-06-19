import tkinter as tk
import secrets
import string


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


#  Generate and print a password
password = generate_password()
print(f"Generated Password: {password}")

#  Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a label to display the generated password
password_label = tk.Label(root, text="", font=("Arial", 12), bg="light grey", padx=100, pady=10)
password_label.pack(pady=10)  # Add padding above the label


# Function to update the password label
def update_password_label():
    generated_password = generate_password()  # Call your password generation function here
    password_label.config(text=generated_password)


# Create a button to generate password
generate_button = tk.Button(root, text="Generate Password", command=update_password_label, bg="#1E90FF", fg="white",
                            font=("Arial", 14, "bold"))
generate_button.pack(pady=20)  # Add padding below the button

# Run the Tkinter main loop
root.mainloop()

