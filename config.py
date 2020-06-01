import os


class Config:
    # 数据库对象发生修改时是否跟踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 配置数据库文件位置
    abs_path = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(abs_path, "todo.sqlite")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + db_path
