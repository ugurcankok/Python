class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"You have {cls.active_users} people in there.."

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(',')
        return cls(first, last, age)

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} logout.."


mainUser = User("Ugurcan", "Kök", 27)
print(User.display_active_users())

ugur = User.from_string("Ugur, Can, 27")
print(ugur.first)

# {"key":"value"}
# dict.fromkeys()
