import os
import uuid
import sqlite3
from flask import Flask, request, session, jsonify, g

# Path to the SQLite database
DB_PATH = os.path.join(os.path.dirname(__file__), 'reviews.db')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'default-secret-key')


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.before_request
def assign_user_id():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())


@app.route('/dashboard')
def dashboard():
    db = get_db()
    cur = db.execute('SELECT sentiment, COUNT(*) as count FROM reviews GROUP BY sentiment')
    data = {row['sentiment']: row['count'] for row in cur.fetchall()}
    return jsonify(data)


@app.route('/keywords')
def keywords():
    db = get_db()
    cur = db.execute('SELECT keyword, COUNT(*) as count FROM keywords GROUP BY keyword ORDER BY count DESC')
    data = [{ 'keyword': row['keyword'], 'count': row['count'] } for row in cur.fetchall()]
    return jsonify(data)


@app.route('/review/<int:review_id>')
def review(review_id):
    db = get_db()
    cur = db.execute('SELECT id, content, ai_response FROM reviews WHERE id=?', (review_id,))
    row = cur.fetchone()
    if row is None:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify({'id': row['id'], 'content': row['content'], 'ai_response': row['ai_response']})


@app.route('/update_review_response', methods=['POST'])
def update_review_response():
    review_id = request.form.get('review_id')
    response = request.form.get('response')
    if not review_id or not response:
        return jsonify({'error': 'Missing review_id or response'}), 400
    db = get_db()
    db.execute('UPDATE reviews SET ai_response=? WHERE id=?', (response, review_id))
    db.commit()
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
