import psycopg2

db = psycopg2.connect(user = "username",
                      password = "password",
                      host = "localhost",
                      port = "port number",
                      database = "database name")

post_cursor = db.cursor()

create_db = """ CREATE TABLE names( id SERIAL PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL ); """

insert_record = """ INSERT INTO names(first_name, last_name) VALUES ('ugur', 'kok'); """

select_record = """ SELECT * FROM names; """

post_cursor.execute(select_record)

list_records = post_cursor.fetchall()

for list_record in list_records:
    print(list_record)

update_record = """ UPDATE names SET first_name = 'ugurcan' where id = 1; """

delete_record = """ DELETE FROM names where first_name = 'ugur' """

post_cursor.execute(delete_record)
db.commit()
