import mysql.connector

def cursor():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root',password='123456',databe='sistema')    
        cursor = db_connection.cursor
        return cursor
    except mysql.connector.Error as error:
	    if error.errno == errorcode.ER_BAD_DB_ERROR:
		    print("Database doesn't exist")
	    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		    print("User name or password is wrong")
	    else:
		    print(error)
    else:
	    db_connection.close()