import time

tick=time.time()
print(tick)#19700101到现在的时间
print(time.localtime(tick))
localtime=time.localtime(tick)

acttime=time.asctime(localtime)
print(acttime)