Linux Commands and Shell Scripting

This is the final project from Hands-on Introduction to Linux Commands and Shell Scripting (https://www.coursera.org/learn/hands-on-introduction-to-linux-commands-and-shell-scripting?specialization=ibm-data-engineer). 

In this scenario, a lead Linux developer at the top-tech company ABC International Inc has been tasked with creating a script called backup.sh which runs every day and automatically backs up any encrypted password files that have been updated in the past 24 hours.

Task 1: Set two variables equal to the values of the first and second command line arguments, as follows:
        1. Set targetDirectory to the first command line argument,
        2. Set destinationDirectory to the second command line argument.
Task 2: Display the values of the two command line arguments in the terminal.        
Task 3: Define a variable called currentTS as the current timestamp, expressed in seconds.
Task 4: Define a variable called backupFileName to store the name of the archived and compressed backup file that the script will create.
Task 5: Define a variable called origAbsPath with the absolute path of the current directory as the variable's value.
Task 6: Define a variable called destAbsPath whose value equals the absolute path of the destination directory.
Task 7: Change directories from the current working directory to the target directory targetDirectory.
Task 8: Find files that have been updated within the past 24 hours. This means to find all files whose last-modified date was 24 hours ago or less.
Task 9: Within the $() expression inside the for loop, write a command that will return all files and directories in the current folder.
Task 10: Inside the for loop, Check whether the $file was modified within the last 24 hours.
Task 11: In the if-then statement, add the $file that was updated in the past 24-hours to the toBackup array.
Task 12: After the for loop, compress and archive the files, using the $toBackup array of filenames, to a file with the name backupFileName.
Task 13: Now the file $backupFileName is created in the current working directory.
