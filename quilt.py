from piece import Piece, Node
import numpy as np
import numpy.linalg as la

#quilt combines many Pieces through sewing and cutting
#nodes only represents the outside of the quilt i.e. what can be sewn
#allowance: seam allowance. default to quarter of an inch
class Quilt:
    def __init__(self,piece,allowance=0.25):
        self.pieces = [piece]
        self.nodes = Node(piece.nodes.x,piece.nodes.y)
        prev = self.nodes
        curr = piece.nodes.next
        while curr != piece.nodes:
            prev.next = Node(curr.x,curr.y)
            prev = prev.next
            curr = curr.next
        prev.next = self.nodes
        self.allowance = allowance

    def sew(self,piece):
        pass

    def trim_nodes(self):
        pass

    def draw(self,axes,offset=[0,0],shownodes=True):
        for p in self.pieces:
            p.draw(axes,offset,shownodes=False)
        curr = self.nodes
        if shownodes:
            axes.plot(curr.x+offset[0],curr.y+offset[1],'ko')
        prev = curr
        curr = curr.next
        while curr != self.nodes:
            if shownodes:
                axes.plot(curr.x+offset[0],curr.y+offset[1],'ko')
            axes.plot([prev.x+offset[0],curr.x+offset[0]],[prev.y+offset[1],curr.y+offset[1]],'k-')
            prev = curr
            curr = curr.next
        axes.plot([prev.x+offset[0],curr.x+offset[0]],[prev.y+offset[1],curr.y+offset[1]],'k-')
