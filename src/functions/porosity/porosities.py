import numpy as np
from PySide6.QtWidgets import QMessageBox

class Sonic:
    def __init__(self, t_log, t_ma, t_fl):
        self.t_log = float(t_log)
        self.t_ma = float(t_ma)
        self.t_fl = float(t_fl)

    def porosity_wyllie(self) -> float:
        """
        Wyllie porosity model.
        
        The calculation of sonic derived porosity, can be done from the time average Wyllie 
        (Wyllie et al., 1958) equation, which is expressed the following way:
        
        ɸS = (Δtlog - Δtma) / (Δtfl - Δtma)
        
        Where:
        ɸS= sonic porosity
        Δtma= matrix interval transit time
        Δtlog= interval transit time of the formation (from the sonic log)
        Δtfl= fluid interval transit time
        
        return: Wyllie porosity (decimal)
        """
        if self.t_fl == self.t_ma:
            QMessageBox.critical(None, "Resultado Inválido", "Ocorreu divisão por zero.")
            return None, None

        w = (self.t_log - self.t_ma) / (self.t_fl - self.t_ma)
        perc_w = np.clip(w, 0, 1) * 100
        
        if w < 0 or w > 1:
            QMessageBox.critical(None, "Resultado Inválido", "Os valores inseridos não estão corretos")
            return None, None

        return w, perc_w

    def porosity_raymer(self) -> float:
        """
        Raymer porosity model.
        
        Other way to calculate sonic derived porosity is through the Raymer-Hunt-Gardner (RHG) 
        equation (Raymer et al., 1980), which calculate it using matrix and sonic log values, and 
        it is expressed the following way:
        
        ɸs = (5/8) * ((Δtlog - Δtma) / Δtlog)
        
        Where:
        ɸs= sonic-derived porosity
        Δtma= interval transit time in the matrix
        Δtlog= interval transit time in the formation
        
        return: Raymer porosity (decimal)
        """
        r = (5/8)*((self.t_log - self.t_ma)/self.t_log)
        perc_r = np.clip(r, 0, 1) * 100

        return r, perc_r
    
    
class Density:
    def __init__(self, rho_ma, rho_fl, rho_b):
        self.rho_ma = float(rho_ma)
        self.rho_fl = float(rho_fl)
        self.rho_b = float(rho_b)
        
    def density_log(self) -> float:
        """
        Density log calculation.
        
        For the calculation of porosity derived from density logs, the equation takes into account
        the density values of the matrix and fluid (from the well folder), and the formation density
        of the study area. The equation is given by:
        
        plog = (pma - pb) / (pma - pfl)
        
        where:
        plog = Density log (g/cm³)
        pma = Matrix density (g/cm³)
        pb = Formation density (g/cm³)
        pfl = Fluid density (g/cm³)
        
        return: Density log (g/cm³)
        """
        rho_log = (self.rho_ma - self.rho_b) / (self.rho_ma - self.rho_fl)
        perc_rho_log = np.clip(rho_log, 0, 1) * 100
        
        return rho_log, perc_rho_log
    
    def neutron_density_combination(self, phi_n, phi_d) -> float:
        """
        Neutron-density combination.
        
        In gas bearing formations, a combination is made between the values obtained from neutron 
        and density logs. For those who know about wells, it is known that when the curves of both 
        logs cross between (crossover), we can infer the presence of a gas accumulation, although 
        other paramaters neeed to be taken into account like well bore conditions (caliper log), 
        among others. The expression is the following:

        ɸNDgas = np.sqrt((ɸN^2 + ɸD^2) / 2)
        
        where:
        ɸNDgas= gas bearing formations porosity
        ɸN= neutron log porosity
        ɸD= density log porosity
        
        return: Neutron-density porosity (g/cm³)
        """
        phi_ndgas = np.sqrt((phi_n**2 + phi_d**2) / 2)
        perc_phi_ndgas = np.clip(phi_ndgas, 0, 1) * 100
        
        return phi_ndgas, perc_phi_ndgas	
    
    
class Resistivity:
    def __init__(self, a, m, n, rw, rt, rmf, rxo, sw):
        self.a: float = a # tortuosity factor
        self.m: float = m # cementation factor
        self.n: float = n # saturation exponent
        self.rw: float = rw # resistivity of formation water
        self.rt: float = rt # true formation resistivity
        self.rmf: float = rmf # resistivity of the mud filtrate
        self.rxo: float = rxo # shallow resistivity from a very shallow reading device
        self.sw: float = sw # water saturation of the uninvaded zone
        
    def resistivity_derived_porosity(self) -> float:
        """
        Starting from the well known Archie's equation, regularly known better for water resistivity
        calculations, it is also used for the resistivity derived porosity. This equation includes 
        the values of tortuosity factor, formation and water resistivities, water saturation, and 
        saturation and cementation exponents, and the expression is the following:
        
        ɸ = ( (a * Rw) / (Rt * (Sw**n)) ) ** (1/m)
        
        Where:
        ɸ = porosity
        Sw= water saturation of the uninvaded zone
        Rw= resistivity of formation water at formation temperature
        Rt= true formation resistivity (i.e., deep induction or deep laterolog corrected for invasion)
        a= tortuosity factor
        m= cementation exponent
        n= saturation exponent
        """
        phi: float = ((self.a * self.rw) / (self.rt * (self.sw**self.n))) ** (1/self.m)
        perc_phi: float = np.clip(phi, 0, 1) * 100
        
        return phi, perc_phi
    
    def resistivity_derived_fz(self) -> float:
        """
        At the flushe zone, resistivity derived porosity can also be calculated. In this case, 
        resistivity of the mud filtrate at formation temperature must be know and the shallow 
        resistivity from a very shallow reading device, besides the tortuosity and cementation 
        exponent values.
        
        For the calculation of resistivity derived porosity at the flushed zone, there are cases 
        where a residual hydrocarbons correction needs to be made. In this case, water saturation 
        of an uninvaded zone and the saturation exponent valuesneed to values must be known. The 
        expression is summarized as the following:
        
        ɸ = ( (a * Rmf) / (Rxo * (Sw**n)) ) ** (1/m)
        
        Where:
        ɸ= porosity
        a= tortuosity factor
        Sw = water saturation of the uninvaded zone
        m= cementation exponent
        Rmf= resistivity of the mud filtrate at formation temperature
        Rxo= shallow resistivity from a very shallow reading device such as lateolog-8, microspherically focused log, or microlaterolog
        """
        
        phi_fz: float = ((self.a * self.rmf) / (self.rxo * (self.sw**self.n))) ** (1/self.m)
        perc_phi_fz: float = np.clip(phi_fz, 0, 1) * 100
        
        return phi_fz, perc_phi_fz
        