from graphviz import Digraph
# 항등식도 방정식인가요?
dict_fmt_input_1 = {
    "entity" : ["방정식", "항등식"],
    "property" : "상속",
    "db_entity_etc" : ["유한해방정식", "해가없는방정식"],
    "edge" : ["12", "13", "14"]
}
dict_vis_input_1 = {
    "node" : ["방정식", "항등식", "유한해방정식", "해가없는방정식"],
    "node_color" : ["blue", "blue", "black", "black"],
    "edge" : ["01", "02", "03"],
    "edge_color" : ["red", "black", "black"]
}

# 무리수도 단항식인가요?
dict_fmt_input_2 = {
    "entity" : ["무리수", "단항식"],
    "property" : "",
    "db_entity_etc" : "",
    "edge" : ""
}
dict_vis_input_2 = {
    "node" : ["무리수", "단항식"],
    "node_color" : ["black", "black"],
    "edge" : "",
    "edge_color" : ""
}


def vis_converter(dict_fmt_input):
    """
    """
    return dict_vis_input_1


def relation_1(vis_input_dict, filename):
    dot = Digraph(comment='vis_output', format='png')
    for i in range(0, len(vis_input_dict["node"])):
        dot.node(str(i), vis_input_dict["node"][i], color=vis_input_dict["node_color"][i], fontname="Sans Not-Rotated 14")
    for i in range(0, len(vis_input_dict["edge"])):
        dot.edge(vis_input_dict["edge"][i][0], vis_input_dict["edge"][i][1], color=vis_input_dict["edge_color"][i])

    print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
    dot.render('test-output/' + filename + '.gv', view=True)
    # dot.render('test-output/round-table.gv')

relation_1(dict_vis_input_1, 'type_1')
relation_1(dict_vis_input_2, 'type_2')

"""
    dot.node('0', 'A')
    dot.node('1', 'B')
    dot.node('2', 'C')
    dot.node('3', 'D')

    dot.edges(['01', '02', '03'])

"""

"""
    dot.node('A', 'King Arthur', color='red')
    dot.node('B', '<<u>Sir Bedevere the Wise</u>>', URL="http://iamaman.tistory.com/", target="_blank")
    dot.node('L', 'Sir Lancelot the Brave')

    dot.edges(['AC', 'AL'])
    dot.edge('B', 'L', constraint='false')
"""