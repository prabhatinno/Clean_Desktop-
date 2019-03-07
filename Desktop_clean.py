import os,sys,operator,shutil,platform
results = []
size=[]
fs = {}
if(platform.system()=='Windows'):     #For Window Enviroment
location=os.path.join(os.environ['HOMEPATH'])
if(platform.system()=='Linux'):       #For Linux Enviroment
location=os.path.join(os.path.join(os.path.expanduser('~')))
for root, dirs, files in os.walk(location):
    for f in files:
            results=os.path.join(root,f) #File
            size=os.path.getsize(results) #size
            fs[results]=size

for file in sorted(fs.items(), key=operator.itemgetter(1), reverse=True)[:10]:  #sort based on size
print file[0] # It will print top 10 file of System.

if(platform.system()=='Windows'):    #For Window Enviroment
location=os.path.join(os.environ['HOMEPATH'],'Desktop')
Dest=os.path.join(os.environ['HOMEPATH'],'Documents')
if(platform.system()=='Linux'):     #For Linux Enviroment
        location=os.path.join(os.path.join(os.path.expanduser('~')),'Desktop')
        Dest=os.path.join(os.path.join(os.path.expanduser('~')),'Documents')
 for root, dirs, files in os.walk(location):
          for f in files:
            results=os.path.join(root,f) 
            print results      # It will print all file on desktop
           filename, file_extension = os.path.splitext(results)  # It gives file and extension.
            if(os.path.exists(Dest+'/'+file_extension)):
                shutil.move(results,Dest+'/'+file_extension)
            else:
                os.makedirs(Dest+'/'+file_extension)
                shutil.move(results,Dest+'/'+file_extension)
             for f1 in dirs:
           os.remove(os.path.join(root,f1))# Remove folder after move all file.
