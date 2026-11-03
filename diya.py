import turtle as t
import math, random

s = t.Screen()
s.setup(1080, 1400, 0, 0)
s.bgcolor("black")
s.title("Happy Diwali")
pen = t.Turtle(visible=False)
pen.speed(4)
sin, cos, PI = math.sin, math.cos, math.pi


def shape(pts, fill, line=None, w=4):
    pen.penup()
    pen.goto(pts[0])
    pen.pendown()
    pen.color(line or fill, fill)
    pen.width(w)
    pen.begin_fill()
    for p in pts:
        pen.goto(p)
    pen.end_fill()


def bowl(rx, ry, cy=-150):
    return [(rx * cos(a / 20 * PI),
             cy - ry * sin(a / 20 * PI))
            for a in range(21)]


# soft glow behind the lamp
s.tracer(0)
for i in range(40, 0, -1):
    pen.penup()
    pen.goto(0, 40)
    r, g = 0.6 - i / 70, 0.25 - i / 170
    pen.dot(i * 17, (r, g, 0))
s.tracer(1)

# the clay diya
GOLD = "#ffcc33"
shape(bowl(360, 230), "#a4310c", GOLD, 6)
shape(bowl(318, 196, -156), "#d9561c")
base = [(-70, -370), (70, -370),
        (115, -420), (-115, -420)]
shape(base, "#a4310c", GOLD, 5)

# gold zigzag pattern
pen.color(GOLD)
pen.width(6)
pen.penup()
for k in range(17):
    a = (k + 0.5) / 17 * PI
    r = 0.5 if k % 2 else 0.78
    pen.goto(360 * r * cos(a),
             -135 - 196 * r * sin(a))
    pen.pendown()

# dots on the clay
for k in range(11):
    a = (k + 1) / 12 * PI
    pen.penup()
    pen.goto(285 * cos(a),
             -170 - 170 * sin(a))
    pen.dot(22, "#fff1c1")
    pen.dot(10, "#e0115f")

# rim filled with ghee
rim = [(360 * cos(a / 30 * PI),
        -150 + 44 * sin(a / 30 * PI))
       for a in range(61)]
shape(rim, "#4a1a05", GOLD, 7)

flame = t.Turtle(visible=False)
deco = t.Turtle(visible=False)
deco.penup()
FIRE = [(1, "#ff5a00"), (0.72, "#ffb000"),
        (0.42, "#fff6c8")]


def draw_flame(h, w, sway):
    for k, c in FIRE:
        right, left = [], []
        for i in range(31):
            u = i / 30
            x = w * k * sin(PI * u ** 0.7)
            x *= (1 - u) ** 0.35
            y = -140 + h * k * u
            dx = sway * u * u
            right.append((dx + x, y))
            left.append((dx - x, y))
        flame.penup()
        flame.goto(right[0])
        flame.color(c)
        flame.begin_fill()
        for p in right + left[::-1]:
            flame.goto(p)
        flame.end_fill()


def sparkle():
    while True:
        x = random.randint(-510, 510)
        y = random.randint(-560, 650)
        if abs(x) > 390 or y > 520:
            break
    r = random.randint(18, 40)
    deco.goto(x, y)
    deco.color(random.choice(
        ["#ffd700", "#ffffff", "#ff9ecb"]))
    deco.begin_fill()
    for k in range(8):
        a = k * PI / 4
        d = r if k % 2 == 0 else r / 3.5
        deco.goto(x + d * cos(a),
                  y + d * sin(a))
    deco.end_fill()


def rangoli(k):
    a = PI + k / 24 * PI
    deco.goto(480 * cos(a),
              -480 + 80 * sin(a))
    colors = ["#ff3c8e", "#ffd700",
              "#00e5ff", "#ff7a00"]
    deco.dot(30, colors[k % 4])


def greet():
    font = ("Pacifico", 96, "normal")
    deco.goto(0, 380)
    deco.color("#ff7a00")
    deco.write("Happy Diwali", align="center",
               font=font)
    deco.goto(-5, 386)
    deco.color("#ffd700")
    deco.write("Happy Diwali", align="center",
               font=font)


frame = 0


def animate():
    global frame
    flame.clear()
    draw_flame(330 + random.randint(-35, 35),
               100 + random.randint(-10, 10),
               random.randint(-25, 25))
    if frame < 25:
        rangoli(frame)
    if 25 <= frame < 70 and frame % 3 == 0:
        sparkle()
    if frame == 75:
        greet()
    frame += 1
    s.update()
    s.ontimer(animate, 60)


s.tracer(0)
animate()
s.mainloop()
