#!/bin/python3

import sys
import os
import sqlite3

def main():
    conn = sqlite3.connect('SAMPLE.db')
    cursor = conn.cursor()

    cursor.execute("drop table if exists ITEMS")
    
    sql_statement = '''CREATE TABLE ITEMS
    (item_id integer not null, item_name varchar(300), 
    item_description text, item_category text, 
    quantity_in_stock integer)'''
    
    cursor.execute(sql_statement)

    items = [(101, 'Nik D300', 'Nik D300', 'DSLR Camera', 3),
             (102, 'Can 1300', 'Can 1300', 'DSLR Camera', 5),
             (103, 'gPhone 13S', 'gPhone 13S', 'Mobile', 10),
             (104, 'Mic canvas', 'Mic canvas', 'Tab', 5),
             (105, 'SnDisk 10T', 'SnDisk 10T', 'Hard Drive', 1)
             ]
  
    try:
        cursor.executemany("Insert into ITEMS values (?,?,?,?,?)", items)
        cursor.executemany("update ITEMS set quantity_in_stock = ? where item_id = ?",
                       [(4, 103),
                        (2, 101),
                        (0, 105)])
        #Add code below to delete items
        cursor.execute("delete from ITEMS where item_id = 105")
        cursor.execute("select item_id from ITEMS")
    except:
        return 'Unable to perform the transaction.'
    rowout=[]     
    for row in cursor.fetchall():
        rowout.append(row)
    return rowout    
    conn.close()

if __name__ == "__main__":
	f = open(os.environ['OUTPUT_PATH'], 'w')
	
	res = main();
	f.write(str(res) + "\n")

	f.close()