
import mysql.connector
from contextlib import contextmanager

from logging_setup import setup_logger

logger = setup_logger('db_helper','server.log')



@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_database_password',
        database='expense_manager'
    )
    if connection.is_connected():
        pass
        # print('connection succesful')
    else:
        print('Failed in connecting to a database')
    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute('select * from expenses')
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

    # cursor.close()
    # connection.close()

def fetch_expense_for_date(expense_date):
    logger.info(f'fetch_expense_for_date called with date {expense_date}')
    with get_db_cursor() as cursor:
        cursor.execute('select * from expenses where expense_date = %s', (expense_date,))
        expenses = cursor.fetchall()
        return expenses

    # cursor.close()
    # connection.close()

def insert_expense(expense_date,amount,category,notes):
    logger.info(f'insert_expense called with date {expense_date}, amount : {amount}, category : {category}')
    with get_db_cursor(commit=True) as cursor:
        cursor.execute('insert into expenses(expense_date,amount,category,notes) values (%s, %s,%s, %s)', (expense_date,amount,category,notes))

def delete_expense_for_date(expense_date):
    logger.info(f'delete_expense_for_date called with date {expense_date}')
    with get_db_cursor(commit = True) as cursor:
        cursor.execute('delete from expenses where expense_date = %s', (expense_date,))

def fetch_expense_summary(start_date, end_date):
    logger.info(f'fetch_expense_summary with startdate : {start_date} and enddate : {end_date} ')
    with get_db_cursor() as cursor:
        cursor.execute(''' select category, sum(amount) as total  from expenses 
                            where expense_date between %s and %s
                                    group by category;''', (start_date, end_date))

        data = cursor.fetchall()
        return data

if __name__ == '__main__':
    # insert_expense('2026-01-20', 500,'Food', 'pizza')
    # delete_expense_for_date('2026-01-20')
    data =  fetch_expense_for_date("2024-08-15")
    print(data)
    # summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    # for items in summary:
    #     print(items)
