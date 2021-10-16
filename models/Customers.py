import sqlite3


'''Responsible for 'Customers' database access'''
class Customers:

    def __init__(self):
        self.conn = sqlite3.connect('database.sqlite')
        self.c = self.conn.cursor()
        print("Opened database successfully")    
    
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
        self.c.execute("SELECT * FROM customers")
        return self.c.fetchall()
    
    def get(self, id):
        '''Returns the record with a specific id'''
        self.c.execute(f"SELECT * FROM customers WHERE id = {id}" )
        return self.c.fetchone()

    def _execute_write_query(self, sql):
        response = 0
        try:
            self.c.execute(sql)
            self.conn.commit()
            response = self.c.rowcount
        except Exception as e:
            print(f'Failed the write operation: {e}')
        finally:
            self.conn.close()

        return response
