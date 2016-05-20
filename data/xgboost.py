import xgboost as xgb

general_parameter={'objective':'reg:linear'}

from graphviz import Digraph
dot=Digraph(comment='test')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
#print dot
#print dot.source
dot.render('./a', view=True)