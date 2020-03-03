# -*- coding: UTF-8 -*-
from socket import *
from wb.public_func.basis import basis_requests
import json
import urllib.parse
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
            self.url = ""
            self.form = {}
            self.head = {}
            # 客户端发来的请求,请求发来的地址
            req_client,req_addr = self.tcptime.accept()
            print("[{}][{}]用户连接上了".format(req_client,req_addr))
            data = req_client.recv(self.buffsize).decode("utf-8")
            data = urllib.parse.unquote(data)

            print(data)

            arr = str(data).split('\n')
            data_list = []
            for i in arr:
                i = i.replace('\r', '')
                key_value = i.split(':')
                data_list.append(key_value)

            self.extrack_url(data_list)
            self.validation_head(data_list)
            content_length = self.validation_head(data=data_list,search="Content-Length")
            self.extrack_form(data_list)

            print("第一次获取客户端数据=================================================================================")
            print(self.form)
            print(self.head)
            print(self.url)
            print(content_length)
            print(len(data_list[-1][0]))
            print("第一次获取客户端数据=================================================================================")

            if int(content_length) != len(data_list[-1][0]):
                # req_client, req_addr = self.tcptime.accept()
                print("用户单次传输，第二次获取数据".format(req_client, req_addr))
                data1 = req_client.recv(self.buffsize).decode("utf-8")
                print(data1)
                self.extrack_form(data1)

                print("第二次获取客户端数据=================================================================================")
                print(self.form)
                print(self.head)
                print(self.url)
                print(content_length)
                print(len(data_list[-1][0]))
                print("第二次获取客户端数据=================================================================================")

            url = "http://dailiintest01.szwbkj.cn/{}".format(self.url)

            req = basis_requests(url=url, form=self.form, header=self.head)
            rep = req.basis_post()

            print("---------")
            print(rep.headers)
            print(type(rep.headers))
            print(rep.text)
            print(type(rep.text))
            print(rep.status_code)
            print("----------0")
            send_head = json.dumps(dict(rep.headers))

            json_head = json.loads(send_head)
            print(json_head)
            print(type(json_head))

            send_headers = ""

            send_headers += "HTTP/1.1 200\r\n"

            for n in json_head:
                if n == "Content-Encoding" or n == "Transfer-Encoding":
                    pass
                else:
                    m = "{}:{}\r\n".format(n, json_head[n])
                    send_headers += m

            # send_headers += "Server:nginx\r\n"
            # send_headers += "Content-Type: application/json;charset=UTF-8\r\n"
            # # send_headers += "Transfer-Encoding: chunked\r\n"
            # send_headers += "Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE\r\n"
            # send_headers += "Access-Control-Max-Age: 3600\r\n"
            # send_headers += "Access-Control-Allow-Headers: *\r\n"
            # send_headers += "Access-Control-Allow-Credentials: true\r\n"
            # send_headers += "Access-Control-Expose-Headers: *\r\n"
            # # send_headers += "Content-Encoding: gzip\r\n"
            # send_headers += "Vary: Accept-Encoding\r\n"
            # send_headers += "Connection: keep-alive\r\n"

            send_headers += "\r\n"
            send_headers += rep.text

            print("------------------------------------------------------------------------------------")
            print(send_headers)
            print("------------------------------------------------------------------------------------")

            req_client.send(bytes(send_headers,encoding="utf-8"))
            print(bytes(send_headers,encoding="utf-8"))

            req_client.close()

    def extrack_url(self, data):
        try:
            http_connect = data[0][0].split(" ")
            self.url = http_connect[1]
        except:
            pass
        return self.url

    def validation_head(self, data, search=None):
        for i in data:
            try:
                k = i[0].replace(" ", "")
                v = i[1].replace(" ", "")
                if k == "Host":
                    pass
                else:
                    self.head[k] = v
            except:
                pass

        if search is None:
            return
        else:
            return self.head[search]

    def extrack_form(self, data):
        try:
            if type(data) == list:
                raw = data[len(data)-1][0]
            else:
                raw = data
            dat = raw.split("&")[0:-1]

            for i in dat:
                j = i.split('=')[0]
                k = i.split('=')[1]
                if j == "password":
                    k = "jgY97tTBRtrnl1T76B3lmt1t73ip1PRg9RHnYiuAj3fT4WnmInY1X9L+AjWMSfFy0/XA2trUBwLdYDurC4E7hILeUsfPu/IN8Dp+876PHxyX0cJazSNWyZ2hyXPpJ7ww8IESN6TsgyBdfc2wBKbGf4ffGwVvKUyJErvgcVsO85Q="
                    self.form[j] = k
                else:
                    self.form[j] = k
        except:
            pass
        return self.form

if __name__ == '__main__':
    Local_TCP().openTCP()