# Définition des constantes

DATA_DIR="/media/bere/USB DISK1/BLUED DATASET/location_001_dataset_001-015"

START_INDEX=1

END_INDEX=400

NUMBER_OF_FILES=END_INDEX - START_INDEX + 1

F_S=12000

F_0=50

NUMBER_OF_ROWS_PER_PERIOD=F_S // F_0

# charge le nom des fichiers de données dans une liste

DATA_FILES_NAMES_TEMPLATES = [f"{DATA_DIR}/location_001_dataset_001/location_001_ivdata_{i:03d}.txt.bz2" for i in range(START_INDEX, END_INDEX + 1)]

V_LIST = []
I_LIST = []
# import des modules nécessaires
import bz2
import pandas as pd
from functions import compute_power

for i in range(28,len(DATA_FILES_NAMES_TEMPLATES)):

    data_file=pd.read_csv(DATA_FILES_NAMES_TEMPLATES[i],compression='bz2',header=22,usecols=[0,1,2,3])

    data_file.to_csv(f"{DATA_DIR}/location_001_dataset_001_csv/location_001_ivdata_{i+START_INDEX:03d}.csv")
     





