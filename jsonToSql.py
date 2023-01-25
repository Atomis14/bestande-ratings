import json
import sqlite3

# read json file
f = open('Ratings.json')
data = json.load(f)
f.close()

# create and open databse
con = sqlite3.connect('bestande.sqlite3')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS ratings(
  id text PRIMARY KEY,
  review text,
  score integer,
  university text,
  course integer,
  upvotes integer,
  downvotes integer,
  date date,
  courseName text,
  courseNameShort text
)""")
cur.execute("DELETE FROM ratings")

# write into databse
course_names = {}
for rating in data:
  if not 'upvotes' in rating: rating['upvotes'] = 0
  if not 'downvotes' in rating: rating['downvotes'] = 0
  if not 'courseName' in rating: rating['courseName'] = ''
  if not 'courseNameShort' in rating: rating['courseNameShort'] = ''

  cur.execute("INSERT INTO ratings VALUES (?,?,?,?,?,?,?,?,?,?)", 
    (rating['_id'], rating['review'], rating['score'], rating['university'], rating['course'], rating['upvotes'], rating['downvotes'], rating['date'], rating['courseName'], rating['courseNameShort'])
  )
  con.commit()

con.close()