import matplotlib.pyplot as plt

# Create a tall, narrow figure for the infographic
fig = plt.figure(figsize=(8, 18))

# Section 1: Title and Introduction
ax1 = fig.add_axes([0.1, 0.85, 0.8, 0.1])
ax1.axis('off')
ax1.text(0.5, 0.7, "The Rise of Renewable Energy in the United States", 
         ha='center', va='center', fontsize=18, fontweight='bold')
ax1.text(0.5, 0.3, ("Changing the energy landscape by lowering dependency on fossil fuels,\n"
                    "stimulating local economies, and encouraging environmental sustainability."),
         ha='center', va='center', fontsize=10)

# Section 2: Supporting Point 1 - Isotype for Electricity Generation Breakdown
ax2 = fig.add_axes([0.1, 0.73, 0.8, 0.1])
ax2.axis('off')
ax2.text(0.5, 0.85, "2020 Electricity Generation", ha='center', va='center', fontsize=12, fontweight='bold')
# Display the data as text and simple icons (circles) for illustration
ax2.text(0.25, 0.5, "Renewables: 21%", ha='center', va='center', fontsize=10, color='green')
ax2.text(0.75, 0.5, "Fossil Fuels: 79%", ha='center', va='center', fontsize=10, color='gray')
circle1 = plt.Circle((0.25, 0.3), 0.05, color='green', ec='black')
circle2 = plt.Circle((0.75, 0.3), 0.05, color='gray', ec='black')
ax2.add_artist(circle1)
ax2.add_artist(circle2)

# Section 3: Supporting Point 2 - Bar Graph for Renewable Energy Types
ax3 = fig.add_axes([0.1, 0.55, 0.8, 0.15])
energy_types = ['Biomass', 'Wind', 'Hydro', 'Solar', 'Geothermal']
percentages = [39, 26, 22, 11, 2]
bars = ax3.bar(energy_types, percentages, color='skyblue', edgecolor='black')
ax3.set_title("Breakdown of Renewable Energy Types (2020)", fontsize=12)
ax3.set_ylabel("Percentage")
ax3.set_ylim(0, 50)
for bar in bars:
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height}%', ha='center', va='bottom', fontsize=9)

# Section 4: Supporting Point 3 - Pie Chart for Regional Distribution
ax4 = fig.add_axes([0.1, 0.38, 0.8, 0.15])
regions = ['West', 'Midwest', 'South', 'Northeast']
region_percentages = [40, 25, 20, 15]
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']
ax4.pie(region_percentages, labels=regions, autopct='%1.1f%%', colors=colors, startangle=90)
ax4.set_title("Regional Distribution of Renewable Energy Installations", fontsize=12)

# Section 5: Supporting Point 4 - Line Graph for Capacity Growth
ax5 = fig.add_axes([0.1, 0.22, 0.8, 0.12])
years = [2010, 2012, 2014, 2016, 2018, 2020]
capacities = [50000, 70000, 90000, 110000, 130000, 150000]
ax5.plot(years, capacities, marker='o', color='purple')
ax5.set_title("Growth in Renewable Energy Capacity (MW)", fontsize=12)
ax5.set_xlabel("Year")
ax5.set_ylabel("Capacity (MW)")
ax5.set_ylim(40000, 160000)

# Section 6: Supporting Point 5 - Visualized Number for Wind Energy Capacity
ax6 = fig.add_axes([0.1, 0.12, 0.8, 0.08])
ax6.axis('off')
ax6.text(0.5, 0.7, "Record Wind Energy Capacity Installed in 2020", 
         ha='center', va='center', fontsize=12, fontweight='bold')
ax6.text(0.5, 0.3, "120,000 MW", ha='center', va='center', fontsize=24, color='darkblue')

# Section 7: Conclusion and Sources
ax7 = fig.add_axes([0.1, 0.02, 0.8, 0.08])
ax7.axis('off')
ax7.text(0.5, 0.6, ("Renewable energy is reshaping the future of U.S. energy,\n"
                    "challenging viewers to consider its impact on sustainability."), 
         ha='center', va='center', fontsize=10)
ax7.text(0.5, 0.2, "Sources: U.S. EIA | NREL | World Economic Forum", 
         ha='center', va='center', fontsize=8, color='gray')

plt.tight_layout()
plt.show()
