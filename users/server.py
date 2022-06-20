from flask_app import app
from flask_app.controllers import users



if __name__=="__main__":     
    app.run(debug=True)






# @app.route('/')
# def index():
#     users = Users.get_all()
#     print(users)
#     return render_template("index.html" , users = users)


# # Brings me to the add form
# @app.route('/add')
# def add_form():
#     return render_template('add.html')

# # adds new user to the database
# @app.route('/add_user/', methods=['POST'])
# def add_user():
#     data={
#         'fname': request.form['fname'],
#         'lname': request.form['lname'],
#         'email': request.form['email']
#     }
#     Users.add_user(data)
#     return redirect('/')

# # shows only one data info 
# @app.route('/review/<int:user_id>')
# def review(user_id):
#     data={
#         'id': user_id
#     }
#     return render_template('review.html', user=Users.get_one(data))

# # delete the data
# @app.route('/delete/<int:user_id>')
# def delete_user(user_id):
#     data={
#         'id': user_id
#     }
#     Users.destroy(data)
#     return redirect('/')


# # brings me to edit page
# @app.route('/editform/<int:user_id>')
# def edit_form(user_id):
#     data={
#         'id': user_id
#     }
#     return render_template('edit.html',user=Users.get_one(data))


# # edits the data
# @app.route('/edit/<int:user_id>', methods=['POST'] )
# def edit_user(user_id):
#     data={
#         'id': user_id,
#         'fname': request.form['fname'],
#         'lname': request.form['lname'],
#         'email': request.form['email']
#     }
#     Users.edit_user(data)
#     return redirect('/')
















# @app.route('/show/<int:user_id>')
# def showform(user_id):
#     data = {
#         'id': user_id,
#     }
    
#     return render_template("review.html", user=Users.get_one(data))

# @app.route('/add')
# def add():
#     return render_template("add.html")

# @app.route('/add/adduser', methods=['POST'])
# def add_user():
#     data ={
#         "fname": request.form['fname'],
#         "lname": request.form['lname'],
#         "email": request.form['email']
#     }
#     Users.add_user(data)
#     return render_template("/review")

# @app.route('/delete/<int:user_id>')
# def delete(user_id):
#     data = {
#         'id': user_id,
#     }
#     Users.destroy(data)
#     return redirect('/')

# @app.route('/edit/<int:user_id>')
# def edit_user(user_id):
#     data = {
#         'id': user_id,
#     }
    
#     return render_template('review.html' , user=Users.get_one(data))

# # @app.route('/review')
# # def review_user():
# #     data = { "id"= users.id}
# #     return render_template("review.html")


