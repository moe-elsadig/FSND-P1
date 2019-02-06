# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

news_db = psycopg2.connect("dbname=news")

news_c = news_db.cursor()

# The paths ordered by the number of visits where the status is '200 OK'
news_c.execute("select path, count(*) as num from log where status = '200 OK' group by path order by num desc")

# save the result in a list
path_list = news_c.fetchall()

# init an empty list to clean up the results for presenting to the user
top_articles_list = []

# iterate through the result and append to the articles_list
print ("\nThe list of articles ordered by the number of views are:\n\n")
for i in range(1, len(path_list)):
    print("  >   \"" + str(path_list[i][0]).replace("/article/", "").replace("-"," ").title()
    + "\" - " + str(path_list[i][1]) + " views\n")


print("\n\nFrom the authors table:\n")
news_c.execute("select id from authors")
print("\n  > id: " + str(news_c.fetchall()[0][0]))
news_c.execute("select name from authors")
print("\n  > name: " + str(news_c.fetchall()[0][0]))
news_c.execute("select bio from authors")
print("\n  > bio: " + str(news_c.fetchall()[0][0][:30] + "..."))

news_c.execute("select author, title, slug, lead, body, time, id from articles")

print("\n\nFrom the articles table:\n")
news_c.execute("select id from articles")
print("\n  > id: " + str(news_c.fetchall()[0][0]))
news_c.execute("select author from articles")
print("\n  > author: " + str(news_c.fetchall()[0][0]))
news_c.execute("select title from articles")
print("\n  > title: " + str(news_c.fetchall()[0][0]))
news_c.execute("select slug from articles")
print("\n  > slug: " + str(news_c.fetchall()[0][0]))
news_c.execute("select lead from articles")
print("\n  > lead: " + str(news_c.fetchall()[0][0]))
news_c.execute("select body from articles")
print("\n  > body: " + str(news_c.fetchall()[0][0]))
news_c.execute("select time from articles")
print("\n  > time: " + str(news_c.fetchall()[0][0]))


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
