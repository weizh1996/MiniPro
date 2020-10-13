import app, requests,logging


class OrderApi:

    def __init__(self):
        # 获取用户订单列表
        self.get_order_list_url = app.base_url + "/order/by_user"
        # 创建订单
        self.create_order_url = app.base_url + "/order"
        # 查看订单
        self.query_order_url = app.base_url + "/order/{}"

    def get_order_list_api(self, page=1):
        """
        获取订单列表
        :param page: 订单页数
        :return:
        """
        logging.info("订单-获取订单列表")
        # 参数
        data = {"page": page}
        # 请求参数
        logging.info("请求参数:{}".format(data))
        # 返回响应对象
        return requests.get(self.get_order_list_url, params=data, headers=app.headers)

    def create_order_api(self, products_id, count):
        """
        创建订单
        :param products_id: 产品id
        :param count: 购买数量
        :return:
        """
        logging.info("订单-创建订单")
        # 参数
        data = {"products":[{"product_id":products_id,"count":count}]}
        # 请求参数
        logging.info("请求参数:{}".format(data))
        # 返回响应对象
        return requests.post(self.create_order_url, json=data, headers=app.headers)

    def query_order_api(self, order_id):
        """
        查看订单
        :param order_id: 订单id编号
        :return:
        """
        logging.info("订单-查看订单")
        return requests.get(self.query_order_url.format(order_id), headers=app.headers)
