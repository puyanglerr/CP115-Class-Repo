correct_password = "python123"
attempts_used = 0
while attempts_used < 3:
    attempts_used += 1
    password = input()

    if password == correct_password:
        login_successful = True
        break
    login_successful = False

print(login_successful)
print(attempts_used)