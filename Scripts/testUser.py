import utils
from Api.apiFactory import ApiFactory
import app
import pytest,logging


class TestUserApi:

    @pytest.mark.run(order=0)
    def test_get_token(self):
        """获取token"""
        # 响应对象
        res = ApiFactory.get_user_api().get_token_api()
        # 打印 请求地址，请求参数，响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言token存在
        assert len(res.json().get("token")) > 0
        # 保存token
        app.headers["token"] = res.json().get("token")
        print("app.headers:{}".format(app.headers))

    def test_token_verify(self):
        """Token验证"""
        # 响应对象
        res = ApiFactory.get_user_api().token_verify_api()
        # 打印 请求地址，请求参数，响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言token有效
        assert res.json().get("isValid") is True

    def test_user_addr(self):
        """用户地址信息"""
        res = ApiFactory.get_user_api().user_address_api()
        # 打印 请求地址，请求参数，响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言地址信息
        assert False not in [i in res.text for i in ["大王","18888889999","上海市","浦东新区","111号"]]

