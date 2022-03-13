import sqlite3
from tabulate import tabulate


def print_table(data):
    print("\n", tabulate(data, headers = [tp[0] for tp in data.description]), "\n")


conn = sqlite3.connect('blog.db')
cursor = conn.cursor()

users = cursor.execute('''SELECT * FROM users''')
print_table(users)

blogs = cursor.execute('''SELECT * FROM blogs''')
print_table(blogs)


conn.commit()
conn.close()
