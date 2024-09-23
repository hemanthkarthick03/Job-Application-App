from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # To allow requests from different origins

# Env Variables
DB_NAME = "job_db"
DB_USER = "admin"
DB_PASSWORD = "password"
DB_HOST = "localhost"

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )
    return conn

# CRUD for Users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s) RETURNING id;',
        (new_user['username'], new_user['email'], new_user['password'], new_user['role'])
    )
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': user_id}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE id = %s;', (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updates = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE users SET username = %s, email = %s, password = %s, role = %s WHERE id = %s;',
        (updates['username'], updates['email'], updates['password'], updates['role'], user_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'User updated'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = %s;', (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'User deleted'})

# CRUD for Jobs
@app.route('/jobs', methods=['GET'])
def get_jobs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, title, description, company, location, salary FROM jobs;')
    jobs = cur.fetchall()
    cur.close()
    conn.close()

    # Convert query result to a list of dictionaries for JSON serialization
    job_list = []
    for job in jobs:
        job_list.append({
            'id': job[0],
            'title': job[1],
            'description': job[2],
            'company': job[3],
            'location': job[4],
            'salary': job[5]
        })
    
    return jsonify(job_list)

@app.route('/jobs', methods=['POST'])
def create_job():
    new_job = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO jobs (title, description, company, location, salary) VALUES (%s, %s, %s, %s, %s) RETURNING id;',
        (new_job['title'], new_job['description'], new_job['company'], new_job['location'], new_job['salary'])
    )
    job_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': job_id}), 201

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM jobs WHERE id = %s;', (job_id,))
    job = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(job)

@app.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    updates = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE jobs SET title = %s, description = %s, company = %s, location = %s, salary = %s WHERE id = %s;',
        (updates['title'], updates['description'], updates['company'], updates['location'], updates['salary'], job_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Job updated'})

@app.route('/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM jobs WHERE id = %s;', (job_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Job deleted'})

# CRUD for Applications
@app.route('/applications', methods=['GET'])
def get_applications():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM applications;')
    applications = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(applications)

@app.route('/applications', methods=['POST'])
def create_application():
    new_application = request.json
    conn = get_db_connection()
    cur = conn.cursor()

    # Ensure the status is provided or default to 'Applied'
    status = new_application.get('status', 'Applied')

    cur.execute(
        'INSERT INTO applications (job_id, candidate_id, status) VALUES (%s, %s, %s) RETURNING id;',
        (new_application['job_id'], new_application['user_id'], status)
    )
    application_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': application_id}), 201


@app.route('/applications/<int:application_id>', methods=['GET'])
def get_application(application_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM applications WHERE id = %s;', (application_id,))
    application = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(application)

@app.route('/applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    updates = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE applications SET user_id = %s, job_id = %s, status = %s WHERE id = %s;',
        (updates['user_id'], updates['job_id'], updates['status'], application_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Application updated'})

@app.route('/applications/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM applications WHERE id = %s;', (application_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Application deleted'})

if __name__ == '__main__':
    app.run(debug=True)
