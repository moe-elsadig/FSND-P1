# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

news_db = psycopg2.connect("dbname=news")

news_c = news_db.cursor()

# obtain the articles by the number of views
news_c.execute("SELECT title, toparticles.num FROM articles, (SELECT path, count(*) AS num FROM log WHERE log.status = '200 OK' GROUP BY path ORDER BY num desc) as toparticles where toparticles.path LIKE CONCAT('%',articles.slug,'%')")

title_list = news_c.fetchall()
for i in range(len(title_list)):
    print ("\"" + title_list[i][0] + "\" - " + str(title_list[i][1]) + " views\n")

#
#
# print("\n\nFrom the authors table:\n")
# news_c.execute("select id from authors")
# print("\n  > id: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select name from authors")
# print("\n  > name: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select bio from authors")
# print("\n  > bio: " + str(news_c.fetchall()[1][0][:30] + "..."))
#
# news_c.execute("select author, title, slug, lead, body, time, id from articles")
#
# print("\n\nFrom the articles table:\n")
# news_c.execute("select id from articles")
# print("\n  > id: " + str(news_c.fetchall()[0][0]))
# news_c.execute("select author from articles")
# print("\n  > author: " + str(news_c.fetchall()[0][0]))
# news_c.execute("select title from articles")
# print("\n  > title: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select slug from articles")
# print("\n  > slug: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select lead from articles")
# print("\n  > lead: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select body from articles")
# print("\n  > body: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select time from articles")
# print("\n  > time: " + str(news_c.fetchall()[1][0]))
#
# print("\n\nFrom the log table:\n")
# news_c.execute("select id from log")
# print("\n  > id: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select path from log")
# print("\n  > path: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select ip from log")
# print("\n  > ip: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select method from log")
# print("\n  > method: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select status from log")
# print("\n  > status: " + str(news_c.fetchall()[1][0]))
# news_c.execute("select time from log")
# print("\n  > time: " + str(news_c.fetchall()[1][0]))

news_c.close()




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
