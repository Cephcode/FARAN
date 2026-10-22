from event_detector import EventDetector
from functions import *
from constants import *
from seeder import *
from window import Window

detector=EventDetector(SIDE_TH,P_TH,MID_TH,SLOPE_TH,ST_TH,PHI,D_MIN,e_power=0.5)

window=Window(detector)

seed(window,DATA_DIR,F_0,F_S,START_INDEX,NUMBER_OF_FILES,NUMBER_OF_ROWS_PER_PERIOD)

    
  