import subprocess

def run_subprocess(execute_this):
    try: 
        # shell=True for single single string
        subprocess.run(execute_this, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f'error: {e}')

print ("Warning: any input will be kept unencryted in ram while this software is running.")
print (" ")

username     = input("username:")
useremail    = input("useremail:")

run_subprocess(f'git config --global user.name "{username}" && git config --global user.email "{useremail}" && ssh-keygen -t rsa -b 4096 -C "{useremail}"')

copy
cat ~/.ssh/id_rsa.pub")
print(" ")
print("copy output")
print("go  to: https://github.com/settings/ssh/new")
print("give title, paste, add SSH key") #FIXME: ask for title?
print("MFA")

_ = input("setup complete, hit enter to test.")
print("run to test:\nssh -T git@github.com")
print("type \"yes\" and hit [enter]")

#git clone git@github.com:your-username/your-repository.git

