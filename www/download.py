import urllib.request
import sys
import os
import threading
def callbackfunc(blocknum, blocksize, totalsize):
	print('wwq')
    global url
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    downsize=blocknum * blocksize
    if downsize >= totalsize:
    	downsize=totalsize
    s ="%.2f%%"%(percent)+"====>"+"%.2f"%(downsize/1024/1024)+"M/"+"%.2f"%(totalsize/1024/1024)+"M \r"
    sys.stdout.write(s)
    sys.stdout.flush()
    if percent == 100:
        print('wwq')
def downimg():
    url='http://dlsw.baidu.com/sw-search-sp/soft/e7/10520/KanKan_V2.7.8.2126_setup.1416995191.exe'
    filename=os.path.basename(url)
    urllib.request.urlretrieve(url, filename, callbackfunc)
threading.Thread(target=downimg,args=('')).start()