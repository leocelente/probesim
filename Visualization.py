from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

def Viz(data, time) -> None:
  altitudes =     data[:, 0] * 1e-3
  speed =         data[:, 1]
  volumes =       data[:, 2]
  buoyancy =      data[:, 3]
  drag =          data[:, 4]
  density =       data[:, 5]
  acceleration =  data[:, 6]
  weights =       data[:, 7]
  
  minutes =       time / 60

  fig = plt.figure(figsize=(14, 8), constrained_layout=True)
  fig.suptitle('Simulation Results', fontsize=16)

  ax = plt.subplot(3,2,1)
  plt.plot(minutes, altitudes, linewidth=2, color="black", label='Altitude ($h$)')
  plt.legend(loc=0)
  plt.ylabel("Altitude [km]")
  plt.grid()

  plt.subplot(3,2,2, sharex=ax)
  plt.plot(minutes, altitudes, linewidth=2, color="black", label="Altitude ($h$)")
  plt.legend(loc=0)
  plt.ylabel("Altitude [km]")
  plt.grid()

  plt.subplot(3,2,3, sharex=ax)
  plt.plot(minutes, speed, linewidth=2, color="orange", label="Ascent Rate ($\dot h$)")
  plt.legend(loc=0)
  plt.ylabel("Speed [m/s]")
  plt.grid()
  
  plt.subplot(3,2,5, sharex=ax)
  plt.plot(minutes, buoyancy, linewidth=2, color="red", label="Buoyancy ($B$)")
  plt.plot(minutes, drag, linewidth=2, color="green", label="Drag ($D$)")
  plt.plot(minutes, weights, linewidth=2, color="yellow", label="Weight ($W$)")
  plt.ylabel("Force [N]")
  plt.legend(loc=0)
  plt.grid()
  plt.xlabel("Time [minutes]")  

  plt.subplot(3,2,4, sharex=ax)
  plt.plot(minutes, acceleration, linewidth=2, color="purple", label="Acc. ($\ddot h$)")
  plt.ylabel("Acceleration [$m/s^2$]")
  plt.legend(loc=0)
  plt.grid()

  ax2 = plt.subplot(3,2,6, sharex=ax)
  plt.plot(minutes, volumes, linewidth=2, color="blue", label="Volume ($V_{B}$)")
  plt.ylabel("Volume [$m^3$]")
  plt.xlabel("Time [minutes]")
  plt.grid()
  
  ax3 = ax2.twinx()
  ax3.plot(minutes, density, color='cyan', linewidth=2, label="Density ($\\rho_{He}$) ")
  ax3.set_ylabel("Density [$kg/m^3$]")
  lines, labels = ax2.get_legend_handles_labels()
  lines2, labels2 = ax3.get_legend_handles_labels()
  ax2.legend(lines + lines2, labels + labels2, loc=0)
  
  plt.show()

  

