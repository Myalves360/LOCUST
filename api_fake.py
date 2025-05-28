from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/users')
def get_users():
    return jsonify({
        "page": 1,
        "per_page": 6,
        "total": 12,
        "total_pages": 2,
        "data": [
            {"id": 1, "name": "Mylena"},
            {"id": 2, "name": "João"},
            {"id": 3, "name": "Maria"}
        ]
    })

if __name__ == '__main__':
    app.run(port=5000)
