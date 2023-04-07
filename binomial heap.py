
import pygame as pg

class Node:
  def __init__(self,key):
    self.key = key
    self.parent = None
    self.order = 0
    self.children = []

  def add_child(self,node):
    node.parent = self
    self.children.append(node)

  
    



  
    


class BinomialHeap:
  def __init__(self):
    self.width = 800
    self.node_radius = 20
    self.min = None
    self.orders=[None]*20
  
  def make_heap(self,array):
    for val in array:
      self.insert(val)

  def insert(self,key):
    node = Node(key)
    
    self.assign_minimum(node)
    
    
    if not self.orders[0]:
      self.orders[0] = node
    else:
      self.union(node)
      

     
    
      

  def minimum(self):
    return self.min.key

  def assign_minimum(self,node):
    if not self.min:
      self.min = node
    elif node.key<self.min.key:
      self.min = node

  def find_minimum(self):
    for root in self.orders:
      if root:
        self.assign_minimum(root)

  def extract_min(self):
    node = self.min
    
    
    children=[]
    self.min = None
    for child in node.children:
      child.parent = None
      children.append(child)
      
    
    self.orders[node.order] = None
    
        
    for child in children:
      #print(child.key,child.order)
      self.union(child)

    self.find_minimum()

    return node
    
    

  def union(self,node):
    order = node.order
    while self.orders[order]:
      root = self.orders[order]
      self.orders[order]=None
      if node.key < root.key:
        node.add_child(root)
        root = node
      else:
        root.add_child(node)
      root.order+=1
      node = root
      order+=1
    self.orders[order] = node
    node.order = order
    

  def decrease_key(self,key,newKey):
    node = self.search(key)
    node.key = newKey
    while node.parent:
      if node.parent.key>newKey:
        node.key = node.parent.key
        node = node.parent
        node.key = newKey
      else:
        break

    if newKey<self.min.key:
      self.min = node
    
    

  def delete(self,key):
    self.decrease_key(key,-float('inf'))
    self.extract_min()


  def searchInNode(self,key,node):
    if node:
      if node.key == key:
        return node

      for child in node.children:
        node = self.searchInNode(key,child)
        if node:
          return node


  def search(self,key):
    for root in self.orders:
      node = self.searchInNode(key,root)
      if node:
        return node
      


  def draw(self,window,root,x,y):
        color = (0,0,0)
        pg.draw.circle(window,color,(x,y),self.node_radius,width=2)
        font = pg.font.SysFont('Comic Sans MS', self.node_radius)
        text = font.render(str(root.key),True,(0,0,0))
        text_rect = text.get_rect(center=(x,y))
        window.blit(text,text_rect)

  def draw_nodes(self,window,root,x,y):
    self.draw(window,root,x,y)
    x_offset = 0
    for child in root.children:
      self.draw_nodes(window,child,x+x_offset,y+self.node_radius*3)
      pg.draw.line(window,(0,0,0),(x,y+self.node_radius),(x+x_offset,y+self.node_radius*2),width=2)
      x_offset+=self.node_radius*(root.order+1)
      
    
        

            

  def visualize(self):
        window = pg.display.set_mode((self.width,self.width))
        pg.display.set_caption('Binomial Heaps')
        pg.font.init()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return

            
            window.fill((255,255,255))
            x=100
            y=self.node_radius+5
            for root in self.orders:
              if root:
                self.draw_nodes(window,root,x,y)
                x+=self.node_radius*((root.order+1)*2)+5

            pg.display.update()



        


h = BinomialHeap()

#a=[7 2 4 17 1 11 6 8 15 10 20 5]


while True:
    print('Enter 1 for make heap')
    print('Enter 2 for insert')
    print('Enter 3 for delete')
    print('Enter 4 for extract min')
    print('Enter 5 for minimum')
    print('Enter 6 for visualize')
    print('Ennter 7 for decrease-key')
    print('Enter 8 to quit')
    print('-'*80)
    x=int(input('Enter choice: '))
    if x ==1:
        h.make_heap(map(int,input('Enter space separated values: ').split()))
    elif x==2:
      h.insert(int(input('Enter value to insert: ')))
    elif x==3:
      h.delete(int(input('Enter value to delete: ')))
    elif x==4:
       print('Extratced ',h.extract_min().key)

    elif x==5:
      print('Minimum is ',h.minimum())
      
    elif x==6:
        h.visualize()
    elif x==7:
        key = int(input('Enter key: '))
        newKey = int(input('Enter new key: '))
        h.decrease_key(key,newKey)
    else:
        break




