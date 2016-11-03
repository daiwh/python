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
new_user = User(id='5', name='Bob', password='123456')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()