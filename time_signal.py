import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from rtlsdr import RtlSdr

# Frecuencia central y ancho de banda de la señal de interés (en Hz)
center_freq = 1.42e9   # Frecuencia del LNB
bandwidth = 100e6   # Ancho de banda de 5 MHz

# Configuración del dongle
sdr = RtlSdr()
sdr.rs = 2.4e6   # Frecuencia de muestreo (en Hz)
sdr.fc = center_freq
sdr.gain = 100
sdr.bandwidth = bandwidth

# Inicialización del gráfico
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Amplitud (V)')
ax.set_title('Espectro de frecuencia')
ax.set_ylim(bottom=-1, top=1)

inputs = sdr.read_samples(10)
print(inputs)

# Función que se ejecuta en cada frame de la animación
def update(frame):
    # Captura de datos
    samples = sdr.read_samples(256*1024)  # Número de muestras
    fft_data = np.fft.fft(samples)
    real_data = np.fft.ifft(fft_data)

    # Actualización de los datos del gráfico
    line.set_xdata(np.arange(len(real_data))/sdr.rs)
    line.set_ydata(real_data)
    ax.relim()
    ax.autoscale_view()

    return line,

# Configuración de la animación
ani = FuncAnimation(fig, update, interval=500)

# Mostrar el gráfico
plt.show()

# Cierre del dispositivo SDR
sdr.close()