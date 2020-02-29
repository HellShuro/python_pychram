# -*- coding: UTF-8 -*-
from socket import *
from wb.public_func.basis import basis_requests
import json


class Local_TCP():
    def __init__(self):
        self.host = "188.188.1.135"
        self.port = 9004
        self.buffsize = 20480
        self.ADDR = (self.host,self.port)

        self.tcptime = socket(AF_INET,SOCK_STREAM)
        self.tcptime.bind(self.ADDR)
        self.tcptime.listen(128)
        print(self.tcptime)

        self.url = ""
        self.form = {}
        self.head = {}
    def openTCP(self):
        while True:
            print('Wait for connection ...')
            # 客户端发来的请求,请求发来的地址
            req_client,req_addr = self.tcptime.accept()
            print("[{}][{}]用户连接上了".format(req_client,req_addr))

            data = req_client.recv(self.buffsize).decode("utf-8")

            print(data)
            arr = str(data).split('\n')
            data_list = []
            for i in arr:
                i = i.replace('\r', '')
                key_value = i.split(':')
                data_list.append(key_value)
            self.extrack_url(data_list)
            self.head = self.validation_head(data_list)
            content_length = self.validation_head(data,search="content_length")
            self.extrack_form(data_list)

            print("==============")
            print(self.form)
            print(self.head)
            print(self.url)
            print("%%%")
            print(content_length)
            print(len(self.form))
            print("============")

            if content_length != len(self.form):
                data1 = []
                req_client, req_addr = self.tcptime.accept()
                print("[{}][{}]用户单次传输，第二次获取数据".format(req_client, req_addr))
                data1 = req_client.recv(self.buffsize).decode("utf-8")
                print(data1)
                self.extrack_form(data1)
                print("第二次获取的数据解析后form显示：{}".format(self.form))


            url = "http://dailiintest01.szwbkj.cn/{}".format(self.url)

            req = basis_requests(url=url, form=self.form, header=self.head)
            rep = req.basis_post()

            print("---------")
            print(rep)
            print("----------0")
            send_rep = json.dumps(rep)

            h = "HTTP/1.1 200 OK\r\n"
            h+= "Server: nginx/1.10.2\r\n"
            # h += "Date: Tue, 26 Nov 2019 08:42:18 GMT\r\n"
            h += "Content-Type: application/json;charset=UTF-8\r\n"
            h += "Transfer-Encoding: chunked\r\n"
            h += "Access-Control-Allow-Origin: *\r\n"
            h += "Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE\r\n"
            h += "Access-Control-Max-Age: 3600\r\n"
            h += "Access-Control-Allow-Headers: *\r\n"
            h += "Access-Control-Allow-Credentials: true\r\n"
            h += "Access-Control-Expose-Headers: *\r\n"
            h += "Content-Encoding: gzip\r\n"
            h += "Vary: Accept-Encoding\r\n"
            h += "Connection: keep-alive\r\n"
            h += "\r\n"
            h +=send_rep

            req_client.send(bytes(h,encoding="utf-8"))

            req_client.close()

    def extrack_url(self, data):
        try:
            http_connect = data[0][0].split(" ")
            self.url = http_connect[1]
        except:
            pass
        return self.url

    def validation_head(self, data, search="UserKey"):
        for i in data:
            try:
                k = i[0].replace(" ", "")
                v = i[1].replace(" ", "")
                if i[0] == search:
                    value = i[0]
                    return value
            except:
                pass

    def extrack_form(self, data):
        try:
            raw = data[len(data)-1][0]
            dat = raw.split("&")[0:-1]
            for i in dat:
                j = i.split('=')[0]
                k = i.split('=')[1]
                self.form[j] = k

        except:
            pass
        return self.form

if __name__ == '__main__':
    Local_TCP().openTCP()