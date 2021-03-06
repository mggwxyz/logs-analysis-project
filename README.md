# Logs Analysis Project
A project where a database of logs is queried to analyze usage data for Udacity's Full Stack Web Developer Nanodegree

## Table of Contents

1. [Project Overview](#project-overview)
1. [Setting up the project](#setting-up-the-project)
1. [Running the project](#running-the-project)
1. [Resource Links](#resource-links)

## Project Overview

This project is a part of Udacity's Full Stack Web Developer Nanodegree. In this project, server-side code
 was written to query a database and analyze the table containing the logs. The main script will go throught the logs and returns
 the three most popular articles, the three most popular authors, and the days where the error rate for requests was above 1%.

## Setting up the project

> In order to run this project, you must have [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) set up on your computer.

```bash
# Clone the git repository into a directory using a bash terminal
git clone https://github.com/mggwxyz/logs-analysis-project.git

# Once the project has been setup, navigate into the project directory with `Vagrantfile`
cd logs-analysis-project

# Start the virtual machine
vagrant up

# Connect to the virtual machine
vagrant ssh

# Navigate to the folder where the guest/host files are shared
cd /vagrant
    
# Unzip the news database data SQL script
unzip ./data/newsdata.sql
    
# Apply SQL to Postgres to create news database
psql -d news -f newsdata.sql
```
## Running the project

```bash
# Once the project has been setup, navigate into the project directory on your home computer
cd logs-analysis-project

# Then, run the following command to ssh into the vagrant box
vagrant ssh

# Navigate to the folder shared between the host and virtual machine
cd /vagrant

# Run `analyze-logs.py` and log analysis will be printed
python3 ./scripts/analyze-logs.py
```

Example Output:
```bash
Q: What are the most popular three articles of all time?

"Candidate is jerk, alleges rival" - 342102 views
"Bears love berries, alleges bear" - 256365 views
"Bad things gone, say good people" - 171762 views

Q: Who are the most popular article authors of all time?

Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views

Q: On which days did more than 1% of requests lead to errors?

July 17, 2016 - 2.3% errors
```

## Resource Links

- [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
- [Source Code](https://github.com/mggwxyz/logs-analysis-project)
