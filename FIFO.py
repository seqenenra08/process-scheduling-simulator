from PLOT import PLOT

class FIFO:
    _segments = []
    _data = []

    def __init__(self, data):
        self._data = data
    
    def run(self):
        self._data.sort(key=lambda x: x[2])
        for i in range(0, len(self._data)):
            self._segments.append([i, self._data[i][1], self._data[i][2]])
        self.print_results()

    def run_plot(self):
        plot = PLOT(self._segments)
        plot.run()

    def print_results(self):
        print(self._data)
        self.run_plot()
        """ print("Process\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
        for i in range(len(self._data)):
            print(f"{self._segments[i][0]}\t{self._data[i][1]}\t\t{self._data[i][2]}\t\t{self._segments[i][1] - self._data[i][1] - self._data[i][2]}\t\t{self._segments[i][1] - self._data[i][2]}") """
        