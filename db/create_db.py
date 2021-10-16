import sqlite3


sql = "CREATE TABLE customers "\
        +"(id INTEGER PRIMARY KEY AUTOINCREMENT,"\
        +"first_name TEXT NOT NULL,"\
        +"last_name TEXT NOT NULL,"\
        +"zipcode INT NOT NULL,"\
        +"price_paid REAL NOT NULL);"


def main():
    conn = sqlite3.connect('database.sqlite')
    
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

        print("Opened database successfully")
    except Exception as e:
        print(f'Failed the creation databaee operation: {e}')
    finally:
        conn.close()

if __name__ == '__main__':
    main()
