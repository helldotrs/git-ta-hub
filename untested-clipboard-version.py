import subprocess
import os
import sys
import platform

def run_command(command, shell=True, capture_output=True):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=shell, capture_output=capture_output, text=True)
    if result.returncode != 0 and result.stderr:
        print(f"Error: {result.stderr}")
    return result

def copy_to_clipboard(text):
    """Copy text to clipboard in a cross-platform way."""
    system = platform.system()
    try:
        if system == 'Windows':
            # Windows approach
            subprocess.run('clip', input=text.encode('utf-8'), check=True)
            return True
        elif system == 'Darwin':
            # macOS approach
            subprocess.run('pbcopy', input=text.encode('utf-8'), check=True)
            return True
        elif system == 'Linux':
            # Try xclip first, then xsel for Linux
            try:
                subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode('utf-8'), check=True)
                return True
            except FileNotFoundError:
                try:
                    subprocess.run(['xsel', '--clipboard', '--input'], input=text.encode('utf-8'), check=True)
                    return True
                except FileNotFoundError:
                    return False
        return False
    except Exception as e:
        print(f"Clipboard operation failed: {e}")
        return False

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
    
    # Display the public key and copy to clipboard
    print("\nYour SSH public key:")
    public_key_path = os.path.expanduser("~/.ssh/id_rsa.pub")
    if os.path.exists(public_key_path):
        with open(public_key_path, 'r') as f:
            public_key = f.read().strip()
            print("\n" + public_key + "\n")
        
        # Try to copy to clipboard
        if copy_to_clipboard(public_key):
            print("✅ SSH key has been automatically copied to your clipboard!")
        else:
            print("⚠️  Automatic clipboard copy not available. Please manually copy the key above.")
            
            # Offer manual copy option with input prompt
            copy_prompt = input("Press Enter after you've copied the key manually...")
        
        print("\nInstructions:")
        print("1. Go to: https://github.com/settings/ssh/new")
        print("2. Give it a title, paste the key, and click 'Add SSH key'")
        print("3. Complete any MFA verification if prompted")
        
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
