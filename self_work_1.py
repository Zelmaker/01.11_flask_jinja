from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/users/<id>')
def users(id):
    return render_template(
        'users/show.html',
        id=id, nickname = 'user-'+id
    )


if __name__ == '__main__':
    app.run()
