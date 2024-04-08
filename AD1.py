import datetime
import sysconfig
import platform 

date_time = datetime.datetime.now()
python_version = sysconfig.get_python_version()
Os_name = platform.system()
Os_version = platform.version()
print("Hello, World!")
print("successful test at ")
print(date_time)
print("python version:",python_version)
print("operating system:", Os_name)
print("operating system version:", Os_version)