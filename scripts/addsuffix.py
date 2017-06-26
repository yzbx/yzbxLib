import os,sys

if len(sys.argv) < 2:
    print("usage: python addsuffix.py xxxdir")
    sys.exit(-1)

for f in os.listdir(sys.argv[1]):
    fullpath=os.path.join(sys.argv[1],f)
    if os.path.isfile(fullpath):
        if f.find('.') == -1:
            newpath=fullpath+".xml"
            print("mv %s %s"%(fullpath,newpath))
            os.system("mv %s %s"%(fullpath,newpath))
        elif f.find('JPG.xml') !=-1 or f.find('jpg.xml')!=-1 :
            newpath=fullpath.replace(".xml","")
            print("mv %s %s" % (fullpath, newpath))
            os.system("mv %s %s" % (fullpath, newpath))
        elif f.find('.xml.xml') !=-1:
            newpath=fullpath.replace(".xml.xml",".xml")
            print("mv %s %s" % (fullpath, newpath))
            os.system("mv %s %s" % (fullpath, newpath))

        if f.find('.jpg') == -1 and f.find('.xml') == -1 :
            print("warning, bad file: %s" % fullpath)