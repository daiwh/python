__author__ = 'wenhai.dai'
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(10), primary_key=True)
    name = Column(String(10))
    password = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/mytest')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()
# 创建新User对象:
#new_user = User(id='5', name='Bob', password='123456')
# 添加到session:
#session.add(new_user)
# 提交即保存到数据库:
#session.commit()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
# 关闭session:
session.close()