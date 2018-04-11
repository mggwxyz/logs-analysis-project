import psycopg2
import datetime

# Connect to database and setup cursor for queries
connection = psycopg2.connect("dbname=news")
cursor = connection.cursor()


def print_most_popular_articles():
    # Print out the questions being answered
    print("\nQ: What are the most popular three articles of all time?\n")

    # Query the database to count the number of logged views for each article
    cursor.execute("select title, slug from articles")
    articles = cursor.fetchall()
    article_views = []
    for article in articles:
        query = """select count(*) from log l
         where l.path like '%""" + article[1] + "%'"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        article_views.append((article[0], count))

    # Sort articles by number of views and return top three
    top_articles = sorted(article_views, key=lambda x: x[1], reverse=True)[:3]

    # Print out the three articles with the most views
    for article in top_articles:
        (title, views) = article
        print("\"" + title + "\" - " + str(views) + " views")


def print_most_popular_authors():
    # Print out the questions being answered
    print("\nQ: Who are the most popular article authors of all time?\n")

    # Query the database to count the number of logged views for each article
    cursor.execute("select name, id from authors")
    authors = cursor.fetchall()
    author_views = []
    for author in authors:
        (name, id) = author
        query = """select count(*) from log l
            where REPLACE(l.path, '/article/', '') in
            (select slug from articles where author = """ + str(id) + ")"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        author_views.append((name, count))

    # Sort authors by number of views and return top three
    top_authors = sorted(author_views, key=lambda x: x[1], reverse=True)[:3]

    # Print out the three authors with the most views
    for author in top_authors:
        (name, views) = author
        print(name + " - " + str(views) + " views")


def print_days_with_many_errors():
    # Print out the questions being answered
    print("\nQ: On which days did more than 1% of requests lead to errors?\n")

    # Query the database to count the number of logged views for each article
    cursor.execute("select distinct(date_trunc('day', time)) from log")
    days = cursor.fetchall()
    bad_days = []
    for day in days:
        cursor.execute("""select count(*) from log
            where status <> '200 OK'
            and date_trunc('day', time) = '""" + str(day[0]) + "'::date")
        errors = cursor.fetchone()[0]
        cursor.execute("""select count(*) from log
            where date_trunc('day', time) = '""" + str(day[0]) + "'::date")
        requests = cursor.fetchone()[0]
        error_rate = round((errors/requests) * 100, 1)
        if (error_rate >= 1):
            bad_days.append((day[0], error_rate))

    # Sort dates by error rate
    bad_days = sorted(bad_days, key=lambda x: x[1], reverse=True)

    # Print out the tdates with the highest error rates
    for day in bad_days:
        (date, error_rate) = day
        formatted_date = date.strftime("%B %-d, %Y")
        print(formatted_date + " - " + str(error_rate) + "% errors")


# Print out the answers
print_most_popular_articles()
print_most_popular_authors()
print_days_with_many_errors()

# Print new line for added whitespace
print("\n")

# Close database connection
connection.close()
