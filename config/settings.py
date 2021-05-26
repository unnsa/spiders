# "dev", "test", "prod"
ENV = "dev"

# 全局代理控制
GLOBAL_PROXY = False
PROXY_POOL_URL = "http://localhost:5010"

""" mysql 配置 """
MysqlConfig = {
    'dev': {
        'host': '10.143.133.42',
        'port': 3306,
        'db': 'spider_qichacha',
        'username': 'bigdata',
        'password': 'zcbigdata'
    },
    'test': {

    },
    'prod': {

    }
}




