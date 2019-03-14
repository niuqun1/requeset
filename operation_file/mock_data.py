#coding:utf-8
from unittest import mock
#模拟mock 封装
def mock_test(mock_method,request_data,url,method,response_data):
    """

    :param mock_method:要返回数据的函数
    :param request_data:要返回的数据
    :param url:要返回的接口地址
    :param method:请求方式
    :param response_data:请求数据
    :return:
    """
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(mock_method,url,method,request_data)
    return res