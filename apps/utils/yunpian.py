import requests


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_msg(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【陈辉你好】您的验证码是#code#。我就是来测试的，请给通过审核"
        }

        response = requests.post(self.single_send_url, data=parmas)
        import json
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    yun_pian = YunPian('key')
    yun_pian.send_msg('123456', 15659766216)
