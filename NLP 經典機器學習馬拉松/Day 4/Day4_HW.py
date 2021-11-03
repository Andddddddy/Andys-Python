import re


# 讀取資料文本
sample = open("/Users/shijunliao/Desktop/Python/Github/Andys-Python/Raw_data/fradulent_emails.txt",'r').read()
sample_corpus = sample[:11590]


# 讀取寄件者資訊
match = re.findall('(?=From:).+',sample_corpus)
print(match)


# 只讀取寄件者姓名
for i in re.findall('(?<=From: ).+(?= <)',sample_corpus):
    print(i)


# 只讀取寄件者電子信箱
### 只讀取電子信箱中的寄件機構資訊
for i in re.findall('(?<=From: ).+((?<=@)\w+)',sample_corpus):
    print(i)


### 結合上面的配對方式, 將寄件者的帳號與機構訊返回
for i in re.findall('(?<=From: ).+(?<=<)(\w+)@(\w+)',sample_corpus):
    print(", ".join(i))



# 使用正規表達式對email資料進行處理
### 讀取與切分Email
import re
import pandas as pd
import email

###讀取文本資料:fradulent_emails.txt###
#<your code>#
fradulent_emails = open("/Users/shijunliao/Desktop/Python/Github/Andys-Python/Raw_data/fradulent_emails.txt",'r').read()
emails = re.split(r'From r  ', fradulent_emails)

#<your code>#
len(emails) #查看有多少封email



emails_list = [] #創建空list來儲存所有email資訊
for mail in emails[:20]: #只取前20筆資料 (處理速度比較快)
    emails_dict = dict() #創建空字典儲存資訊
    ###取的寄件者姓名與地址###
    
    #Step1: 取的寄件者資訊 (hint: From:)
    #<your code>#
    sender_infomation = re.findall('From:.+',mail)
    
    
    #Step2: 取的姓名與地址 (hint: 要注意有時會有沒取到配對的情況)
    #<your code>#
    sender_name = re.findall('(?<=\").+(?=\")',str(sender_infomation))
    sender_email_addr = re.findall('\w+@\w+\.\w+',str(sender_infomation))
    
    #Step3: 將取得的姓名與地址存入字典中
    #<your code>#
    for i in range(len(sender_email_addr)):
        if len(sender_name) != 0:
            emails_dict['Sender'] = sender_name[i]
        if len(sender_email_addr) != 0:
            emails_dict['Sender_addr'] = sender_email_addr[i]
    
    ###取的收件者姓名與地址###
    #Step1: 取的寄件者資訊 (hint: To:)
    #<your code>#
    receiver_information = re.findall('To: (.+)',mail)
    
    #Step2: 取的姓名與地址 (hint: 要注意有時會有沒取到配對的情況)
    #<your code>#
    receiver_name = re.findall('(?<=\").+(?=\")',str(receiver_information))
    receiver_email_addr = re.findall('\w+@\w+\.\w+',str(receiver_information))
        
    #Step3: 將取得的姓名與地址存入字典中
    #<your code>#
    for i in range(len(receiver_email_addr)):
        if len(receiver_name) != 0:
            emails_dict['Receiver'] = receiver_name[i]
        else:
            emails_dict['Receiver'] = None
        if len(receiver_email_addr) != 0:
            if receiver_email_addr[i] != emails_dict['Sender_addr']:
                emails_dict['Receiver_addr'] = receiver_email_addr[i]
        
        
    ###取得信件日期###
    #Step1: 取得日期資訊 (hint: To:)
    #<your code>#
    date_information = re.findall('Date: .+',mail)
    
    #Step2: 取得詳細日期(只需取得DD MMM YYYY)
    #<your code>#
    Date = re.findall('\d+ \w+ \d+',str(date_information))
        
    #Step3: 將取得的日期資訊存入字典中
    #<your code>#
    if len(Date) != 0:
        emails_dict["Date"] = Date[0]
    else:
        emails_dict["Date"] = None
        
    ###取得信件主旨###
    #Step1: 取得主旨資訊 (hint: Subject:)
    #<your code>#
    subject_information = re.findall('Subject: .+',mail)
    
    #Step2: 移除不必要文字 (hint: Subject: )
    #<your code>#
    subject = re.findall(' (.+)\'',str(subject_information))
    
    #Step3: 將取得的主旨存入字典中
    #<your code>#
    emails_dict['Subject'] = subject
    
    
    ###取得信件內文###
    #這裡我們使用email package來取出email內文 (可以不需深究，本章節重點在正規表達式)
    try:
        full_email = email.message_from_string(mail)
        body = full_email.get_payload()
        emails_dict["email_body"] = body
    except:
        emails_dict["email_body"] = None
    
    ###將字典加入list###
    #<your code>#
    emails_list.append(emails_dict)


#將處理結果轉化為dataframe
emails_df = pd.DataFrame(emails_list)
emails_df












