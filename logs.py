#!/usr/bin/env python
import psycopg2
"""Log Anaylsis of newsdata.sql files that provides stats on the articles."""

def connect(dbname="news"):
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        c = db.cursor()
        return db, c
    except:
        print("Error in connecting to database")

"""Next Five statments include basic stats about the articles and authors """

def popular_article():
    """Prints the three most popular articles of all time"""
    db, c = connect()
    query = "select * from popular_articles limit 3"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print "\nPopular Articles:\n"
    for i in range(0, len(result), 1):
        print "\"" + result[i][0] + "\" - " + str(result[i][1]) + " views"


def popular_authors():
    """Prints out the most popular article authors of all time"""
    db, c = connect()
    query = "select * from popular_authors"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print "\nPopular Authors:\n"
    for i in range(0, len(result), 1):
        print "\"" + result[i][0] + "\" - " + str(result[i][1]) + " views"

def least_popular_article():
    """Prints the three least viewed articles"""
    db, c = connect()
    query = "select * from least_popular_articles limit 3"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print "\nLeast Viewed Articles:\n"
    for i in range(0, len(result), 1):
        print "\"" + result[i][0] + "\" - " + str(result[i][1]) + " views"


def least_popular_authors():
    """Prints out the least article authors of all time"""
    db, c = connect()
    query = "select * from least_popular_authors"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print "\nLeast Viewed Authors:\n"
    for i in range(0, len(result), 1):
        print "\"" + result[i][0] + "\" - " + str(result[i][1]) + " views"


def log_stats():
    """Print days on which more than 1% of requests lead to errors"""
    db, c = connect()
    query = "select * from log_stats"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print "\nDays with more than 1% of errors:\n"
    for i in range(0, len(result), 1):
        print str(result[i][0])+ " - "+str(round(result[i][3], 2))+"% errors"

"""Posts all the stats """

if __name__ == '__main__':
    popular_article()
    popular_authors()
    least_popular_article()
    least_popular_authors()
    log_stats()
    print "\nDatebase Stats Completed!\n"
