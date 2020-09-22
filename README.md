# python-finally：项目名称：分析“乌托邦式”下冰岛女性婚姻观的形成
## 问题表述：
### 1. 项目为什么要这样做
1. 探讨“乌托邦式”下冰岛女性婚姻观的形成，对于研究不同地区环境下女性的婚姻观的形成有相应的参考意义
### 2. 用户需求
- 使用场景：女性婚姻研究人员对于冰岛女性婚姻观的研究，希望能得到一份较直观的分析图表
- 任务：快速得到一份冰岛女性状况的研究数据
- 痛点：网络上对于此项的研究数据较少，而且不是很直观
Python website based on Flask
## 展示页面URL:
http://penwey.pythonanywhere.com/
## 使用到的Python module
numpy
pandas
flask
werkzeug
plotly
pyecharts
## 文档描述
- data: website data
- statisc: html java script and css script
- templates: 放置html page
- main.html: 网站第一页面的内容
- second.html: 网站第二页面的内容
- third.html: 网站第三页面的内容
- final.html: 网站最后页面的内容
- app.py: flask的入口程序文件：定义函数（def），使用循环语句（if）等等！！
## webapp 动作
- 一共设置了四个页面
- 第一页为首页面介绍分析“乌托邦式”下冰岛女性婚姻观的形成下数据故事的背景，引入接下来的分析内容，内容接近结尾处将通过两种情况对内容深入分析，因此设置了两个分页面的按钮（冰岛高生育率和高离婚率）和（冰岛女性社会地位），点击可分别进入第二页面和第三页面。

- 其中冰岛高生育率和高离婚率和冰岛女性社会地位顶部设置了返回的按钮,点击即可回到首页面。
- 尾页为项目的总结：冰岛女性不婚较多的原因。
