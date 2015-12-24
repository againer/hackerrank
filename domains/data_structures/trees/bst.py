

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def find(self, value):
    if self.value == value:
      return True

    if value > self.value:
      if self.right:
        return self.right.find(value)
      else:
        return False

    if value < self.value:
      if self.left:
        return self.left.find(value)
      else:
        return False

  def lookup(self, value, parent=None):
    if value < self.value:
      if self.left is None:
        return None, None
      return self.left.lookup(value, self)
    elif value > self.value:
      if self.right is None:
        return None, None
      return self.right.lookup(value, self)
    else:
      return self, parent


  def children_count(self, count=0):
    if self.right:
      count += 1
    if self.left:
      count += 1
    return count

  def delete(self, value):
    node, parent = self.lookup(value)
    if node:
      children_count = node.children_count()
      if children_count == 0:
        # If node has no children then remove it
        if parent.left is node:
          parent.left = None
        else:
          parent.right = None
        del node
      elif children_count == 1:
        if node.left:
          child = node.left
        else:
          child = node.right
        if parent:
          if parent.left is node:
            parent.left = child
          else:
            parent.right = child
        del node
      else:
        parent = node
        successor = node.right
        while successor.left:
          parent = successor
          successor = successor.left
        node.value = successor.value
        if parent.left == successor:
          parent.left = successor.right
        else:
          parent.right = successor.right

  def insert(self, value):
    if self.value == value:
      return False
    if self.value:
      if value < self.value:
        if self.left is None:
          self.left = Node(value)
        else:
          return self.left.insert(value)

      if value > self.value:
        if self.right is None:
          self.right = Node(value)
        else:
          return self.right.insert(value)
    else:
      self.value = value
    return True

  def post_order_traversal(self):
    if self:
      if self.left:
        self.left.post_order_traversal()
      if self.right:
        self.right.post_order_traversal()
      print self.value

  def in_order_traversal(self):
    if self:
      if self.left:
        self.left.in_order_traversal()
      print self.value
      if self.right:
        self.right.in_order_traversal()

  def pre_order_traversal(self):
    if self:
      print self.value
      if self.left:
        self.left.pre_order_traversal()
      if self.right:
        self.right.pre_order_traversal()


class Tree(object):
  def __init__(self):
    self.root = None

  def get_root(self):
    return self.root

  def insert(self, value):
    if not self.root:
      self.root = Node(value)
      return True
    return self.root.insert(value)

  def find(self, value):
    if not self.root:
      return False
    return self.root.find(value)




if __name__ == '__main__':
  tree = Tree()
  for i in range(0, 8):
    tree.insert(i)
  tree.get_root().post_order_traversal()

