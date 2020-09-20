"""
加载系统模块
"""
"""
加载python库
"""
from flask import Flask, render_template, json, request, redirect, session, jsonify, url_for
from werkzeug import generate_password_hash, check_password_hash
import numpy as np
import plotly as py
import plotly.graph_objs as go
import pandas as pd
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, ThemeType
from pyecharts.charts import Bar

# 基于Flask生成系统实例
app = Flask(__name__)


###### 系统功能
# 系统主界面
@app.route("/")
def main():
    pyplt = py.offline.plot
    labels = ["男性", "女性"]
    values = [50.17, 49.83]
    data = [go.Pie(labels=labels, values=values)]
    layout = go.Layout(
        title="冰岛男女比例（%）",
    )
    fig = go.Figure(data=data, layout=layout)
    div = pyplt(fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)

    labels = ["未婚父母", "已婚父母", "母亲", "父亲", "其他"]
    values = [67.61, 20.27, 10.61, 0.97, 0.54]
    trace = [go.Pie(labels=labels, values=values, hole=0.7, hoverinfo="label + percent")]
    layout = go.Layout(
        title="2017年冰岛0-5岁儿童的家庭成员组成情况",
    )
    fig = go.Figure(data=trace, layout=layout)
    div2 = pyplt(fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)

    context = {}
    context['graph'] = div
    context['graph2'] = div2
    return render_template('main.html', context=context)


@app.route("/page_second")
def page_second():
    pyplt = py.offline.plot
    df = pd.read_csv('data\\The divorce rate.csv', encoding='ANSI', index_col=['Name'])
    header_list = ['Name'] + list(df.columns)
    contents_list = []
    for i in range(len(df)):
        contents_list.append([df.index[i]] + df.iloc[i].values.tolist())
    x = [int(x) for x in df.columns.values]
    iceland = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Iceland', :].values, name='Iceland')
    switzerland = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['Switzerland', :].values, name='Switzerland')
    southkorea = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['SouthKorea', :].values, name='SouthKorea')
    nordic = go.Scatter(
        x=[pd.to_datetime('01/01/{y}'.format(y=x), format="%m/%d/%Y") for x in df.columns.values],
        y=df.loc['The Nordic countries', :].values, name='The Nordic countries')
    layout = dict(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=3,
             label="3年",
             step="year",
             stepmode="backward"),
        dict(count=5,
             label="5年",
             step="year",
             stepmode="backward"),
        dict(count=10,
             label="10年",
             step="year",
             stepmode="backward"),
        dict(count=20,
             label="20年",
             step="year",
             stepmode="backward"),
        dict(step="all")
    ])),
        rangeslider=dict(bgcolor="grey"),
        title='年份'
    ),
        yaxis=dict(title='不同地区总离婚率'),
        title="不同地区离婚情况"
    )
    fig = dict(data=[iceland, switzerland, southkorea, nordic], layout=layout)
    div = pyplt(fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)
    df1 = pd.read_csv('data\\The fertility rate.csv', encoding='ANSI', index_col=['Name'])
    header_list2 = ['Name'] + list(df1.columns)
    contents_list2 = []
    for i in range(len(df1)):
        contents_list2.append([df1.index[i]] + df1.iloc[i].values.tolist())
    trace_1 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['冰岛', :].values, name='冰岛')

    trace_2 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['世界水平', :].values, name='世界平均')

    trace_3 = go.Bar(
        x=[int(x) for x in df1.columns.values],
        y=df1.loc['欧洲联盟', :].values, name='欧盟')

    trace = [trace_1, trace_2, trace_3]

    layout = go.Layout(title="冰岛与欧盟国家、世界国家总生育率对比情况")

    fig = go.Figure(data=trace, layout=layout)
    div2 = pyplt(fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)
    context = {}
    context['graph'] = div
    context['graph2'] = div2
    context['header_list'] = header_list
    context['contents_list'] = contents_list
    context['header_list2'] = header_list2
    context['contents_list2'] = contents_list2
    return render_template('second.html', context=context)


