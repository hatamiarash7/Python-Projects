from openpyxl import load_workbook
import sqlite3

conn = sqlite3.connect("index.db") #connect to database
cur = conn.cursor() #set cursor
table_name = "List"

cur.execute('drop table if exists List') #drop exist table
cur.execute('create table List (A TEXT, B TEXT, C TEXT, D TEXT, E TEXT, F TEXT, G TEXT, H TEXT, I TEXT, J TEXT, K TEXT, L TEXT, M TEXT, N TEXT, O TEXT, P TEXT, Q TEXT, R TEXT, S TEXT, T TEXT, U TEXT, V TEXT, W TEXT, X TEXT, Y TEXT, Z TEXT, No TEXT)')

wb = load_workbook(filename = 'Movies.xlsm') #open workbook
sheet = wb['List'] #select sheet

par = []

print ("Writing ...")

#reverse selecting for alphabetic order and discipline
#select each row in excel and add to database by tuple
for row in range(1000,0,-1): #select rows
    for col in range(65, 91): #select columns
        cell_value = str(sheet['{0}{1}'.format(chr(col) ,row)].value)
        if cell_value == "None": cell_value = '' #change None cell to '' for database
        par.append(cell_value) #add to end
    cell_value = str(sheet['AA{0}'.format(row)].value) #for number column ( last )
    par.append(cell_value)
    tup = tuple(par) #change list to tuple
    cur.execute('insert into List VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',tup) #add to database
    par = [] #empty list

conn.commit() #save database
conn.close() #close database
print ("Done !")