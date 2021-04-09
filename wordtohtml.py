def openFile(fileName):
    return open(fileName,'r')

def saveToHtml(file):
    newfile = open('newfile.html','a+')
    text='<html><head></head><body><p>this is the test body</p></body></html>'
    newfile.write(text)


fileopen = openFile('testfile.txt')
saveToHtml(fileopen)

print(fileopen.read())