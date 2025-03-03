from PLOT import PLOT   

class RR:
    _data = []
    _segments = []
    _time_accumulator = 0
    _quantum = 0

    def __init__(self, data, quantum):
        self._data = data
        self._quantum = quantum

    def run(self):
        self._data.sort(key=lambda x: x[2])
        self._get_segments()

    def _get_segments(self):
        if self._data == []:
            self._run_plot()
        else:
            for process in self._data:
                if process[1] > 0:
                    if process[1] - self._quantum > 0:
                        self._segments.append([process[0], self._quantum])
                        process[1] -= self._quantum
                    else:
                        self._segments.append([process[0], process[1]])
                        process[1] = 0

            self._data = [process for process in self._data if process[1] > 0]
            self._get_segments()

    def _run_plot(self):
        plot = PLOT(self._segments)
        plot.run()

         