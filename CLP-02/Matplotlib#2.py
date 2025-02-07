import matplotlib.pyplot as plt;
import numpy as np;

regions = ["North", "South", "East", "West"];
revenues = [50000, 60000, 45000, 70000];

plt.bar(regions, revenues, color="blue");
plt.xlabel("Regions");
plt.ylabel("Revenue ($)");
plt.title("Sales Revenue Across Regions");
plt.show();
