import duolingo

user = duolingo.Duolingo('user ID', 'password goes here')

# prints user information

print(user.get_user_info())
print('******************************************************')

# prints user settings

print(user.get_settings())
print('******************************************************')

# prints languages learning 

print(user.get_languages())
print('******************************************************')

# prints user streak info

print(user.get_streak_info())
print('******************************************************')
