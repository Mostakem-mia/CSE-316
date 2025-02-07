import matplotlib.pyplot as plt;
import numpy as np;

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
temps = [31, 34, 33, 29, 28, 27, 26];

plt.plot(days, temps, marker="o");
plt.xlabel("Days");
plt.ylabel("Temperature (°C)");
plt.title("Temperature Variations Over a Week");
plt.grid(True);
plt.show();