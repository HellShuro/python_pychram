# -*- coding: UTF-8 -*-
import requests
class basis_requests():
    def __init__(self,url=None,form=None,header=None,**kwargs):
        self.url = url
        self.form = form
        self.header = header
        self.key = kwargs['key']
        print("发起请求: {}".format(self.url))

    # get请求
    # 需要提供url,form
    def basis_get(self):
        r = requests.get(url=self.url,params=self.form)
        r.encoding = 'utf-8'
        if r.status_code == 200:
            try:
                print("json")
                response = r.json()
                return response
            except:
                print("text")
                response = r.text
                return response
        else:
            print('请求失败 : {}'.format(r.status_code))

    # post请求
    # 需要提供url,form ,heander
    # 存在302响应问题
    def basis_post(self):
        r = requests.post(url = self.url,data=self.form,headers = self.header)
        r.encoding = 'utf-8'
        if r.status_code == 200 or r.status_code == 302 :
            try:
                print("json")
                response = r.json()
                return response
            except:
                print("text")
                response = r.text
                return response
        else:
            print('请求失败 : {}'.format(r.status_code))

if __name__ == '__main__':
    a = basis_requests()
    data = a.basis_post()
    print(data)
