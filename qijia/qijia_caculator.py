import pandas as pd
import xlrd
import xlwt as xlwt

EXCEL_IN = 'C:\workspace\python\qijia\qijia\月报分站模板-腾讯改.xlsx'
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


def get_whole_data_list(table, nrows, ncols):
    # 获取数据
    data = []
    for i in range(1, nrows):
        row_data = []
        for j in range(0, ncols):
            row_data.append(table.cell(i, j).value)
        data.append(row_data)
    return data

def calculate():
    excel = open_excel()
    # 整体消耗表
    whole_sheet = read_excel(excel,0)
    # 分账户消耗表
    part_sheet = read_excel(excel,1)
    # 整体消耗数据，转换为list
    whole_list = get_whole_data_list(whole_sheet[0], whole_sheet[1], whole_sheet[2])
    # 分账户消耗数据，转换为dict,key 为账户id，value为list
    part_dict = get_part_data_dict(get_whole_data_list(part_sheet[0], part_sheet[1], part_sheet[2]))
    # 遍历whole_list
    for i in range(len(whole_list)):
        # 当第9列差额为0或者空时，跳过
        if whole_list[i][3] == 0 or whole_list[i][3] == '':
            continue
        # 获取差值
        diff = whole_list[i][3]
        # 令当前第6列（地域消耗）=第8列（实际消耗）
        whole_list[i][2] = whole_list[i][1]
        # 令当前第9列（差额）=0
        whole_list[i][3] = 0
        # 获取地域消耗对应的账户消耗
        key_col =  whole_list[i][0].strip() if isinstance(whole_list[i][0],str) else whole_list[i][0]
        part_list = part_dict.get(key_col, [])
        # 当前地域的总消耗part_list中第3列的和
        part_sum = sum([x[2] for x in part_list])
        for j in range(len(part_list)):
            # 当前地域消耗占总消耗的比例
            part_ratio = part_list[j][2] / part_sum
            # 当前地域消耗占总消耗的比例 * 差值,保留两位小数
            part_list[j][2] = part_list[j][2] + round(part_ratio * diff, 3)
    # 将part_dict转换为list
    part_list = []
    for key in part_dict:
        part_list.extend(part_dict[key])
    return whole_list, part_list


def write_excel(data, name=EXCEL_OUT):
    #在已存在的excel中写入数据
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1')
    sheet2 = workbook.add_sheet('sheet2')
    # 用循环的方式给sheet3加第一列，第一个列为【账户,账户id,渠道,代理商,备注,消耗,赠款消耗,实际消耗,地域表,差额,账号ID,求和项:消耗]
    sheet1_col = ['ID','实际消耗','区域消耗','差额']
    sheet2_col = ['账号ID','城市','消耗']
    for i in range(len(sheet1_col)):
        sheet1.write(0, i, sheet1_col[i])
    for i in range(len(sheet2_col)):
        sheet2.write(0, i, sheet2_col[i])
    for i in range(len(data[0])):
        for j in range(len(data[0][i])):
            sheet1.write(i + 1 , j, data[0][i][j])
    for i in range(len(data[1])):
        for j in range(len(data[1][i])):
            sheet2.write(i + 1, j, data[1][i][j])
    workbook.save(name)


def get_part_data_dict(sheet_data):
    sheet_dict = {}
    for i in range(len(sheet_data)):
        # 将sheet_data[i][0]中的数据前后去空格
        key = sheet_data[i][0].strip() if isinstance(sheet_data[i][0],str) else sheet_data[i][0]
        if key not in sheet_dict:
            sheet_dict[key] = [sheet_data[i]]
        else:
            sheet_dict[key].append(sheet_data[i])
    # 将sheet_dict中value的list按照第4列从小到大排序
    for key in sheet_dict:
        sheet_dict[key].sort(key=lambda x: x[2])
    return sheet_dict



if __name__ == '__main__':
    data =calculate()
    write_excel(data)