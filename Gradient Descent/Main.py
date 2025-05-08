from gradient import Gradient

if __name__ == '__main__':
    GD = Gradient()

    (x1, it1) = GD.myGD1(.1, -10)
    (x2, it2) = GD.myGD1(.1, 10)
    print('Solution x1 = %f, cost = %f, obtained after %d iterations'%(x1[-1], GD.cost(x1[-1]), it1))
    print('Solution x2 = %f, cost = %f, obtained after %d iterations'%(x2[-1], GD.cost(x2[-1]), it2))

    (x3, it3) = GD.myGD1(.5, 10)
    print('Solution x3 = %f, cost = %f, obtained after %d iterations'%(x3[-1], GD.cost(x3[-1]), it3))

    (x4, it4) = GD.myGD1(.01, 10)
    print('Solution x4 = %f, cost = %f, obtained after %d iterations'%(x4[-1], GD.cost(x4[-1]), it4))