import uart
import plot
import numpy as np


if __name__ == "__main__":
    my_uart = uart.Uart()
    my_uart.connect_uart(synchronization_time=0.15)
    my_uart.add_s16("X")
    my_uart.add_s16("Y")
    my_uart.add_s16("Z")
    line = my_uart.data_pars(100)
    print(line)
    my_uart.data_save()
    my_uart.disconnect_uart()
    my_uart.plt()



