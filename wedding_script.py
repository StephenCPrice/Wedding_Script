import gspread, pprint, re

sa = gspread.service_account()
sh = sa.open('Master Wedding Planner')
wks = sh.worksheet('Guests')
count = wks.row_count
def mklist(n):
    for i in range(n):
        yield []
names_list = list(mklist(count))

for i in range(4, count):

    names_list[i].append(wks.get(f'A{i}'))
    names_list[i].append(wks.get(f'E{i}'))
    print(names_list)
'''
for i in range(count):
    current_row = wks.row_values(1)
    print(current_row)
    #for x in range(len(current_row)):
     #   print(f'{current_row[x]} ' )
'''