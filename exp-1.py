import os
import multiprocessing

def child_process():
    print(f"Child Process: PID = {os.getpid()}, PPID = {os.getppid()}")

def main():
    print(f"Original Process: PID = {os.getpid()}, PPID = {os.getppid()}")

    # Create a new process using multiprocessing
    p = multiprocessing.Process(target=child_process)
    p.start()
    p.join()

if __name__ == "__main__":
    main()
