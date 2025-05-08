from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QSizePolicy

from Camera.CameraThread import CameraThread
from ClientServer.ClientThread import ClientThread
from GPS.GPSClientThread import GPSClientThread
from Windows.ArasBar import ArasBar
from Windows.MainWindow_Controller import MainWindow_Controller
from Windows.MainWindow_UI import Ui_MainWindow
from Windows.Graph import Graph


class MainWindow_Form(QMainWindow):
    def __init__(self):
        super(MainWindow_Form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cntlr = MainWindow_Controller(self, self.ui)
        ## Grafik ekleme kısmı
        self.graphs = []
        positions = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]  # 3x3 grid gibi
        self.ui.rhrh_button.clicked.connect(self.gonder_rhrh_kodu)

        aras_layout = QVBoxLayout(self.ui.arasWidget)
        self.ui.arasWidget.setLayout(aras_layout)
        aras = ArasBar()
        aras_layout.addWidget(aras)

        for i, pos in enumerate(positions):
            graph = Graph()
            self.graphs.append(graph)
            self.ui.graphs_container.layout().addWidget(graph, *pos)

            # Test verisiyle (sonra buraya uydu verisi koyarız)
        import numpy as np
        for idx, graph in enumerate(self.graphs):
            dummy_data = np.sin(np.linspace(0, 10, 100) + idx)
            graph.plot_data(dummy_data, title=f"Grafik {idx + 1}")

        ### -----------------------------------------------------
        ## Telemetri Labelları
        label_names_pairs = [
            ("PaketNumLabel", "PaketNumLabel2"),
            ("TakimNoLabel", "TakimNoLabel2"),
            ("BasincLabel", "BasincLabel2"),
            ("Basinc2Label", "Basinc2Label2"),
            ("GorevYukuYukseklikLabel", "GorevYukuYukseklikLabel2"),
            ("TasiyiciYukseklikLabel", "TasiyiciYukseklikLabel2"),
            ("InisHiziLabel", "InisHiziLabel2"),
            ("GpsLatLabel", "GpsLatLabel2"),
            ("GpsLonLabel", "GpsLonLabel2"),
            ("GpsAltLabel", "GpsAltLabel2"),
            ("PitchLabel", "PitchLabel2"),
            ("RollLabel", "RollLabel2"),
            ("YawLabel", "YawLabel2"),
            ("PilGerilimiLabel", "PilGerilimiLabel2"),
            ("S1Label", "S1Label2"),
            ("S2Label", "S2Label2"),
            ("SicaklikLabel", "SicaklikLabel2"),
            ("UyduStatLabel", "UyduStatLabel2"),
        ]

        self.data_labels = {}
        num_rows = 3
        labels_per_row = len(label_names_pairs) // num_rows
        row = 0
        col = 0

        for index, (label1_name, label2_name) in enumerate(label_names_pairs):
            label1 = getattr(self.ui, label1_name)
            label2 = getattr(self.ui, label2_name)

            self.ui.gridLayoutTelemetry.addWidget(label1, row, col)
            col += 1
            self.ui.gridLayoutTelemetry.addWidget(label2, row, col)
            col += 1

            # Bir satırdaki etiket çifti sayısına ulaşıldığında bir sonraki satıra geç
            if (index + 1) % labels_per_row == 0 and index < len(label_names_pairs) - 1:
                row += 1
                col = 0

            label1.setAlignment(Qt.AlignCenter)
            label2.setAlignment(Qt.AlignCenter)

            self.data_labels[label1_name] = label1
            self.data_labels[label2_name] = label2

        self.ui.gridLayoutTelemetry.setVerticalSpacing(5)
        self.ui.gridLayoutTelemetry.setHorizontalSpacing(35)

        ######-----------------------------------------------------

        # Soket istemcisi thread'i başlat
        self.client_thread = ClientThread(host="localhost", port=7001)
        self.client_thread.received_data.connect(self.add_log)
        self.client_thread.start()

        self.camera_thread = CameraThread()
        self.camera_thread.frame_signal.connect(self.update_camera_frame)  # Kamerayı QLabel'e bağla
        self.camera_thread.start()

        self.gps_thread = GPSClientThread("IP_ADRESS", 5000)
        self.gps_thread.received_gps.connect(self.update_gps_label)
        self.gps_thread.start()

    def gonder_rhrh_kodu(self):
        kod = self.ui.rhrh_input.text()
        print(f"Gönderilen RHRH Kodu: {kod}")
        self.ui.rhrh_input.clear()

    def add_log(self, text):
        """Terminale yeni satır ekler."""
        self.ui.terminal_plainTextEdit.appendPlainText(text)

    def update_camera_frame(self, image):
        """Kamera görüntüsünü QLabel içinde güncelle"""
        """Kamera görüntüsünü QLabel içine sığdırarak güncelle"""
        scaled_image = image.scaled(self.ui.camera_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.camera_label.setPixmap(QPixmap.fromImage(scaled_image))

    def update_gps_label(self, gps_text):
        self.ui.GorevYukuYukseklikLabel_2.setText(gps_text)

    def closeEvent(self, event):
        """Pencere kapatıldığında thread'leri durdur"""
        self.gps_thread.stop()
        self.client_thread.stop()
        self.client_thread.wait()
        self.camera_thread.stop()
        self.camera_thread.wait()
        event.accept()

        # self.initilizeComponents()

#   def initilizeComponents(self):
