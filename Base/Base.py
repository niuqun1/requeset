#coding:utf-8
import requests
import json
class RunMethod:
	def post_main(self,url,data,header=None):#post请求
		res = None
		if header !=None:#若果header不为空
			res = requests.post(url=url,data=data,headers=header)
		else:
			res = requests.post(url=url,data=data)
		return res.json()

	def get_main(self,url,data=None,header=None):#get请求
		res = None
		if header !=None:
			res = requests.get(url=url,data=data,headers=header)
		else:
			res = requests.get(url=url,data=data)
		return res.json()

	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'Post':#判断请求方式
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)#格式化返回值
if __name__ == '__main__':
	url = 'https://p-api-test.kanche.com/v1/crmpassport/login'
	data = """{
        "username":"10000000888",
        "password":"uat.portal"
    }"""
	Headers = {
		"Content-Type": "application/json",
		'x-target-app': 'app_xiaomada_android'
	}
	run =RunMethod()
	print (run.run_main('Post',url,data,Headers))
	print(Headers)
