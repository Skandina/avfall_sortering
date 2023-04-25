import mysql.connector

def how_to_sort(waste):
#    if waste == None:
    conn = mysql.connector.connect(
            user='adminuser', 
            password='91Djemals', 
            host='localhost', 
            database='sorting')
    if conn.is_connected():
        db_info = conn.get_server_info()
        print('mysql Version : ', db_info)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT waste_sort FROM how_to_sort WHERE waste_name = '{waste}'""")
        rows = cursor.fetchone()
    return (rows[0])

