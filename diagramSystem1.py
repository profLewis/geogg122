import networkx as nx
import pylab as plt

plt.clf()
G=nx.MultiDiGraph()
H=nx.Graph(G)
G.add_edge('root /','/home')
G.add_edge('root /','/data')
G.add_edge('/data','/data/geospatial_10')
G.add_edge('/data/geospatial_10','/data/geospatial_10/plewis')
G.add_edge('/data/geospatial_10','/data/geospatial_10/ucfajlg')
G.add_edge('/home','/home/plewis')
G.add_edge('/home/plewis','/home/plewis/Data')
G.add_edge('/home/plewis','/home/plewis/msc')
G.add_edge('/home/plewis/msc','/home/plewis/msc/hello.dat')
G.add_edge('/home/plewis/msc','/home/plewis/msc/helloWorld.dat')
G.add_edge('/home/plewis/msc','/home/plewis/msc/head.dat')


pos=nx.spring_layout(G,iterations=2000)
#pos=nx.graphviz_layout(G)
#nx.draw_networkx_labels(G,pos,fontsize=14)
nx.draw(G,pos,node_size=0,alpha=0.4,edge_color='r',font_size=16)
plt.savefig("diagramSystem1.png")
plt.show()
