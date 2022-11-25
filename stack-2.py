import hello
a=["waqas","muaaz","ali"]
b=["waqas", "Muaaz","mUaaz","Ali","waqas","aLi","ali","waqas"]
c=["waqas pvt", "Muaaz ltd","mUaaz-pvt","Ali","waqas ltd","aLi.co","ali","waqas"]
ignore_words=[" pvt"," ltd","-pvt",".co"] 
count=0


for i in range(len(a)):
  for j in range(len(b)):
     
    if a[i].upper() == c[j].upper(): 
      
        count=count+1
        
  print(a[i],"appeared ", count ,"times")
  count=0
  #hello.hello()

'''def ingonre():
    for k in c:
        for l in ignore_words: 
         if ignore_words[l] in c[k]:
            c[k].replace("")'''




     


