from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Docker is working</title>
</head>
<body>
    <h1>Hello from Flask inside Docker!</h1>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
