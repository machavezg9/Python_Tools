import os
rootdir = os.path.dirname(os.path.realpath(__file__)) #current dir of the python file
arrayToReplace = ["copy","remove"] #array of words to be replaced

wordToReplace = "toremove"
wordToReplaceWith = "to remove" #replacement word

for filename in os.listdir(rootdir): #looping for each file in the current dir
    #for element in arrayToReplace: #looping for each element in the array of words that want to be repalced
        if wordToReplace in filename: 
            filepath = os.path.join(rootdir, filename)
            newfilepath = os.path.join(rootdir, filename.replace(wordToReplace,wordToReplaceWith))
            os.rename(filepath,newfilepath)
