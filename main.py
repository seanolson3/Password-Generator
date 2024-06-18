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
