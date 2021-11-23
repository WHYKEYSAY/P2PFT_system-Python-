
list_1 = ['REGISTER',10003,'Kecheng','192.168.1.1','UDP111','TCP111']
list_2 = ['REGISTER',10004,'cheng','192.168.1.2','UDP112','TCP112']
list_3 = ['REGISTER',10005,'Kec','192.168.1.3','UDP113','TCP113']
listx = [list_1,list_2, list_3]
listfiles1 = ['Kecheng1', '192.168.1.1','UDP111','TCP111']
listfiles2 = ['Kecheng2', '192.168.1.2','UDP111','TCP222']
listfiles3 = ['Kecheng3', '192.168.1.3','UDP333','TCP333']

list_1.append(listfiles1)
list_1.append(listfiles2)
list_1.append(listfiles1)

list_2.append(listfiles2)
list_2.append(listfiles1)
list_3.append(listfiles2)

list_3.append(listfiles3)
list_3.append(listfiles1)
list_3.append(listfiles2)



def check(sub_li):
    l = len(sub_li)
    for j in range(0, l):
        if name == sub_li[j][2]:
            print(0)
        else:
            print(1)
    return sub_li
#check(listx)

#print('\n'.join(map(str, listx)))

#print list of files by name_infot

name = input('Name:')
for item in listx:
    if item[:6]:
        print("\n",item[:6],"\n The lists of files are shown as following: ")
        for x in item[6:]:
            print(x)
        print

#def appendd(addlist):
   # for item in listx:
      #  if item[2] == addlist[2]:


#publish 
""""
Library = [["kecheng","IP","TCP socket",["book","fiel1","file2"]],["Jeff","IP","TCP socket",["file1","file2"]]]
print(Library)

Name = input("Search: ")
Listfile = input("Book: ")
i = 0
for sublist in Library:
    for i in range(0,len(sublist)-1):
        if Name == Library[i-1][0]:
            Library[i-1][-1].append(Listfile)
            break

print(Library)
"""

#Remove
#Name_to_remove = Remove[2]
""""
Name_to_remove = input("name: ")
removefile = input("book: ")
for sublist in Library:
    for i in range(0,len(sublist)):
        #name exit, remove
        if Name_to_remove == Library[i-1][0]:
            for j in range(0,len(Library[i-1][1])):
                #file exit, remove
                if removefile == Library[i-1][1][j-1]:
                    del Library[i-1][1][j-1]
                    print("Remove_accepted")
                else:
                    print("file doesnt exit!") 
        else:
            print("Remove_denied")   

print(Library)
"""

""""
def publish(sub_li):
    l = len(sub_li)
    for j in range(0, l):
        # name verified, store the lists
        if Name == sub_li[j][2]:
            sub_li.append(List of_files)
            print(Publish_accepted)
        else:
            print(Publish_denied)            
    return sub_li
"""
""""
Library = [["kecheng","IP1","TCP socket1",["book","fiel1","file2"]],["Jeff","IP2","TCP socket2",["file1","file2"]],["kechen","IP3","TCP socket3",["book","fiel1","file2"]]]
Name_to_research = input("name: ")
research_file = input("book: ")

for sublist in Library:
    for counter in range(0,len(sublist)-1):
        #name exit, research
        print(counter, "->", Library[counter])
        print(len(sublist))
        if Name_to_research == Library[counter][0]:
            print("matched!")
            found = False
            for sub_list in Library:
                for i in range(0,len(sub_list)-1):
                    for j in range(0,len(Library[i][-1])):
                    #file exit, display name
                        if research_file == Library[i][-1][j]:                           
                            print("The list of files ","<<",research_file,">>"," is from: \n",Library[i][:3])
                            found = True
                            break
                else:
                    print("file doesnt exit!")
                    break 
        else:
            print("research_denied")   
"""
""""
Library = [["kecheng","IP1","TCP socket1",["book","fiel1","file2"]],["Jeff","IP2","TCP socket2",["file1","file2"]],["kechen","IP3","TCP socket3",["book","fiel1","file2"]]]
"""
""""
Name = input("name: ")
update_info = input("info: ")

Info = [["name1","IP1","TCP1","UDP1"],["name2","IP2","TCP2","UDP2"],["name3","IP3","TCP3","UDP3"]]
Session = ["function","RQ",Name,"IP","UDP","TCP","file"]


print(Info)
for sublist in Info:
    for i in range(0,len(sublist)-1):
        if Session[2] == Info[i][0]:
            print("match!")
            del Session[:2],Session[-1]
                  
            Info[i] = Session
        else:
            print("successful!")
    else:
        print("name doesnt exist!")
print(Info)

"""



#print(Library)

#Register[]
Library=["name","IP","TCP","file"]
Info = ["name","IP","TCP","UDP"]

session = ["function","RQ","name","IP","UDP","TCP","file"]

#Register = ['REGISTER',RQ_NO,Name,IP,UDP_NO,TCP_NO]
#Register_accepted = ['REGISTER',RQ_NO]
#Register_denied = ['REGISTER_DENIED', RQ_NO, 'Name do not exist!']
#De_Register = ['DE_REGISTER', RQ_NO, Name]


#Publish = ['PUBLISH', RQ_NO, Name, List_of_files]
#Publish_accepted = ['PUBLISH', RQ_NO]
#Publish_denied = ['PUBLISH_DENIED', RQ_NO, 'Name do not exist!']

#Remove = ['REMOVE',RQ_NO,Name,List of files to remove]
#Remove_accepted = ['REMOVE',RQ_NO]
#Remove_denied = ['REMOVE',RQ_NO, 'Name do not exist!']

#Retrieve_all = ['RETRIEVE_ALL', RQ_NO]   
#Retrieve_all_back = ['RETRIEVE', RQ_NO, List of (Name, IP address, TCP socket#, list of available files)]

#Retrieve_infot = ['RETRIEVE_INFOT', RQ_NO, Name]
#Retrieve_infot_back = ['RETRIEVE_INFOT', RQ_NO, Name, IP Address, TCP socket#, List of available files]
#Retrive_denied = ['RETRIEVE_ERROR', RQ_NO, 'Name do not exist!']

#Research = ['SEARCH_FILE', RQ_NO, File_name]
#Research_back = ['SEARCH_FILE', RQ_NO, List of (Name, IP address, TCP socket#)]
#Research_denied = ['RESEARCH_ERROR', RQ_NO, 'Name do not exist!']

#Download = ['DOWNLOAD', RQ_NO, File_name]
#Download_back = ['FILE', RQ_NO, File_name, Chunk#, Text]
#Download_end = ['FILE_END', RQ_NO, File_name, Chunk#, Text]
#Download_denied = ['DOWNLOAD_ERROR', RQ_NO, 'Name do not exist!']

#Update = ['UPDATE_CONTACT',RQ_NO,Name,IP,UDP_NO,TCP_NO]
#Update_accepted = ['UPDATE_CONFIRMED',RQ_NO,Name,IP,UDP_NO,TCP_NO]
#Update_denied = ['UPDATE_DENIED', RQ_NO, Name, 'Name do not exist!']


