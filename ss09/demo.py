import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Polygon, Rectangle

def draw_duong_face():
    fig, ax = plt.subplots(figsize=(4, 6))

    # ================== NỀN ==================
    bg = Rectangle((0, 0), 1, 1,
                   facecolor="#0b63c5", edgecolor="none")
    ax.add_patch(bg)

    # ================== CỔ + ÁO ==================
    # cổ
    neck = Rectangle((0.42, 0.20), 0.16, 0.13,
                     facecolor="#f5cfa6", edgecolor="#e0a878", linewidth=1.5)
    ax.add_patch(neck)

    # thân áo
    shirt = Polygon(
        [
            (0.25, 0.00),
            (0.75, 0.00),
            (0.85, 0.20),
            (0.15, 0.20),
        ],
        closed=True,
        facecolor="#ffffff",
        edgecolor="#c0c0c0",
        linewidth=1.5,
    )
    ax.add_patch(shirt)

    # cổ áo trái
    collar_left = Polygon(
        [
            (0.42, 0.20),
            (0.30, 0.17),
            (0.36, 0.10),
        ],
        closed=True,
        facecolor="#ffffff",
        edgecolor="#c0c0c0",
        linewidth=1.0,
    )
    ax.add_patch(collar_left)

    # cổ áo phải
    collar_right = Polygon(
        [
            (0.58, 0.20),
            (0.70, 0.17),
            (0.64, 0.10),
        ],
        closed=True,
        facecolor="#ffffff",
        edgecolor="#c0c0c0",
        linewidth=1.0,
    )
    ax.add_patch(collar_right)

    # bóng cổ áo / áo trong
    inner_shirt = Polygon(
        [
            (0.42, 0.20),
            (0.36, 0.10),
            (0.64, 0.10),
            (0.58, 0.20),
        ],
        closed=True,
        facecolor="#e6e6e6",
        edgecolor="none",
    )
    ax.add_patch(inner_shirt)

    # ================== KHUÔN MẶT ==================
    # form mặt (oval dọc)
    face = Ellipse(
        (0.5, 0.58),  # tâm
        0.44,         # ngang
        0.62,         # dọc
        facecolor="#f5cfa6",
        edgecolor="#e0a878",
        linewidth=2,
    )
    ax.add_patch(face)

    # tai
    ear_left = Ellipse(
        (0.28, 0.58),
        0.06,
        0.16,
        facecolor="#f5cfa6",
        edgecolor="#e0a878",
        linewidth=1.5,
    )
    ear_right = Ellipse(
        (0.72, 0.58),
        0.06,
        0.16,
        facecolor="#f5cfa6",
        edgecolor="#e0a878",
        linewidth=1.5,
    )
    ax.add_patch(ear_left)
    ax.add_patch(ear_right)
    plt.axis("off")
    plt.show()
draw_duong_face()