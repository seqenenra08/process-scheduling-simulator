from FIFO import FIFO
from SR_F import SR_F

def run_FIFO(data):
    fifo = FIFO(data)
    fifo.run()

def SJF():
    print("SJF")

def ALG_P():
    print("ALG_P")

def run_SR_F(data):
    sr_f = SR_F(data)
    sr_f.run()

def RR():
    print("RR")

def input_data():
    data = []
    n = int(input("Enter the number of processes: "))
    for i in range(n):
        data.append([i, int(input(f"Enter the burst time for process {i}: ")), int(input(f"Enter the arrival time for process {i}: "))])
    return data

def menu():
    print("choose the algorithm you want to run: ")
    print("1. FIFO")
    print("2. SJF")
    print("3. ALG P")
    print("4. SR+F")
    print("5. RR")
    print("6. SALIR")
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
        RR()
    elif choice == 6:
        exit()
    else:
        print("Invalid choice")
        menu()

def main():
    menu()

if __name__ == "__main__":
    main()