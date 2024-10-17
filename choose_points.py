import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_point_clicker import clicker

class ChoosePoints:
    def __init__(self, path) -> None:
        matplotlib.use('TkAgg')
        self.fig, self.ax = plt.subplots(constrained_layout=True)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        klicker = clicker(self.ax, ["event"], markers=["x"])

        plt.show()
        self.positions = klicker.get_positions()['event']
        self.path = path

        self.save_points()

    def save_points(self):
        with open(self.path, 'w') as file:
            for position in self.positions:
                file.write(f'{position}\n')