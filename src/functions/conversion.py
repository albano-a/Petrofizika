"""
This module contains a class that provides methods for 
converting units of measurement in the gas industry.
"""
import numpy as np
from PySide6.QtWidgets import QMessageBox


class ConversionOilGasIndustry:
    def __init__(self) -> None:
        pass
    
    class Distance:
        def __init__(self) -> None:
            pass
        
        def convert_distance(self, distance: float, from_unit: str, to_unit: str) -> float:
            """
            Convert distance between different units.

            Parameters
            ----------
            distance : float
                Distance in the specified 'from_unit'.
            from_unit : str
                The unit of the input distance. Must be one of the following:
                'feet', 'meters', 'miles', 'kilometers'.
            to_unit : str
                The unit to convert to. Must be one of the following:
                'feet', 'meters', 'miles', 'kilometers'.

            Returns
            -------
            float
                Distance in the specified 'to_unit'.

            Raises
            ------
            ValueError
                If 'from_unit' or 'to_unit' is not one of the valid options.
            """
            conversion_factors = {
                'feet': {
                    'meters': 0.3048, 
                    'miles': 0.000189394, 
                    'kilometers': 0.0003048
                    },
                'meters': {
                    'feet': 3.28084, 
                    'miles': 0.000621371, 
                    'kilometers': 0.001
                    },
                'miles': {
                    'feet': 5280, 
                    'meters': 1609.34, 
                    'kilometers': 1.60934
                    },
                'kilometers': {
                    'feet': 3280.84, 
                    'meters': 1000, 
                    'miles': 0.621371
                    }
            }

            try:
                if conversion_factors[from_unit][to_unit] is None:
                    raise ValueError(f"Cannot convert from {from_unit} to {to_unit}.")
                return f"{distance * conversion_factors[from_unit][to_unit]:.4f}"
            except KeyError:
                raise ValueError(
                    "Invalid unit. Must be one of the following: 'feet', 'meters', 'miles', 'kilometers'.")
    
    class Area:
        def __init__(self) -> None:
            pass
        
        def convert_area(self, area: float, from_unit: str, to_unit: str) -> float:
            """
            Convert area between different units.

            Parameters
            ----------
            area : float
                Area in the specified 'from_unit'.
            from_unit : str
                The unit of the input area. Must be one of the following:
                'acres', 'square feet', 'square meters', 'square kilometers'.
            to_unit : str
                The unit to convert to. Must be one of the following:
                'acres', 'square feet', 'square meters', 'square kilometers'.

            Returns
            -------
            float
                Area in the specified 'to_unit'.

            Raises
            ------
            ValueError
                If 'from_unit' or 'to_unit' is not one of the valid options.
            """
            conversion_factors = {
                'acres': {
                    'square feet': 43560, 
                    'square meters': 4046.86, 
                    'square kilometers': 0.00404686
                    },
                'square feet': {
                    'acres': 1/43560, 
                    'square meters': 0.092903, 
                    'square kilometers': 0.000000092903
                    },
                'square meters': {
                    'acres': 1/4046.86, 
                    'square feet': 10.7639, 
                    'square kilometers': 0.000001
                    },
                'square kilometers': {
                    'acres': 247.105, 
                    'square feet': 10763910.4, 
                    'square meters': 1000000}
                
            }

            try:
                if conversion_factors[from_unit][to_unit] is None:
                    raise ValueError(f"Cannot convert from {from_unit} to {to_unit}.")
                return f"{area * conversion_factors[from_unit][to_unit]:.4f}"
            except KeyError:
                raise ValueError(
                    "Invalid unit. Must be one of the following: 'acres', 'square feet', 'square meters', 'square kilometers'.")
        
    class Volume:
        def __init__(self) -> None:
            pass
        
        def convert_volume(self, volume: float, from_unit: str, to_unit: str) -> float:
            """
            Convert volume between different units.

            Parameters
            ----------
            volume : float
                Volume in the specified 'from_unit'.
            from_unit : str
                The unit of the input volume. Must be one of the following:
                'acre-feet', 'barrels', 'cubic feet', 'cubic meters', 'gallons', 'metric tons'.
            to_unit : str
                The unit to convert to. Must be one of the following:
                'acre-feet', 'barrels', 'cubic feet', 'cubic meters', 'gallons', 'metric tons'.

            Returns
            -------
            float
                Volume in the specified 'to_unit'.

            Raises
            ------
            ValueError
                If 'from_unit' or 'to_unit' is not one of the valid options.
            """
            conversion_factors = {
                'acre-feet': {
                    'barrels': 7758.4, 
                    'cubic feet': 43560, 
                    'cubic meters': 1233.48, 
                    'gallons': 325851.43, 
                    'metric tons': 8921.77
                    },
                'barrels': {
                    'acre-feet': 1/7758.4, 
                    'cubic feet': 5.615, 
                    'cubic meters': 0.158987, 
                    'gallons': 42, 
                    'metric tons': 0.13652
                    },
                'cubic feet': {
                    'acre-feet': 1/43560, 
                    'barrels': 1/5.615, 
                    'cubic meters': 0.0283168, 
                    'gallons': 7.48052, 
                    'metric tons': 0.0283168
                    },
                'cubic meters': {
                    'acre-feet': 1/1233.48, 
                    'barrels': 6.28981, 
                    'cubic feet': 35.3147, 
                    'gallons': 264.172, 
                    'metric tons': 1
                    },
                'gallons': {
                    'acre-feet': 1/325851.43, 
                    'barrels': 1/42, 
                    'cubic feet': 1/7.48052, 
                    'cubic meters': 1/264.172, 
                    'metric tons': 0.00378541
                    },
                'metric tons': {
                    'acre-feet': 1/8921.77, 
                    'barrels': 7.3, 
                    'cubic feet': 35.3147, 
                    'cubic meters': 1, 
                    'gallons': 264.172
                    }
            }

            try:
                if conversion_factors[from_unit][to_unit] is None:
                    raise ValueError(f"Cannot convert from {from_unit} to {to_unit}.")
                return f"{volume * conversion_factors[from_unit][to_unit]:.4f}"
            except KeyError:
                raise ValueError("Invalid unit. Must be one of the following: 'acre-feet', 'barrels', 'cubic feet', 'cubic meters', 'gallons', 'metric tons'.")
        
    class Pressure:
        def __init__(self) -> None:
            pass
        
        def convert_pressure_energy(self, value: float, from_unit: str, to_unit: str) -> float:
            """
            Convert pressure or energy between different units.

            Parameters
            ----------
            value : float
                Pressure or energy in the specified 'from_unit'.
            from_unit : str
                The unit of the input value. Must be one of the following:
                'psia', 'kPa', 'bar', 'BTU', 'joules'.
            to_unit : str
                The unit to convert to. Must be one of the following:
                'psia', 'kPa', 'bar', 'BTU', 'joules'.

            Returns
            -------
            float
                Pressure or energy in the specified 'to_unit'.

            Raises
            ------
            ValueError
                If 'from_unit' or 'to_unit' is not one of the valid options.
            """
            conversion_factors = {
                'psia': {
                    'kpa': 6.89476, 
                    'bar': 0.0689476, 
                    'BTU': None, 
                    'joules': None
                    },
                'kpa': {
                    'psia': 1/6.89476, 
                    'bar': 0.01, 
                    'btu': None, 
                    'joules': None
                    },
                'bar': {
                    'psia': 14.5038, 
                    'kpa': 100, 
                    'btu': None, 
                    'joules': None
                    },
                'btu': {
                    'psia': None, 
                    'kpa': None, 
                    'bar': None, 
                    'joules': 1055.06
                    },
                'joules': {
                    'psia': None, 
                    'kpa': None, 
                    'bar': None, 
                    'btu': 1/1055.06
                    }
            }

            try:
                if conversion_factors[from_unit][to_unit] is None:
                    raise ValueError(f"Cannot convert from {from_unit} to {to_unit}.")
                return f"{value * conversion_factors[from_unit][to_unit]:.4f}"
            except KeyError:
                raise ValueError(
                    "Invalid unit. Must be one of the following: 'psia', 'kPa', 'bar', 'BTU', 'joules'.")


