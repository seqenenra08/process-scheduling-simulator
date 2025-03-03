from PLOT import PLOT

class SR_F:

    def __init__(self, data):
        self._data = data.copy()
        self._ready_queue = []
        self._running_queue = []
        self._waiting_queue = []
        self._segments = []
        self._time_running = 0
        self._time_accumulator = 0

    
    def run(self):
        self._get_ready_queue()
        self._get_waiting_queue()
        self._get_running_queue() 
        self._get_segments()


    def _get_ready_queue(self):
        self._ready_queue = sorted(self._data, key=lambda x: x[2])
    
    def _get_running_queue(self):
        for process in list(self._waiting_queue):  
            if self._time_running >= process[2]:
                self._running_queue.append(process)
                self._waiting_queue.remove(process)  
        
        self._running_queue.sort(key=lambda x: (x[1], x[2]))

    def _get_waiting_queue(self):        
        self._waiting_queue = self._ready_queue

    def _check_new_process(self, number_process):   
        if self._running_queue == []:
            return False
        else:
            return self._running_queue[0][0] != number_process 

    def _get_segments(self):
        if self._running_queue == []:
            self._run_plot()
        else:
            self._time_accumulator += 1
            self._time_running += 1
            self._running_queue[0][1] -= 1
            current_process = self._running_queue[0]
            self._get_running_queue()
            
            if current_process[1] == 0:
                self._running_queue.pop(0)
                verif = True
            else:
                verif = self._check_new_process(current_process[0])

            if verif:
                self._segments.append([current_process[0], self._time_accumulator])
                self._time_accumulator = 0
                self._get_segments()
            else:
                self._get_segments()
            
    def _run_plot(self):
        plot = PLOT(self._segments)
        plot.run()
        del plot
