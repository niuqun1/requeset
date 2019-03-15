# coding:utf-8
from Base.Base import RunMethod
from get_data.get_data import GetData
import json
from jsonpath_rw import jsonpath,parse
from operation_file.operation_excel import OpenrationExcel
class DependdentData:
    def __init__(self,case_id):
        self.case_id=case_id
        self.data=GetData()
        self.opera_excel=OpenrationExcel()
        # 获取casr_id去获取该casr——id正航数据
    def get_case_line_data(self):
        rows_data=self.opera_excel.get_rows_data(self.case_id)
        return rows_data#返回依赖接口的所属行
    def run_depemdent(self):
        run_menthon=RunMethod()
        row_num=self.opera_excel.get_row_num(self.case_id)#执行数据依赖的行数获取结果
        data=self.data.get_data_for_json(row_num)
        request_data=json.dumps(data)
        header=self.data.is_headel(row_num)
        method=self.data.get_request_method(row_num)
        url=self.data.get_request_url(row_num)
        res=run_menthon.run_main(method,url,request_data,header)#传入所需行的请求数据
        return json.loads(res)#返回所需行的接口返回数据

    def get_data_for_key(self,row):
        depend_data=self.data.get_depend_key(row)#获取依赖上个接口的字段
        response_data=self.run_depemdent()#获取依赖接口返回的数据
        json_exe=parse(depend_data)
        madle=json_exe.find(response_data)
        return [math.value for math in madle][0]#数据依赖的具体数据


if __name__ == '__main__':
    order = {'data': {'crmUserId': '710b3e8041a4418b875be99f3d9e3208', 'token': '82c8924c618a42d38e7d2916aecf2302', 'userId': '5c2d7d2931000051108ab225'}, 'errorCode': '', 'errorMsg': '', 'ok': True}
    res = "data.crmUserId"
    json_exe = parse(res)
    madle = json_exe.find(order)