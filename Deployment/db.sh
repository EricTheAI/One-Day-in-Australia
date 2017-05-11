# [Team 2]
# Posung Chen / poc2 / 773278
# Xiao liang / liangx4 / 754282
# Jiawei Zhang / jiaweiz6 / 815546
# Jia Wang / jiaw8 / 815814
# Fan Hong / hongf / 795265


curl -X PUT localhost:5984/_config/admins/admin -d '"admin"'
curl -X PUT http://admin:admin@localhost:5984/_config/httpd/bind_address -d '"0.0.0.0"'