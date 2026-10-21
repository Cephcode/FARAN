# Définition des constantes

DATA_DIR="/media/bere/USB DISK1/BLUED DATASET/location_001_dataset_001-015"

START_INDEX=14

END_INDEX=27

NUMBER_OF_FILES=END_INDEX - START_INDEX + 1

F_S=12000

F_0=50

NUMBER_OF_ROWS_PER_PERIOD=F_S // F_0

DATA_FILES_NAMES_TEMPLATES = [f"{DATA_DIR}/location_001_dataset_001/location_001_ivdata_{i:03d}.txt.bz2" for i in range(START_INDEX, END_INDEX + 1)]

SIDE_TH=25

P_TH=25

MID_TH=20

SLOPE_TH=0.5

ST_TH=1

D_MIN=5000

PHI=0.1

V_LIST = []
I_LIST = []


# import des modules nécessaires
import csv
from functions import compute_power

def seed(Event):

    for i in range(NUMBER_OF_FILES):

        with open(f"{DATA_DIR}/location_001_dataset_001_csv/location_001_ivdata_{i+START_INDEX:03d}.csv", 'r',newline='') as f:
            data_file=csv.reader(f)
            next(data_file)  # skip the header row

            for row in data_file:

                if(NUMBER_OF_ROWS_PER_PERIOD==0):

                    power=compute_power(V_LIST,I_LIST)

                    print(f"Power: {power:.2f} W",f"I: {i} ")
                    NUMBER_OF_ROWS_PER_PERIOD=F_S // F_0
                    V_LIST.clear()
                    I_LIST.clear()
            
                V_LIST.append(float(row[4]))
                I_LIST.append(float(row[2]))
                NUMBER_OF_ROWS_PER_PERIOD-=1



