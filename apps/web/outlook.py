import win32com.client
import xlsxwriter
import pandas
wb = xlsxwriter.Workbook('Planned_power_outage.xlsx')
ws = wb.add_worksheet()
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI").Folders
folder = outlook(1)
inbox = folder.Folders("Inbox")
messages = inbox.Items
for message in messages:
       if (message.SenderEmailAddress) == 'youssri.ahmed@cg-eg.com':
              sent_date = message.senton.date()
              sender = message.Sender
              subject = message.Subject
              content = message.body 
              possible_node = subject.split(" ")[1]
              print(sender,subject,content)