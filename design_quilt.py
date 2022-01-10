from piece import Piece, Rectangle, RightTriangle
from quilt import Quilt
import matplotlib.pyplot as plt

strip1 = Rectangle(40.5,2.5,color='C0')
strip2 = Rectangle(40.5,2.5,color='C1')
strip3 = Rectangle(40.5,2.5,color='C2')

tri1 = RightTriangle(40.5,2.5,color='C3')

fig,axes = plt.subplots()
# strip1.draw(axes)
# strip2.draw(axes,offset=(0,-4))
# tri1.draw(axes,offset=(1,-4))

quilt = Quilt(strip1)
# quilt.sew(2,3,strip2,1,0)
# quilt.sew(2,3,strip3,1,0)
# quilt.sew(2,3,tri1,1,0)

quilt.draw(axes)
plt.show()
