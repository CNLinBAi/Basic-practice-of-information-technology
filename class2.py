import requests
from bs4 import BeautifulSoup
import os
import time

#*创建存储图片的文件
def mkdir(path):
    path = path.strip()
    path = path.rstrip('\\')
    if os.path.exists(path):
        return False
    os.makedirs(path)
    return True

#*获取图片地址并下载
def get_img_src(url):
    # url = "https://www.xiaohua.com/"
    headers = {
        "Referer" : "https://www.xiaohua.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    resp = requests.get(url,verify=False,headers=headers)
    # print(resp.text)
    #*把源代码交给beautifulsoup
    main_page = BeautifulSoup(resp.text,"html.parser")
    alist = main_page.find("div",class_="content-left").find_all("div",class_="one-cont")
    # print(alist)
    for a1 in alist:#*循环列表，寻找每一张头像
        div1=a1.find("div",class_ = "one-cont-title clearfix")
        div2=div1.find("div",class_ = "one-cont-font clearfix")
        a = div2.find("a")
        em = a.find("em")
        img=em.find("img")
        src = img.get("src")#得到图片地址
        # print(src)
        img_resp = requests.get(src,headers=headers)#抓取图像网页
        # print(img_resp.text)
        filename = src.split("/")[-1]#文件命名
        #*下载图像
        with open(f'./img_load/{filename}',mode="wb") as f:
            f.write(img_resp.content)#地址字节
        print("over",src)
        time.sleep(1)

#*主函数运行
if __name__ == "__main__":
    mkdir('./img_load')#在当前文件下，创建文件夹以存储图像
    for i in range(1,20):#*获取第i页的内容
        url = f"https://www.xiaohua.com/hot?page={i}"
        get_img_src(url)