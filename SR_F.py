from PLOT import PLOT
import copy

class SR_F:

    def __init__(self, data):
        self._data = data.copy()
        self._ready_queue = []
        self._ready_queue_copy = []
        self._running_queue = []
        self._waiting_queue = []
        self._segments = []
        self._waiting_times = [0] * len(self._data)
        self._turnaround_times = [0] * len(self._data)
        self._time_running = 0
        self._time_accumulator = 0

    def run(self):
        self._get_ready_queue()
        self._get_waiting_queue()
        self._get_running_queue() 
        self._get_segments()

    def _get_ready_queue(self):
        self._ready_queue = sorted(self._data.copy(), key=lambda x: x[2])
        self._ready_queue_copy = copy.deepcopy(self._ready_queue)
    
    def _get_running_queue(self):
        for process in list(self._waiting_queue):  
            if self._time_running >= process[2]:
                self._running_queue.append(process)
                self._waiting_queue.remove(process)  
        
        self._running_queue.sort(key=lambda x: (x[1], x[2]))

    def _get_waiting_queue(self):        
        self._waiting_queue = self._ready_queue.copy()

    def _check_new_process(self, number_process):   
        if self._running_queue == []:
            return False
        else:
            return self._running_queue[0][0] != number_process 

    def _get_segments(self):
        if self._running_queue == [] and self._waiting_queue == []:
            self._print_results()
        else:
            if self._running_queue == [] and self._waiting_queue != []:
                self._time_running += 1
                self._get_running_queue()
                self._get_segments()
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
                    self._waiting_times[current_process[0]] = self._time_running - self._ready_queue_copy[current_process[0]][1] - self._ready_queue_copy[current_process[0]][2]
                    self._turnaround_times[current_process[0]] = self._time_running - current_process[2]
                    self._segments.append([current_process[0], self._time_accumulator, current_process[2]])
                    self._time_accumulator = 0
                    self._get_segments()
                else:
                    self._get_segments()

    def _print_results(self):
        print("Proceso | Tiempo de espera | Tiempo en el sistema")
        for i in range(len(self._data)):
            print(f"{self._data[i][0]}\t   | {self._waiting_times[i]}\t\t   | {self._turnaround_times[i]}")
        
        avg_waiting_time = sum(self._waiting_times) / len(self._waiting_times)
        avg_turnaround_time = sum(self._turnaround_times) / len(self._turnaround_times)
        
        print(f"\nTiempo de espera promedio: {avg_waiting_time:.2f}")
        print(f"Tiempo en el sistema promedio: {avg_turnaround_time:.2f}")
        
        self._run_plot()
            
    def _run_plot(self):
        plot = PLOT(self._segments)
        plot.run()