import mongoengine

#
# mongodb: // <dbuser > : < dbpassword > @ds031657.mlab.com: 31657/nikefanboy

host = "ds031657.mlab.com"
port = 31657
db_name = "nikefanboy"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port,
                        username=user_name, password=password)


def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
