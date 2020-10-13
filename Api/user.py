import app, requests,logging


class UserApi:

    def __init__(self):
        # 获取token
        self.get_token_url = app.base_url + "/token/user"
        # token验证
        self.token_verify_url = app.base_url + "/token/verify"
        # 用户地址信息
        self.user_addr_url = app.base_url + "/address"

    def get_token_api(self):
        """获取token"""
        logging.info("用户-获取token")
        # 请求体
        data = {"code": app.code}
        # 请求参数
        logging.info("请求参数:{}".format(data))
        # 返回请求对象
        return requests.post(self.get_token_url, json=data, headers=app.headers)

    def token_verify_api(self):
        """Token验证"""
        logging.info("用户-Token验证")
        # 请求体
        data = {"token": app.headers.get("token")}
        # 请求参数
        logging.info("请求参数:{}".format(data))
        # 返回请求对象
        return requests.post(self.token_verify_url, json=data, headers=app.headers)

    def user_address_api(self):
        """用户地址信息"""
        logging.info("用户-用户地址信息")
        # 返回请求对象
        return requests.get(self.user_addr_url,headers=app.headers)
