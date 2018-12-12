from urllib.request import urlopen
html = urlopen("https://zhuanlan.zhihu.com/p/40355137")
print(html.read())
