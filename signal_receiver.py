import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from rtlsdr import RtlSdr

# Frecuencia central y ancho de banda de la señal de interés (en Hz)
center_freq = 1e9   # Frecuencia del LNB
bandwidth = 5e6   # Ancho de banda de 5 MHz

# Configuración del dongle
sdr = RtlSdr()
sdr.rs = 2.4e6   # Frecuencia de muestreo (en Hz)
sdr.fc = center_freq
sdr.gain = 49.6
sdr.bandwidth = bandwidth

# Inicialización del gráfico
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlabel('Frecuencia (Hz)')
ax.set_ylabel('Potencia (dB)')
ax.set_title('Espectro de frecuencia')
ax.set_ylim(bottom=-40, top=70)

# Función que se ejecuta en cada frame de la animación
def update(frame):
    # Captura de datos
    samples = sdr.read_samples(512*1024)  # Número de muestras
    fft_data = np.fft.fft(samples)
    freqs = np.fft.fftfreq(len(samples), 1/sdr.sample_rate)
    power_spectrum = 20*np.log10(np.abs(fft_data))

    # Actualización de los datos del gráfico
    line.set_xdata(freqs)
    line.set_ydata(power_spectrum)
    ax.relim()
    ax.autoscale_view()

    return line,

# Configuración de la animación
ani = FuncAnimation(fig, update, interval=500)

# Mostrar el gráfico
plt.show()

# Cierre del dispositivo SDR
sdr.close()
