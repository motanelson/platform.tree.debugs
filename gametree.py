import tkinter as tk
import time


# ==========================================
# TREE NODE
# ==========================================

class nodes:
    def __init__(self, value):
        self.value = value
        self.nexts = None
        self.childs = None


# ==========================================
# LOAD TREE FROM TEXT
# ==========================================

def loads(files):

    tree = nodes("start")

    stack = [tree]

    f1 = open(files, "r")
    contents = f1.read().split("\n")
    f1.close()

    for n in contents:

        if n.strip() == "":
            continue

        count = 0

        while count < len(n) and n[count] == " ":
            count += 1

        nodex = nodes(n.strip())

        # child
        if count > len(stack) - 1:

            stack[-1].childs = nodex
            stack.append(nodex)

        # next
        elif count == len(stack) - 1:

            stack[-1].nexts = nodex
            stack[-1] = nodex

        # back levels
        else:

            while count < len(stack) - 1:
                stack.pop()

            stack[-1].nexts = nodex
            stack[-1] = nodex

    return tree


# ==========================================
# GAME WINDOW
# ==========================================

class Game:

    def __init__(self, rootnode):

        self.rootnode = rootnode
        self.current = rootnode

        self.stack = [rootnode]

        self.cooldown = False

        self.win = tk.Tk()

        self.win.title("Tree Dungeon")

        self.canvas = tk.Canvas(
            self.win,
            width=900,
            height=600,
            bg="black",
            highlightthickness=0
        )

        self.canvas.pack(fill="both", expand=True)

        self.win.bind("<Left>", self.go_back)
        self.win.bind("<Right>", self.go_next)
        self.win.bind("<Up>", self.go_child)

        self.draw()

        self.win.mainloop()

    # ======================================
    # DRAW ROOM
    # ======================================

    def draw(self):

        self.canvas.delete("all")

        w = 900
        h = 600

        # title
        self.canvas.create_text(
            w // 2,
            40,
            text="ROOM : " + self.current.value,
            fill="white",
            font=("Courier", 24, "bold")
        )

        # path
        path = ""

        for n in self.stack:
            path += "\\" + n.value

        self.canvas.create_text(
            w // 2,
            80,
            text=path,
            fill="white",
            font=("Courier", 12)
        )

        # ground
        self.canvas.create_line(
            0,
            500,
            w,
            500,
            fill="white"
        )

        # =========================
        # BACK DOOR
        # =========================

        if len(self.stack) > 1:

            self.draw_door(
                80,
                300,
                "BACK",
                "LEFT"
            )

        # =========================
        # NEXT DOOR
        # =========================

        if self.current.nexts is not None:

            self.draw_door(
                350,
                250,
                self.current.nexts.value,
                "RIGHT"
            )

        # =========================
        # CHILD DOOR
        # =========================

        if self.current.childs is not None:

            self.draw_door(
                620,
                180,
                self.current.childs.value,
                "UP"
            )

        # controls
        self.canvas.create_text(
            w // 2,
            560,
            text="LEFT = BACK     RIGHT = NEXT     UP = CHILD",
            fill="white",
            font=("Courier", 14)
        )

    # ======================================
    # DRAW DOOR
    # ======================================

    def draw_door(self, x, y, title, keyname):

        # door rectangle
        self.canvas.create_line(x, y, x, y + 140, fill="white", width=3)
        self.canvas.create_line(x + 100, y, x + 100, y + 140, fill="white", width=3)

        self.canvas.create_line(x, y, x + 100, y, fill="white", width=3)

        self.canvas.create_line(
            x,
            y,
            x + 50,
            y - 50,
            fill="white",
            width=3
        )

        self.canvas.create_line(
            x + 100,
            y,
            x + 50,
            y - 50,
            fill="white",
            width=3
        )

        # label
        self.canvas.create_text(
            x + 50,
            y - 80,
            text=title,
            fill="white",
            font=("Courier", 16, "bold")
        )

        # key
        self.canvas.create_text(
            x + 50,
            y + 170,
            text=keyname,
            fill="white",
            font=("Courier", 12)
        )

    # ======================================
    # KEY COOLDOWN
    # ======================================

    def lock(self):

        self.cooldown = True

        self.win.after(250, self.unlock)

    def unlock(self):

        self.cooldown = False

    # ======================================
    # MOVE BACK
    # ======================================

    def go_back(self, event):

        if self.cooldown:
            return

        if len(self.stack) > 1:

            self.stack.pop()

            self.current = self.stack[-1]

            self.flash()

            self.lock()

    # ======================================
    # MOVE NEXT
    # ======================================

    def go_next(self, event):

        if self.cooldown:
            return

        if self.current.nexts is not None:

            self.current = self.current.nexts

            self.stack[-1] = self.current

            self.flash()

            self.lock()

    # ======================================
    # MOVE CHILD
    # ======================================

    def go_child(self, event):

        if self.cooldown:
            return

        if self.current.childs is not None:

            self.current = self.current.childs

            self.stack.append(self.current)

            self.flash()

            self.lock()

    # ======================================
    # ROOM TRANSITION EFFECT
    # ======================================

    def flash(self):

        self.canvas.delete("all")

        self.canvas.create_rectangle(
            0,
            0,
            900,
            600,
            fill="white",
            outline="white"
        )

        self.win.update()

        time.sleep(0.05)

        self.draw()


# ==========================================
# START
# ==========================================

tree = loads("map.txt")

Game(tree)
