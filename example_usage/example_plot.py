import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------
# Important part
# --------------------------------------
import kimmdy_paper_theme

# Auto initialize
# plot_colors = kimmdy_paper_theme.auto_init()

# OR manually

plot_config = kimmdy_paper_theme.default_plot_config  # Load custom plot configs
# If you want to adjust something for your custom figure use
# plot_config['legend.fontsize'] = 5

kimmdy_paper_theme.apply_plot_config(plot_config=plot_config)  # Apply custom matplotlib style
# If you don't have roboto installed, you can manually load it like this

kimmdy_paper_theme.init_roboto_font()
plot_colors = kimmdy_paper_theme.plot_colors  # These are the predefined colors
# --------------------------------------


# --------------------------------------
# Usage example
# --------------------------------------

# Sine example
np.random.seed(0)
xs = np.linspace(0, 2*np.pi, 100)
ys_true = np.sin(xs)
ys_experiment = ys_true + np.random.normal(0, 0.2, size=ys_true.size)
ys_kimmdy_1 = 1.1 * np.sin(xs*0.95)
ys_kimmdy_2 = 0.9 * np.sin(xs*1.05)


fig, axes = plt.subplots(2, 1, figsize=(10, 10))

ax = axes[0]
ax.scatter(xs, ys_experiment, label="Experiment", color=plot_colors["experiment"],
           facecolor="None", edgecolors="black")  # Make transparent with only outline
ax.plot(xs, ys_kimmdy_1, label="Kimmdy 1", color=plot_colors["kimmdy"])
ax.plot(xs, ys_kimmdy_2, label="Kimmdy 2", color=plot_colors["kimmdy_light"])

ax.set_title("THIS is a catchy title")

ax.set_xlabel("x axis")
ax.set_ylabel("y axis")

ax.legend()

# Bar example
xs = np.arange(3)
width = 1/4
offset = 1/4

ys_true = 1 + xs
ys_experiment = ys_true + np.random.normal(0, 0.2, size=ys_true.size)
ys_kimmdy_1 = ys_true - 0.3 + np.random.normal(0, 0.2, size=ys_true.size)
ys_kimmdy_2 = ys_true + 0.1 + np.random.normal(0, 0.2, size=ys_true.size)


ax = axes[1]
ax.bar(xs, ys_kimmdy_1, width=width, label="KIMMDY 1", color=plot_colors["kimmdy"])
ax.bar(xs + offset, ys_kimmdy_2, width=width, label="KIMMDY 2", color=plot_colors["kimmdy_light"])
ax.bar(xs + 2*offset, ys_experiment, width=width, label="Experiment", color=plot_colors["experiment"])

ax.set_xlabel("x axis")
ax.set_ylabel("y axis")

ax.grid(True)

ax.legend()
plt.tight_layout()
fig.savefig("example.png", bbox_inches='tight')

plt.show()
