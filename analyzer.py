import os
import platform

def system_info():
    print("System:", platform.system())
    print("Node:", platform.node())
    print("Release:", platform.release())
    print("Processor:", platform.processor())

def list_processes():
    print("\nRunning Processes:")
    for proc in os.popen('tasklist'):
        print(proc.strip())

if __name__ == "__main__":
    system_info()
    list_processes()
