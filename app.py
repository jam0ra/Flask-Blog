from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'John Doe',
        'title': 'Sample Blog Post',
        'content': 'This is the post.',
        'date_posted': 'January 21, 2021'
    }, {
        'author': 'Bob Sanders',
        'title': 'Alternate Post',
        'content': 'Hello universe.',
        'date_posted': 'March 7th, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
