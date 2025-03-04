import matplotlib.pyplot as plt
import numpy as np

class PLOT:
    def __init__(self, segments):
        self._segments = segments

    def run(self):
        plt.close('all')  
        fig = plt.figure(figsize=(10, 6))  

        lineas = []
        sum_x = 0  

        for i in range(len(self._segments)): 
            if i == 0:
                lineas.append(((self._segments[i][2], self._segments[i][0]), (self._segments[i][1] + self._segments[i][2], self._segments[i][0])))
                sum_x = self._segments[i][2]
            else:                            
                lineas.append(((sum_x, self._segments[i][0]), (self._segments[i][1] + sum_x, self._segments[i][0])))
            sum_x += self._segments[i][1]

        for (x1, y1), (x2, y2) in lineas:
            plt.plot([x1, x2], [y1, y2], marker='o', linestyle='-', label=f"({x1},{y1}) → ({x2},{y2})")

        plt.xticks(np.arange(0, sum_x + 10, 1))
        plt.yticks(np.arange(0, 10, 1))
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.title("Gráfica con múltiples líneas")

        ax = plt.gca()
        if ax.get_legend():
            ax.get_legend().remove()

        plt.legend()
        plt.grid()
        plt.show()