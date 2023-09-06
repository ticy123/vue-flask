import pandas as pd
import xlrd
import xlwt as xlwt

EXCEL_IN = r'C:\workspace\python\vue-flask\qijia\excel\工作簿1.xlsx'
EXCEL_OUT = EXCEL_IN.split('.')[0] + '111.xlsx'

def open_excel(name=EXCEL_IN):
    # 打开excel
    data = xlrd.open_workbook(name)
    return data

def read_excel(data, sheet=0):
    # 读取excel
    table = data.sheets()[sheet]
    nrows = table.nrows
    ncols = table.ncols
    return table, nrows, ncols


def get_data_list(table, nrows, ncols):
    # 获取数据
    data = []
    for i in range(1, nrows):
        row_data = []
        for j in range(0, ncols):
            row_data.append(table.cell(i, j).value)
        data.append(row_data)
    return data

def run():
    excel = open_excel()
    #sheet1
    qudao_sheet = read_excel(excel, 0)
    #sheet2
    city_sheet = read_excel(excel, 1)
    qudao_data = get_data_list(qudao_sheet[0], qudao_sheet[1], qudao_sheet[2])
    city_data = get_data_list(city_sheet[0], city_sheet[1], city_sheet[2])
    avg_data = calculate(qudao_data,city_data)
    wirit_to_excel(qudao_data,avg_data)


def calculate(qudao_data,city_data):
    res = []
    for i in range(len(qudao_data)):
        qudao_name = qudao_data[i][0]
        daili_name = qudao_data[i][3]
        avg_amount = round(float(qudao_data[i][4]) / len(city_data),3)
        for j in range(len(city_data)):
            city_name = city_data[j][0]
            res.append([qudao_name,daili_name,city_name,avg_amount])
    return res

def wirit_to_excel(qudao_data,avg_data,name=EXCEL_OUT):
    # 在已存在的excel中写入数据
    workbook = xlwt.Workbook()
    write_to_sheet(workbook,qudao_data,['渠道','主题','账号','代理','消耗'],'sheet1')
    write_to_sheet(workbook,avg_data,['渠道','代理','城市','消耗'],'sheet2')
    workbook.save(name)

def write_to_sheet(workbook,data,col,sheet_name):
    sheet = workbook.add_sheet(sheet_name)
    for i in range(len(col)):
        sheet.write(0, i, col[i])
    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.write(i+1, j, data[i][j])
    return sheet

if __name__ == '__main__':
    run()