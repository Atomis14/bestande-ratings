from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def database_setup():
    con = sqlite3.connect('bestande.sqlite3')
    cur = con.cursor()
    return cur, con

@app.route('/')
def index():
    courses = None
    if 'course' in request.args:
        search_string = request.args['course']
        if search_string != '':
            cur, con = database_setup()
            res = cur.execute("SELECT * FROM courses WHERE name LIKE ?", ('%'+search_string+'%',))
            courses = res.fetchall()
            con.close()
    return render_template('search.html', courses=courses)

@app.route('/course/<id>/')
def course(id=None):
    if id == None:
        return redirect(url_for('index'))
    course = None
    cur, con = database_setup()
    res = cur.execute("SELECT * FROM courses WHERE courseId=?", (id,))
    course = res.fetchone()
    if course == None:
        return redirect(url_for('index'))
    res = cur.execute("SELECT * FROM ratings WHERE course=? ORDER BY date DESC", (id,))
    ratings = res.fetchall()
    con.close()
    # create stats
    stats = { 'ratings': [0,0,0,0,0], 'average_rating': 0, 'comment_ratings': [] }
    for rating in ratings:
        rating = list(rating)
        stats['ratings'][rating[2]-1] += 1
        if rating[1] != None:
            rating[6] = datetime.utcfromtimestamp(rating[6]/1000).strftime("%d.%m.%Y")
            stats['comment_ratings'].append(rating)
    print(stats['ratings'])
    stats['average_rating'] = (stats['ratings'][0] + stats['ratings'][1]*2 + stats['ratings'][2]*3 + stats['ratings'][3]*4 + stats['ratings'][4]*5) / sum(stats['ratings'])
    return render_template('course.html', course=course, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)