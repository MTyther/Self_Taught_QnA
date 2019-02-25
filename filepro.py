#Question 1: Find a file on your computer and print its contents using Python.

import os

file_path = os.path.join("C:\\","readme.txt")

with open(file_path, "r") as f:
    print(f.read())


#Question 2: Write a program that asks a user a question, and saves their answer to a file.
q_string = []
f_name = input("Please enter your firstname: ")
l_name = input("Please enter your lastname: ")
m_address = input("Please enter your address: ")
m_city = input("Please enter your city: ")
m_state = input("Please enter your state: ")
m_zip = input("Please enter your zip code: ")

q_string.append(f_name)
q_string.append(l_name)
q_string.append(m_address)
q_string.append(m_city)
q_string.append(m_state)
q_string.append(m_zip)
                   
with open("datafile.txt", "w") as f:
    f.write(str(q_string))

with open("datafile.txt", "r") as f:
    print(f.read())
