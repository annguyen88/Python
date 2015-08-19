import shutil
import os
import distutils

src = "/Users/anguyen/bitbucket/mss-amerisourcebergen/ABCScript/Reports"
dst = "/Users/anguyen/Google Drive/Workday Sync Files/Reports"

os.system("cp -rf /Users/anguyen/bitbucket/mss-amerisourcebergen/ABCScript/Reports /Users/anguyen/Google\ Drive/Workday\ Sync\ Files/")

# distutils.dir_util.copy_tree(src, dst)
# shutil.copytree(src, dst)
