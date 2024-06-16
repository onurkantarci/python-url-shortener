from flask import Flask, request, redirect, render_template, url_for
import string
import random

app = Flask(__name__)

url_mapping = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(6))
        if short_code not in url_mapping:
            return short_code

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short_code()
        url_mapping[short_code] = long_url
        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_long_url(short_code):
    long_url = url_mapping.get(short_code)
    if long_url is None:
        return 'URL not found', 404
    return redirect(long_url)

if __name__ == '__main__':
    app.run(debug=True)
