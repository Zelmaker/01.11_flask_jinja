from flask import Flask, request
from flask import render_template

app = Flask(__name__)



@app.route('/users/')
def write_all_users():

    users_1 = ['mike', 'mishel', 'adel', 'keks', 'kamila']
    term = request.args.get('term')
    if term:
        filtered_users = [i for i in users_1 if term in i]
    else:
        filtered_users = users_1
        term =''

    return render_template('users/users_output.html',
                           search=term,users_2 = filtered_users)



# @app.route('/users/<id>')
# def users(id):
#     return render_template(
#         'index.html',
#         name=id,
#     )
#
# @app.route('/courses/')
# def courses():
#     courses = get_courses()
#
#     return render_template(
# 				'courses/index.html',
#         courses=courses
#     )
#


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
# @app.route('/courses/<name>/')
# def courses(name):
#     courses = get_courses(name)
#
#     return '''
#             <html>
#               <head>
#                 <title>''' + courses.name + '''</title>
#               </head>
#               <body>
#                 <h1>''' + courses.name + '''</h1>
#                 <div>''' + courses.body + '''</div>
#               </body>
#             </html>
#            '''

if __name__ == '__main__':
    app.run()
