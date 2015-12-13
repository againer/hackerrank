from sets import Set

def bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q = [start]
  while q:
    v = q.pop(0)
    if not v in path:
      path = path + [v]
      q = q + graph[v]
  return path


if __name__ == '__main__':
  number_of_cases = int(raw_input())
  for _ in range(number_of_cases):
    number_of_nodes, number_of_edges = raw_input().split()
    number_of_nodes, number_of_edges = int(number_of_nodes), int(number_of_edges)
    graph = {number: [] for number in range(1, number_of_nodes + 1)}
    for _ in range(number_of_edges):
      x, y = raw_input().split()
      x, y = int(x), int(y)
      graph[x].append(y)
      print graph
      print bfs(graph, 1)

