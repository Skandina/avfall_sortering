import mysql.connector

def how_to_sort(waste):
    conn = mysql.connector.connect(
            user='adminuser', 
            password='91Djemals', 
            host='localhost', 
            database='sorting')
    if conn.is_connected():
        db_info = conn.get_server_info()
        print('mysql Version : ', db_info)
        cursor = conn.cursor()
        print("A")
        cursor.execute("SELECT waste_text FROM how_to_sort WHERE waste_name = 'bikarbonat'")
        print("B")
        rows = cursor.fetchone()
    return print(rows[0])

waste = 'bikarbonat'
how_to_sort(waste)
