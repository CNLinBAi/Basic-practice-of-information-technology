import requests
from bs4 import BeautifulSoup


def getHtml(url):
    """请求网页"""
    hd = {"User-Agent": "Mozilla/5.0"}  # 加入请求头
    r = requests.get(url, headers=hd, timeout=30)  # get请求方法
    r.encoding = "utf-8"  # r.apparent_encoding
    return r.text


def extrachhtml(html):
    "解析与提取网页信息"
    s = BeautifulSoup(html, "html.parser")  # 解析网页
    txt = s.find_all("p", class_="comment-content")
    # print(txt)
    context = ""
    for item in txt:
        d = item.get_text()  # 去掉标签只保留文字
        # print(d)
        context = context + d
        context.strip(" ")
    # print(context)
    save_text(context)  # 调用


def save_text(context):
    """存储文件"""
    with open("评论爬取.csv", "a", encoding="utf-8") as f:
        f.write(context)


for i in range(1, 20):
    url = f"https://book.douban.com/subject/35268372/comments/?limit={i * 20}&status=P&sort=new_score"
    html = getHtml(url)
    extrachhtml(html)

# 接下来，我们就对保存好的数据进行深加工。

# 制作词云，我们需要用到 wordcloud 模块、matplotlib 模块、jieba 模块，同样都是第三方模块，直接用 pip 进行安装。

from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import jieba
import numpy
from PIL import Image

# 去除一些词语
exclude = {"我的", "我", "得", "的", "有", "了", "是", "你"}

# 解析背景图片
mask_img = numpy.array(Image.open('C:/Users/Konfx/Desktop/HC/leaf.jpg'))

# 设置词云样式
simhei_path = r'C:\Users\Konfx\Desktop\HC\simhei.ttf'
wc = WordCloud(
    scale=5,  # 这个数值越大，产生的图片分辨率越高，字迹越清晰，最好不要超过64，运行很慢
    font_path=simhei_path,
    background_color='wheat',
    mask=mask_img)

# 接下来，我们要读取文本信息，进行分词并连接起来

# 读取文件内容
br = pd.read_csv('E:\CODE\pythonProject1\评论爬取.csv', header=None)  # 和上边保存数据的路径一样
# 进行分词，并用空格连起来
text = ''
for line in br[0]:
    text += ' '.join(jieba.cut(line, cut_all=False))

wc.generate(text)
plt.imshow(wc)  # 显示词云
plt.axis("off")  # 关闭坐标轴
plt.show()  # 显示图像