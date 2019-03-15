# 操作excel封装
#coding:utf-8
import xlrd
from xlutils.copy import copy
class OpenrationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        """

        :param file_name: excel的存储路径
        :param sheet_id:
        """
        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id
        else:
            self.file_name='D:\qq\data_excel.xlsx'
            self.sheet_id=0
        self.data=self.get_data()
    # 获取sheets内容
    def get_data (self):
        data = xlrd.open_workbook(self.file_name,)
        tables = data.sheets()[self.sheet_id]
        return tables
    # 获取行数
    def get_lines(self):
        tables=self.data
        return tables.nrows
    # 获取单元格内容
    def get_cell_value(self,row,col):
        """

        :param row: excel的行
        :param col: excel的第几格
        :return:
        """
        return self.data.cell_value(row,col)
    # 将数据写入excel
    def write_value(self,row,col,vale):
        read_data=xlrd.open_workbook(self.file_name)
        write_data=copy(read_data)
        sheet_data=write_data.get_sheet(0)
        sheet_data.write(row,col,vale)
        write_data.save(self.file_name)
    # 根据csse_id 找到对应行的内容
    def get_rows_data(self,casr_id):
        row_num=self.get_row_num(casr_id)
        rows_data=self.get_row_values(row_num)
        return rows_data

   # 根据对应caseid找到对应行号
    def get_row_num(self,case_id):
        num= 0
        clols_data=self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num=num+1
   # 根据行号，找到该行内容
    def get_row_values(self,row):
        tables=self.data
        row_data=tables.row_values(row)
        return row_data
    # 获取某一列内容
    def get_cols_data(self,col_id=None):
        if col_id!=None:
            cols=self.data.col_values(col_id)
        else:
            cols=self.data.col_values(0)
        return cols
if __name__=='__main__':
    Opers=OpenrationExcel()
    print(Opers.get_data().nrows)
    print(type(Opers.get_cell_value(1,9)))
    print((Opers.get_cell_value(1,9)))


