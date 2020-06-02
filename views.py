import datetime
from flask import render_template, request, redirect
from models import Todo
from main import app


@app.route("/")
@app.route("/show/")
def show():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    all_todo_list = Todo.query.filter(Todo.status == 0).order_by(Todo.estimated_time).order_by(
        Todo.level).all()[:7]
    archive_list = Todo.query.filter(Todo.status != 0).all()[:7]
    dct = {
        "all_todo_list": all_todo_list,
        "archive_list": archive_list
    }
    return render_template("TODO.html", dct=dct)

@app.route("/show_all_todo/")
def show_all_todo():
    all_todo_list = Todo.query.filter(Todo.status == 0).order_by(Todo.estimated_time).order_by(
        Todo.level).all()
    dct = {
        "all_todo_list": all_todo_list,
    }
    return render_template("show_all_todo.html",dct=dct)



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


@app.route("/edit/<int:id>/", methods=['GET', 'POST'])
def edit(id):
    todo = Todo.query.get(id)

    if request.method == "POST":
        name = request.form.get("name")
        category = request.form.get("category")
        level = request.form.get("level")
        add_time = request.form.get("add_time")
        estimated_time = request.form.get("estimated_time")
        remark = request.form.get("remark")
        status = request.form.get("status")
        estimated_time = datetime.datetime.strptime(estimated_time, "%Y-%m-%d")
        add_time = datetime.datetime.strptime(add_time, "%Y-%m-%d")

        # 如果 status为1 ,则该任务为已完成,记录当前完成时间
        if status == "1":
            real_time = datetime.datetime.now()
            todo.real_time = real_time
        else:
            todo.real_time = None
        todo.todo_name = name
        todo.category = category
        todo.level = level
        todo.add_time = add_time
        todo.estimated_time = estimated_time
        todo.status = status
        todo.remark = remark
        todo.update()
        return redirect("/show/")

    return render_template("edit.html", todo=todo)


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
