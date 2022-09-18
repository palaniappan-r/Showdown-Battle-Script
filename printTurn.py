from email.policy import default
import monTypes
import pandas as pd

dataObj = pd.read_json('gen8randombattle.json')

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    OKRED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    
def printData(mon_name,mon2_name):
    mon = dataObj[mon_name]
    lv = mon["level"]
    

    df = pd.read_csv('mon_data.csv')
    df.drop('Num',axis = 1,inplace = True)
    type1 = df[df['Name'] == mon2_name]['Type1'].values[0]
    type2 = df[df['Name'] == mon2_name]['Type2'].values[0]
    
    print(
        f"{bcolors.BOLD}{bcolors.OKBLUE}{mon_name} Lv {lv}{bcolors.ENDC}{bcolors.ENDC}",end="\t"
        )
    
    print("Abilities : ",end="")
    for j in mon["abilities"] : print(f"{bcolors.OKCYAN}{j}{bcolors.ENDC}",end = "")
    
    print("\nItems : ",end="")
    for j in range(0,len(mon["items"])-1) : 
        s = mon["items"][j]
        print(f"{bcolors.HEADER}{s}{bcolors.ENDC}",end = "/")
    s = mon["items"][-1]
    print(f"{bcolors.HEADER}{s}{bcolors.ENDC}")
    
    moves = pd.read_csv('moves.csv')

    for j in mon["moves"] : 
        move_type = moves[moves['Name'] == j]['Type'].values[0]
        dmg = monTypes.getDmg(move_type,type1,type2)
        
        if dmg == 4:
            print(
            f"{bcolors.BOLD}{bcolors.OKGREEN}{j}{bcolors.ENDC} -> {dmg}"
            )
        elif dmg == 2:
            print(f"{bcolors.OKGREEN}{bcolors.BOLD}{j}{bcolors.ENDC}{bcolors.ENDC} -> {dmg}")
        elif dmg == 0.5:
            print(f"{bcolors.OKRED}{j}{bcolors.ENDC} -> {dmg}")
        elif dmg == 0.25:
            print(f"{bcolors.OKRED}{j}{bcolors.ENDC} -> {dmg}")
        elif dmg == 0:
            print(f"{j} -> {dmg}")
        else:
            print(f"{bcolors.WARNING}{j}{bcolors.ENDC} -> {dmg}")
                