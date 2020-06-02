from main import db
import datetime


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# TODO 库 模型
class Todo(Base):
    todo_name = db.Column(db.String(231), unique=True)
    category = db.Column(db.String(50))
    level = db.Column(db.Integer, default=1)
    add_time = db.Column(db.Date, nullable=False)
    estimated_time = db.Column(db.Date, nullable=False)
    real_time = db.Column(db.Date)
    status = db.Column(db.Integer)
    remark = db.Column(db.Text)

    def __init__(self, todo_name, category, level, add_time, estimated_time, real_time, status, remark):
        self.todo_name = todo_name
        self.category = category
        self.level = level
        self.add_time = add_time
        self.estimated_time = estimated_time
        self.real_time = real_time
        self.status = status
        self.remark = remark

# db.create_all()

# now = datetime.datetime.now()
# rw = Todo(todo_name="呵qq呵你qwe知道11吗傻逼",category="1",level="1",status="0",add_time=now,estimated_time=now,remark="",real_time=None)
# rw.save()
# rw = Todo(todo_name="华友多qq少q任务a",category="2",level="2",status="0",add_time=now,estimated_time=now,remark="",real_time=None)
# rw.save()
# rw = Todo(todo_name="我去折q磨多q今日",category="3",level="3",status="0",add_time=now,estimated_time=now,remark="",real_time=None)
# rw.save()
# rw = Todo(todo_name="难顶wq了啊",category="4",level="4",status="0",add_time=now,estimated_time=now,remark="",real_time=None)
# rw.save()
# rw = Todo(todo_name="卧槽哈q哈q哈哈醉了",category="5",level="5",status="0",add_time=now,estimated_time=now,remark="",real_time=None)
# rw.save()
# rw = Todo(todo_name="上卖弄q的再干嘛",category="4",level="4",status="0",add_time=now,estimated_time=now,remark="",real_time=None)
# rw.save()
# rw = Todo(todo_name="和hi黑黑q恶黑一群🐖",category="5",level="5",status="0",add_time=now,estimated_time=now,remark="",real_time=None)
# rw.save()
