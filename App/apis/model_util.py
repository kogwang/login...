from App.ext import db
#工具类  一般都是公司给封装好  我们只需要调用

def save(self):
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        abort(400)