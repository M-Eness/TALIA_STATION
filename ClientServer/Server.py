import socket

def server_program():
    host = "localhost"  # İstemcilerin bağlanacağı adres
    port = 6000  # Port numarası (client ile aynı olmalı)

    server_socket = socket.socket()  # Sunucu soketi oluştur
    server_socket.bind((host, port))  # IP ve portu bağla
    server_socket.listen(1)  # 1 istemci kabul et

    print(f"Sunucu {host}:{port} üzerinde dinliyor...")

    conn, address = server_socket.accept()  # Bağlantı kabul et
    print(f"Bağlandı: {address}")

    # İstemciye mesaj gönder
    conn.send("Bağlantı başarılı!".encode())

    msg = "Merhaba, istemci!"  # Gönderilecek mesaj
    conn.send(msg.encode())
    print(f"Mesaj gönderildi: {msg}")
    while True:
        msg = input("Sunucudan bağlantıyı kapatmak için 'exit' yazın: ") # Gönderilecek mesaj
        conn.send(msg.encode())  # Mesaj gönderiliyor
        print(f"Mesaj gönderildi: {msg}")

        # Komut girişi bekliyoruz
        if msg.lower() == 'exit':  # 'exit' komutuyla bağlantı kapatılır
            print("Bağlantı kapatılıyor...")
            conn.send("Bağlantı kapatılıyor.".encode())  # İstemciye kapatma mesajı gönder
            break  # Bağlantıdan çıkılıyor


    # Sürekli olarak istemciye veri gönder


    conn.close()  # Bağlantıyı kapat

if __name__ == "__main__":
    server_program()