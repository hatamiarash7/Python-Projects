import platform

info = platform.uname()
platform_type = str(info[0])
system_name = str(info[1])
platform_name = str(info[2])
platform_version = str(info[3])
machine_type = str(info[4])
machine_info = str(info[5])

print(info)
