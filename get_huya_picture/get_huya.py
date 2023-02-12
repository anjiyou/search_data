"""
@File_name:    /get_huya
@Author:         liuwei
@Time:            2023/2/12 15:57
"""
import datetime
import os
from pathlib import Path
import requests
from lxml import etree

response = requests.get(url="https://www.huya.com/g/4079")
html = etree.HTML(response.text)
pic_list = html.xpath("//img[@class='pic']")
now_str = str(datetime.datetime.now().strftime("%Y-%d-%m~%H时%M分%S秒"))
pic_path = Path(f"D:/爬虫/美女/{now_str}")
if not pic_path.exists():
        os.mkdir(f"D:/爬虫/美女/{now_str}")
for pic in pic_list:
        pic_url = str(pic.xpath("./@data-original")[0])
        pic_url = pic_url.split("?")[0]
        pic_content = requests.get(url=pic_url).content
        pic_name = str(pic.xpath("./@alt")[0])
        with open(f"{pic_path}/{pic_name}.jpg",mode="wb") as f:
                f.write(pic_content)
                print(f"{pic_name}.jpg成功下载到->{pic_path}目录下")




