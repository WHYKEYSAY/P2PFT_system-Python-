
list_1 = ['REGISTER',10003,'Kecheng','192.168.1.1','UDP111','TCP111']
list_2 = ['REGISTER',10004,'cheng','192.168.1.2','UDP112','TCP112']
list_3 = ['REGISTER',10005,'Kec','192.168.1.3','UDP113','TCP113']
listx = ['REGISTER',RQ_NO,Name,IP,UDP_NO,TCP_NO]

name = input('Name:')
def check(sub_li):
    l = len(sub_li)
    for j in range(0, l):
        if name == sub_li[j][2]:
            print(1)
        else:
            print(REGISTER_DENIED)
    return sub_li

check(listx)

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







#print(word_freq.values()[0])
#tuple = [[],[]]

