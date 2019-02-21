# Project Name: News Website Statistics

The following tool is an internal reporting tool for a newspaper site. A database is setup using **PostgreSQL** to record data on the site's articles as well as the web server log for the site. Using that information the Python script **newsdb.py** takes advantage of the **psycopg2** library to query the data and extract some useful information to answering the following questions:

* Question 1: **What are the most popular three articles?**


* Question 2: **Who are the most popular article authors?**


* Question 3: **On which days did more than 1% of requests lead to errors?**


## Requirements

* Terminal Application
* VirtualBox
* vagrant
* Vagrant configuration file as provided by Udacity
* Python
* PostgreSQL
* pyscopg2 library


For this project a Virtual Machine (VM) is provided setup with Vagrant which contains the PostgreSQL database and support software required for the project.

### Use a terminal

You'll be using a Unix-style terminal on your computer for this project. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows you can use the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from [git-scm.com](https://git-scm.com/downloads).

### Install VirtualBox

VirtualBox is the software that actually runs the virtual machine. You can [download it from virtualbox.org, here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

### Install Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

If Vagrant is successfully installed, you will be able to run `vagrant --version` in your terminal to see the version number.

### Download the VM configuration

There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: F[SND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternately, you can use Github to fork and clone the repository [Github Repo](https://github.com/udacity/fullstack-nanodegree-vm).

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:

Navigating to the `FSND-Virtual-Machine` directory and listing the files in it.

Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

Starting the Ubuntu Linux installation with `vagrant up`
Starting the Ubuntu Linux installation with vagrant up.
This screenshot shows just the beginning of many, many pages of output in a lot of colors.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

Logging into the Linux VM with `vagrant ssh`.
Logging into the Linux VM with vagrant ssh.

Logged in!
If you are now looking at a shell prompt that starts with the word vagrant (as in the above screenshot), congratulations — you've gotten logged into your Linux VM.

Inside the VM, change directory to /vagrant and look around with ls.

The files you see here are the same as the ones in the vagrant subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.

Running the database
The PostgreSQL database server will automatically be started inside the VM. You can use the psql command-line tool to access it and run SQL statements:

Running `psql`, the PostgreSQL command interface, inside the VM.
Running psql, the PostgreSQL command interface, inside the VM.

Logging out and in
If you type exit (or Ctrl-D) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type vagrant ssh again.

If you reboot your computer, you will need to run vagrant up to restart the VM.


### Installing the Virtual Machine
In the next part of this course, you'll use a virtual machine (VM) to run an SQL database server and a web app that uses it. The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be running a web service inside the VM which you'll be able to access from your regular browser.

We're using tools called Vagrant and VirtualBox to install and manage the VM. You'll need to install these to do some of the exercises. The instructions on this page will help you do this.

Why are we using a VM? It seems complicated.
It is complicated. In this case, the point of it is to be able to offer the same software (Linux and PostgreSQL) regardless of what kind of computer you're running on.

I got some other error message.
If you're getting a specific textual error message, try looking it up on your favourite search engine. If that doesn't help, take a screenshot and post it to the discussion forums, along with as much detail as you can provide about the process you went through to get there.

If all else fails, try an older version.
Udacity mentors have noticed that some newer versions of Vagrant don't work on all operating systems. Version 1.9.2 is reported to be stabler on some systems, and version 1.9.1 is the supported version on Ubuntu 17.04. You can download older versions of Vagrant from the Vagrant releases index.

## How to use

To bring up the virtual machine online use `vagrant up` and then log into it with `vagrant ssh`

You can download the [database data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Place this into the Vagrant shared directory, and to load the data `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`

- `psql` - the PostgreSQL command line program.
- `-d news` - connect to the database named news which has been set up for you.
-  `-f newsdata.sql` - run the SQL statements in the file newsdata.sql

Running the command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### Explore the data

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


`
