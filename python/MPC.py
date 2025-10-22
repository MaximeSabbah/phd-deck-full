import numpy as np
import matplotlib.pyplot as plt

plt.style.use("./python/MPC.mplstyle")

# Custom colors
color_target = "#FFBC75"
color_state = "#6941EB"


def compute_trajectory(xinit, xtarget, T):
    coefficients = np.polyfit(
        [xinit[0], xtarget[0] - 1, xtarget[0]], [xinit[1], xtarget[1], xtarget[1]], 3
    )
    poly_func = np.poly1d(coefficients)

    x_values = np.linspace(xinit[0], xtarget[0], T)
    y_values = poly_func(x_values)

    return x_values, y_values


def setup_figure(fig):
    ax = plt.gca()
    ax.set_xlim([-0.5, 8.5])
    ax.set_ylim([-1, 9])
    ax.set_xlabel("Time")
    ax.set_ylabel("State")
    ax.set_xticks([])
    ax.set_yticks([])

    # Remove the lines on the top and right of the graph
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # Add arrows to the end of the axis
    ax.plot(1, 0, ">k", transform=ax.transAxes, clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.transAxes, clip_on=False)


# Parameters
alpha1 = 0.6
kwargs_state = {
    "marker": "o",
    "markersize": 7,
    "markeredgewidth": 0,
    "color": color_state,
}
kwargs_target = {
    "marker": "x",
    "markersize": 7,
    "markeredgewidth": 2,
    "color": color_target,
}
kwargs_int_state = kwargs_state.copy()
kwargs_int_state["color"] = color_target
kwargs_traj = {"linestyle": "--", "linewidth": 2, "color": color_target}
kwargs_arrow = {
    "width": 0.1,
    "head_width": 0.3,
    "edgecolor": "None",
    "color": color_target,
    "antialiased": True,
    "length_includes_head": True,
}
#   Starting state
x0 = [0, 0]
#   Target state
xtarget = [8, 8]

X0, Y0 = compute_trajectory(x0, xtarget, 5)
x1 = [X0[1], np.ceil(Y0[1]) + 1]
X1, Y1 = compute_trajectory(x1, xtarget, 4)

# Figure 1
fig = plt.figure()
setup_figure(fig)
# x0
plt.plot(x0[0], x0[1], **kwargs_state)
# xtarget
plt.plot(xtarget[0], xtarget[1], **kwargs_target)
fig.savefig("./assets/part-I/MPC/1.svg", bbox_inches="tight")

# Figure 2
fig = plt.figure()
setup_figure(fig)
# Optimal trajectory
plt.plot(X0, Y0, **kwargs_traj)
# x0
plt.plot(x0[0], x0[1], **kwargs_state)
# xtarget
plt.plot(xtarget[0], xtarget[1], **kwargs_target)
fig.savefig("./assets/part-I/MPC/2.svg", bbox_inches="tight")

# Figure 3
fig = plt.figure()
setup_figure(fig)
# Optimal trajectory
plt.plot(X0, Y0, **kwargs_traj)
# x0
plt.plot(x0[0], x0[1], **kwargs_state)
# Desired x1
plt.plot(X0[1], Y0[1], **kwargs_int_state)
# xtarget
plt.plot(xtarget[0], xtarget[1], **kwargs_target)
# Optimal command
plt.arrow(x0[0], x0[1], 0.7 * (X0[1] - x0[0]), 0.7 * (Y0[1] - x0[1]), **kwargs_arrow)
fig.savefig("./assets/part-I/MPC/3.svg", bbox_inches="tight")

# Figure 4
fig = plt.figure()
setup_figure(fig)
# Optimal trajectory
plt.plot(X0, Y0, alpha=alpha1, **kwargs_traj)
# x0
plt.plot(x0[0], x0[1], alpha=alpha1, **kwargs_state)
# x1
plt.plot(x1[0], x1[1], **kwargs_state)
# Desired x1
plt.plot(X0[1], Y0[1], alpha=alpha1, **kwargs_int_state)
# xtarget
plt.plot(xtarget[0], xtarget[1], **kwargs_target)
fig.savefig("./assets/part-I/MPC/4.svg", bbox_inches="tight")

# Figure 5
fig = plt.figure()
setup_figure(fig)
# Optimal trajectories
plt.plot(X0, Y0, alpha=alpha1, **kwargs_traj)
plt.plot(X1, Y1, **kwargs_traj)
# x0
plt.plot(x0[0], x0[1], alpha=alpha1, **kwargs_state)
# x1
plt.plot(x1[0], x1[1], **kwargs_state)
# xtarget
plt.plot(xtarget[0], xtarget[1], **kwargs_target)
fig.savefig("./assets/part-I/MPC/5.svg", bbox_inches="tight")

plt.show()
