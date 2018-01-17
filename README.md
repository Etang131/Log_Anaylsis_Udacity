# Log_Anaylsis_Udacity

Logs.py is a reporting tool made for the Udacity newsdata.sql database.


## Requirements:
Python,
PotgreSQL,
Vagrant,
Virtual Box

## How To Run Logs.py

1. Follow the Udacity steps to setting up your vitrual box and vagrant.
2. Inset newsdata.sql into your vagrant directory.
3. Log into vagrant with vagrant ssh
4. Change directory to /vagrant/
5. Use command psql -d news -f newsdata.sql to connect the file.
6. use psql -d news to connect to database.
7. Inset views (listed below) into sql in order.
8. Quit the database with \quit
9. Run logs.py

## Output:
Popular Articles:

"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views

Popular Authors:

"Ursula La Multa" - 507594 views
"Rudolf von Treppenwitz" - 423457 views
"Anonymous Contributor" - 170098 views
"Markoff Chaney" - 84557 views

Least Viewed Articles:

"Media obsessed with bears" - 84383 views
"There are a lot of bears" - 84504 views
"Balloon goons doomed" - 84557 views

Least Viewed Authors:

"Markoff Chaney" - 84557 views
"Anonymous Contributor" - 170098 views
"Rudolf von Treppenwitz" - 423457 views
"Ursula La Multa" - 507594 views

Days with more than 1% of errors:

2016-07-17 - 2.26% errors



### Views :

create view popular_articles as
select title, count(title) as views from articles,log
where log.path = concat('/article/',articles.slug)
group by title order by views desc;


create view popular_authors as
select authors.name, count(articles.author) as views from articles, log, authors
where log.path = concat('/article/',articles.slug) and articles.author = authors.id
group by authors.name order by views desc;


create view log_stats as
select Date,Total,Error, (Error::float*100)/Total::float as Percent from
(select time::timestamp::date as Date, count(status) as Total,
sum(case when status != '200 OK' then 1 else 0 end) as Error from log
group by time::timestamp::date) as result
where (Error::float*100)/Total::float > 1.0 order by Percent desc;
