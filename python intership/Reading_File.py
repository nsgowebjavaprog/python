# 1
info_file=open("info.txt","r")
# print(info_file.read())
for i in info_file.readlines():
    print(i)
# print(info_file.readline())
# print(info_file.readlines())
# print(info_file.__module__)
# print(info_file.seekable())
# print(info_file.flush())
# print(info_file.isatty())
info_file.close()