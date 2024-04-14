import numpy as np
from PySide6.QtWidgets import QMessageBox

def porosity_wyllie(t_log, t_ma, t_fl) -> float:
    """
    Wyllie porosity model.
    
    :param t_log: Total porosity log (decimal)
    :param t_ma: Matrix porosity (decimal)
    :param t_fl: Fluid porosity (decimal)
    
    :return: Wyllie porosity (decimal)
    """
    try:
        t_log = float(t_log)
        t_ma = float(t_ma)
        t_fl = float(t_fl)
    except ValueError:
        QMessageBox.critical(
            None, 
            "Entrada inválida", 
            "Por favor, entre com valores válidos para os campos de entrada")
        return None, None
    
    if t_fl == t_ma:
        QMessageBox.critical(None, "Resultado Inválido", "Ocorreu divisão por zero.")
        return None, None

    w = (t_log - t_ma) / (t_fl - t_ma)
    perc_w = np.clip(w, 0, 1) * 100
    
    if w < 0 or w > 1:
        QMessageBox.critical(None, "Resultado Inválido", "Os valores inseridos não estão corretos")
        return None, None

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