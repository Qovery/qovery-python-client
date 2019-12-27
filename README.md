# qovery-python-sdk

Get Qovery instance
```$python
qovery = Qovery()

db = qovery.get_database_by_name("my-pql")

host = db.host
port = db.port
username = db.username
password = db.password
```

