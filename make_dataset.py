import uart
import glob
import numpy as np
import re

n_file = 1

if __name__ == "__main__":
    my_uart = uart.Uart()
    my_uart.connect_uart(synchronization_time=0.15)
    my_uart.add_s16("X")
    my_uart.add_s16("Y")
    my_uart.add_s16("Z")
    line = my_uart.data_pars(1000)

    filenames = glob.glob('raw/*.csv')
    for filename in filenames:
        d = list(filter(str.isdigit, str(filename)))
        if d:
            n_file = int(d[0])

    my_uart.data_save(np.array(line) / 1.7, name=('shake_' + str(n_file + 1)))
    my_uart.disconnect_uart()
    my_uart.plt()
