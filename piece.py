from matplotlib.patches import Polygon

#Piece represents a shape cut from one fabric
class Piece:
    #creates a fabric piece with vertices at each nodes
    #nodes must be in counter-clockwise circular order e.g. node1 adjacent to node2 adjacent to node3 adjacent to node1
    def __init__(self, nodes, color = 'C0'):
        self.nodes = Node(nodes[0][0],nodes[0][1])
        head = prev = self.nodes
        for i in range(1,len(nodes)):
            prev.next = Node(nodes[i][0],nodes[i][1])
            prev = prev.next
        prev.next = head
        self.color = color

    #draws the fabric piece on axes
    #offset: where to draw the lower right corner node. default at origin
    def draw(self,axes,offset=(0,0),shownodes=True):
        curr = self.nodes
        vertices = [[curr.x+offset[0],curr.y+offset[1]]]
        if shownodes:
            axes.plot(curr.x+offset[0],curr.y+offset[1],'ko')
        prev = curr
        curr = curr.next
        while curr != self.nodes:
            vertices.append([curr.x+offset[0],curr.y+offset[1]])
            if shownodes:
                axes.plot(curr.x+offset[0],curr.y+offset[1],'ko')
            axes.plot([prev.x+offset[0],curr.x+offset[0]],[prev.y+offset[1],curr.y+offset[1]],'k-')
            prev = curr
            curr = curr.next
        axes.plot([prev.x+offset[0],curr.x+offset[0]],[prev.y+offset[1],curr.y+offset[1]],'k-')
        p = Polygon(vertices, closed=True, color=self.color)
        axes.add_patch(p)


class Rectangle(Piece):
    def __init__(self, width, height, color):
        nodes = [[0,0],[width,0],[width,height],[0,height]]
        Piece.__init__(self, nodes, color)

class RightTriangle(Piece):
    def __init__(self, width, height, color):
        nodes = [[0,0],[width,0],[width,height]]
        Piece.__init__(self, nodes, color)

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.next = None
