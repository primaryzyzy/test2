import requests
import json


class Translation(object):
    ''''''

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        }

    def requests_post(self, url, data):
        '''发送post，'''
        response = requests.post(url=url, data=data, headers=self.headers)
        # 将json字符串转化为字典返回
        return json.loads(response.content.decode())

    def langdetect(self):
        '''识别语言类型'''
        url = "https://fanyi.baidu.com/langdetect"
        data = {"query": self.query}
        response_dict = self.requests_post(url, data)
        # print(response_dict.get("lan"))
        return response_dict.get("lan")

    def extendtrans(self):
        '''翻译：中文翻译为英文，除中文外其他语言翻译成中文'''
        url = "https://fanyi.baidu.com/extendtrans"
        # if self.l_from == "zh":
        #     l_to = "en"
        # else:
        #     l_to = "zh"
        l_to = "en" if self.l_from == "zh" else l_to = "zh"
        data = {"query": self.query, "from": self.l_from, "to": l_to}
        # print(data)
        response_dict = self.requests_post(url, data)
        # 返回翻译结果，list型
        return response_dict["data"]["st_tag"]

    def run(self):
        ''''''
        self.query = input("input your word:")
        self.l_from = self.langdetect()
        print(self.extendtrans())


if __name__ == '__main__':
    Translation().run()
