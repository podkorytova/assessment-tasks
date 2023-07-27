## This repository contains solution for Automatiion Teeam Asesment which I got from your HR specialist
All code is made by standard python libraries, I hope it doesn't have some dependencies and you need just python3.11 for run all scripts

- Task1 Remove middle element, contains:
- - code_remove_middle_element.py - script with main code, you can run it without args and it ask you for data in console OR with parameter('-l', '--list', nargs='*') and put elements one by one with whitespace. 
    Example: 
        python3.11 remove-middle-element-code.py --list 9 8 7 
- - test_remove_middle_element.py - contain several tests for main code, just run it and look the result in console
---
- Task2 Find array with target element, contains:
- - code_find_array_with_target_element.py - script with main code. You can run it with parameters: "-la" - put each element of one array one by one with whitespace, "-t" target number. 
    Example:  
        python3.11 find-array-with-target-element.py -la 9 8 7 4 -la 5 4 3 2 -t 4
---
- Task3 Search members from DB, contains:
- - code_search_members_from_db_sql.py - script which creates a DB with necessary structure, generate and insert data in DB, generate SQL query according to the task and showed the result. You should just run script without any args and look at console.
- - search_members_from_db_sql.s3db - file with DB, DON'T delete this, SQLite must have it :)
