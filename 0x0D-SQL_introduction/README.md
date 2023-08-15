**SQL - Learning Objectives**

This project will help you understand the fundamental concepts of databases and SQL (Structured Query Language). Upon completion, you'll be able to explain the following concepts without the need for external references:

**General**
- The definition of a database and its importance in software development.
- What a relational database is and how it organizes data.
- The acronym SQL stands for "Structured Query Language."
- An understanding of MySQL as a popular open-source relational database management system.
- How to create a database in MySQL to store and manage data.
- Differentiating between Data Definition Language (DDL) and Data Manipulation Language (DML).
- The ability to use DDL to CREATE or ALTER database tables.
- The capability to SELECT data from a database table using SQL queries.
- How to INSERT, UPDATE, or DELETE data in a database table.
- The concept of subqueries and how they can be used to retrieve specific data.
- Utilizing MySQL functions to perform calculations, transformations, and comparisons.

**Copyright - Plagiarism**
- The necessity to independently come up with solutions to fulfill project tasks.
- The prohibition of copying and pasting work from other sources.
- The inadmissibility of publishing any part of the project's content.
- The severe consequences of plagiarism, including expulsion from the program.

**Requirements**
- Using allowed editors such as vi, vim, or emacs.
- Ensuring your SQL scripts are compatible with MySQL 8.0 (version 8.0.25).
- Each script should conclude with a new line.
- Including a comment immediately before each SQL query to clarify its purpose.
- Starting each file with a descriptive comment outlining the task being solved.
- Writing SQL keywords in uppercase for clarity and consistency.
- Mandatory inclusion of a README.md file at the root of the project folder.
- The project's file lengths will be measured using the "wc" command.

**More Info**
- Clarifying comments to explain each SQL script's purpose.
- Example of a comment structure in a SQL file:

```sql
-- Retrieve the 3 most recent students from Batch ID=3
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

**Setting Up MySQL 8.0 on Ubuntu 20.04 LTS**
- Update your package repository using:
  ```bash
  sudo apt update
  ```
- Install MySQL 8.0:
  ```bash
  sudo apt install mysql-server
  ```
- Verify the MySQL version:
  ```bash
  mysql --version
  ```

**Connecting to MySQL Server**
- Start the MySQL interactive monitor:
  ```bash
  sudo mysql
  ```
- Connect to the MySQL server using the username "root":
  ```sql
  mysql -u root -p
  ```
- To exit the MySQL monitor, type:
  ```sql
  quit
  ```

**Using "container-on-demand" for MySQL**
- In the container, use the credentials "root/root".
- Ask for an Ubuntu 20.04 container, connect via SSH, or use the Web terminal.
- Ensure to start MySQL within the container:
  ```bash
  service mysql start
  ```

**Note:** The provided instructions and objectives are for educational purposes. They guide you in building a strong foundation in SQL and databases.
