# coding:utf-8
# 获取数据
import json
from operation_file import data_config
from operation_file.operation_excel import OpenrationExcel
class GetData:
    def __init__(self):
        self.opera_excel=OpenrationExcel()
        # 获取excel行数
    def get_case_lines(self):
        return self.opera_excel.get_lines()#获取excel行数
    # 获取是否执行
    def get_is_run(self,row):#判断是否运行
        flag=None
        col=int(data_config.get_run())
        run_model=self.opera_excel.get_cell_value(row,col)#获取是否运行内容
        if run_model=="yes":
            flag = True
        else:
            flag = False
        return flag
    # 获取herder数据
    def is_herder_data(self,row):#获取herder内容
        col = int(data_config.get_header_value())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method#返回herder

    def is_headel(self,row):#判断是否需要herder
        col=int(data_config.get_header())
        header=self.opera_excel.get_cell_value(row,col)#获取是否需要herder内容
        if header=="yes":
            d1 = json.loads(self.is_herder_data(row))
            return d1#返回herder数据
        else:
            return None
    def get_request_method(self,row):#获取请求方式
        col=int(data_config.get_request_way())
        request_method=self.opera_excel.get_cell_value(row,col)
        return request_method
    def get_request_url(self,row):#获取接口地址
        col=int(data_config.get_url())
        url=self.opera_excel.get_cell_value(row,col)
        return  url
    def get_request_data(self,row):#获取接口请求数据
        col=int(data_config.get_data())
        data=self.opera_excel.get_cell_value(row,col)
        if data=='':
            return None
        return data
    def get_expcet_data(self,row):#获取预期结果
        col=int(data_config.get_dield_expect())
        expect=self.opera_excel.get_cell_value(row,col)
        if expect=="":
            return None
        return expect
    def write_result(self,row,value):#讲预期结果写入excel
        col=int(data_config.get_resuit())
        self.opera_excel.write_value(row,col,value)
    def get_depend_key(self,row):#获取数依赖key
        col=int(data_config.get_data_depend())
        depent_key=self.opera_excel.get_cell_value(row,col)
        if depent_key=="":
            return None
        else:
            return depent_key
    def is_depend(self,row):        # 判断是否有数据依赖
        col=int(data_config.get_case_depend())
        depend_keys_id=self.opera_excel.get_cell_value(row,col)
        if depend_keys_id=="":
            return None
        else:
            return depend_keys_id
    def get_depend_field(self,row):# 获取数据依赖字段
        col=int(data_config.get_field_deoend())
        data=self.opera_excel.get_cell_value(row,col)
        if data=="":
            return None
        else:
            return data
