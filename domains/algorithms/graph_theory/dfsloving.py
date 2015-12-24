def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs(graph, start, path=[]):
  '''iterative depth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path

def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path

'''
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
'''
graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print 'recursive dfs ', recursive_dfs(graph, 'A')
print 'iterative dfs ', iterative_dfs(graph, 'A')
print 'iterative bfs ', iterative_bfs(graph, 'A')

other_graph = {'A': set(['B','C']),'B':set(['D','E']),'C':set(['D','E']),'D':set(['E']),'E':set(['A'])}

new_graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print 'other graph iterative dfs', dfs(other_graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
print 'new graph iterative dfs', dfs(new_graph, 'A')
