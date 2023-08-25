from flask import Flask, url_for
from markupsafe import escape

# 程序的主页
app = Flask(__name__) # 程序对象app

# 请求处理函数，官方叫做视图函数
# 请求处理函数需要使用装饰器,使用app.route来为这个函数绑定对应的URL,当用户在浏览器访问这个URL
# 时就会触发这个函数,获得返回值,并将这个返回值显示到浏览器窗口

# 一个视图函数可以绑定多个URL,这通过附加多个装饰器来实现
@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    str = '<h1>Welcomeeee to my list!</h1><img src="https://tutorial.helloflask.com/images/2-2.png">'
    return str

@app.route('/user/<name>')
def user_name(name):
    return f'User: {escape(name)}'

@app.route('/test')
def test_url_for():
    print(url_for("hello")) # 生成hello函数对应的URL
    print(url_for("user_name", name="cqk"))
    print(url_for("user_name", name="cqk"))
    print(url_for("test_url_for"))

    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test Page'







