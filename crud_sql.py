import sqlite3  
cnt = sqlite3.connect("backup.dp")  

""""
# create a database named backup
cnt = sqlite3.connect("backup.dp")  

# create a table named gfg
cnt.execute('''CREATE TABLE gfg(
NAME TEXT,
POINTS INTEGER,
ACCURACY REAL);''')
"""
# Python3 Code to insert data into
# the database

# Insert three tuples into the gfg table
# insert in default order
""""
cnt.execute('''INSERT INTO gfg VALUES(
'Count Inversion',20,80.5);''')

# insert in different order
cnt.execute('''INSERT INTO gfg(ACCURACY, POINTS, NAME) VALUES(
90.5, 15, 'Kadanes Algo');''')

cnt.execute('''INSERT INTO gfg(NAME, ACCURACY, POINTS) VALUES(
'REVERSE STR', 100, 5);''')

# commit changes to the database
cnt.commit()
"""
# Python3 code to read data from a table
"""
print('Name, Points and Accuracy from '
      'records with accuracy greater than 85')

cursor = cnt.execute('''SELECT * FROM gfg WHERE ACCURACY>85;''')

# print data using the cursor object
for i in cursor:
    print(i[0]+"    "+str(i[1])+"   "+str(i[2]))

print('')  # Print new line

print('Name, Accuracy from '
      'records with accuracy greater than 85')

cursor = cnt.execute('''SELECT NAME, ACCURACY FROM
gfg WHERE ACCURACY>85;''')

# print data using the cursor object
for i in cursor:
    print(i[0]+"    "+str(i[1]))
"""
# Python3 code to update records in a database

# Print records before updation
"""
cursor = cnt.execute('''SELECT * FROM gfg''')
print('Before Updation')
for i in cursor:
    print(i[0]+"    "+str(i[1])+"    "+str(i[2]))

print('')  # print a newline

# Execute an Update statement
cnt.execute('''UPDATE gfg SET POINTS=POINTS+5 WHERE
POINTS<20;''')

cursor = cnt.execute('''SELECT * FROM gfg''')
print('After Updation')
for i in cursor:
    print(i[0]+"    "+str(i[1])+"    "+str(i[2]))

"""   
# Python3 code to delete records from database

# Print records before deletion
cursor = cnt.execute('''SELECT * FROM gfg''')
print('Before Deletion')
for i in cursor:
    print(i[0]+"    "+str(i[1])+"    "+str(i[2]))

print('')  # print a newline

# Execute a delete statement
cnt.execute('''DELETE FROM gfg WHERE ACCURACY>91;''')

cursor = cnt.execute('''SELECT * FROM gfg''')
print('After Deletion')
for i in cursor:
    print(i[0]+"    "+str(i[1])+"    "+str(i[2])) 


