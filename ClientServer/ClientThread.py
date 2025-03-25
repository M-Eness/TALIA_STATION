from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, Signal
import sys
import socket


class ClientThread(QThread):
    """Sunucu ile sürekli veri alışverişi yapan arka plan thread'i"""
    received_data = Signal(str)  # Gelen veriyi GUI'ye göndermek için sinyal

    def __init__(self, host="localhost", port=6000):
        super().__init__()
        self.host = host
        self.port = port
        self.running = True  # Thread kontrolü için flag
        self.client_socket = None

    def run(self):
        """Thread çalıştığında sürekli sunucudan veri alır"""
        try:
            self.client_socket = socket.socket()
            self.client_socket.connect((self.host, self.port))
            print("Sunucuya bağlandı!")

            while self.running:
                try:
                    data = self.client_socket.recv(1024).decode()
                    if data:
                        self.received_data.emit(f"Sunucudan gelen: {data}")
                except socket.error:
                    break  # Hata olursa döngüden çık

        except Exception as e:
            print(f"Bağlantı hatası: {e}")

    def stop(self):
        """Thread'i güvenli şekilde durdurur"""
        self.running = False
        if self.client_socket:
            self.client_socket.close()

