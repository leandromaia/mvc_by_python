import sqlite3


'''Responsible for 'Customers' database access'''
class Customers:
    
    def add(self, fields):
        '''Adds a customer in database'''       
        sql = "INSERT INTO customers (first_name, last_name, zipcode, price_paid)" \
            + f"VALUES ('{fields[0].get()}', '{fields[1].get()}', {fields[2].get()}, {fields[3].get()})"

        return self._execute_write_query(sql)
    
    def update(self, fields):
        '''Updates a record in database'''
        sql = f"UPDATE customers SET "\
                +f"first_name = '{fields[1].get()}',"\
                    +f"last_name = '{fields[2].get()}',"\
                        +f" zipcode = {fields[3].get()},"\
                            +f" price_paid = {fields[4].get()}"\
                                +f" WHERE id = {fields[0].get()}"

        return self._execute_write_query(sql)
    
    def delete(self, id_customer):
        '''Delete a customer in database'''
        sql = f"DELETE FROM customers WHERE id = {id_customer}"

        return self._execute_write_query(sql)

    def getAll(self):
        '''Returns list of all customers records in database'''
        self._connect_database()
        sql = "SELECT * FROM customers"

        return self._execute_read_query(sql, self.cursor.fetchall)
    
    def get(self, id):
        '''Returns the record with a specific id'''
        self._connect_database()
        sql = f"SELECT * FROM customers WHERE id = {id}"

        return self._execute_read_query(sql, self.cursor.fetchone)

    def _connect_database(self):
        self.conn = sqlite3.connect('database.sqlite')
        self.cursor = self.conn.cursor()
        print("Database created and Successfully Connected to SQLite")  

    def _execute_write_query(self, sql):
        self._connect_database()
        response = 0
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            response = self.cursor.rowcount

            self.cursor.close()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if self.conn:
                self.conn.close()
                print("The SQLite connection is closed")

        return response

    def _execute_read_query(self, sql, operation):
        record = None
        try:
            self.cursor.execute(sql)
            record = operation()

            self.cursor.close()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if self.conn:
                self.conn.close()
                print("The SQLite connection is closed")

        return record
