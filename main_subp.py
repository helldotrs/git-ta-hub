import subprocess

#note: error handling has been intentionally left out. as this code is run locally and you should know how to answer a simple prompt, it would just be bloat.

def get_input(prompt, confirm = False):
    user_input = input(f"{prompt}: ")

    if confirm:
        if input("Confirm: " != user_input:
            exit("confirmation failed. exiting.")

    return user_input

def run_cmd(cmd):
    subprocess.run(cmd, shell = True)

gh_name      = get_input("enter gh username: ")
gh_email     = get_input("ente gh email: ")
local_passwd = get_input("enter password/-phrase (NOT YOUR GH LOGIN: ")

run_cmd(f'git config --global user.name  "{gh_name}"' )
run_cmd(f'git config --gloval user.email "{gh_email}"')

run_cmd(f'ssh-keygen -t rsa -b 4096 -C "{gh_name}" -N "{local_passwd}" -f ~/.ssh/id_rsa')

print("output:\n\n")

run_cmd(f'cat ~/.ssh/id_rsa.pub')

print("""\n 
-copy output above\n
-open https://github.com/settings/ssh/new\n 
-output goes under 'key', you'll figure the rest out\n
-test by running 'ssh -T git@github.com' in terminal\n
""")

exit('done. exiting.')

#fix me:add "ssh -T git@github.com" test
#fix me:research copying output automatically
