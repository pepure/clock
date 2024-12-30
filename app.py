from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


# 创建了网址 /show/info 和函数index之间的对应关系，以后用户在浏览器上访问/show/info，网站自动执行index函数
@app.route('/clock')
def index():
    # 默认去项目根目录下templates文件夹中寻找
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7860)
