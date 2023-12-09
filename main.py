output    = ""
username  = input("username:")
useremail = input("useremail:")

output += "git config --global user.name \"" + username + "\"\n"
output += "git config --global user.email \"" + useremail + "\"\n"


#end of program:
print(output)
exit()
