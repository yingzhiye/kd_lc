# 配置文件
class Config:
    ENV = 'development'
    DEBUG = True
    # 数据库类型://用户名：密码@ip:port/数据名称
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:3@10.91.221.46:5432/KidneyBioDB"

class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
