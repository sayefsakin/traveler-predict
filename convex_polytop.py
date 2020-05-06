import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial import ConvexHull, convex_hull_plot_2d
from mpl_toolkits.mplot3d import Axes3D
from _linprog import linprog

#ref materials
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html
#https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

def in_hull(points, x):
    n_points = len(points)
    n_dim = len(x)
    c = np.zeros(n_points)
    A = np.r_[points.T, np.ones((1, n_points))]
    b = np.r_[x, np.ones(1)]
    lp = linprog(c, A_eq=A, b_eq=b)
    return lp.success

def hull_test():
    # n_points = 10000
    # n_dim = 10
    # Z = np.random.rand(n_points,n_dim)
    # x = np.random.rand(n_dim)
    points = [[0, 0], [8, 3], [20, 5], [24, 10], [18, 20], [12, 25], [3, 13]]
    print(in_hull(points, [20, 1]))


def main():
    print("hello")
    hull_test()
    # plt.style.use('seaborn-whitegrid')
    # # points = np.random.rand(30, 2)   # 30 random points in 2-D
    # # hull = ConvexHull(points)
    # # plt.plot(points[:, 0], points[:, 1], 'o')
    # # for simplex in hull.simplices:
    # #     plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
    # # plt.plot(points[hull.vertices, 0], points[hull.vertices, 1], 'r--', lw=2)
    # # plt.plot(points[hull.vertices[0], 0], points[hull.vertices[0], 1], 'ro')
    #
    # points = np.random.rand(20, 10)
    # fig = plt.figure()
    # ax = plt.axes(projection="3d")
    # hull = ConvexHull(points)
    # hull_indices = np.unique(hull.simplices.flat)
    # print(len(hull_indices))
    # # ax.plot(points[:, 0], points[:, 1], points[:, 2], 'o')
    # # for simplex in hull.simplices:
    # #     ax.plot3D(points[simplex, 0], points[simplex, 1], points[simplex, 2], color='black')
    # #
    # # plt.show()


if __name__ == '__main__':
    main()
