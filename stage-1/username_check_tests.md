#   Input                   Expected output                 Actual Output               Pass?
1. " "                  no space in username            no space in username            Yes
2. my user name         no space in username            no space in username            Yes
3. use                  valid                           valid                           Yes
4. myusernamemyuser     must be between 3 and 15 char   must be between 3 and 15 char   Yes
5. 1user                cannot start with digit         cannot start with digit         Yes        
6.  Jude                valid                           valid                           Yes
7. Jude                 valid                           valid                           Yes
8. my                   must be between 3 and 15 char   must be between 3 and 15 char   Yes
9. " Jude "             no space in username            no space in username            Yes
10.                     cannot be empty                 cannot be empty                 Yes
11. myusernamemyuse     valid                           valid                           Yes