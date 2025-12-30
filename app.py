from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Jenkins CI/CD! </h1><p>Deployed successfully!</p>'

@app.route('/health')
def health():
    return {'status': 'healthy', 'deployed_by': 'Jenkins', 'timestamp': '2025'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
