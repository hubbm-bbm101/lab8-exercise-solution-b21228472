import sys
names=[]
student_info={}
uni_names=[]
dep_names=[]
file=open("student.txt","r",encoding="utf-8")
for f in file:
    name=f.split(":")[0]
    student_info[name]=(f.split(":")[1].split(","))
file.close()
a=comuts=input()

for eleman in a.split(","):
    try:
        uni_name=student_info[eleman][0]
        departmant=student_info[eleman][1]
        print("Name: "+str(eleman)+" \nUniversity: "+str(uni_name)+"\nDepartman: "+str(departmant))
    except KeyError:
        print("No record of '{}' was found!".format(eleman))


print(names)