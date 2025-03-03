from FIFO import FIFO
from SR_F import SR_F
from RR import RR

def run_FIFO(data):
    fifo = FIFO(data)
    fifo.run()
    del fifo

def SJF():
    print("\n[ Running Shortest Job First (SJF) Algorithm ]\n")

def ALG_P():
    print("\n[ Running Priority Scheduling Algorithm ]\n")

def run_SR_F(data):
    sr_f = SR_F(data)
    sr_f.run()
    del sr_f

def run_RR(data):
    print("\n===== Round Robin Scheduling =====")
    quantum = int(input("Enter the time quantum: "))
    rr = RR(data, quantum)
    rr.run()
    del rr

def input_data():
    print("\n===== Enter Process Data =====")
    data = []
    n = int(input("Enter the number of processes: "))
    print("\nFormat: Process ID | Burst Time | Arrival Time")
    print("------------------------------------------------")
    for i in range(n):
        burst_time = int(input(f"Process {i} - Burst Time: "))
        arrival_time = int(input(f"Process {i} - Arrival Time: "))
        data.append([i, burst_time, arrival_time])
        print("------------------------------------------------")
    return data

def input_data_priority():
    print("\n===== Enter Process Data (With Priority) =====")
    data = []
    n = int(input("Enter the number of processes: "))
    print("\nFormat: Process ID | Burst Time | Arrival Time | Priority")
    print("--------------------------------------------------------")
    for i in range(n):
        burst_time = int(input(f"Process {i} - Burst Time: "))
        arrival_time = int(input(f"Process {i} - Arrival Time: "))
        priority = int(input(f"Process {i} - Priority: "))
        data.append([i, burst_time, arrival_time, priority])
        print("--------------------------------------------------------")
    return data

def menu():
    while True:
        print("\n===== CPU Scheduling Algorithms Menu =====")
        print("1. First In First Out (FIFO)")
        print("2. Shortest Job First (SJF)")
        print("3. Priority Scheduling (ALG P)")
        print("4. Shortest Remaining Time First (SR+F)")
        print("5. Round Robin (RR)")
        print("6. Exit")
        print("==========================================")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                run_FIFO(input_data())
            elif choice == 2:
                SJF()
            elif choice == 3:
                ALG_P()
            elif choice == 4:
                run_SR_F(input_data())
            elif choice == 5:
                run_RR(input_data())
            elif choice == 6:
                print("\nExiting program. Goodbye!\n")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.\n")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")

def main():
    menu()

if __name__ == "__main__":
    main()