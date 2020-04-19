import requests


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self,code ,mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【陈辉】您的验证码是#code#。有效期为1分钟，请尽快验证".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        import json
        re_dict = json.loads(response.text)
        return re_dict


# if __name__ == '__main__':
#     yun_pian = YunPian('261ee184839ff91be6d425c01cd416f2')
#     yun_pian.send_msg('1234'15659766216)
