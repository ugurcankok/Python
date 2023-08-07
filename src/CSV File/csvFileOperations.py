import csvFileOperations

def add_user(first_name, last_name):
    with open("users.csv","a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first_name,last_name])

print(add_user("ugur","can"))

def get_users():
    with open("users.csv") as file:
        csv_reader = csv.DictReader(file) # return format is dictionary, you can use delimiter (ex. delimiter = "|")
        for user in csv_reader:
            print(f'{user["FirstName"]} {user["LastName"]}')

get_users()

def find_user(first_name,last_name):
    with open("users.csv") as file:
        csv_reader = csv.reader(file) # return format is list
        for (index,row) in enumerate(csv_reader):
            if (row[0]==first_name) and (row[1]==last_name):
                return index
        return -1

find_user("ugur","can")

def update_users(f_name,l_name,new_first,new_last):
    with open('users.csv') as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)

    count = 0
    with open('users.csv','w') as file:
        csv_writer = csv.writer(file)
        for user in users:
            if user[0] == f_name and user[1] == l_name:
                csv_writer.writerow([new_first,new_last])
                count += 1
            else:
                csv_writer.writerow(user)

    return f"{count} record updated."

update_users('ugur','can','ugurcan','kok')
def delete_users(f_name,l_name):
    with open('users.csv') as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)

    count = 0
    with open('users.csv','w') as file:
        csv_writer = csv.writer(file)
        for user in users:
            if user[0] == f_name and user[1] == l_name:
                count += 1
            else:
                csv_writer.writerow(user)

    return f"{count} record deleted."

delete_users('ugurcan','kok')
