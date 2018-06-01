import os
import glob
import time
 
# Enable One Wire Interface 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_sensor():
    lines = ["" for i in range(2)]
    while lines[0].strip()[-3:] != 'YES':
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        time.sleep(0.2)
    return lines


def read_temp():
    lines = read_sensor()
    temp_line = lines[1]
    t_pos = temp_line.find('t=')
    if t_pos != -1:
        temp_string = lines[1][t_pos+2:] # Read the raw value
        temp_c = float(temp_string) / 1000.0 # Convert to Celcius
        temp_f = temp_c * 9.0 / 5.0 + 32.0 # Convert to Farenheit
        return temp_c, temp_f


if __name__ == "__main__":
    c,f = read_temp()
    str = "Temperature - C: {0:.2f} \nTemperature - F: {1:.2f}".format(c,f)
    print(str)

    