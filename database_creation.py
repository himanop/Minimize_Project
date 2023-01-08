import sqlite3

def creating_database_user_table(db_name):
    """This function creates Minimize user information table if they do not exist"""

    db_connection = None
    try:
        db_connection = sqlite3.connect(db_name)
        print(db_connection)
        db_cursor = db_connection.cursor()
        print(db_cursor)
        try:
            db_cursor.execute('''CREATE TABLE IF NOT EXISTS User_Info(
                                email TEXT PRIMARY KEY,
                                f_name TEXT,
                                l_name TEXT,
                                password TEXT,
                                IsUserVerified INTEGER,
                                 verify_email_code INTEGER);''')
        except sqlite3.Error as table_error:
            print(f'Table creation error {table_error}')

    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')

    finally:
        if db_connection:
            db_connection.commit()
            db_cursor.close()