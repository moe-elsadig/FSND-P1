# FSND-P1

Udacity's Full-Stack Nanodegree
Log Analysis Project

The following tool is an internal reporting tool, for newspaper site. The site's database contains articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information the following code will be used to answer some key questions.

For this project a Virtual Machime (VM) is provided setup with Vagrant which contains the PostgreSQL database and support software required for the project.

To bring up the virtual machine online use `vagrant up` and then log into it with `vagrant ssh`

You can download the (database data)[https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip]. Place this into the Vagrant shared directory, and to load the data `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`

- `psql` - the PostgreSQL command line program.
- `-d news` - connect to the database named news which has been set up for you.
-  `-f newsdata.sql` - run the SQL statements in the file newsdata.sql

Running the command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.



Getting an error?
If this command gives an error message, such as —
psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused
— this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added. To continue, download the virtual machine configuration into a fresh new directory and start it from there.

Explore the data
Once you have the data loaded into your database, connect to your database using psql -d news and explore the tables using the \dt and `\d` table commands and select statements.

`\dt` — display tables — lists the tables that are available in the database.
`\d` table — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

The `authors` table includes information about the authors of articles.
The `articles` table includes the articles themselves.
The `log` table includes one entry for each time a user has accessed the site.
As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.

Connecting from your code
The database that you're working with in this project is running PostgreSQL, like the forum database that you worked with in the course. So in your code, you'll want to use the psycopg2 Python module to connect to it, for instance:

`db = psycopg2.connect("dbname=news")`




How to Use:

**You must first obtain the newsdata.sql database file from [UDACITY's FSND Project 1 VM](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and place it in the `/vagrant/` directory*

To run the project navigate to the vagrant directory in a terminal window and run the following command:

        python newsdb.py


The output will be an answer to the following questions

Question 1: `What are the most popular three articles?`


Question 2: `Who are the most popular article authors?`


Question 3: `On which days did more than 1% of requests lead to errors?`
