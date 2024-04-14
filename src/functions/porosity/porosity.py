import numpy as np

def porosity_wyllie(t_log, t_ma, t_fl) -> float:
    """
    Wyllie porosity model.
    
    :param t_log: Total porosity log (decimal)
    :param t_ma: Matrix porosity (decimal)
    :param t_fl: Fluid porosity (decimal)
    
    :return: Wyllie porosity (decimal)
    """
    w = (t_log - t_ma) / (t_fl - t_ma)
    perc_w = np.clip(w, 0, 1) * 100

    return w, perc_w

def porosity_raymer(t_log, t_ma) -> float:
    """
    Raymer porosity model.
    
    :param t_log: Total porosity log (decimal)
    :param t_ma: Matrix porosity (decimal)
    
    :return: Raymer porosity (decimal)
    """
    r = (5/8)*((t_log - t_ma)/t_log)
    perc_r = np.clip(r, 0, 1) * 100

    return r, perc_r