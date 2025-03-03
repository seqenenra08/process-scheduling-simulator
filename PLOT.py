import matplotlib.pyplot as plt
import numpy as np

class PLOT:
    _segments = []
    def __init__(self, segments):
        self._segments = segments

    def run(self):
        lineas = []
        sum = 0
        for i in range(len(self._segments)): 
            if i == 0:
                lineas.append(((self._segments[i][0], 0), (self._segments[i][1], self._segments[i][0])))
            else:                            
                lineas.append(((sum, self._segments[i][0]), (self._segments[i][1] + sum, self._segments[i][0])))
            sum += self._segments[i][1]

        plt.figure(figsize=(10, 6))

        for (x1, y1), (x2, y2) in lineas:
            plt.plot([x1, x2], [y1, y2], marker='o', linestyle='-', label=f"({x1},{y1}) → ({x2},{y2})")

        plt.xticks(np.arange(0, sum + 10, 1))
        plt.yticks(np.arange(0, 10, 1))
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.title("Gráfica con múltiples líneas")
        plt.legend()
        plt.grid()
        plt.show()