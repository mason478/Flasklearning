from flask import Blueprint

# 通过实例化一个 Blueprint 类对象可以创建蓝本。这个构造函数有两个必须指定的参数:
# 蓝本的名字和蓝本所在的包或模块。和程序一样,大多数情况下第二个参数使用 Python 的
# __name__ 变量即可
main = Blueprint("main", __name__)

from Flasklearning.flaskyy.app.main import views, errors
from Flasklearning.flaskyy.app.models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
