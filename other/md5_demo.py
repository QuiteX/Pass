import hashlib
import datetime
# m = hashlib.md5()
# print(m)
# m.update('itcast'.encode("utf8"))
#
# print(m.hexdigest())
KEY_VALUE = 'Itcast'
now = datetime.datetime.now()
m = hashlib.md5()
str = '%s%s' % (KEY_VALUE,now.strftime("%Y%m%d"))
m.update(str.encode('utf-8'))
value = m.hexdigest()
print(value)
print(now.strftime("%Y%m%d"))

m.update('itcast'.encode("utf8"))

print(m.hexdigest())


python -m http.server 8080
