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
from functions.porosity import Sonic, Density, Resistivity, ShaleCorrected
from functions.conversion import Conversion_gas_industry

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)
        self.setWindowTitle("Petrofizika")
        
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
        self.exportSonicPorosityTable.clicked.connect(self.export_table)
        
        ### Conversions
        self.conversion = Conversion_gas_industry()
        self.fromDistanceInput.textChanged.connect(self.conversionDistance)
        self.fromAreaInput.textChanged.connect(self.conversionArea)
        
    def conversionDistance(self, _=None):
        dict_translation = {
            'pés': 'feet',
            'metros': 'meters',
            'milhas': 'miles',
            'quilômetros': 'kilometers'
        }
        
        distance_text = self.fromDistanceInput.text()
        if distance_text:
            distance = float(distance_text)
        else:
            distance = 0.0  # or any other default value
        from_unit = self.distanceSelector1.currentText().lower()
        to_unit = self.distanceSelector2.currentText().lower()
        
        # Translate the units from Portuguese to English
        from_unit = dict_translation[from_unit]
        to_unit = dict_translation[to_unit]
        
        distance_class = self.conversion.Distance()
        converted_distance = distance_class.convert_distance(
            distance=distance, from_unit=from_unit, to_unit=to_unit
        )
        self.toDistanceOutput.setText(str(converted_distance))
        
    def conversionArea(self, _=None):
        dict_translation = {
            'pés quadrados': 'square feet',
            'metros quadrados': 'square meters',
            'hectares': 'hectares',
            'acres': 'acres'
        }
        area_text = self.fromAreaInput.text()
        if area_text:
            area = float(area_text)
        else:
            area = 0.0  # or any other default value
        from_unit = self.areaSelector1.currentText().lower()
        to_unit = self.areaSelector2.currentText().lower()
        
        # Translate the units from Portuguese to English
        from_unit = dict_translation[from_unit]
        to_unit = dict_translation[to_unit]
        
        area_class = self.conversion.Area()
        converted_area = area_class.convert_area(
            area=area, from_unit=from_unit, to_unit=to_unit
        )
        self.toAreaOutput.setText(str(converted_area))
        
        
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
        
    def add_table_sonic(self, model):
        t_log = float(self.inputDeltaTlog_wyllie.text())
        t_ma = float(self.inputDeltaTma_wyllie.text())
        sonic = Sonic(t_log, t_ma)

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

