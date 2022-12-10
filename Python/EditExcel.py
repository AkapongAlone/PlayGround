import pandas as pd
import xlwings as xl
import xlsxwriter

xl.App().visible = False
count_row = 2
workbook = xlsxwriter.Workbook(r'C:/Users/kuyto/Downloads/new_temp.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0,'screen_id')
worksheet.write(0,1,'width')
worksheet.write(0,2,'visible_range')
worksheet.write(0,3,'Latitude')
worksheet.write(0,4,'Longitude')
worksheet.write(0,5,'direction')
workbook.close()

def insert_value(count_row,list_of_direction,dict_of_item,k):
    
    wb_2 = xl.Book('C:/Users/kuyto/Downloads/new_temp.xlsx')
    ws_2 = wb_2.sheets["Sheet1"]
    # pass
    print(k)
    for z in range(k):
        # print(count_row)
        ws_2.cells(count_row,1).value=dict_of_item['screen_id']
        ws_2.cells(count_row,2).value=dict_of_item['width']
        ws_2.cells(count_row,3).value=dict_of_item['visible_range']
        ws_2.cells(count_row,4).value=dict_of_item['Latitude']
        ws_2.cells(count_row,5).value=dict_of_item['Longitude']
        ws_2.cells(count_row,6).value=list_of_direction[z]
        count_row += 1
    wb_2.save()
    wb_2.close()
    return count_row
    
df = pd.read_excel('C:/Users/kuyto/Downloads/Format.xlsx', sheet_name="Format v.3 22082022")

i = (len(df))


first_row = 3

for row in range(i-1): 
    wb = xl.Book('C:/Users/kuyto/Downloads/Format.xlsx')
    ws = wb.sheets["Format v.3 22082022"]
    dict_of_item = {}
    dict_of_item['screen_id'] = ws.cells(first_row + row,10).value
    dict_of_item['width'] = ws.cells(first_row + row,19).value
    dict_of_item['visible_range'] =ws.cells(first_row + row,21).value
    dict_of_item['Latitude'] =ws.cells(first_row + row,25).value
    dict_of_item['Longitude'] =ws.cells(first_row + row,26).value
    
    # num_of_direction= 0
    k = 0
    list_of_direction = []
    while k > -1:
        if ((ws.cells(first_row + row,27 + k).value != None) and (27 + k <= 42)):
            list_of_direction.append(ws.cells(first_row + row,27 + k).value)
            k += 1
            continue
        # print(count_row,list_of_direction,dict_of_item,k)
        wb.close()
        count_row = insert_value(count_row,list_of_direction,dict_of_item,k)
        break




# wb.save()
