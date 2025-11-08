import os

print("Checking for updates...")
code = os.system('python updater.py')

# os.system returns (exit_code << 8) on Windows
exit_code = code >> 8 if os.name == "nt" else code

if exit_code == 0:
    print("No updates – running normally.")
elif exit_code == 1:
    print("Files updated – reloading...")
    # Optional: restart yourself
    # os.execv(sys.executable, [sys.executable] + sys.argv)
else:
    print("Updater failed – continuing anyway.")


# def exec(cmd):
    # os.system(cmd)

# def setup():
    # exec('python src/ex/title.py')
    # exec('python src/ex/size.py')

# def start():
    # exec('python src/main/main.py')

# setup()
# start()