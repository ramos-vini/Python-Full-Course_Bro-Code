import time

epoch = time.ctime(0)
print(epoch)

since_epoch = time.time()
print(since_epoch)

print(time.ctime(time.time()))

time_object = time.localtime()
print(time_object)

local_time = time.strftime("%d %B %Y - %H:%M:%S", time_object)
print(local_time)
