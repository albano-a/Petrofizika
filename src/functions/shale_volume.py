"""
Shale volume is a fundamental value to evaluate the quality of a reservoir rock.

According to the shale volume that a reservoir rock has, it will be determined 
how exploitable a reservoir is or not.

There are different methods to calculate shale volume, where we can name some of 
these equations: Larionov, Larionov- old rocks, Steiber, Clavier. Some of these 
equations use the gamma ray well log values, and some of them use values from 
spontaneous potential (SP) well logging tool.

Also, this value is used to make shale correction for porosity values derived 
from different well logging tools, so we can have a more reliable porosity value.
"""
import numpy as np
from PySide6.QtWidgets import QMessageBox

class ShaleVolume():
    def __init__(self) -> None:
        pass
    
    def gamma_ray_index(self, gr_log, gr_min, gr_max) -> float:
        """
        Shale volume calculation using gamma ray well log values.

        Parameters
        ----------
        gr_log: float
            numpy array with gamma ray well log values.
        gr_min: 
            minimum gamma ray value for shale.
        gr_max: 
            maximum gamma ray value for shale.

        Returns:
        float 
            Shale volume value.
        """
        self.igr = (gr_log - gr_min) / (gr_max - gr_min)
        igr_perc = np.clip(self.igr, 0, 1) * 100
        
        return self.igr, igr_perc
    
    def shale_volume(self, model) -> float:
        """
        Shale volume calculation using Larionov equation.
        
        Parameters
        ----------
        model: string
            Type of model to use for shale volume calculation. 
            It can be: 'cenozoic', 'old rocks'
        
        """
        if model == 'cenozoic':
            vsh = 0.083 * ((2 ** (3.7 * self.igr)) - 1)
        elif model == 'old rocks':
            vsh = 0.33 * ((2 ** (2.0 * self.igr)) - 1)
        elif model == 'steiber':
            vsh = self.igr / (3 - 2*self.igr)
        elif model == 'clavier':
            vsh = 1.7 - (3.38 - (self.igr + 0.7) ** 2) ** 0.5
            
        vsh_perc = np.clip(vsh, 0, 1) * 100
        
        return vsh, vsh_perc
        
    def shale_volume_sp(self, psp, ssp, method, sp_sh=None) -> float:
        """
        Calculate the shale volume using the given parameters.

        Parameters:
        psp: float 
            Pseudostatic Spontaneous Potential (maximum SP of shaly formation), in millivolts.
        ssp: float 
            Static spontaneous potential of a nearby thick clean sand, in millivolts
        method: str 
            The method to use for calculating the shale volume. Must be either 'standard' or 'alternative'.
        sp_sh: float, optional
            The volume of the shale in the standard shale sample, in cubic units. 
            Required when using the 'alternative' method.

        Returns:
        - vsh (float): The calculated shale volume.
        - vsh_perc (float): The shale volume as a percentage.

        Raises:
        - ValueError: If an invalid method is provided.

        """
        if method == 'standard':
            if psp > ssp:
                QMessageBox.critical(None, "Error", "PSP must be less than SSP.")
                return
            vsh = 1 - psp / ssp
            
        elif method == 'alternative':
            if sp_sh is None:
                QMessageBox.critical(
                    None, 
                    "Error", 
                    "The 'sp_sh' parameter must be provided when using the 'alternative' method.")
                return
            vsh = (psp - ssp) / (sp_sh - ssp)
        else:
            QMessageBox.critical(
                None, 
                "Error", 
                "Invalid method. Must be either 'standard' or 'alternative'.")
            return

        if vsh < 0 or vsh > 1:
            QMessageBox.critical(
                None, 
                "Error", 
                "Calculated Vsh is out of range. It should be between 0 and 1.")
            return

        vsh_perc = np.clip(vsh, 0, 1) * 100

        return vsh, vsh_perc

#shale_volume = ShaleVolume()
#igr = shale_volume.gamma_ray_index(50, 10, 100)
#print(shale_volume.shale_volume('old rocks'))