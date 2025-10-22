import numpy as np
import matplotlib.pyplot as plt

# Parameters
#  Custom colors
color_1 = "#62C4DD"  # Blue
color_2 = "#E94B57"  # Red
color_horizon = "#00284b"  # Deep blue

ylim = [0.75, 1.25]
#  Targets
y = 1
texts = ["i","i+1","i+N"]

#  MPC Horizon
N = 4  # Horizon size
y_offset = 0.1

def setup_figure(fig, yticklabel):
    ax1 = fig.gca()
    # X-axis
    ax1.xaxis.set_ticks_position("top")
    ax1.xaxis.set_label_position("top")

    ax1.set_xlabel("Time", fontsize=14)

    ax1.set_xticks([0, 1, N])
    ax1.set_xticklabels(texts, fontsize=12)
    # Y-axis
    ax1.set_ylabel("MPC iteration", fontsize=14)
    ax1.set_ylim(ylim)
    ax1.set_yticks([y])
    ax1.set_yticklabels([yticklabel], fontsize=12)

    # Remove the outer square (axis spines)
    ax1.spines["top"].set_visible(True)  # Keep the top spine for the arrow
    ax1.spines["right"].set_visible(False)
    ax1.spines["left"].set_visible(True)
    ax1.spines["bottom"].set_visible(False)

    # Add arrows to the end of the axis
    ax1.plot(1, 1, ">k", transform=ax1.transAxes, clip_on=False)

# Variables
x_target_1 = np.array(range(N))
x_target_2 = np.array(range(N, 2 * N))

xmin_horizon = 0
xmax_horizon = N - 1

for i in range(N+1):
    if i == 0:
        ylabel = "i"
    elif i == N:
        ylabel = "i+N"
    else:
        ylabel = "i+{}".format(i)

    fig = plt.figure(figsize=(10, 2.5))
    setup_figure(fig, ylabel)
    plt.plot(x_target_1, np.ones(N)*y, "o", color=color_1)
    plt.plot(x_target_2, np.ones(N)*y, "o", color=color_2)

    xmin = i
    xmax = xmin + N - 1

    if i == 0:  # Set label only on first run
        plt.text(
            (xmax + xmin) / 2,
            y + y_offset,
            "MPC horizon",
            va="bottom",
            ha="center",
            fontsize=12,
            color="black",
            fontweight="bold",
        )

    plt.plot(
        [xmin, xmax],
        [y + y_offset] * 2,
        marker="|",
        markersize=7,
        markeredgewidth=1.5,
        color=color_horizon,
    )

    plt.tight_layout()

    fig.savefig("./assets/part-II/targetSwitch/{}.svg".format(i), bbox_inches="tight")
plt.show()
