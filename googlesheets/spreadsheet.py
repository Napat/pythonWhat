import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
pp = pprint.PrettyPrinter()

credentials = ServiceAccountCredentials.from_json_keyfile_name('googlesheetapi-af76ae602700.json', scope)
gclient = gspread.authorize(credentials)
sheet = gclient.open("Legislators 2017").sheet1

'''
Get Meta data
'''
print(sheet.row_count)
print(sheet.col_count)

'''
Access all data
'''
#legislators = sheet.get_all_records()
#pp.pprint(legislators)

'''
Access row data
'''
result = sheet.row_values(6)
pp.pprint(result)

'''
Access col data
'''
result = sheet.col_values(6)
pp.pprint(result)

'''
Get specific cell data
And Update cell data
'''
result = sheet.cell(6,11).value
pp.pprint(result)               # '202-224-6324'
result = sheet.update_cell(6,11, '123-456-7890')
result = sheet.cell(6,11).value         
pp.pprint(result)               # '123-456-7890'
result = sheet.update_cell(6,11, '202-224-6324')
result = sheet.cell(6,11).value         
pp.pprint(result)               # '202-224-6324'

'''
Create new row and insert to row index 3
Sleep 5 sec
Then Delete row index 3
'''
row = ["I'm", "updating", "a", "spreedsheet", "from", "Python!"]
rindex = 3
sheet.insert_row(row, rindex)
time.sleep(5)
sheet.delete_row(rindex)
