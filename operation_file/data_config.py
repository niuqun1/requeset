#coding:utf-8
class global_var:
    id="0"#用例id
    url='2'#测试接口地址
    run='3'#是否允许
    request_way='4'#接口请求类型
    header='5'#herder
    case_depend='6'#依赖的用例id
    data_depend='7'#依赖数据的data
    field_depend='8'#数据依赖字段
    data='9'#接口请求数据
    expect='10'#预期结果
    resuit='11'#时间结果
    data_herder='12'#herder
    # 用例id
def get_id():
    return global_var.id
# 接口地址
def get_url():
    return global_var.url
# 是否运行
def get_run():
    return  global_var.run
# 请求方式
def get_request_way():
    return global_var.request_way
# 是否需要header
def get_header():
    return global_var. header
# case依赖
def get_case_depend():
    return  global_var.case_depend
# 依赖的返回数据
def get_data_depend():
    return global_var.data_depend
# 数据依赖字段
def get_dield_depend():
    return global_var.field_depend
# 请求数据
def get_data():
    return  global_var.data
# 预期结果
def get_dield_expect():
    return global_var.expect
# 实际结果
def get_resuit():
    return  global_var.resuit
# 获取header
def get_header_value():

    return global_var.data_herder
def get_field_deoend():
    return global_var.field_depend




