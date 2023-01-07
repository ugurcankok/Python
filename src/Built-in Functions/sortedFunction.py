# Difference between sorted and sort is that sort is changing list given but sorted just reorder the list.

number_list = [11, 2, 3, 45, 85, 8, 23]

result = sorted(number_list)

reverse_result = sorted(number_list, reverse=True)

users = [
    {"username": "ugur", "tweets": ["tweet1", "tweet2"], "email": "a@b.c"},
    {"username": "can", "tweets": ["tweet1", "tweet2", "tweet3"], "email": "a@b.c"},
    {"username": "ali", "tweets": ["tweet1"], "email": "a@b.c"}
]

user_sorted = sorted(users, key=len)

user_username_sorted = sorted(users, key=lambda user: user["username"])

user_tweet_sorted = sorted(users, key=lambda user: len(user["tweets"]), reverse=True)

print(user_tweet_sorted)
