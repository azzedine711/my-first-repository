the_user_age = int(input("what is your age: "))
the_year_of_birth = int(input("what year you were born in: "))

if the_user_age > 18:
    print("your old")
elif the_user_age < 18 or the_user_age == 18:
    print("you're young")
the_current_year = int(input('what year are we in: '))
the_calculated_age = the_current_year - the_year_of_birth
if the_calculated_age == the_user_age:
    print("you were right")
else:
    print( 'NO!,you are ' + str(the_calculated_age))