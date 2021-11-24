import xlsxwriter


def execute_excel(data):
    str_path = r'E:\py_workspace\graduation\data.xlsx'
    workbook = xlsxwriter.Workbook(str_path)
    worksheet = workbook.add_worksheet('学生')

    cell_f = workbook.add_format({"bold": True})
    cell_f.set_font('黑体')
    cell_f.set_font_color('blue')
    cell_f.set_align('center')

    worksheet.write(0, 0, '学号', cell_f)
    worksheet.write(0, 1, '课程', cell_f)
    worksheet.write(0, 2, '签到时间', cell_f)
    worksheet.write(0, 3, '签到状态', cell_f)
    worksheet.write(0, 4, '异常原因', cell_f)

    worksheet.set_column('A:A', 15)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 15)
    worksheet.set_column('D:D', 10)
    worksheet.set_column('E:E', 15)

    style = workbook.add_format({
        "fg_color": "yellow",  # 单元格的背景颜色
        # "bold": 1,  # 字体加粗
        "align": "left",  # 对齐方式
        "valign": "vcenter",  # 字体对齐方式
        "font_color": "red"  # 字体颜色
    })

    for i, item in zip(range(1, len(data) + 1), data):
        worksheet.write_string(i, 0, item[0])
        worksheet.write_string(i, 1, item[1])
        worksheet.write_string(i, 2, str(item[2]))
        worksheet.write_string(i, 3, item[3])
        if item[3] == '失败':
            worksheet.write(i, 3, "失败", style)
        worksheet.write_string(i, 4, item[4])

    workbook.close()
    return workbook
