import subprocess
import os
import time
import getpass
import sys

def run_command(command, shell=True, capture_output=True):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=shell, capture_output=capture_output, text=True)
    if result.returncode != 0 and result.stderr:
        print(f"Error: {result.stderr}")
    return result

def main():
    print("Warning: any input will be kept unencrypted in RAM while this software is running.")
    print("")
    
    # Get user inputs
    username = input("Username: ")
    useremail = input("User email: ")
    
    # Configure git global settings
    print("\nConfiguring Git global settings...")
    run_command(f'git config --global user.name "{username}"')
    run_command(f'git config --global user.email "{useremail}"')
    
    # Generate SSH key
    print("\nGenerating SSH key...")
    ssh_dir = os.path.expanduser("~/.ssh")
    if not os.path.exists(ssh_dir):
        os.makedirs(ssh_dir)
    
    # Use subprocess.Popen for interactive ssh-keygen
    print("You'll be prompted for a passphrase (optional but recommended).")
    ssh_keygen_process = subprocess.Popen(
        f'ssh-keygen -t rsa -b 4096 -C "{useremail}"',
        shell=True,
        stdin=sys.stdin,
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    ssh_keygen_process.communicate()
    
    # Display the public key
    print("\nYour SSH public key:")
    public_key_path = os.path.expanduser("~/.ssh/id_rsa.pub")
    if os.path.exists(public_key_path):
        with open(public_key_path, 'r') as f:
            public_key = f.read().strip()
            print("\n" + public_key + "\n")
        
        print("Instructions:")
        print("1. Copy the SSH key above")
        print("2. Go to: https://github.com/settings/ssh/new")
        print("3. Give it a title, paste the key, and click 'Add SSH key'")
        print("4. Complete any MFA verification if prompted")
        
        # Test the SSH connection
        input("\nPress Enter when you've added the key to GitHub to test the connection...")
        print("\nTesting GitHub SSH connection...")
        print("If prompted with 'Are you sure you want to continue connecting?', type 'yes'")
        
        ssh_test_process = subprocess.Popen(
            'ssh -T git@github.com',
            shell=True,
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        ssh_test_process.communicate()
        
        print("\nSetup complete!")
    else:
        print(f"Error: Could not find SSH public key at {public_key_path}")

if __name__ == "__main__":
    main()
