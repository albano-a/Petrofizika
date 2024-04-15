import sys
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QTableWidgetItem,
    QFileDialog,
    QMenu,
    QProgressDialog
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
import pandas as pd
from interface.mainWindow_ui import Ui_MainWindow
from functions.porosity import (
    Sonic, 
    Density, 
    Resistivity, 
    ShaleCorrected
)
from functions.permeability import Permeability
from functions.resistivity import Resistivity
from functions.shale_volume import ShaleVolume
from functions.conversion import ConversionOilGasIndustry


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)
        self.setWindowTitle("Petrofizika")
        
        ## Porosity > Sonic
        self.calculateWylliePorosity.clicked.connect(
            lambda: self.calculate_porosity_sonic('wyllie')
        )
        self.calculateRaymerPorosity.clicked.connect(
            lambda: self.calculate_porosity_sonic('raymer')
        )
        self.addTableWyllie.clicked.connect(
            lambda: self.add_table_sonic('wyllie')
        )
        self.addTableRaymer.clicked.connect(
            lambda: self.add_table_sonic('raymer')
        )
        self.exportPorosityTable.clicked.connect(self.export_table)
        
        ## Porosity > Density
        self.calculateDensityLogPorosity.clicked.connect(
            lambda: self.calculate_porosity_density('density')
        )
        self.calculateNeutronDensityGas.clicked.connect(
            lambda: self.calculate_porosity_density('neutron-density')
        )
        
        ## Shale Volume
        self.methodSPInput.currentTextChanged.connect(self.updateSPInputState)
        self.calculateShaleVolumeGeneral.clicked.connect(
            lambda: self.calculate_shale_volume('general')
        )
        self.calculateShaleVolumeSP.clicked.connect(
            lambda: self.calculate_shale_volume('sp')
        )
        
        
        ### Conversions
        self.conversion = ConversionOilGasIndustry()
        self.fromDistanceInput.textChanged.connect(self.conversionDistance)
        self.fromAreaInput.textChanged.connect(self.conversionArea)
        self.fromVolumeInput.textChanged.connect(self.conversionVolume)
        self.fromPressureInput.textChanged.connect(self.conversionPressure)
        
    def conversionDistance(self, _=None):
        distance_text = self.fromDistanceInput.text()
        if distance_text:
            distance = float(distance_text)
        else:
            distance = 0.0  # or any other default value
        from_unit = self.fromDistanceUnitInput.currentText().lower()
        to_unit = self.toDistanceUnitOutput.currentText().lower()
        
        distance_class = self.conversion.Distance()
        converted_distance = distance_class.convert_distance(
            distance=distance, from_unit=from_unit, to_unit=to_unit
        )
        self.toDistanceOutput.setText(str(converted_distance))
        
    def conversionArea(self, _=None):
        area_text = self.fromAreaInput.text()
        if area_text:
            area = float(area_text)
        else:
            area = 0.0  # or any other default value
        from_unit = self.fromAreaUnitInput.currentText().lower()
        to_unit = self.toAreaUnitOutput.currentText().lower()
        
        area_class = self.conversion.Area()
        converted_area = area_class.convert_area(
            area=area, from_unit=from_unit, to_unit=to_unit
        )
        self.toAreaOutput.setText(str(converted_area))
        
    def conversionVolume(self, _=None):
        volume_text = self.fromVolumeInput.text()
        if volume_text:
            volume = float(volume_text)
        else:
            volume = 0.0
        from_unit = self.fromVolumeUnitInput.currentText().lower()
        to_unit = self.toVolumeUnitOuput.currentText().lower()
        
        volume_class = self.conversion.Volume()
        converted_volume = volume_class.convert_volume(
            volume=volume, from_unit=from_unit, to_unit=to_unit
        )
        self.toVolumeOutput.setText(str(converted_volume))
    
    def conversionPressure(self, _=None):
        pressure_text = self.fromPressureInput.text()
        if pressure_text:
            pressure = float(pressure_text)
        else:
            pressure = 0.0
        from_unit = self.fromPressureUnitInput.currentText().lower()
        to_unit = self.toPressureUnitOutput.currentText().lower()
        
        pressure_class = self.conversion.Pressure()
        converted_pressure = pressure_class.convert_pressure_energy(
            value=pressure, from_unit=from_unit, to_unit=to_unit
        )
        self.toPressureOutput.setText(str(converted_pressure))
    
    def calculate_porosity_sonic(self, model):
        t_log = float(self.inputDeltaTlog_wyllie.text())
        t_ma = float(self.inputDeltaTma_wyllie.text())
        t_fl = float(self.inputDeltaTfl_wyllie.text())
        
        sonic = Sonic(t_log, t_ma, t_fl)
        if model == 'wyllie':
            porosity, perc_porosity = sonic.porosity_wyllie()
            self.resultWyllieDec.setText(f"{porosity:.4f}")
            self.resultWylliePerc.setText(f"{perc_porosity:.2f}%")
        elif model == 'raymer':
            porosity, perc_porosity = sonic.porosity_raymer()
            self.resultRaymerDec.setText(f"{porosity:.4f}")
            self.resultRaymerPerc.setText(f"{perc_porosity:.2f}%")
       
    def calculate_porosity_density(self, type):
        density = Density(0, 0, 0)
        if type == 'density':
            pma = float(self.matrixDensityInput.text())
            pb = float(self.bulkFormationDensityInput.text())
            pfl = float(self.fluidDensityInput.text())
            density = Density(pma, pfl, pb)
        
            d_porosity, d_perc_porosity = density.density_log()
            self.resultDensityPorosityDec.setText(f"{d_porosity:.4f}")
            self.resultDensityPorosityPerc.setText(f"{d_perc_porosity:.2f}%")
        if type == 'neutron-density':
            phi_n = float(self.neutronLogPorosityInput.text())
            phi_d = float(self.densityLogPorosityInput.text())
            if self.chooseNeutronDensityModel.currentText() == 'Standard Model':
                nd_porosity, nd_perc_porosity = density.neutron_density_combination(
                    phi_n, phi_d, model='standard'
                    )
            elif self.chooseNeutronDensityModel.currentText() == 'Alternative Model':
                nd_porosity, nd_perc_porosity = density.neutron_density_combination(
                    phi_n, phi_d, model='alternative'
                    )
            
            self.resultNeutronDensityPorosityDec.setText(f"{nd_porosity:.4f}")
            self.resultNeutronDensityPorositPerc.setText(f"{nd_perc_porosity:.2f}%")
            
    def calculate_shale_volume(self, method):
        from dicts.dicts import shale_methods
        shale_volume = ShaleVolume()
        
        if method == 'general':
            gr_log = float(self.GRlogInput.text())
            gr_min = float(self.GRminInput.text())
            gr_max = float(self.GRmaxInput.text())
            igr = shale_volume.gamma_ray_index(gr_log, gr_min, gr_max)[0]
            self.outputIGR.setText(f"{igr:.4f}")
            
            model = self.shaleVolumeMethodInput.currentText()
            
            model = shale_methods[model]
            
            vsh, vsh_perc = shale_volume.shale_volume(model)
            self.shaleVolumeOutputDec.setText(f"{vsh:.4f}")
            self.shaleVolumeOutputPerc.setText(f"{vsh_perc:.2f}%")
            
        elif method == 'sp':
            psp = float(self.PSPInput.text())
            ssp = float(self.SSPInput.text())
            method = self.methodSPInput.currentText().lower()
            if method == 'standard':
                vsh, vsh_perc = shale_volume.shale_volume_sp(psp, ssp, method)
                self.spOutputDec.setText(f"{vsh:.4f}")
                self.spOutputPerc.setText(f"{vsh_perc:.2f}%")
            elif method == 'alternative':
                sp_sh = float(self.SPshaleInput.text())
                vsh, vsh_perc = shale_volume.shale_volume_sp(psp, ssp, method, sp_sh)
                self.spOutputDec.setText(f"{vsh:.4f}")
                self.spOutputPerc.setText(f"{vsh_perc:.2f}%")
    
    def updateSPInputState(self, currentText):
        if currentText.lower() == 'alternative':
            self.SPshaleLabel.setEnabled(True)
            self.SPshaleInput.setEnabled(True)
        else:
            self.SPshaleLabel.setEnabled(False)
            self.SPshaleInput.setEnabled(False)
        
        
    def add_table_sonic(self, model):
        t_log = float(self.inputDeltaTlog_wyllie.text())
        t_ma = float(self.inputDeltaTma_wyllie.text())
        t_fl = float(self.inputDeltaTfl_wyllie.text())
        sonic = Sonic(t_log, t_ma, t_fl)

        if model == 'wyllie': 
            t_fl = float(self.inputDeltaTfl_wyllie.text())
            sonic.t_fl = t_fl
            porosity, perc_porosity = sonic.porosity_wyllie()
            headers = ["Tlog", "Tma", "Tfl", "Porosity", "Porosity (%)"]
            values = [t_log, t_ma, t_fl, f"{porosity:.4f}", f"{perc_porosity:.2f}%"]
            
        elif model == 'raymer':
            porosity, perc_porosity = sonic.porosity_raymer()
            headers = ["Tlog", "Tma", "Porosity", "Porosity (%)"]
            values = [t_log, t_ma, f"{porosity:.4f}", f"{perc_porosity:.2f}%"]

        self.outputTableSonicPorosity.setHorizontalHeaderLabels(headers)
        currentRowCount = self.outputTableSonicPorosity.rowCount()
        self.outputTableSonicPorosity.setRowCount(currentRowCount + 1)
        self.outputTableSonicPorosity.setColumnCount(len(headers))

        for i, value in enumerate(values):
            self.outputTableSonicPorosity.setItem(currentRowCount, i, QTableWidgetItem(str(value)))
        
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)

        addRowAction = QAction("Add row", self)
        addRowAction.triggered.connect(self.add_row)
        contextMenu.addAction(addRowAction)

        resetTableAction = QAction("Reset table", self)
        resetTableAction.triggered.connect(self.reset_table)
        contextMenu.addAction(resetTableAction)

        contextMenu.exec(event.globalPos())
        
    def add_row(self):
        currentRow = self.outputTableSonicPorosity.currentRow()
        self.outputTableSonicPorosity.insertRow(currentRow)

    def reset_table(self):
        self.outputTableSonicPorosity.setRowCount(0)
    
    def export_table(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()", "","Excel Files (*.xlsx);;All Files (*)", options=options)
        if filename:
            if not filename.endswith(".xlsx"):
                filename += ".xlsx"
                
            # Create a DataFrame from the QTableWidget
            data = []
            headers = [self.outputTableSonicPorosity.horizontalHeaderItem(i).text()\
                for i in range(self.outputTableSonicPorosity.columnCount())]
            for row in range(self.outputTableSonicPorosity.rowCount()):
                row_data = []
                for column in range(self.outputTableSonicPorosity.columnCount()):
                    item = self.outputTableSonicPorosity.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                data.append(row_data)
            
            df = pd.DataFrame(data, columns=headers)
            
            # Create a QProgressDialog
            progress = QProgressDialog("Saving...", "Cancel", 0, 100, self)
            progress.setWindowModality(Qt.WindowModal)

            # Update the progress bar while the DataFrame is being written to an Excel file
            for i in range(1, 101):
                progress.setValue(i)
                if progress.wasCanceled():
                    break
                df.to_excel(filename, index=False, header=True)
     
     
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        
if __name__ == '__main__':
    main()

