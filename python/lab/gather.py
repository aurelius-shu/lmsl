from ntpath import join
import os, shutil

sour = r'D:\WorkSpace\inotebook\extension\尚硅谷'
dest = r'D:\WorkSpace\inotebook\extension\atguigu'
dirs = os.listdir(sour)
dest_dirs = { d : os.path.join(dest, d) for d in dirs if os.path.isdir(os.path.join(sour, d)) }
sour_dirs = { d : os.path.join(sour, d) for d in dirs if os.path.isdir(os.path.join(sour, d)) }

# print(dirs)
# print(dest_dirs)
# print("------")
# print(sour_dirs)

print(len(dest_dirs))
print("------")
print(len(sour_dirs))

counts = 0

def copy(sroot, droot):
    global counts
    files = [ file for file in os.listdir(sroot) if ((not os.path.isdir(os.path.join(sroot, file))) and ((file[::-1][:3][::-1] in ['.md']) or (file[::-1][:4][::-1] in ['.pdf', '.doc', '.ppt', '.txt']) or (file[::-1][:5][::-1] in ['.docx', '.pptx', '.mmap', '.emmx']) or (file[::-1][:6][::-1] in ['.xmind']))) ]
    for file in files:
        shutil.copyfile(os.path.join(sroot, file), os.path.join(droot, file))
        print('copy: ' + os.path.join(sroot, file) + ' -> ' + os.path.join(droot, file))
        counts+=1
    fonds = [ fond for fond in os.listdir(sroot) if os.path.isdir(os.path.join(sroot, fond))]
    for fond in fonds:
        copy(os.path.join(sroot, fond), droot)


for fond in dest_dirs.keys():    
    if not os.path.isdir(dest_dirs[fond]):
        os.mkdir(dest_dirs[fond])
    copy(sour_dirs[fond], dest_dirs[fond])

# if not os.path.isdir(r'D:\WorkSpace\inotebook\extension\atguigu\Redis'):
#     os.mkdir(r'D:\WorkSpace\inotebook\extension\atguigu\Redis')
# shutil.copyfile(r"D:\WorkSpace\inotebook\extension\尚硅谷\Redis\尚硅谷_Redis6课件.docx", r"D:\WorkSpace\inotebook\extension\atguigu\Redis\尚硅谷_Redis6课件.docx")

# a = '123456'
# print(a[-3:-1])
print('end:' + str(counts))