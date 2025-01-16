#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os

# Schedule Library imported
import schedule
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def read_number():
    with open('number.txt', 'r') as f:
        return int(f.read().strip())

def write_number(num):
    with open('number.txt', 'w') as f:
        f.write(str(num))

def git_commit():
    # Stage the changes
    subprocess.run(['git', 'add', 'number.txt'])
    
    # Create commit with current date
    date = datetime.now().strftime('%Y-%m-%d')
    commit_message = f"Update number: {date}"
    subprocess.run(['git', 'commit', '-m', commit_message])

def commit_changes():
    # Add all changes
    os.system("git config user.name sasikanth300789")
    os.system("git config user.email sasikanth.nagalla2683@gmail.com")
    os.system("git add .")

    # Commit with a message
    commit_message = f"commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    os.system(f'git commit -m "{commit_message}"')

    # Push changes
    os.system("git push")

def main():
    try:
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)
        #git_commit()
        commit_changes()
        
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
    #commit_changes()
    
    # Task scheduling
    # After every hour medium() is called.
    schedule.every(5).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
