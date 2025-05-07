from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Graph(FigureCanvas):
    def __init__(self, parent=None):
        # Şeffaf figür oluştur
        self.fig = Figure(figsize=(4, 3), dpi=100)
        self.fig.patch.set_alpha(0.0)  # Arkaplan şeffaf

        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

        self.setParent(parent)
        self.setStyleSheet("background: transparent")  # Canvas arkaplan şeffaf

        # Kenar boşluklarını sıfırla (figure ile axes arasındaki boşluklar kalkar)
        self.fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

        # Grafik başlangıçta temiz görünsün
        self.axes.set_facecolor("none")  # Eksen arkaplanını da şeffaf yap
        self.plot_data([0, 0, 0])  # Boş bir grafik çiz (başta hata olmasın diye)

    def plot_data(self, data, title="Veri Grafiği"):
        self.axes.cla()  # Önce temizle
        self.axes.plot(data, color='white')
        self.axes.set_title(title)
        self.axes.grid(True, linestyle='--', alpha=0.5)  # Hafif grid ekledim, istersen silebiliriz
        self.draw()