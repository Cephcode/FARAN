def print_row(v,i):
    row_text = f"Row {i}: " + ", ".join(f"{value:.2f}" for value in v)


# calculer la puissance moyenne à partir 
# des listes de tension et de courant

def compute_power(v_list:list, i_list:list):

    v_rms=max(v_list)*0.7071

    sum_i_squared = sum(x**2 for x in i_list)
    i_rms = (sum_i_squared / len(i_list))**0.5
    power = v_rms * i_rms
    return power

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
# la detection d'un grnad changement au milieu de la fenetre
def compute_mean_difference(w_s:list,w_e:list)->float:
    
    w_s_mean=sum(w_s)/len(w_s)
    w_e_mean=sum(w_e)/len(w_e)

    mean_difference=abs(w_s_mean-w_e_mean)
    return mean_difference


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