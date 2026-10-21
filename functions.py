# calculer la puissance moyenne à partir 
# des listes de tension et de courant

def compute_power(v_list:list, i_list:list):

    v_rms=max(v_list)*0.7071

    sum_i_squared = sum(x**2 for x in i_list)
    i_rms = (sum_i_squared / len(i_list))**0.5
    power = v_rms * i_rms
    return power


#divise la fenetre de puissance en trois regions
def select_window_region_to_analyse(option:str,window:list)->list:

    if option=='left':
        w_s=window[1:len(window)//3]
        return w_s
    
    elif option=='middle':
        w_m=window[(len(window)//2)-2:(len(window)//2)+3:]

        return w_m

    else:
        w_e=window[len(window)-(len(window)//3)+1:]

        return w_e




# calcule la plus difference  en valeur absolue
#  des elements d'une liste 

def maximum_difference(w_m:list)->int:
    # fixer un element et faire la difference avec tous le reste
    difference_array=[]

    for i in range(len(w_m)-1):
        diff=max([abs(w_m[i]-w_m[x]) for x in range(i+1,len(w_m))])
        difference_array.append(diff)

    return max(difference_array)


# renvoie une copie mise a jour de la liste des 25 dernieres valeurs de puissances
# envoye au detecteur d'evenement 
# 
def update_array(window:list,value:float)->list:

    new_window=window.copy()
    new_window.pop(0)
    new_window.append(value)

    return new_window


# dit si la valeur depasse la valeur seuille
def is_higher_than_threshold(value:float,thresold:float)->bool:

    if (value>thresold):
        return True
    
    return False

# calcule la difference moyenne avant et apres
# la detection d'un grand changement au milieu de la fenetre
def compute_mean_window_difference(w_s:list,w_e:list)->float:
    
    w_s_mean=sum(w_s)/len(w_s)
    w_e_mean=sum(w_e)/len(w_e)

    mean_difference=abs(w_s_mean-w_e_mean)
    return mean_difference


# calcule la difference de puissance correspondant a un evenement candidat
def compute_candidate_event_mean_difference(s_before,window):

    w_e=window[len(window)-(len(window)//3)+1:]
    s_after=sum(w_e)//len(w_e)
    power_variation=abs(s_before-s_after)

# calcule la pente de la 3e region de la fenetre des puissances
# qui contient les puissances les plus proches
# pour savoir si la variation est maintenu dans le temps

def calculate_slope(window)->float:
    half_window=window[len(window)//2:]

    index_arrays=[int(cpt) for cpt in range(1,(len(window)//2)+1)]

    mean_index=sum(index_arrays)/len(index_arrays)

    mean_power=sum(half_window)/len(half_window)

    denominator=sum([(x-mean_index)**2 for x in index_arrays])

    power_gap=[(s-mean_power) for s in half_window]

    numerator=sum([(x-mean_index)*power_gap[x] for x in index_arrays])
    
    slope=numerator/denominator

    return slope

# verifie si 80% des valeurs de pentes sont inferieur a un seuil
# permet de detecter le retour a la stabilite du courant
def detect_steady_state(slopes_list:list,phi:float)->bool:

    steady_slopes=filter(lambda x: abs(x)>=phi,slopes_list)

    expected_steady_slopes_number= round(0.8*len(slopes_list))

    if len(list(steady_slopes))>=expected_steady_slopes_number:
        
        print("marche")

        return True
    
    print("pas de valeurs")
    
    return False

