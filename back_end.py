import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from rtlsdr import RtlSdr



class DownloadData:

    def __init__(self):

        self.amount_read_samples = 256*1024
        self.amount_sample_rate = 2.4e6
        self.bandwidth = 5000000
        self.center_freq = 0


    def get_data(self):
        self.init_dongle()

        samples = self.sdr.read_samples(self.amount_read_samples)  # Número de muestras
        fft_data = np.fft.fft(samples)
        freqs = np.fft.fftfreq(len(samples), 1/self.sdr.sample_rate)
        power_spectrum = 20*np.log10(np.abs(fft_data))

        self.close_dongle()

        return freqs, power_spectrum


    

    
    def init_dongle (self):
        self.sdr = RtlSdr()
        self.sdr.sample_rate = self.amount_sample_rate
        self.sdr.center_freq = self.center_freq
        self.sdr.bandwidth = self.bandwidth


    def close_dongle(self):
        self.sdr.close()














if __name__ == "__main__":
    print("pan")

    # Función que se ejecuta en cada frame de la animación
    def update(frame):
        # Captura de datos
        samples = sdr.read_samples(c)  # Número de muestras
        fft_data = np.fft.fft(samples)
        freqs = np.fft.fftfreq(len(samples), 1/sdr.sample_rate)
        power_spectrum = 20*np.log10(np.abs(fft_data))

        # Actualización de los datos del gráfico
        line.set_xdata(freqs)
        line.set_ydata(power_spectrum)
        ax.relim()
        ax.autoscale_view()

        return line,

    # Frecuencia central y ancho de banda de la señal de interés (en Hz)
    center_freq = 0   # Frecuencia del LNB
    bandwidth = 5000000   # Ancho de banda de 5 MHz

    # Configuración del dongle
    sdr = RtlSdr()
    sdr.sample_rate = 2.4e6   # Frecuencia de muestreo (en Hz)
    sdr.center_freq = center_freq
    sdr.bandwidth = bandwidth

    # Inicialización del gráfico
    fig, ax = plt.subplots()
    line, = ax.plot([], [])
    ax.set_xlabel('Frecuencia (Hz)')
    ax.set_ylabel('Potencia (dB)')
    ax.set_title('Espectro de frecuencia')
    ax.set_ylim(bottom=-40, top=70)


        # Configuración de la animación
    ani = FuncAnimation(fig, update, interval=500)

    # Mostrar el gráfico
    plt.show()

    # Cierre del dispositivo SDR
    sdr.close()
