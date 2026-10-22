# import des modules nécessaires
import csv
from functions import compute_power
from window import Window
from time import sleep

V_LIST = []
I_LIST = []


def seed(window:Window,DATA_DIR,F_0,F_S,START_INDEX,NUMBER_OF_FILES,NUMBER_OF_ROWS_PER_PERIOD):

    for i in range(NUMBER_OF_FILES):

        with open(f"{DATA_DIR}/location_001_dataset_001_csv/location_001_ivdata_{i+START_INDEX:03d}.csv", 'r',newline='') as f:
            data_file=csv.reader(f)

            next(data_file)  # skip the header row

            for row in data_file:

                if(NUMBER_OF_ROWS_PER_PERIOD==0):

                    power=compute_power(V_LIST,I_LIST)

                    window.push(power)

                    NUMBER_OF_ROWS_PER_PERIOD=F_S // F_0
                    V_LIST.clear()
                    I_LIST.clear()

                    sleep(0.2)
            
                V_LIST.append(float(row[4]))
                I_LIST.append(float(row[2]))
                NUMBER_OF_ROWS_PER_PERIOD-=1

               
    

