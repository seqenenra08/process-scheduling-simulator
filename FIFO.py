from PLOT import PLOT

class FIFO:
    def __init__(self, data):
        self._data = data.copy()
        self._segments = []
    
    def run(self):
        self._data.sort(key=lambda x: x[2])
        for i in range(0, len(self._data)):
            self._segments.append([self._data[i][0], self._data[i][1], self._data[i][2]])
        self.print_results()

    def run_plot(self):
        plot = PLOT(self._segments)
        plot.run()

    def print_results(self):
        print(self._data)
        self.run_plot()