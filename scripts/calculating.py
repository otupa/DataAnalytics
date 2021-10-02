from typing import Counter


def counter_runs(argument):
    """[summary]
    Args:
        argument ([type]): [description]

    Returns:
        [type]: [description]
    """    
    dict_ = Counter([(item[1], item[2]) for item in argument])
    return [[item[0], dict_[item], item[0] * dict_[item], item[1]] for item in dict_]

def porcent(item, arg):
    if item[0] == 10:
        if item[3] == '+':
            item.append(round(item[2] * arg[0], 0))
        if item[3] == '-':
            item.append(round(item[2] * arg[1], 0))

    elif item[0] <= 20:
        if item[3] == '+':
            item.append(round(item[2] * arg[2], 0))

        if item[3] == '-':
            item.append(round(item[2] * arg[3], 0))

    elif item[0] >= 20:
        if item[3] == '+':
            item.append(round(item[2] * arg[4], 0))

        if item[3] == '-':
            item.append(round(item[2] * arg[5], 0))

    return [item[0], item[1], item[2], item[4]]



def calc_porcent(argument, porcents):
    return [[item for item in porcent(item, porcents)] 
                    for item in counter_runs(argument)]
                           
def calculate(argument, porcents):
    list_ = calc_porcent(argument, porcents)
    runs_ = round(sum([item[1] for item in list_]), 0)
    porcent_ = round(sum([item[2] for item in list_]), 0)
    faturation_ = round(sum([item[3] for item in list_]), 0)
    list_.append([runs_, porcent_, faturation_])
    return list_