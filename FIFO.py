from PLOT import PLOT

class FIFO:
    def __init__(self, data):
        self._data = data.copy()
        self._segments = []
        self._waiting_times = []
        self._turnaround_times = []
    
    def run(self):
        self._data.sort(key=lambda x: x[2])  
        current_time = 0

        while current_time < self._data[0][2]:
            current_time += 1
        
        for i in range(len(self._data)):
            pid, burst_time, arrival_time = self._data[i]
            
            waiting_time = current_time - arrival_time
            turnaround_time = waiting_time + burst_time
            
            self._waiting_times.append(waiting_time)
            self._turnaround_times.append(turnaround_time)
            print(pid, burst_time, arrival_time)
            self._segments.append([pid, burst_time, arrival_time])
            
            current_time += burst_time
        
        self.print_results()
    
    def run_plot(self):
        plot = PLOT(self._segments)
        plot.run()
    
    def print_results(self):
        print("Proceso | Tiempo de espera | Tiempo en el sistema")
        for i in range(len(self._data)):
            print(f"{self._data[i][0]}\t   | {self._waiting_times[i]}\t\t   | {self._turnaround_times[i]}")
        
        avg_waiting_time = sum(self._waiting_times) / len(self._waiting_times)
        avg_turnaround_time = sum(self._turnaround_times) / len(self._turnaround_times)
        
        print(f"\nTiempo de espera promedio: {avg_waiting_time:.2f}")
        print(f"Tiempo en el sistema promedio: {avg_turnaround_time:.2f}")
        
        self.run_plot()
