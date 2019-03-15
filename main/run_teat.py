# coding:utf-8
from Base.Base import RunMethod
from get_data.get_data import GetData
from operation_file.comonutil import CommonUtil
from data.dependdent_data import DependdentData
import json
class RunTest:
    def __init__(self):
        self.run_method=RunMethod()
        self.data=GetData()
        self.com_util=CommonUtil()
    # 程序执行流程
    def go_on_run(self):
        res=None
        # 获取所有行
        roes_count=self.data.get_case_lines()
        # 跳过1在行里循环
        for i in range(1,3):
            is_run = self.data.get_is_run(i)
            if is_run:#执行
                url=self.data.get_request_url(i)#接口地址
                method=self.data.get_request_method(i)#请求方式
                aaa=self.data.get_data_for_json(i)#请求数据
                data=json.dumps(aaa)
                expect=self.data.get_expcet_data(i)#预期结果
                header=self.data.is_headel(i)#获取header
                depend_case=self.data.is_depend(i)#获取是否有数据依赖
                if depend_case !=None:#判断数据依赖不是空
                    self.depend_data=DependdentData(depend_case)#实列化depend_data
                    depend_response_data=self.depend_data.get_data_for_key(i)#获取依赖返回data
                    # 获取依赖的key
                    depend_key=self.data.get_depend_field(i)#获取数据依赖字段
                    aaa[depend_key]=depend_response_data
                    print(aaa)
                res=self.run_method
                if is_run:#判断是否执行
                    res=self.run_method.run_main(method,url,data,header)
                    if self.com_util.is_contain(expect,res):#判断预期结果
                        self.data.write_result(i,"测试通过")
                    else:
                        self.data.write_result(i,"测试失败")
                print(res)

if __name__=="__main__":
    run=RunTest()
    print(run.go_on_run())