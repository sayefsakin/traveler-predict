from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from commonUtils import *


class Drawing(object):
    def __init__(self):
        plt.style.use('seaborn-whitegrid')

    def plotSampleIn2D(self, label_list, d1, d2):
        # 2d drawing
        plt.scatter(d1, d2)
        # plt.xticks(xInd, xInd)
        plt.xlabel(label_list[0])
        plt.ylabel(label_list[1])
        plt.title('PAPI_TOT_CYC Rate')
        plt.show()

    def plotSampleIn3D(self, label_list, d1, d2, d3):
        # 3d drawing
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(d1, d2, d3, alpha=1)
        ax.set_xlabel(label_list[0])
        ax.set_ylabel(label_list[1])
        ax.set_zlabel(label_list[2])
        plt.show()

    def plotTimeSeries(self, data, color, plot_title):
        plt.scatter(getTimeFromList(data), getRateFromList(data), c=color, cmap='viridis', alpha=1)
        # plt.xticks(xInd, xInd)
        plt.xlabel('Timestamp')
        plt.ylabel(getLocationTitleFromList(data))
        plt.title(plot_title)
        plt.show()
