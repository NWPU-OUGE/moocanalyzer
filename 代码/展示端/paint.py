line = (
    Line()
    #添加x轴数据
    .add_xaxis(country)
    #添加y轴数据
    .add_yaxis("各国分布数",country_count, markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"), #标记最大值
                opts.MarkPointItem(type_="min", name="最小值"), #标记最小值
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")] #标记平均值线
        ),)
    #折线图标题及位置
    .set_global_opts(title_opts=opts.TitleOpts(title="海外分布", pos_left = "30%"))
)

pie = Pie()
#add第一个参数为标签（一般为空就行）
#第二个参数为整合的数据
#第三个参数center为饼图圆心在的位置
#第四个参数rosetype = ’radius‘ 表示要画玫瑰饼图
#第五个参数为标签配置项，这里选择不显示标签
pie.add('', list(zip(country, country_count)), center = ["75%", "40%"],
        rosetype = "radius", label_opts = opts.LabelOpts(is_show = False))
pie.set_global_opts(
    title_opts = opts.TitleOpts(
        #饼状图标题
        title = '海外各国分布占比',
        #标题位置
        pos_left = "70%",
        title_textstyle_opts = opts.TextStyleOpts(
            #标题颜色
            color = 'black',
            #标题大小
            font_size = '12'
        )
    ),
    #图例配置项
    legend_opts = opts.LegendOpts(
        #是否显示图例
        is_show = True,
        #图例纵向排列
        orient = 'vertical',
        #图例位置
        pos_left = "90%"
    )
)
#radius = [70, 100]表示圆环大小,半径70-100的部分
#后面的表示饼图数据显示为百分比形式
pie.set_series_opts(radius=[70, 100], label_opts=opts.LabelOpts(formatter='{b} : {d}%'))

grid = (
    Grid(
        init_opts=opts.InitOpts(
            #并行图主题为浅色
            theme='light',
            #并行图宽度为1200像素
            width='1200px',
        )
    )
    #添加折线图，不显示边框，折线图高度大小，折线图位置
    .add(line, grid_opts=opts.GridOpts(is_show=False, height='50%', pos_right='55%'))
    #添加饼图，不显示边框，饼图高度大小，饼图位置
    .add(pie, grid_opts=opts.GridOpts(is_show=False, height='50%', pos_left='50%'))
)

#渲染成html文件
grid.render('海外分布统计图.html')