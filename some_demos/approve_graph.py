from graphviz import Digraph

gz = Digraph(
    "准入/合入流程图",
    "comment",
    None,
    None,
    "png",
    None,
    "UTF-8",
    {"rankdir": "TB"},
    {
        "color": "black",
        "fontcolor": "black",
        "fontname": "FangSong",
        "fontsize": "12",
        "style": "rounded",
        "shape": "box",
    },
    {
        "color": "#999999",
        "fontcolor": "#888888",
        "fontsize": "16",
        "fontname": "SongTi",
    },
    None,
    False,
)

gz.node("0", "准入/合入")
gz.node("1", "是否是最新RB分支", shape="diamond")
gz.node("2", "是否可以cherry_pick\n(commit数量是否为1 && 合并是否有冲突)", shape="diamond")
gz.node("3", "是否是最新的DEV", shape="diamond")
gz.node("4", "直接approve")
gz.node("5", "不会创建流水线")
gz.node("6", "cherry pick")
gz.node("7", "提示用户手工合入")
gz.node("8", "cherry pick是否成功?", shape="diamond")
gz.node("9", "approve&merge")
gz.node("a", "")
gz.edge("0", "1")
gz.edge("1", "2", label="是")
gz.edge("1", "3", label="否")
gz.edge("3", "4", label="是")
gz.edge("3", "5", label="否")
gz.edge("2", "6", label="是")
gz.edge("2", "7", label="否")
gz.edge("6", "8")
gz.edge("8", "9", label="是")
gz.edge("8", "7", label="否")
# gz.node('2','直播页面')
# gz.node('a','现场会议')
# gz.node('b','报名')
# gz.node('i','报名')
# gz.node('c','选择门票')
# gz.node('d','填写需求单')
# gz.node('j','填写需求单')
# gz.node('e','报名成功',{'color':'red','fontcolor':'red'})
# gz.node('f','订单页面')
# gz.node('g','报名购票成功',{'color':'red','fontcolor':'red'})

# t=set(['01','0a','12'])
# a=set(['ab','bd','de'])
# b=set(['ab','be'])
# c=set(['ac','ci','ij','jf','fg'])
# d=set(['ac','ci','if','fg'])
# gz.edges(a|b|c|d|t)
# gz.edge('c','f','已报名')
# print(gz.source)
gz.view()
