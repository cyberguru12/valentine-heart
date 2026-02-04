def create_valentine_gif(filename="valentine.gif"):
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    def heart(t):
        x = 16 * np.sin(t)**3
        y = (
            13 * np.cos(t)
            - 5 * np.cos(2*t)
            - 2 * np.cos(3*t)
            - np.cos(4*t)
        )
        return x, y

    t = np.linspace(0, 2*np.pi, 900)
    hx, hy = heart(t)

    px = np.random.uniform(-30, 30, len(hx))
    py = np.random.uniform(-30, 30, len(hx))

    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.axis("off")
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)

    dots = ax.scatter(px, py, s=6, c="red", alpha=0.85)

    ax.text(
        0, -17,
        "will you be my Vlentine",
        color="white",
        fontsize=14,
        ha="center",
        fontweight="bold"
    )

    def animate(frame):
        nonlocal px, py
        beat = 1 + 0.06 * np.sin(frame / 5)
        tx = hx * beat
        ty = hy * beat
        px += (tx - px) * 0.06
        py += (ty - py) * 0.06
        dots.set_offsets(list(zip(px, py)))
        return dots,

    anim = FuncAnimation(fig, animate, frames=120, interval=50)
    anim.save(filename, writer="pillow", fps=20)
    plt.close()
