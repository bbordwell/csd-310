#Bordwell, Hadi, Morales, Songcuan Module 10.3 assignment (milestone #3)
#Generates some reports for the winery.

import mysql.connector
from mysql.connector import errorcode
from mysql.connector import connection


config = {
    'user': 'wine_user',
    'password' : 'MySQL8IsGreat!',
    'host': '127.0.0.1',
    'database': 'wine',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

def printTable(results,cursor):
    """Prints an inputed table in MySQL format."""
    #Modified version of https://stackoverflow.com/a/20383011
    widths = []
    columns = []
    tavnit = '|'
    separator = '+' 

    for column,cd in enumerate(cursor.description):
        width = len(cd[0])
        for rowNumber in range(len(response)):
            if len(str(response[rowNumber][column])) > width:
                width = len(str(response[rowNumber][column]))
        widths.append(width)
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator)
    print()


for number, name in [(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]:
    #print(f"The on time performance for {name}:")
    cursor.execute(f"""
    SELECT t1.supplier_name, t1.orders, t2.on_time, t3.late, t4.late_days/t1.orders AS avg_days_late FROM

        #Temp tble to compute total number of orders
        (SELECT supplier_name, COUNT(*) AS orders FROM supplier_orders WHERE MONTH(order_date) = {number} GROUP BY supplier_name) t1
    
    LEFT JOIN
    #Temp table to compute number of on time orders
        (SELECT supplier_name, COUNT(*) on_time FROM supplier_orders WHERE DATEDIFF(deliver_date,order_date) < 15 AND MONTH(order_date) = {number} GROUP BY supplier_name) t2
    ON (t1.supplier_name = t2.supplier_name)

    LEFT JOIN
    #Temp table to compute the number of late orders
        (SELECT supplier_name, COUNT(*) late FROM supplier_orders WHERE DATEDIFF(deliver_date,order_date) > 14 AND MONTH(order_date) = {number} GROUP BY supplier_name) t3
    ON (t3.supplier_name = t1.supplier_name)

    LEFT JOIN
    #Temp table to compute the average number of days late for each supplier
        (SELECT supplier_name, SUM(days_late) AS late_days FROM 
            (SELECT supplier_name, order_date, deliver_date,
            CASE
            WHEN DATEDIFF(deliver_date, order_date) < 15 THEN 0
            ELSE DATEDIFF(deliver_date, order_date) - 14
            END AS days_late
            FROM supplier_orders WHERE MONTH(order_date) = {number}) temp1
        GROUP BY supplier_name) t4
    ON t4.supplier_name = t1.supplier_name
    ;
    """)
    response = cursor.fetchall()
    if response:
        print(f"On time performance for {name}: ")
        printTable(response,cursor)
    else:
        print(f"There are no orders for {name}")
        print()


cursor.execute("""
SELECT employees.ID, first_name, last_name, Q1.hours AS 'Q1 Hours', Q2.hours AS 'Q2 Hours', Q3.hours AS 'Q3 Hours', Q4.hours AS 'Q4 Hours'
FROM employees 
  LEFT JOIN
    (SELECT ID, SUM(worked)*8 AS hours
    FROM time_clock
    WHERE MONTH(date_worked) = 1 OR MONTH(date_worked) = 2 OR MONTH(date_worked) = 3
    GROUP BY ID) Q1
  ON employees.ID = Q1.ID
  LEFT JOIN
    (SELECT ID, SUM(worked)*8 AS hours
    FROM time_clock
    WHERE MONTH(date_worked) = 4 OR MONTH(date_worked) = 5 OR MONTH(date_worked) = 6
    GROUP BY ID) Q2
  ON employees.ID = Q2.ID
  LEFT JOIN
    (SELECT ID, SUM(worked)*8 AS hours
    FROM time_clock
    WHERE MONTH(date_worked) = 7 OR MONTH(date_worked) = 8 OR MONTH(date_worked) = 9
    GROUP BY ID) Q3
  ON employees.ID = Q3.ID
  LEFT JOIN
    (SELECT ID, SUM(worked)*8 AS hours
    FROM time_clock
    WHERE MONTH(date_worked) = 10 OR MONTH(date_worked) = 11 OR MONTH(date_worked) = 12
    GROUP BY ID) Q4
  ON employees.ID = Q4.ID
GROUP BY employees.ID;
""")
response = cursor.fetchall()
print("Quarterly hours worked:")
printTable(response,cursor)


cursor.execute("""
SELECT distributor_orders.distributor_name,
totals.merlot,
totals.cabernet,
totals.chablis,
totals.chardonnay,
totals.merlot + totals.cabernet + totals.chablis + totals.chardonnay AS total
FROM distributor_orders
LEFT JOIN
  (SELECT distributor_name, 
  SUM(merlot_qty) AS merlot, 
  SUM(cabernet_qty) AS cabernet, 
  SUM(chablis_qty) AS chablis, 
  SUM(chardonnay_qty) AS chardonnay
  FROM distributor_orders
  GROUP BY distributor_name) totals
ON totals.distributor_name = distributor_orders.distributor_name;
""")
response = cursor.fetchall()
print("Total wine Sales by distributor:")
printTable(response,cursor)
