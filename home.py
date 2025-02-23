import csv, random

# names = ["Ram", "shyam", "Rita", "Geeta", "hari", "kabita", "laxman","krishna", "mathura","garim"]

# data = []
# for _ in range(len(names)):
#     random_name = random.choice(names)
#     age = random.randint(1, 10)
#     email = random_name.lower() + f"{age}" + "@gmail.com"
#     data.append((random_name, age, email))
# print(data)
# file_path = "home.csv"
# with open(file_path, mode = 'w' , newline='') as file:
#     csv_writer = csv.writer(file)
#     for row in data:
#         csv_writer.writerow(row)


import sqlite3
conn = sqlite3.connect("home.db")
mycursor = conn.cursor()

mycursor.execute(
""" 
Create table if not exists users(
id integer primary key autoincrement,
username text not null,
age integer,
email text unique
) """
)
with open("home.csv", mode = 'r') as file:
    users = csv.reader(file)
    mycursor.executemany("insert into users (username,age,email) values(?,?,?)",users)
conn.commit()
