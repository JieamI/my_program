from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, render_template, make_response
from flask import request, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from uploader import UpLoader
import json
import os
import traceback
import re
import sys

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
#配置模型数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

#注意需要在传入实例之前配置
db = SQLAlchemy(app) 
#初始化flask-login,登录后变量current_user即为当前用户模型类记录              
login_manager = LoginManager(app)
#当访客不处于登录状态时将其重定向至login端点   
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    user = User.query.get(int(id))
    return user

#创建用户数据库，通过继承于UserMixin使current_user拥有is_authenticated等方法
class User(db.Model, UserMixin):                
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(20))
    username = db.Column(db.String(20))
    #存入密码的散列值以增强安全性
    password_hash = db.Column(db.String(20))       
    
    def if_pass(self, password):
        return check_password_hash(self.password_hash, password)

 #创建反馈数据库
class Feedback(db.Model):         
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    text = db.Column(db.Text)
    category = db.Column(db.String(50))


#登录路由
@app.route('/login', methods = ['POST', 'GET']) 
def login():
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        
        user = User.query.filter_by(username = username).first()
        if not user:
            flash("用户名不存在")
            return redirect(url_for('login'))
        if not user.if_pass(password):
            flash("密码错误")
            return redirect(url_for('login'))
        else:
            login_user(user)
            flash("登录成功")
            return redirect(url_for('index'))

    return render_template("login.html")


#注册路由
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        nickname = request.form.get('Nickname')
        c_password = request.form.get('Confirm_Password')
        
        if nickname == '' or username == '' or password == '' or c_password == '':
            flash("输入框不得为空")
            return redirect(url_for('register'))
        
        if password != c_password:
            flash("两次密码输入不一致")
            return redirect(url_for('register'))
        
        
        if User.query.filter_by(username = username).first():
            flash('用户名已存在')
            return redirect(url_for('register'))
        
        user = User(nickname = nickname, username = username, password_hash = generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash("注册成功")
        return redirect(url_for('login'))
    
    resp = make_response(render_template("register.html"))
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    if request.method == 'GET':
        return resp

#登出路由
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('登出成功')
    return redirect(url_for('index'))           

#首页路由
@app.route('/index', methods = ['POST', 'GET'])
def index():
    if current_user.is_authenticated:
        return render_template('index.html', nickname = current_user.nickname)
    else:
        return render_template('index.html')

#反馈路由
@app.route('/feedback', methods = ['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        text = request.form.get("Feedback")                      
        checkbox = ','.join(request.form.getlist("Checkbox"))
        '''
        if not text:
            flash("反馈内容不能为空")
            return redirect(url_for('feedback')) 
        if not checkbox:
            flash("请选择反馈类型")
        
            return render_template('feedback.html', text = text)              
        '''
        if not text or not checkbox:
            flash("请保证输入完整！")

        text = text.strip('<p>/;&nbsp')
        if current_user.is_authenticated:
            username = current_user.username
        else:
            username = "Visitor"                                                   #这里需要优化
        feedback = Feedback(username = username, text = text, category = checkbox)
        db.session.add(feedback)
        db.session.commit()
        flash("感谢您的反馈！")
        return redirect(url_for("index"))
    return render_template('feedback.html')
   

#文件上传路由   
@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    """UEditor文件上传接口
        config 配置文件flask
        result 返回结果
        """
    result = {}
    basedir = os.path.dirname(__file__)
    action = request.args.get('action', None)
    with open(os.path.join(basedir, 'static', 'ueditor', 'python', 'config.json'), encoding='utf8') as f:
        t = f.read()
        try:
            CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', t))
        except Exception as e:
            traceback.print_exc(e)
            CONFIG = {}
    if action == 'config':
        result = CONFIG

    if request.method == 'POST':
        if action in ('uploadimage', 'uploadfile'):
            # 图片、文件、视频上传
            if action == 'uploadimage':
                fieldName = CONFIG.get('imageFieldName', None)
                config = {
                    "pathFormat": CONFIG['imagePathFormat'],
                    "maxSize": CONFIG['imageMaxSize'],
                    "allowFiles": CONFIG['imageAllowFiles']
                }
            else:
                fieldName = CONFIG.get('fileFieldName', None)
                config = {
                    "pathFormat": CONFIG['filePathFormat'],
                    "maxSize": CONFIG['fileMaxSize'],
                    "allowFiles": CONFIG['fileAllowFiles']
                }

            if fieldName in request.files:
                file = request.files[fieldName]
                uploader = UpLoader(file_obj=file, config=config, upload_path=os.path.join(basedir, 'static'))
                uploader.up_file()
                result = uploader.callback_info()
            else:
                result['state'] = '上传接口出错'

    result = json.dumps(result)
    res = make_response(result)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,X_Requested_With'
    return res













if __name__ == '__main__':
    app.run()
