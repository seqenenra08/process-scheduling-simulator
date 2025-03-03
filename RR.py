from PLOT import PLOT

class RR:
    def __init__(self, data, quantum):
        self._data = data.copy()
        self._quantum = quantum
        self._segments = []
        self._waiting_times = {process[0]: 0 for process in data}
        self._turnaround_times = {process[0]: 0 for process in data}
        self._completion_times = {}  
        self._time_accumulator = 0

    def run(self):
        self._data.sort(key=lambda x: x[2]) 
        self._get_segments()

    def _get_segments(self):
        queue = self._data[:]
        current_time = 0
        remaining_bursts = {process[0]: process[1] for process in self._data}
        arrival_times = {process[0]: process[2] for process in self._data}
        
        while queue:
            process = queue.pop(0)
            pid, burst_time, arrival_time = process
            
            if current_time < arrival_time:
                current_time = arrival_time
            
            execution_time = min(self._quantum, remaining_bursts[pid])
            self._segments.append([pid, execution_time, arrival_time])
            remaining_bursts[pid] -= execution_time
            current_time += execution_time
            
            if remaining_bursts[pid] > 0:
                queue.append([pid, remaining_bursts[pid], arrival_time])
            else:
                self._completion_times[pid] = current_time
        
        self._calculate_times(arrival_times)
        self.print_results()
        self._run_plot()

    def _calculate_times(self, arrival_times):
        for pid in self._completion_times:
            self._turnaround_times[pid] = self._completion_times[pid] - arrival_times[pid]
            self._waiting_times[pid] = self._turnaround_times[pid] - next(b for p, b, a in self._data if p == pid)
    
    def print_results(self):
        print("Proceso | Tiempo de espera | Tiempo en el sistema")
        for pid in self._waiting_times:
            print(f"{pid}\t   | {self._waiting_times[pid]}\t\t   | {self._turnaround_times[pid]}")
        
        avg_waiting_time = sum(self._waiting_times.values()) / len(self._waiting_times)
        avg_turnaround_time = sum(self._turnaround_times.values()) / len(self._turnaround_times)
        
        print(f"\nTiempo de espera promedio: {avg_waiting_time:.2f}")
        print(f"Tiempo en el sistema promedio: {avg_turnaround_time:.2f}")
    
    def _run_plot(self):
        plot = PLOT(self._segments)
        plot.run()