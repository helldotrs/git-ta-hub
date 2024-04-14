import subprocess

def get_input(prompt, confirm = False):
    user_input = input(f"{prompt}: ")

    if confirm:
        if input("Confirm: " != user_input:
            exit("confirmation failed. exiting.")

    return user_input
