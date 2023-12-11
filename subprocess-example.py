import subprocess

# Replace the following with your actual Bash command
bash_command = "ls -l"

# Run the Bash command from within Python
result = subprocess.run(bash_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Print the result
print("Output:")
print(result.stdout)

# Print any errors (if any)
print("Errors:")
print(result.stderr)
