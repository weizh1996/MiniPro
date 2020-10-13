from Api.apiFactory import ApiFactory

# # 调用轮播图api
# print("轮播图：{}".format(ApiFactory.get_home_api().banner_api().json()))
# # 调用专题栏api
# print("专题栏:{}".format(ApiFactory.get_home_api().theme_api().json()))
# # 调用最近新品api
# print("最近新品：{}".format(ApiFactory.get_home_api().recent_product_api().json()))

# # 调用商品分类
# print("商品分类:{}".format(ApiFactory.get_product_api().product_classify_api().json()))
# # 分类下的商品
# print("分类下的商品:{}".format(ApiFactory.get_product_api().classify_product_api().json()))
# # 商品信息
# print("商品信息:{}".format(ApiFactory.get_product_api().product_detail_api().json()))

# 调用用户获取token
# print("返回值:{}".format(ApiFactory.get_user_api().get_token_api().json()))

print("获取订单列表:{}".format(ApiFactory.get_order_api().get_order_list_api().json()))
print("创建订单:{}".format(ApiFactory.get_order_api().create_order_api(9,4).json()))
print("查看订单:{}".format(ApiFactory.get_order_api().query_order_api(110).json()))



