username    = input("username:")
useremail   = input("useremail:")
passphrase  = input("ssh passphrase (NOT YOUR GH PW):")
if input("again:") != passphrase:
    exit("does not match, exiting")

print(f'run:git config --global user.name "{username}" && git config --global user.email "{useremail}"')

#FIXME: autorun
print(f'run: ssh-keygen -t rsa -b 4096 -C "{useremail}"')
print("hit:enter")
print("optional, type passphrase, enter, passphrase")
print("hit [enter]")
print("run:cat ~/.ssh/id_rsa.pub")
print("copy output")
print("go  to: https://github.com/settings/ssh/new")
print("give title, paste, add SSH key") #FIXME: ask for title?
print("MFA")
print("run to test: ssh -T git@github.com")

#git clone git@github.com:your-username/your-repository.git

