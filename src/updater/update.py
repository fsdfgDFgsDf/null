import subprocess
import sys
import os

def run_git_pull():
    """Run 'git pull origin main' and check if updates were applied."""
    try:
        result = subprocess.run(
            ['git', 'pull', 'origin', 'main'],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout.lower()
        
        # Check if there were actual changes
        if "already up to date" in output:
            print("No updates available.")
            return 0
        else:
            print("Updates applied successfully.")
            return 1
    except subprocess.CalledProcessError as e:
        print(f"Git pull failed: {e}")
        return 2
    except FileNotFoundError:
        print("Git not found. Is this a Git repo?")
        return 2

if __name__ == "__main__":
    if os.path.exists('.git'):
        status = run_git_pull()
        sys.exit(status)
    else:
        print("Not a Git repository.")
        sys.exit(2)