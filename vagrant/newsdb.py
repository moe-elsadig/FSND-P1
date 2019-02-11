#! /usr/bin/env python

# "Database code" for the DB Forum.
import datetime
import psycopg2

DBNAME = "news"


def connect(database_name):
    """
       Connect to the PostgreSQL database.  Returns a database connection.
       Use this like so:
       db, cursor = connect(DBNAME)
    """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
        """
                db, cursor : is a tuple.
                The first element (db) is a connection to the database.
                The second element (cursor) is a cursor for the database.
        """
    except psycopg2.Error as err:
        print "Unable to connect to database"
        print err
        sys.exit(1)      # The easier method - exit the program


def answer1():
    """Answer the first question ..."""
    print("Question 1: "
          + "What are the most popular three articles of all time?\n")

    db, news_c = connect(DBNAME)

    # obtain the articles by the number of views
    news_c.execute("""
        SELECT title, top_path.num
        FROM articles,
            (SELECT path, count(*) AS num
            FROM log
            WHERE log.status = '200 OK'
            GROUP BY path
            ORDER BY num DESC) AS top_path
        WHERE top_path.path LIKE CONCAT('%', articles.slug, '%')""")

    # Fetch the results of the query and print the top 3 items
    title_list = news_c.fetchall()
    for i in range(0, len(title_list[:3])):
        print("\"" + title_list[i][0]
              + "\" - "
              + str(title_list[i][1])
              + " views\n")


def answer2():
    """Answer second question ..."""
    print("Question 2: "
          + "Who are the most popular article authors of all time?\n")

    db, news_c = connect(DBNAME)

    # obtain the authors ordered by the sum of their article's views
    news_c.execute("""
        SELECT authors.name, top_auth_id.path_sum
        FROM authors,
            (SELECT articles.author, sum(top_path.num) AS path_sum
            FROM articles, (
                SELECT path, count(*) AS num
                FROM log
                WHERE log.status = '200 OK'
                GROUP BY path
                ORDER BY num DESC) AS top_path
            WHERE top_path.path = concat('/article/',articles.slug)
            GROUP BY articles.author
            ORDER BY path_sum DESC
            LIMIT 3) AS top_auth_id
        WHERE authors.id = top_auth_id.author
        LIMIT 4""")

    #  Fetch the results of the query and print in descending order
    # (already sorted from the query)
    author_views_list = news_c.fetchall()
    for i in range(len(author_views_list)):
        print("\""
              + author_views_list[i][0]
              + "\" - "
              + str(author_views_list[i][1])
              + " views\n")


def answer3():
    """Answer the third first question ..."""
    print("Question 3: "
          + "What are the most popular three articles of all time?\n")

    db, news_c = connect(DBNAME)

    # Obtain the day where the percentage error is > 1%
    news_c.execute("""
        SELECT TO_CHAR(day,'Month DD, YYYY') dayformat, perror
        FROM (SELECT DATE(time) AS day,
                count(*) as num,
                ROUND (sum(CASE WHEN status='404 NOT FOUND'
                    THEN 1 ELSE 0 END)*100.00/count(status), 2) AS perror
              FROM log
              GROUP BY day
              ORDER BY perror DESC) AS query1
        WHERE perror > 1.00""")

    # print all the days where the error rate was more than 1%
    high_error_list = news_c.fetchall()

    for i in range(len(high_error_list)):
        print((high_error_list[i][0])
              + "  "
              + str(high_error_list[i][1])
              + "%")


def run():
    """Running report ..."""
    print("Running reporting tools...\n")
    answer1()
    print("\n")

    answer2()
    print("\n")

    answer3()
    print("\n")


if __name__ == '__main__':
    run()

else:
    print ('Importing ...')
