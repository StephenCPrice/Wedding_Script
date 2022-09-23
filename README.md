# Utilizes gspread to pull data from a google sheet and pushes out wedding save the date invitations to those listed on your google sheet.
## conda environmet called stephenp python==3.10.4 see requirements.txt for library versions
## conda create -n stephenp -r requirements.txt

# Work in progress

# Needs to iterate through the spreadsheet, check that there is a phone number/email/fbmessage attached to each name, and give the user a log of all people that will receive a text/email/fbmessage.
# Asks users for input regarding the message that they would like to send mentioning they can include url's. 
# Asks the user if they would like to proceed.
# Proceeds, and returns a log of all users with whom errors occured. 
# stores a log of all names that didn't receive a text 'theoretically', although you could theoretically provide validation as well with twilio. 





## Future feature: Because it takes Twilio time to que messages and send them, perhaps it would be good to include an interface that would provide validation when sucessfully sent. 
