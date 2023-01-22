import yagmail
import pyautogui

def runMail(name, key, address, mail):
    yag = yagmail.SMTP(user='pyexpress07@gmail.com', password=pyautogui.password()) #เมลผู้ส่งและสร้าง popup ปิดรหัส
    recipients =  {mail:'PYEXPRESS'} #ผู้รับ #aline add 
    subject = 'อีเมล์ตอบกลับอัตโนมัติด้วย Python' 
    # name = 'user'
    # key = '123456TH'
    # address = 'ขอนแก่น'
    body = f"เรียน {name} \n\n Tracking number :{key} \n สถานะการขนส่ง {address}\nโปรดอย่าตอบกลับอีเมลนี้เรื่องจากอีเมล์นี้เป็นอีเมล์อัตโนมัติที่ส่งจากระบบ Python  \n\nด้วยความเคารพ \npyexpress"
    #f string ปรับเปลี่ยนข้อมูลของผู้รับ
    #yagmail.inline ('Bootcamp.png') แนบไฟล์เข้าไปใน body ในข้อความ
    #email_attachment 'Bootcamp.png'  แนบไฟล์
    yag.useralias = 'tacking number'  #ชื่อผู้ส่ง

    yag.send(to=recipients, subject=subject,contents=[body])  #, attachments=email_attachment)

def updateMail(mail,mails):
    yag = yagmail.SMTP(user='pyexpress07@gmail.com', password=pyautogui.password()) #เมลผู้ส่งและสร้าง popup ปิดรหัส
    recipients =  {mails:'PYEXPRESS'} #ผู้รับ #aline add 
    subject = 'อีเมล์ตอบกลับอัตโนมัติด้วย Python' 
    # name = 'user'
    # key = '123456TH'
    # address = 'ขอนแก่น'
    strMail = ' '.join([str(elem) for elem in mail])
    contents = f"สถานะการขนส่ง {strMail} โปรดอย่าตอบกลับอีเมลนี้เรื่องจากอีเมล์นี้เป็นอีเมล์อัตโนมัติที่ส่งจากระบบ Python ด้วยความเคารพ pyexpress"
    #f string ปรับเปลี่ยนข้อมูลของผู้รับ
    #yagmail.inline ('Bootcamp.png') แนบไฟล์เข้าไปใน body ในข้อความ
    #email_attachment 'Bootcamp.png'  แนบไฟล์
    yag.useralias = 'tacking number'  #ชื่อผู้ส่ง

    yag.send(to=recipients, subject=subject,contents=contents)  #, attachments=email_attachment)
