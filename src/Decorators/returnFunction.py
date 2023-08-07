def power_number(number):
    def inner_function(power):
        return number ** power

    return inner_function

two = power_number(2)
three = power_number(3)

print(two(3))
print(three(4))

def authority(page):
    def inner_function(role):
        if role == 'Admin':
            return f"{role} role can reach {page}."
        else:
            return f"{role} role cannot reach {page}."

    return inner_function

user1 = authority("Product Edit")

print(user1('Admin'))
