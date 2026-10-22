from functions import *

class EventDetector:

    def __init__(self,side_th,p_th,mid_th,slope_th,st_sl_th,phi,d_min,e_power):

        self.window=[]
        self.w_s=[]
        self.w_m=[]
        self.w_e=[]
        self.side_th=side_th
        self.p_th=p_th
        self.mid_th=mid_th
        self.slope_th=slope_th
        self.st_sl_th=st_sl_th
        self.phi=phi
        self.d_min=d_min
        self.e_power=e_power     


        self.mean_power_before=0
    # ====================================
    # add a new power value to the window 
    # ====================================  
    def push_power(self,power_list:list):
        print(f"received:{power_list},len:{len(power_list)}")
        pass