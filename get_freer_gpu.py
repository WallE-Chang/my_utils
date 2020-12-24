import os
import numpy as np
def get_freer_gpu():
    os.system('nvidia-smi -q -d Memory |grep -A4 GPU|grep Free >tmp')
    memory_available = [int(x.split()[2]) for x in open('tmp', 'r').readlines()]
    free_gpu_list = np.argwhere(memory_available == np.amax(memory_available))
    for free_gpu in free_gpu_list:
        if free_gpu != 0:
            return free_gpu.item()
