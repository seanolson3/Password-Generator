import secrets
import string 



#Builds letter bank from string module
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

#Combines into letter_bank
letter_bank = letters + digits + special_chars

#Function to generate passwor
def generate_pwd(length):
    #Infinate while loop until requirements are met
    while True:
      pwd = ''
      #Generates password of size pwd_length
      for i in range(pwd_length):
        pwd += ''.join(secrets.choice(letter_bank))
    
      #Checks for at least one special_chars and at least two digits
      if (any(char in special_chars for char in pwd) and 
          sum(char in digits for char in pwd)>=2):
              break
    return pwd


#Gets desired password length from user
pwd_length = int(input("Password Length: ")) 
password = generate_pwd(pwd_length)
print(password)
