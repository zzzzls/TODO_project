import datetime
from flask import render_template, request, redirect
from models import Todo
from main import app


@app.route("/")
@app.route("/show/")
def show():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today_todo_list = Todo.query.filter(Todo.estimated_time == today,Todo.status == 0).order_by(Todo.level.desc()).all()
    all_todo_list = Todo.query.all()[-10:]
    dct = {
        "today_todo": today_todo_list,
        "all_todo_list": all_todo_list
    }
    return render_template("TODO.html", dct=dct)


@app.route("/add/", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        if request.form.get("name") and request.form.get("estimated_time"):
            name = request.form.get("name")
            category = request.form.get("category")
            level = request.form.get("level")
            estimated_time = request.form.get("estimated_time")
            remark = request.form.get("remark")
            now = datetime.datetime.now()
            estimated_time = datetime.datetime.strptime(estimated_time, "%Y-%m-%d")
            todo = Todo(name, category, level, now, estimated_time, None, 0, remark)
            todo.save()
            return redirect("/")
    elif request.method == "GET":
        return render_template("add.html")


@app.route("/info/<int:id>/")
def info(id):
    todo = Todo.query.get(id)
    return render_template("info.html",todo=todo)


# 任务状态 过滤器
@app.template_filter("todo_status")
def todo_status(status):
    status_list = ["未完成", "已完成", "已放弃"]
    return status_list[int(status)]

# 任务级别 过滤器
@app.template_filter("todo_level")
def todo_level(level):
    status_list = ["较低", "默认", "搞不定表碎觉"]
    return status_list[int(level)]