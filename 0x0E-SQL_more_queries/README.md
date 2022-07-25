# 0x0E. SQL - More queries

### SHOW GRANTS:
This statement lists the GRANT statements.
GRANT is intended to add privileges to users.
It also has the ability to create users and change their passwords.

### CREATE USER:
This will create the user, if we add IF NOT EXISTS, it will create it if the user we will provide after the above named does not exist.

### IDENTIFIED:
If you use GRANT with IDENTIFIED you can change the password of the user:

When IDENTIFIED is present and has the global grant privilege (GRANT OPTION), any password specified becomes the new password for the account, even if the account exists and already has a password. Without IDENTIFY, the account password remains unchanged.


## In summary use CREATE to create a user and use GRANT to add privileges

## FLUSH:
You can use the FLUSH command if you want to clear some of the internal cache used by MySQL. Although it is not always necessary to use, it is recommended to use it to avoid certain errors.
Using statements such as INSERT, UPDATE or DELETE, your changes have no effect on the privilege check until you restart the server or instruct it to reload the tables.

