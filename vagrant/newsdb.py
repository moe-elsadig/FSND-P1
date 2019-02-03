# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

news_db = psycopg2.connect("dbname=news")

news_c = news_db.cursor()

news_c.execute("select status, count(*) as num from log group by status")

print(news_c.fetchall()[0:100])







# def get_posts():
#     db = psycopg2.connect("dbname=forum")
#     c = db.cursor()
#     """Return all posts from the 'database', most recent first."""
#     c.execute("""select content, time from posts order by time desc""")
#     return c.fetchall()
#     # return reversed(POSTS)
#
# def add_post(content):
#     db = psycopg2.connect("dbname=forum")
#     c = db.cursor()
#     content = bleach.clean(content)
#     """Add a post to the 'database' with the current timestamp."""
#     c.execute("insert into posts values (%s)", (content,))
#     c.execute("update posts set content = '' where content like '%spam%'")
#     c.execute("delete from posts where content like ''")
#     db.commit()
#     db.close()
