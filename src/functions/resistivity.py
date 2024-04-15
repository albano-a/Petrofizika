import numpy as np
from PySide6.QtWidgets import QMessageBox

class Resistivity:
    def __init__(self) -> None:
        pass
    
    def water_resistivity_archie(self, ro, phi, m, a) -> float:
        """
        Calculate water resistivity using Archie's Law.

        This function implements Archie's Law for the calculation of water resistivity.
        It uses the resistivity of the formation (`ro`), the porosity (`phi`), 
        the cementation exponent (`m`), and the tortuosity factor (`a`).

        Parameters
        ----------
        ro : float
            Resistivity of the formation.
        phi : float
            Porosity of the formation.
        m : float
            Cementation exponent.
        a : float
            Tortuosity factor.

        Returns
        -------
        float
            Water resistivity calculated using Archie's Law, in ohm.m.

        Raises
        ------
        ZeroDivisionError
            If the tortuosity factor (`a`) is zero.
        Exception
            If an unknown error occurs during the calculation.
        """
        try:
            rw = (ro * phi**m) / a
            
            return rw
        
        except ZeroDivisionError:
            QMessageBox.critical(None, 
                                "Erro de divisão por zero", 
                                "O fator de tortuosidade (a) não pode ser zero.")
            return None, None

        except Exception as e:
            QMessageBox.critical(None, 
                                "Erro desconhecido", 
                                f"Ocorreu um erro desconhecido: {str(e)}")
            return None, None
        
    def water_resistivity_western_atlas(self, 
                                        bht, # Bottom Hole Temperature
                                        fd, # Formation depth
                                        td, # Total Depth
                                        amst, # Annual Mean Surface Temperature
                                        tsurf, # measured temperature of rmf
                                        rmfsurf, # resistivity of mud filtrate at measured temperature
                                        sp, # Spoteaneous Potential measurement
                                        ) -> float:
        """
        Calculate water resistivity using the Western Atlas method.

        This function implements the Western Atlas method for the calculation of water resistivity.
        It uses the bottom hole temperature (`bht`), formation depth (`fd`), total depth (`td`), 
        annual mean surface temperature (`amst`), measured temperature of rmf (`tsurf`), 
        resistivity of mud filtrate at measured temperature (`rmfsurf`), and spontaneous potential measurement (`sp`).

        Parameters
        ----------
        bht : float
            Bottom Hole Temperature.
        fd : float
            Formation depth.
        td : float
            Total Depth.
        amst : float
            Annual Mean Surface Temperature.
        tsurf : float
            Measured temperature of rmf.
        rmfsurf : float
            Resistivity of mud filtrate at measured temperature.
        sp : float
            Spontaneous Potential measurement.

        Returns
        -------
        tuple
            Water resistivity (`rw`), equivalent water resistivity (`rwe`), mud filtrate resistivity (`rmf`), 
            and formation temperature (`tf`), all in ohm.m.

        Raises
        ------
        ZeroDivisionError
            If the denominator in the calculation of `rw` is zero.
        Exception
            If an unknown error occurs during the calculation.
        """
        try:
            tf = (((bht - amst)/(td)) * fd) + amst
            rmf = (rmfsurf * (tsurf + 6.77)) / (tf + 6.77)
            rwe = rmf * 10 ** (sp / (61 + 0.133*bht))
            rw_num = rwe + 0.131 * 10 ** ((1/(np.log(bht/19.9))) - 2)
            rw_den = -0.5 * rwe + 10 ** ((0.0426)/(np.log(bht/50.8)))
            rw = rw_num / rw_den
            
            return rw, rwe, rmf, tf
        
        except ZeroDivisionError:
            QMessageBox.critical(None, 
                                "Erro de divisão por zero", 
                                "Ocorreu uma divisão por zero!")
            return None, None

        except Exception as e:
            QMessageBox.critical(None, 
                                "Erro desconhecido", 
                                f"Ocorreu um erro desconhecido: {str(e)}")
            return None, None
        
    def water_resistivity_sp(self, sp, tf, rmf) -> float:
        """
        Calculate water resistivity using the spontaneous potential (SP) method.

        This function implements the SP method for the calculation of water resistivity.
        It uses the spontaneous potential (`sp`), formation temperature (`tf`), and mud filtrate resistivity (`rmf`).

        Parameters
        ----------
        sp : float
            Spontaneous Potential measurement.
        tf : float
            Formation temperature.
        rmf : float
            Mud filtrate resistivity.

        Returns
        -------
        float
            Water resistivity calculated using the SP method, in ohm.m.

        Raises
        ------
        Exception
            If an unknown error occurs during the calculation.
        """
        try:
            K = (0.133 * tf) + 60
            rw = 10 ** ((K * np.log(rmf) + sp)/K)
        
            return rw
        
        except Exception as e:
            QMessageBox.critical(None, 
                                "Erro desconhecido", 
                                f"Ocorreu um erro desconhecido: {str(e)}")
            return None, None
        
    def apparent_water_resistivity_archie(self, rt, phi, m, a) -> float:
        """
        Calculate apparent water resistivity using Archie's Law.

        This function implements Archie's Law for the calculation of apparent water resistivity.
        It uses the resistivity of the formation (`rt`), the porosity (`phi`), the cementation exponent (`m`),
        and the tortuosity factor (`a`).

        Parameters
        ----------
        rt : float
            Resistivity of the formation.
        phi : float
            Porosity of the formation.
        m : float
            Cementation exponent.
        a : float
            Tortuosity factor.

        Returns
        -------
        float
            Apparent water resistivity calculated using Archie's Law, in ohm.m.

        Raises
        ------
        ZeroDivisionError
            If the tortuosity factor (`a`) is zero.
        Exception
            If an unknown error occurs during the calculation.
        """
        try:
            rwa = (rt * (phi ** m)) / a
            
            return rwa
        
        except ZeroDivisionError:
            QMessageBox.critical(None, 
                                "Erro de divisão por zero", 
                                "O fator de tortuosidade (a) não pode ser zero.")
            return None, None

        except Exception as e:
            QMessageBox.critical(None, 
                                "Erro desconhecido", 
                                f"Ocorreu um erro desconhecido: {str(e)}")
            return None, None
    
    def total_resistivity_archie(self, a, rw, phi, m, n, sw) -> float:
        """
        
        """
        try:
            rt = (a * rw) / ((phi**m) * (sw**n))
            
            return rt
        
        except ZeroDivisionError:
            QMessageBox.critical(None, 
                                "Erro de divisão por zero", 
                                "Houve divisão por zero!")
            return None, None

        except Exception as e:
            QMessageBox.critical(None, 
                                "Erro desconhecido", 
                                f"Ocorreu um erro desconhecido: {str(e)}")
            return None, None