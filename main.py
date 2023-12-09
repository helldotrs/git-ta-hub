username    = input("username:")
useremail   = input("useremail:")
passphrase  = input

print("run:git config --global user.name \"" + username + "\"\n
git config --global user.email \"" + useremail + "\"")

#FIXME: autorun
print("run: ssh-keygen -t rsa -b 4096 -C \"" + useremail + "\"")
print("hit:enter")
print("optional, type passphrase, enter, passphrase")
print("hit [enter]")
print("run:cat ~/.ssh/id_rsa.pub")
print("copy output")
print("go  to: https://github.com/settings/ssh/new")
print("give name, paste, add SSH key")
print("MFA")
print("run to test: ssh -T git@github.com")

#git clone git@github.com:your-username/your-repository.git




#end of program:
print(output)
exit()
