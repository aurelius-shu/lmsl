#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import xlrd

excel_path = r'D:\WorkSpace\projects\datahub-client\app_data\datahub-client-tests.xlsx'
excel_result = r'D:\WorkSpace\projects\datahub-client\app_data\result.xlsx'
d = pd.read_excel(excel_path, sheet_name='数据完整性测试 50')
d = d[1:]
d.columns = ['table', 'counts', 'test1', '', '', 'test2', '', '', 'size']
result = pd.DataFrame({
    'table': d['table'],
    'counts': d['counts'],
    'test1': d['test1'],
    'test2': d['test2'],
    'lose_rows1': d['counts'] - d['test1'],
    'lost_packages1': (d['counts'] - d['test1']) / d['size'],
    'lose_rows2': d['counts'] - d['test2'],
    'lost_packages2': (d['counts'] - d['test2']) / d['size'],
    'size': d['size'],
})
print(result)
result.to_excel(excel_result, sheet_name='result')
