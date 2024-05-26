print ("Warning: any input will be kept unencryted in ram while this software is running.")
print (" ")

username    = input("username:")
useremail   = input("useremail:")

print(f'run:\ngit config --global user.name "{username}" && git config --global user.email "{useremail}" && ssh-keygen -t rsa -b 4096 -C "{useremail}"')

print(" ")
print("hit:enter")
print("optional, type passphrase, enter, passphrase")
print("hit [enter]")

print("run:\ncat ~/.ssh/id_rsa.pub")
print(" ")
print("copy output")
print("go  to: https://github.com/settings/ssh/new")
print("give title, paste, add SSH key") 
print("MFA")
print("run to test:\nssh -T git@github.com")
print("type \"yes\" and hit [enter]")
