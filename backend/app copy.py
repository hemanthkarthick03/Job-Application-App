from flask import Flask, render_template, url_for, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 


@app.route('/jobs')
def job_page():
    return {'jobs': ['Full Stack Engineer', 'AI Engineer', 'Software Engineer', 'Blockchain Developer']}


if __name__ == "__main__":    
    app.run(debug=True)