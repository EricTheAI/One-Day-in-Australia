curl -X PUT localhost:5984/_config/admins/admin -d '"admin"'
curl -X PUT http://admin:admin@localhost:5984/_config/httpd/bind_address -d '"0.0.0.0"'