@app.route("/page_third")
def page_third():
    pyplt = py.offline.plot
    df = pd.read_csv("data\\The proportion of women in the national parliament.csv", encoding='ANSI')
    header_list = [''] + list(df.columns)
    contents_list = []
    for i in range(len(df)):
        contents_list.append([df.index[i]] + df.iloc[i].values.tolist())
    x = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
          2017, 2018]
    y = [25.4, 25.4, 34.9, 34.9, 34.9, 34.9, 30.2, 30.2, 33.3, 33.3, 33.3, 33.3, 42.9, 42.9, 39.7, 39.7, 39.7, 39.7,
          41.3, 47.6, 47.6, 38.1, 38.1]
    iceland = go.Scatter(
        x=x,
        y=y,
    )
    layout = dict(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=3,
             label="3年",
             step="year",
             stepmode="backward"),
        dict(count=5,
             label="5年",
             step="year",
             stepmode="backward"),
        dict(count=10,
             label="10年",
             step="year",
             stepmode="backward"),
        dict(count=20,
             label="20年",
             step="year",
             stepmode="backward"),
        dict(step="all")
    ])),
        rangeslider=dict(bgcolor="grey"),
        title='年份'
    ),
        yaxis=dict(title='国家议会中女性参与的比例'),
        title="冰岛国家议会中女性参与的比例情况"
    )
    fig = dict(data=[iceland], layout=layout)
    div = pyplt(fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)
    df = pd.read_csv("data\\country_female_ployment rate.csv", encoding='ANSI')
    header_list2 = [''] + list(df.columns)
    contents_list2 = []
    for i in range(len(df)):
        contents_list2.append([df.index[i]] + df.iloc[i].values.tolist())

    map = (
        Map()
            .add("2019年(%)", list(zip(list(df.country), list(df.YS2019))), 'world')
            .add("2018年(%)", list(zip(list(df.country), list(df.YS2018))), 'world')
            .add("2017年(%)", list(zip(list(df.country), list(df.YS2017))), 'world')
            .add("2016年(%)", list(zip(list(df.country), list(df.YS2016))), 'world')
            .add("2015年(%)", list(zip(list(df.country), list(df.YS2015))), 'world')
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=150, min_=5),
            title_opts=opts.TitleOpts(title="全球女性就业比率"),
        )
    )
    df = pd.read_csv('data\\country_female_ployment rate1.csv', encoding='ANSI')
    header_list3 = [''] + list(df.columns)
    contents_list3 = []
    for i in range(len(df)):
        contents_list3.append([df.index[i]] + df.iloc[i].values.tolist())
    bar = (
        Bar()
            .add_xaxis(
            ['冰岛', '尼泊尔', '老挝', '瑞士', '荷兰', '澳大利亚', '加拿大', '丹麦', '越南', '挪威', '新西兰', '英国', '瑞典', '北美', '美国', '德国', '芬兰',
             '中国', '日本', '中国香港特别行政区', '马尔代夫', '爱尔兰', '新加坡', '巴西', '哥伦比亚', '泰国', '大韩民国', '不丹', '法国'])
            .add_yaxis("2017",
                       [76.71, 74.37, 63.56, 62.45, 61.61, 58.69, 56.96, 56.83, 52.24, 50.05, 51.29, 48.79, 45.85,
                        46.31, 44.77, 44.52, 41.81, 40.9, 41.4, 37.81, 37.96, 40.52, 35.95, 35.25, 34.42, 32.22, 31.03,
                        31.98, 25.53], gap="0%", color="#285171")
            .add_yaxis("2018",
                       [78.27, 74.35, 62.11, 62.58, 61.48, 58.61, 57.04, 56.72, 50.56, 49.97, 51.57, 49.02, 44.74, 46.4,
                        44.85, 44.22, 41.7, 40.53, 41.83, 37.18, 38.46, 41.61, 35.86, 35.69, 34.69, 32.32, 31.14, 30.7,
                        23.99], gap="0%", color="#82c0af")
            .add_yaxis("2019",
                       [76.36, 74.38, 63.28, 62.58, 61.63, 58.68, 57.19, 56.13, 53.21, 51.77, 51.04, 49.33, 46.17,
                        46.09, 44.94, 44.18, 43.14, 42.98, 40.79, 37.68, 37.55, 37.37, 36.19, 36.01, 35.27, 32.63,
                        30.93, 30.92, 26.14], gap="0%", color="#dad4b9")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各国女性就业率对比"),
            datazoom_opts=opts.DataZoomOpts(orient="vertical"))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .reversal_axis()
    )

    context = {}
    context['graph'] = div
    context['header_list'] = header_list
    context['contents_list'] = contents_list
    context['map'] = map.render_embed()
    context['header_list2'] = header_list2
    context['contents_list2'] = contents_list2
    context['bar'] = bar.render_embed()
    context['header_list3'] = header_list3
    context['contents_list3'] = contents_list3
    return render_template('third.html', context=context)


@app.route("/page_final")
def page_final():
    return render_template('final.html')


if __name__ == "__main__":
    # 运行 Flask 系统实例
    app.run()
