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

        request_data=self.data.get_request_data(row_num)
        header=self.data.is_headel(row_num)
        method=self.data.get_request_method(row_num)
        url=self.data.get_request_url(row_num)
        res=run_menthon.run_main(method,url,request_data,header)#传入所需行的请求数据
        return json.loads(res)#返回所需行的接口返回数据
    def get_data_for_key(self,row):
        depend_data=self.data.get_depend_key(row)
        response_data=self.run_depemdent()
        json_exe=parse(depend_data)
        madle=json_exe.find(response_data)
        return [math.value for math in madle][0]#数据依赖的具体数据


if __name__ == '__main__':
    order = {
		"data": {
			"_input_charset": "utf-8",
			"body": "慕课网订单-1710141907182334",
			"it_b_pay": "1d",
			"notify_url": "http://order.imooc.com/pay/notifyalipay",
			"out_trade_no": "1710141907182334",
			"partner": "2088002966755334",
			"payment_type": "1",
			"seller_id": "yangyan01@tcl.com",
			"service": "mobile.securitypay.pay",
			"sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
			"sign_type": "RSA",
			"string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
			"subject": "慕课网订单-1710141907182334",
			"total_fee": 299
			},
			"errorCode": 1000,
			"errorDesc": "成功",
			"status": 1,
			"timestamp": 1507979239100
		}
    res = "data.out_trade_no"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print([math.value for math in madle][0])