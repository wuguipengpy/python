import graphviz # doctest: +SKIP
from sklearn import tree
print(data.columns)
#ID3为决策树分类器fit之后得到的模型，注意这里必须在fit后执行，在predict之后运行会报错
dot_data = tree.export_graphviz(ID3, out_file=None,feature_names=data.columns[:-1],class_names=np.unique(y)) # doctest: +SKIP
graph = graphviz.Source(dot_data) # doctest: +SKIP
#在同级目录下生成tree.pdf文件
graph.render("tree") # doctest: +SKIP