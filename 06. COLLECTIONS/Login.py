# Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is 
# different, send an error message. 
# (need to use loop while)

while True:
  dict={'login':'First'}
  a=input("Enter your login: ")
  if dict.get('login')==a:
    print("Greetings")
    break
  elif  dict.get('login')!=a:
    print("Error")
