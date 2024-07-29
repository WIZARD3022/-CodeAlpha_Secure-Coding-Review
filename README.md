# Secure Coding Review
## Step by step Procedure: -
1. Open termianl by pressing 'window + R' and then write 'cmd' and click 'Enter'.
2. write code in terminal.
   ```
   pip install bandit
   ```
4. Now open browser and search for python download.
5. Here is the direct lind for python download [Download link](https://www.python.org/downloads/) and add the path of python bin in environment variables.
6. Now to to check every thing is ok write this on terminal.
   ```
   bandit --version
   ```
   if it shows the bandit and python both file versions then every thing is ok if not check last few steps are performed properly.
7. Now your are ready with installed bandit and can check any python file security by command
   ```
   bandit <file_name.py>
   ```
   and if your not in the directory in which the file is saved then make sure to change directory by command
   ```
   cd C:/path_to_file/file_stored_directory
   ```
8. you can also run the file with command
   ```
   python <file_name.py>
   ```
9. Now to show the tool is working. Here I present and example of Right and Wrong code file.
10. Create a folder with name you want and open it.
11. Save the attached files in this repositry and not forgot to create .bandit.json file with content saved in it.
    ```
    {
    "include": ["B101", "B102"],
    "exclude": ["B404"]
    }
    ```
13. Now run command to check the file security.
    ```
    bandit -r -c .bandit.json Right.py
    ```
    this will give no issues found and
    ```
    bandit -r -c .bandit.json Wrong.py
    ```
    this will give issues found which means the file data has security issue code.
