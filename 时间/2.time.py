import time

print(time.localtime())

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#"%Y-%m-%d %H:%M:%S"不能插入中文

mystr="2019-03-09 01:01:25"
mytime=time.strptime(mystr,"%Y-%m-%d %H:%M:%S")
print(type(mytime))
print(mytime)
print(time.mktime(mytime))