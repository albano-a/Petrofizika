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
from functions.porosity import porosity as poro

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)
        self.setWindowTitle("Petrofizika")
        
        self.calculateWylliePorosity.clicked.connect(self.calculate_wyllie_porosity)
        self.calculateRaymerPorosity.clicked.connect(self.calculate_raymer_porosity)
        self.addTableWyllie.clicked.connect(self.add_table_wyllie)
        self.addTableRaymer.clicked.connect(self.add_table_raymer)
        self.exportSonicPorosityTable.clicked.connect(self.export_table)
        
    def calculate_wyllie_porosity(self):
        t_log = float(self.inputDeltaTlog_wyllie.text())
        t_ma = float(self.inputDeltaTma_wyllie.text())
        t_fl = float(self.inputDeltaTfl_wyllie.text())
        
        w, perc_w = poro.porosity_wyllie(t_log, t_ma, t_fl)
        self.resultWyllieDec.setText(f"{w:.4f}")
        self.resultWylliePerc.setText(f"{perc_w:.2f}%")
        
    def calculate_raymer_porosity(self):
        t_log = float(self.inputDeltaTlog_raymer.text())
        t_ma = float(self.inputDeltaTma_raymer.text())
        
        r, perc_r = poro.porosity_raymer(t_log, t_ma)
        self.resultRaymerDec.setText(f"{r:.4f}")
        self.resultRaymerPerc.setText(f"{perc_r:.2f}%")
        
    def add_table_wyllie(self):
        t_log = float(self.inputDeltaTlog_wyllie.text())
        t_ma = float(self.inputDeltaTma_wyllie.text())
        t_fl = float(self.inputDeltaTfl_wyllie.text())
        
        w, perc_w = poro.porosity_wyllie(t_log, t_ma, t_fl)
        
        headers = ["Tlog", "Tma", "Tfl", "Porosity", "Porosity (%)"]
        self.outputTableSonicPorosity.setHorizontalHeaderLabels(headers)
        
        currentRowCount = self.outputTableSonicPorosity.rowCount()
        self.outputTableSonicPorosity.setRowCount(currentRowCount + 1)
        self.outputTableSonicPorosity.setColumnCount(5)
        
        values = [t_log, t_ma, t_fl, f"{w:.4f}", f"{perc_w:.2f}%"]
        for i, value in enumerate(values):
            self.outputTableSonicPorosity.setItem(currentRowCount, i, QTableWidgetItem(str(value)))
        
    def add_table_raymer(self):
        t_log = float(self.inputDeltaTlog_raymer.text())
        t_ma = float(self.inputDeltaTma_raymer.text())
        
        r, perc_r = poro.porosity_raymer(t_log, t_ma)
        
        headers = ["Tlog", "Tma", "Porosity", "Porosity (%)"]
        self.outputTableSonicPorosity.setHorizontalHeaderLabels(headers)
        
        currentRowCount = self.outputTableSonicPorosity.rowCount()
        self.outputTableSonicPorosity.setRowCount(currentRowCount + 1)
        self.outputTableSonicPorosity.setColumnCount(4)
        values = [t_log, t_ma, f"{r:.4f}", f"{perc_r:.2f}%"]
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
            for row in range(self.outputTableSonicPorosity.rowCount()):
                row_data = []
                for column in range(self.outputTableSonicPorosity.columnCount()):
                    item = self.outputTableSonicPorosity.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                data.append(row_data)
            
            df = pd.DataFrame(data)
            
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

