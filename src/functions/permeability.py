import numpy as np
from PySide6.QtWidgets import QMessageBox

class Permeability:
    def __init__(self, phi, swirr):
        self.phi = phi
        self.swirr = swirr # Water saturation (Sw) of a zone at irreductible water saturation
        
    def willy_rose_permeability(self, type_of_fluid) -> float:
        """
        Calculates permeability in reservoirs of medium gravity oils or dry gas using
        Wyllie & Rose (1950).
        
        Parameters
        ----------
        type_of_fluid: string
            dry-gas or medium-oil
            
        Return
        ------
        k: float
            Permeability in milidarcys
        """
        try:
            if type_of_fluid == 'dry-gas':
                constant = 79
            elif type_of_fluid == 'medium-oil':
                constant = 250
            else:
                QMessageBox.critical(None, 
                                    "Entrada inválida", 
                                    "Tipo de porosidade deve ser 'dry-gas' ou 'medium-oil'.")
                return None, None
            
            k_wyllie = ((constant * (self.phi**3))/self.swirr) ** 2
            
            return k_wyllie

        except ZeroDivisionError:
            QMessageBox.critical(None, 
                                "Erro de divisão por zero", 
                                "A saturação de água irredutível (swirr) não pode ser zero.")
            return None, None

        except Exception as e:
            QMessageBox.critical(None, 
                                "Erro desconhecido", 
                                f"Ocorreu um erro desconhecido: {str(e)}")
            return None, None
    def timur_permeability(self) -> float:
        """
        Calculate permeability using the Timur (1968) method.

        Timur (1968) proposed an equation for permeability calculation. This function
        implements that equation, which involves the porosity and irreducible water saturation.

        Returns
        -------
        float
            Permeability calculated using the Timur method, in millidarcys.

        Raises
        ------
        ZeroDivisionError
            If the irreducible water saturation (swirr) is zero.
        """
        try:
            k_timur = ((93 * (self.phi**2.2))/self.swirr) ** 2
            return k_timur

        except ZeroDivisionError:
            QMessageBox.critical(None, 
                                "Erro de divisão por zero", 
                                "A saturação de água irredutível (swirr) não pode ser zero.")
            return None

        except Exception as e:
            QMessageBox.critical(None, 
                                "Erro desconhecido", 
                                f"Ocorreu um erro desconhecido: {str(e)}")
            return None
        

    def coates_dumanoir_permeability(self, rw, rtirr, ph) -> float:
        """
        Calculate permeability using the Coates & Dumanoir (1973) method.

        Coates & Dumanoir (1973) proposed a more complex expression for permeability calculation. 
        This equation includes water resistivity and water resistivity of a formation at an 
        irreducible water saturation zone values, and some constants that are related to resistivity 
        and density values.
        
        Parameters
        ----------
        rw: float
            formation water resistivity at formation temperature
        rtirr: float
            true formation resistivity from a formation at 
            irreducible water saturation (Swirr)
        ph: float
            hydrocarbon density g / cm³

        Return
        ------
        k_coates:
            Permeability calculated using the Coates & Dumanoir method
        """
        try:
            W = ((3.75 - self.phi) + ( ((np.log(self.rw/self.rtirr) + 2.2)**2) / (2.0) )) ** (1/2)
            C = (23 + 465 * self.phi) - (188 * self.phi ** 2)
            
            k_coates = ( (C * self.phi**(2*W)) * ( W**4 * (self.rw/self.rtirr)) ) ** 2
            
            return k_coates

        except ZeroDivisionError:
            QMessageBox.critical(None, 
                                "Erro de divisão por zero", 
                                "rtirr não pode ser zero.")
            return None

        except Exception as e:
            QMessageBox.critical(None, 
                                "Erro desconhecido", 
                                f"Ocorreu um erro desconhecido: {str(e)}")
            return None
    
    def nmr_permeability_coates(self, phi_nmr, c, ffi, bvi) -> float:
        """
        Calculates the permeability using nuclear magnetic resonance well logs (NMR) and
        the "three-fluid model" proposed by Coates.
        
        Parameters
        ----------
        phi_nmr : float
            NMR-derived effective porosity.
        c : float
            Constant, depending on formation.
        ffi : float
            Proportion of moveable fluids occupying effective porosity.
        bvi : float
            Proportion of capillary-bound fluids occupying effective porosity.

        Returns
        -------
        float
            Permeability calculated using the Coates NMR method, in millidarcys.

        Raises
        ------
        ZeroDivisionError
            If `ffi` or `bvi` is zero.
        
        """
        try:
            k_nmr = ((phi_nmr)/(c))**4 * ((ffi)/(bvi))**2
            
            return k_nmr

        except ZeroDivisionError:
            QMessageBox.critical(None, 
                                "Erro de divisão por zero", 
                                "A saturação de água irredutível (swirr) não pode ser zero.")
            return None

        except Exception as e:
            QMessageBox.critical(None, 
                                "Erro desconhecido", 
                                f"Ocorreu um erro desconhecido: {str(e)}")
            return None
        
    def nmr_permeability(self, phi_nmr, t2gm, a) -> float:
        """
        Calculate permeability using nuclear magnetic resonance (NMR) measurements.

        This function implements an equation for permeability calculation using NMR-derived
        effective porosity (`phi_nmr`), geometric mean relaxation time (`t2gm`), and a constant (`a`).

        Parameters
        ----------
        phi_nmr : float
            NMR-derived effective porosity.
        t2gm : float
            geometric mean of the T2 distribution
        a : float
            Constant, depending on formation.

        Returns
        -------
        k_nmr: float
            Permeability calculated using the NMR method, in millidarcys.

        Raises
        ------
        Exception
            If an unknown error occurs during the calculation.
        """
        
        try:
            k_nmr = a * ((phi_nmr)**4) * ((t2gm)**2)
            
            return k_nmr
        
        except Exception as e:
            QMessageBox.critical(None, 
                                "Erro desconhecido", 
                                f"Ocorreu um erro desconhecido: {str(e)}")
            return None