try:
    import random
    import string

    password = ""
    my_list = []

    #Asks the user for the length of their password or, if it is less than 8, will set password to 8 characters 
    how_long = int(input("How long? "))
    if how_long < 8:
        how_long = 8

    #Input questions
    user_special_charcters = int(input("How many special characters do you want? "))
    user_uppercase = int(input("How many uppercase letters do you want? "))
    user_lowercase = int(input("How many lowercase letters do you want? "))
    user_numbers = int(input("How many numbers do you want? "))
    if user_special_charcters + user_lowercase + user_uppercase + user_numbers != how_long:
        print("Does not match your desired length!!!")


    #Defines all the possible characters we can use in the password
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "123456789"
    special_characters = "!@#$%^&*()?~+_-/\,."

    #Implements the algorithm in which we generate a random password
    for i in range(user_special_charcters):
        my_list.append(special_characters[random.randint(0, 19)])
    for x in range(user_uppercase):
        my_list.append(upper_case[random.randint(0, 26)])
    for y in range(user_lowercase):
        my_list.append(lower_case[random.randint(0, 26)])
    for z in range(user_numbers):
        my_list.append(nums[random.randint(0, 9)])

    random.shuffle(my_list)

    for p in my_list:
        password += p

    print(f"Your new password is...{password}...")

except IndexError:
    print("Dude, you crashed my program!!!")
