import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender_email = entry_sender.get()
    password = entry_password.get()
    recipient_email = entry_recipient.get()
    subject = entry_subject.get()
    message = text_message.get('1.0',tk.END)

    message_html = message.replace('\n','<br>')

    html =f"""
    <html>
      <body style='font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;'>
        <div style='max-width: 500px; margin: auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px #ccc; padding: 20px;'>
          <h2 style='color: #4CAF50;'>You've got a new message!</h2>
          <p style='font-size: 16px; color: #333;'>{message_html}</p>
          <hr>
          <p style='font-size: 12px; color: #888;'>Sent via SMTP Mail Sender</p>
        </div>
      </body>
    </html>
    """


    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html,'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com',587) as server:
            server.starttls()
            server.login(sender_email,password)
            server.sendmail(sender_email,recipient_email,msg.as_string())
        messagebox.showinfo('Succes','Email sent succesfully!')
    except Exception as e:
        messagebox.showerror('Error',f'Failed to send email:{e}')

root = tk.Tk()
root.title('SMTP Mail Sender')
root.geometry('400x400')

#sender Email
label_sender = tk.Label(root,text='Sender Email:')
label_sender.pack()
entry_sender = tk.Entry(root,width=40)
entry_sender.pack()

#Password
label_password = tk.Label(root,text='Password:')
label_password.pack()
entry_password = tk.Entry(root, show='*',width=40)
entry_password.pack()

#recipient email
label_recipient = tk.Label(root,text='Recipient Email:')
label_recipient.pack()
entry_recipient= tk.Entry(root,width=40)
entry_recipient.pack()

#Subject
label_subject = tk.Label(root,text='Subject:')
label_subject.pack()
entry_subject= tk.Entry(root,width=40)
entry_subject.pack()

#Message
label_message = tk.Label(root,text='Message:')
label_message.pack()
text_message= tk.Text(root,height=8,width=40)
text_message.pack()

#Send Button
send_button = tk.Button(root,text='Send Email',command=send_email)
send_button.pack(pady=10)

root.mainloop()