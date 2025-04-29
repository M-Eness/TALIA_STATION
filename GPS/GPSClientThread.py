# GPSClientThread.py
from PySide6.QtCore import QThread, Signal
import socket

class GPSClientThread(QThread):
    received_gps = Signal(str)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.running = True

    def run(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, self.port))

            while self.running:
                try:
                    data = sock.recv(1024)
                    if not data:
                        break
                    decoded = data.decode("utf-8").strip()
                    self.process_data(decoded)
                except:
                    break

            sock.close()
        except Exception as e:
            print(f"[GPSClientThread] Hata: {e}")

    def process_data(self, raw_data):
        # Örnek veri: "id: 1, zaman: 12:00, Konum: 40.123,29.456"
        parts = raw_data.split(",")
        for p in parts:
            if "Konum:" in p:
                konum = p.split("Konum:")[1].strip()
                self.received_gps.emit(konum)

    def stop(self):
        self.running = False
        self.quit()
        self.wait()