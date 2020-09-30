def checker_password(password):
   str_check1 = "password"
   str_check2 = "Password"
   spcl_char = ('!@#$%^&*')
   if len(password) < 8: 
        print('Password is invalid. The length should be grater than 8')
   elif len(password) > 20: 
        print('Password is invalid. The length should be not be greater than 30') 
   elif str_check1 in password or str_check2 in password:
        print('Password is invalid.This should not consists of word passsword')
   elif not any(char in spcl_char for char in password):
        print('Password is invalid.This consists of at least one special character')
   elif not any(char.isdigit() for char in password):
        print('Password is invalid.This consists of at least one number')
   elif not any(char.isupper() for char in password):
        print('Password is invalid.This consists iof at least one UPPERCASE')
   else:
       print('Password is valid')
checker_password("passwd'")