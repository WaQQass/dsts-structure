'''students= {'name': "Mark","age": 30,"DOB": "1-2-3000"}
#2:{'name': "waqas","age": 28,"DOB": "2-3-9220"},'''
#a=["waqas","muaaz","ali"]
#

#students= {'name': "Mark","age": 30,"DOB": "1-2-3000"}
#
L1=["muaaz","waqas","ali"]

names=["waqas", "muaaz","muaaz","ali","waqas","ali","ali","waqas"]
#names=1,2,3,1,1,2,3]
if 5 not in names:
    print("awla")
counted={}

count=0
for i in range (0,len(L1)):
   
    if counted.keys() not in counted:
        for j in range(0,len(names)):
            if names[i]==names[j]:
                count=count+1
        print(L1[i],"appeared" ,count)
        count=0
        counted[L1[i]]='0'
        #counted.append(L1[i])
        
           
    
   














'''print(students[1])
print(students)#all values key and values
print(students['name'])#access by key

#print(students.keys())#key access
#print(students.values())#access just values
#print(students.items())#key value pairs as a tupple
#print(students.get("email","No found"))
#tudents["wawa"]="mark" #add new element
#print(students)
#students["DOB"]="CHANGED"
#print(students)
#students.pop("name")
#print(students)

#for i in students.items():
    #print(i)'''