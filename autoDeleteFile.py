import os
rootdir = './'
#%%
def delete_files(part_file_name, rootdir = './'):
    count = 0
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file[-len(part_file_name):] == part_file_name:
                count += 1
                os.remove(os.path.join(subdir, file))
                print("%s is removed" % file)
    return count
#%%
part_file_name = input("輸入想刪除檔案的關鍵字: ")
count = delete_files(part_file_name)
print("Totally remove {} files".format(count))
os.system('pause')