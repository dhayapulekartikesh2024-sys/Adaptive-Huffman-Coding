import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# Data for Figure 1: Performance Comparison
# ==========================================
methods = ['Traditional Adaptive', 'Proposed Selective (T=5)']
tree_updates = [14502, 2901]
execution_times = [18.45, 4.12]

# Create Figure 1
fig1, ax1 = plt.subplots(figsize=(8, 5))

# Setup X-axis positions
x = np.arange(len(methods))
width = 0.35

# Plot Bar 1 (Tree Updates) on the left Y-axis
color1 = '#1f77b4' # IEEE standard blue
ax1.set_ylabel('Total Tree Updates', color=color1, fontweight='bold')
bars1 = ax1.bar(x - width/2, tree_updates, width, label='Tree Updates', color=color1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim(0, 16000)

# Plot Bar 2 (Execution Time) on the right Y-axis
ax2 = ax1.twinx()
color2 = '#d62728' # IEEE standard red
ax2.set_ylabel('Execution Time (ms)', color=color2, fontweight='bold')
bars2 = ax2.bar(x + width/2, execution_times, width, label='Time (ms)', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim(0, 20)

# Formatting Figure 1
ax1.set_xticks(x)
ax1.set_xticklabels(methods, fontweight='bold')
plt.title('Fig 1. Performance Comparison: Traditional vs. Selective', fontweight='bold', pad=15)
fig1.tight_layout()

# Save Figure 1
plt.savefig('Fig1_Performance_Comparison.png', dpi=300, bbox_inches='tight')
print("Saved: Fig1_Performance_Comparison.png")


# ==========================================
# Data for Figure 2: Threshold Trade-off
# ==========================================
# Simulating the effect of increasing the threshold
thresholds = [1, 2, 5, 10, 20]
exec_times_trend = [18.45, 12.10, 4.12, 2.05, 1.15]
comp_ratios_trend = [56.40, 56.45, 56.60, 57.10, 58.50]

# Create Figure 2
fig2, ax3 = plt.subplots(figsize=(8, 5))

# Plot Line 1 (Execution Time) on left Y-axis
color3 = '#2ca02c' # Green
ax3.set_xlabel('Greedy Decision Threshold (T)', fontweight='bold')
ax3.set_ylabel('Execution Time (ms)', color=color3, fontweight='bold')
ax3.plot(thresholds, exec_times_trend, marker='o', markersize=8, color=color3, linewidth=2.5, label='Time')
ax3.tick_params(axis='y', labelcolor=color3)
ax3.grid(True, linestyle='--', alpha=0.7)

# Plot Line 2 (Compression Ratio) on right Y-axis
ax4 = ax3.twinx()
color4 = '#9467bd' # Purple
ax4.set_ylabel('Compression Ratio (%)', color=color4, fontweight='bold')
ax4.plot(thresholds, comp_ratios_trend, marker='s', markersize=8, color=color4, linewidth=2.5, label='Compression')
ax4.tick_params(axis='y', labelcolor=color4)

# Formatting Figure 2
plt.title('Fig 2. Impact of Threshold on Time vs. Compression', fontweight='bold', pad=15)
fig2.tight_layout()

# Save Figure 2
plt.savefig('Fig2_Threshold_Tradeoff.png', dpi=300, bbox_inches='tight')
print("Saved: Fig2_Threshold_Tradeoff.png")

# Display both graphs on screen
plt.show()