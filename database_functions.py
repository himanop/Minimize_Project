import sqlite3


def user_exists(user_email, db_name):
    """This function is used when registering user account. If user exists already TRUE is returned. If not then FALSE is returned"""
    db_connection = None
    try:
        db_connection = sqlite3.connect(db_name)
        db_cursor = db_connection.cursor()
    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')

    db_cursor.execute("SELECT * FROM User_Info WHERE email = ?", (user_email,) )
    account = db_cursor.fetchone()
    if account:
        return True
    else:
        return False

# def insert_new_user()