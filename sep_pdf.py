import os, time
from pdfrw import PdfReader, PdfWriter

directory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\Separate Me')
#print(directory)
reset_this = 1
#Separator will be added between the file name and the page number
separator = '_Page_' 
delay = False
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        #print(os.path.join(directory, filename))
        #print(filename)
        strt_pg = 1
        pages = PdfReader(filename).pages

        #Small 10 sec delay to avoide crashing
        if delay == True:
            #print('delay')
            time.sleep(10)
        else:
            #print('skipped delay')
            delay = True
        
        for page in pages:
            f_name= filename[:-4]+ separator + str(strt_pg)
            outdata = PdfWriter(fname=f_name+'.pdf')
            #print(f_name) #FILE CHECK
            outdata.addpage(page)
            outdata.write()
            strt_pg = strt_pg + 1
        continue
    else:
        continue
