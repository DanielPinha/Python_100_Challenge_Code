from flask import Flask, render_template, request, redirect, url_for, Markup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo_list.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_item = db.Column(db.String(250), nullable=False)


db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        new_item = ToDoList(
            list_item=request.form.get("message")
        )
        db.session.add(new_item)
        db.session.commit()
    list_items = db.session.query(ToDoList).all()
    column_names = ToDoList.__table__.columns.keys()
    return render_template("index.html", list=list_items, column=column_names)


@app.route('/complete/<int:item_id>')
def complete(item_id):
    item = db.session.query(ToDoList).get(item_id)
    item.list_item = Markup(f"<s>{item.list_item}</s>")
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = db.session.query(ToDoList).get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':

    app.run(debug=True)
