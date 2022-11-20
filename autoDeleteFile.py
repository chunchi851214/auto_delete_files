import os
rootdir = './'
#%%
def delete_files(part_file_name, rootdir = './'):
    count = 0
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if part_file_name in file:
                count += 1
                os.remove(os.path.join(subdir, file))
                print("%s is removed" % file)
    return count
#%%
part_file_name = input("Enter the keywords of files that would be removed: ")
count = delete_files(part_file_name)
print("Totally remove {} files".format(count))
os.system('pause')
