from flask import render_template, request, redirect, url_for
from todo_list import db
from todo_list import app
from todo_list.models import Todo
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        with app.app_context():
            new_todo = Todo(content=content)
            db.session.add(new_todo)
            db.session.commit()
        return redirect('/')
    else:
        with app.app_context():
             todos = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', todos=todos)
@app.route('/delete/<int:id>')
def delete(id):
    with app.app_context():
        todo = Todo.query.get_or_404(id)
        db.session.delete(todo)
        db.session.commit()
    return redirect('/')
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    with app.app_context():
        todo = Todo.query.get_or_404(id)
        if request.method == 'POST':
            todo.content = request.form['content']
            db.session.commit()
            return redirect('/')
        else:
            return render_template('update.html', todo=todo)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
