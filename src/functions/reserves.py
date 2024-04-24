import numpy as np
from PySide6.QtWidgets import QMessageBox


class Reserves:
    def __init__(self, A, h, phi, sh, rf):
        self.A = A  # drainage area in acres
        self.h = h  # reservoir thickness in feet
        self.phi = phi  # porosity (decimal fraction)
        self.sh = sh  # hydrocarbon saturation (1-Sw) (decimal fraction)
        self.rf = rf  # Recovery factor

    def oil_reserves(self, gas, oil) -> float:
        """
        Calculate volumetric recoverable oil reserves.

        This function calculates the volumetric recoverable oil reserves (Nf) in stock-tank barrels (STB)
        using the given gas and oil volumes. It also calculates the gas-oil ratio (GOR),
        the oil volume factor (Boi), and returns these values along with Nf.

        Parameters
        ----------
        gas : float
            Volume of gas in the reservoir in cubic ft
        oil : float
            Volume of oil in the reservoir in Bbls

        Returns
        -------
        tuple
            Nf : float
                Volumetric recoverable oil reserves in stock-tank barrels (STB).
            Boi : float
                Oil volume factor, or reservoir barrels per stock-tank barrel.
            GOR : float
                Gas-oil ratio.

        Notes
        -----
        The calculation uses the following parameters:
        - 7758: barrels per acre-foot
        - A: drainage area in acres
        - h: reservoir thickness in feet
        - ɸ: porosity (decimal fraction)
        - Sh: hydrocarbon saturation (1-Sw) (decimal fraction)
        - RF: recovery factor
        """
        try:
            gas_oil_ratio = gas / oil  # GOR
            oil_volume_factor = 1.05 + 0.5 * (gas_oil_ratio / 100)  # BOI

            if oil_volume_factor == 0:
                raise ZeroDivisionError("Oil volume factor cannot be zero.")

            nf = (
                7758 * self.A * self.h * self.phi * self.sh * self.FR
            ) / oil_volume_factor

            return nf, oil_volume_factor, gas_oil_ratio

        except ZeroDivisionError as e:
            QMessageBox.critical(None, "Erro de Divisão por zero", str(e))
            return None, None, None

        except Exception as e:
            QMessageBox.critical(
                None, "Erro desconhecido", f"Um erro desconhecido ocorreu: {str(e)}"
            )
            return None, None, None

    def gas_reserves(self, depth, tsc, psc, p, z, tf, model) -> float:
        """


        Parameters
        ----------
        depth: float
            depth of the reservoir in feet
        tsc: float
            temperature in deg F at standard conditions
        psc: float
            surface pressure (psi) at standard conditions
        p: float
            reservoir pressure (psi)
        z: float
            gas compressibility factor
        tf: float
            formation temperature in deg F
        model: str
            'standard' or 'alternative'
        """
        try:
            if model == "standard":
                if z * tf == 0:
                    raise ZeroDivisionError("Product of z and tf cannot be zero.")
                bgi = (tsc / psc) * (p / (z * tf))
                gf = 43560 * self.A * self.h * self.phi * self.sh * self.rf * bgi

                return gf, bgi

            elif model == "alternative":
                pf2_pf1 = (0.43 * depth) / 15
                gf = 43560 * self.A * self.h * self.phi * self.sh * self.rf * pf2_pf1

                return gf, pf2_pf1
            else:
                raise ValueError("Model must be 'standard' or 'alternative'.")

        except ZeroDivisionError as e:
            QMessageBox.critical(None, "Divisão por zero", str(e))
            return None

        except ValueError as e:
            QMessageBox.critical(None, "Erro de valor", str(e))
            return None

        except Exception as e:
            QMessageBox.critical(
                None, "Erro desconhecido", f"Um erro desconhecido ocorreu: {str(e)}"
            )
            return None
