import networkx as nx
import pylab as plt
import numpy as np

# this is far from perfect, but does a reasonable job

plt.clf()
G=nx.MultiDiGraph()

names = np.array(['/data/geospatial_10','/data/geospatial_20','/home/ucfajlg/README',\
                  '/home/plewis/msc/helloWorld.dat','/home/plewis/msc/hello.dat',\
                  '/home/plewis/msc/head.dat'])
all = {}
for nn in names:
  thisN = nn.split('/')
  for i in xrange(len(thisN)):
    try:
      all[i].append(thisN[i])
    except:
      all[i] = [thisN[i]] 

xpos = {}
ypos = {}
for k in all.keys():
  all[k] = np.unique(all[k])
  xpos[k] = np.arange(len(all[k]))*200 - (len(all[k])-1)*200/2
  ypos[k] = k * -200


for nn in names:
  thisN = ['/' + i for i in nn.split('/')]
  for i in xrange(1,len(thisN)):
    G.add_edge(thisN[i-1],thisN[i])

pos = {}
for nn in names:
  thisN = ['/' + i for i in nn.split('/')]
  for level in xrange(len(thisN)):
    thisAll = all[level]
    ww = np.where(thisAll == thisN[level][1:])[0]
    thisX = xpos[level][ww][0]
    thisY = ypos[level]
    pos[thisN[level]] = np.array([thisX,thisY])
    G.add_node(thisN[level],pos=pos[thisN[level]])

nx.draw(G,pos,node_size=0,alpha=0.4,edge_color='r',font_size=16)
plt.savefig("diagramSystem1.png")
plt.show()
