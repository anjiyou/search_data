"""
@File_name:    get/get_ershoufang
@Author:         liuwei
@Time:            2023/2/17 22:09
"""
import requests
from lxml import etree
import pandas as pd
from pyecharts.charts import Bar

url = "https://xz.lianjia.com/ershoufang/"
response = requests.get(url).content.decode()
html = etree.HTML(response)
div_list = html.xpath(".//div[@class='info clear']")
name_price_list = []
for div in div_list:
    name = div.xpath(".//div[@class='positionInfo']/a/text()")[0]
    price = div.xpath(".//div[@class='unitPrice']/span/text()")[0].replace(",","").replace("元/平","")
    name_price_list.append([name,price])
table = pd.DataFrame(name_price_list,columns=["小区名称","单价（元/平）"])
bar = Bar()
print(table)
bar.add_xaxis(list(table["小区名称"]))
bar.add_yaxis("徐州二手房价信息",list(table["单价（元/平）"]))
bar.render("./徐州二手房信息.html")