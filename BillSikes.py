#!/usr/bin/env python3
"""
BillSikes — an all-in-one math toolkit.

Covers: Figures (Shapes), Percentages, Ratio & Proportion,
        Rigid Motion, Probability, Conversions, Rates,
        Bearings & Vectors, Tools.

Run with:  python3 BillSikes.py
Requires:  Python 3 standard library only (tkinter is included).
           No external image files or Pillow needed.
"""

import re
import math
import tkinter as tk
from tkinter import ttk, messagebox


# ──────────────────────────────────────────────────────────────────────────── #
#  Design tokens
# ──────────────────────────────────────────────────────────────────────────── #
APP_TITLE   = "BillSikes"
WINDOW_SIZE = (1060, 720)

# Palette — slate-and-indigo professional theme
BG_DEEP      = "#0f1629"   # deep navy sidebar / window bg
BG_MID       = "#1a2340"   # sidebar panel bg
CARD_BG      = "#ffffff"
CARD_BORDER  = "#dde3f0"

ACCENT       = "#4f6ef7"   # indigo-blue primary
ACCENT_DARK  = "#3a56d4"
ACCENT_LIGHT = "#eef1fe"

GOOD         = "#16a34a"
DANGER       = "#dc2626"

TEXT_DARK    = "#1e293b"
TEXT_MID     = "#475569"
TEXT_MUTED   = "#94a3b8"
TEXT_WHITE   = "#f8fafc"

SHAPE_FILL   = "#eef1fe"   # light indigo fill for canvas shapes
SHAPE_STROKE = "#4f6ef7"   # indigo outline
SHAPE_DIM    = "#94a3b8"   # dimension labels

# Typography
FONT_UI      = "Helvetica"
T_DISPLAY    = (FONT_UI, 20, "bold")
T_TITLE      = (FONT_UI, 15, "bold")
T_SECTION    = (FONT_UI, 12, "bold")
T_BODY       = (FONT_UI, 11)
T_SMALL      = (FONT_UI, 9)
T_FORMULA    = (FONT_UI, 12, "bold")
T_RESULT     = (FONT_UI, 12, "bold")
T_NOTE       = (FONT_UI, 9, "italic")

# Sidebar width
SIDEBAR_W = 0          # we use a top menu-bar, sidebar hidden; keep for future use


# ──────────────────────────────────────────────────────────────────────────── #
#  Canvas shape drawers  (replace every hardcoded base64 image)
# ──────────────────────────────────────────────────────────────────────────── #
def _shape_canvas(parent, width=220, height=140):
    """Create and return a blank canvas with the card background."""
    c = tk.Canvas(parent, width=width, height=height,
                  bg=CARD_BG, highlightthickness=0)
    return c


def draw_circle(parent):
    c = _shape_canvas(parent)
    cx, cy, r = 110, 70, 54
    c.create_oval(cx - r, cy - r, cx + r, cy + r,
                  fill=SHAPE_FILL, outline=SHAPE_STROKE, width=2)
    # radius arrow
    c.create_line(cx, cy, cx + r, cy, fill=SHAPE_STROKE, width=1, dash=(4, 3))
    c.create_oval(cx - 3, cy - 3, cx + 3, cy + 3, fill=SHAPE_STROKE, outline="")
    c.create_text(cx + r // 2, cy - 11, text="r", fill=SHAPE_STROKE,
                  font=(FONT_UI, 10, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_rectangle(parent):
    c = _shape_canvas(parent)
    x0, y0, x1, y1 = 30, 35, 190, 105
    c.create_rectangle(x0, y0, x1, y1, fill=SHAPE_FILL,
                        outline=SHAPE_STROKE, width=2)
    # dimension labels
    mx = (x0 + x1) // 2
    my = (y0 + y1) // 2
    c.create_text(mx, y1 + 12, text="L", fill=SHAPE_STROKE,
                  font=(FONT_UI, 10, "bold"))
    c.create_text(x0 - 12, my, text="B", fill=SHAPE_STROKE,
                  font=(FONT_UI, 10, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_square(parent):
    c = _shape_canvas(parent)
    x0, y0, x1, y1 = 55, 20, 165, 120
    c.create_rectangle(x0, y0, x1, y1, fill=SHAPE_FILL,
                        outline=SHAPE_STROKE, width=2)
    mx = (x0 + x1) // 2
    c.create_text(mx, y1 + 12, text="s", fill=SHAPE_STROKE,
                  font=(FONT_UI, 10, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_triangle(parent):
    c = _shape_canvas(parent)
    pts = [110, 15, 25, 120, 195, 120]
    c.create_polygon(pts, fill=SHAPE_FILL, outline=SHAPE_STROKE, width=2)
    # height dashed line
    c.create_line(110, 15, 110, 120, fill=SHAPE_DIM, width=1, dash=(4, 3))
    c.create_text(120, 65, text="h", fill=SHAPE_DIM, font=(FONT_UI, 10))
    c.create_text(110, 132, text="b", fill=SHAPE_STROKE, font=(FONT_UI, 10, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_right_triangle(parent):
    """Pythagorean theorem diagram."""
    c = _shape_canvas(parent, width=200, height=150)
    pts = [30, 120, 30, 20, 170, 120]
    c.create_polygon(pts, fill=SHAPE_FILL, outline=SHAPE_STROKE, width=2)
    # right-angle mark
    c.create_rectangle(30, 100, 50, 120, outline=SHAPE_STROKE, width=1)
    c.create_text(95, 22, text="c  (hyp)", fill=SHAPE_STROKE,
                  font=(FONT_UI, 9, "bold"))
    c.create_text(14, 70, text="a", fill=SHAPE_STROKE,
                  font=(FONT_UI, 10, "bold"))
    c.create_text(100, 133, text="b", fill=SHAPE_STROKE,
                  font=(FONT_UI, 10, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_rhombus(parent):
    c = _shape_canvas(parent)
    cx, cy = 110, 70
    dx, dy = 75, 50
    pts = [cx, cy - dy, cx + dx, cy, cx, cy + dy, cx - dx, cy]
    c.create_polygon(pts, fill=SHAPE_FILL, outline=SHAPE_STROKE, width=2)
    c.create_line(cx - dx, cy, cx + dx, cy, fill=SHAPE_DIM, width=1, dash=(4, 3))
    c.create_line(cx, cy - dy, cx, cy + dy, fill=SHAPE_DIM, width=1, dash=(4, 3))
    c.create_text(cx, cy - dy - 10, text="d₁", fill=SHAPE_STROKE,
                  font=(FONT_UI, 9, "bold"))
    c.create_text(cx + dx + 10, cy, text="d₂", fill=SHAPE_STROKE,
                  font=(FONT_UI, 9, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_parallelogram(parent):
    c = _shape_canvas(parent)
    pts = [50, 110, 90, 30, 190, 30, 150, 110]
    c.create_polygon(pts, fill=SHAPE_FILL, outline=SHAPE_STROKE, width=2)
    c.create_line(90, 30, 90, 110, fill=SHAPE_DIM, width=1, dash=(4, 3))
    c.create_text(100, 70, text="h", fill=SHAPE_DIM, font=(FONT_UI, 9))
    c.create_text(120, 122, text="b", fill=SHAPE_STROKE, font=(FONT_UI, 10, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_kite(parent):
    c = _shape_canvas(parent)
    cx = 110
    pts = [cx, 10, cx + 70, 70, cx, 130, cx - 70, 70]
    c.create_polygon(pts, fill=SHAPE_FILL, outline=SHAPE_STROKE, width=2)
    c.create_line(cx, 10, cx, 130, fill=SHAPE_DIM, width=1, dash=(4, 3))
    c.create_line(cx - 70, 70, cx + 70, 70, fill=SHAPE_DIM, width=1, dash=(4, 3))
    c.create_text(cx + 8, 35, text="d₁", fill=SHAPE_STROKE, font=(FONT_UI, 9, "bold"))
    c.create_text(cx + 40, 60, text="d₂", fill=SHAPE_STROKE, font=(FONT_UI, 9, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_trapezium(parent):
    c = _shape_canvas(parent)
    pts = [55, 30, 175, 30, 200, 115, 30, 115]
    c.create_polygon(pts, fill=SHAPE_FILL, outline=SHAPE_STROKE, width=2)
    # parallel sides labels
    c.create_text(115, 20, text="a", fill=SHAPE_STROKE, font=(FONT_UI, 10, "bold"))
    c.create_text(115, 128, text="b", fill=SHAPE_STROKE, font=(FONT_UI, 10, "bold"))
    # height
    c.create_line(55, 30, 55, 115, fill=SHAPE_DIM, width=1, dash=(4, 3))
    c.create_text(42, 72, text="h", fill=SHAPE_DIM, font=(FONT_UI, 9))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_cylinder(parent):
    c = _shape_canvas(parent, width=180, height=150)
    x0, y0, x1, y1_top = 30, 20, 150, 45
    y1_bot = 130
    # body
    c.create_rectangle(x0, (y0 + y1_top) // 2, x1, y1_bot,
                        fill=SHAPE_FILL, outline="")
    # top ellipse
    c.create_oval(x0, y0, x1, y1_top, fill=SHAPE_FILL,
                  outline=SHAPE_STROKE, width=2)
    # bottom ellipse (partial)
    c.create_arc(x0, y1_bot - 12, x1, y1_bot + 12,
                 start=0, extent=-180, style="arc",
                 outline=SHAPE_STROKE, width=2)
    # side lines
    c.create_line(x0, (y0 + y1_top) // 2, x0, y1_bot, fill=SHAPE_STROKE, width=2)
    c.create_line(x1, (y0 + y1_top) // 2, x1, y1_bot, fill=SHAPE_STROKE, width=2)
    # labels
    cx = (x0 + x1) // 2
    c.create_text(x1 + 12, (y1_top + y1_bot) // 2, text="h",
                  fill=SHAPE_STROKE, font=(FONT_UI, 10, "bold"))
    c.create_text(cx + 10, (y0 + y1_top) // 2 - 4, text="r",
                  fill=SHAPE_STROKE, font=(FONT_UI, 9, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_cone(parent):
    c = _shape_canvas(parent, width=180, height=150)
    cx = 90
    apex_y = 15
    base_y = 125
    rx = 60
    # body triangle
    c.create_polygon([cx, apex_y, cx - rx, base_y, cx + rx, base_y],
                     fill=SHAPE_FILL, outline="")
    # slant sides
    c.create_line(cx, apex_y, cx - rx, base_y, fill=SHAPE_STROKE, width=2)
    c.create_line(cx, apex_y, cx + rx, base_y, fill=SHAPE_STROKE, width=2)
    # base ellipse
    c.create_oval(cx - rx, base_y - 10, cx + rx, base_y + 10,
                  fill=SHAPE_FILL, outline=SHAPE_STROKE, width=2)
    # labels
    c.create_text(cx - rx // 2 - 10, (apex_y + base_y) // 2 - 5,
                  text="l", fill=SHAPE_STROKE, font=(FONT_UI, 10, "bold"))
    c.create_text(cx + rx // 2, base_y + 16, text="r",
                  fill=SHAPE_STROKE, font=(FONT_UI, 9, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_sphere(parent):
    c = _shape_canvas(parent)
    cx, cy, r = 110, 70, 55
    c.create_oval(cx - r, cy - r, cx + r, cy + r,
                  fill=SHAPE_FILL, outline=SHAPE_STROKE, width=2)
    # equator ellipse
    c.create_arc(cx - r, cy - 16, cx + r, cy + 16,
                 start=0, extent=180, style="arc",
                 outline=SHAPE_DIM, width=1, dash=(4, 3))
    c.create_arc(cx - r, cy - 16, cx + r, cy + 16,
                 start=180, extent=180, style="arc",
                 outline=SHAPE_DIM, width=1)
    # radius
    c.create_line(cx, cy, cx + r, cy, fill=SHAPE_STROKE, width=1, dash=(4, 3))
    c.create_text(cx + r // 2, cy - 10, text="r", fill=SHAPE_STROKE,
                  font=(FONT_UI, 10, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_cuboid(parent):
    c = _shape_canvas(parent, width=220, height=145)
    # front face
    pts_f = [30, 50, 140, 50, 140, 120, 30, 120]
    c.create_rectangle(30, 50, 140, 120, fill=SHAPE_FILL,
                        outline=SHAPE_STROKE, width=2)
    # top face (parallelogram)
    pts_t = [30, 50, 75, 15, 185, 15, 140, 50]
    c.create_polygon(pts_t, fill="#d6ddfc", outline=SHAPE_STROKE, width=2)
    # right face
    pts_r = [140, 50, 185, 15, 185, 85, 140, 120]
    c.create_polygon(pts_r, fill="#c8d0f8", outline=SHAPE_STROKE, width=2)
    # labels
    c.create_text(85, 133, text="L", fill=SHAPE_STROKE, font=(FONT_UI, 9, "bold"))
    c.create_text(15, 85, text="H", fill=SHAPE_STROKE, font=(FONT_UI, 9, "bold"))
    c.create_text(170, 12, text="B", fill=SHAPE_STROKE, font=(FONT_UI, 9, "bold"))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_pyramid(parent):
    c = _shape_canvas(parent, width=200, height=150)
    cx, apex_y = 100, 10
    base_pts = [25, 125, 90, 100, 175, 125, 110, 150]
    # back face
    c.create_polygon([25, 125, cx, apex_y, 110, 150], fill="#d6ddfc",
                     outline=SHAPE_STROKE, width=1)
    c.create_polygon([cx, apex_y, 110, 150, 175, 125], fill="#c8d0f8",
                     outline=SHAPE_STROKE, width=1)
    # front faces
    c.create_polygon([25, 125, cx, apex_y, 90, 100], fill=SHAPE_FILL,
                     outline=SHAPE_STROKE, width=2)
    c.create_polygon([90, 100, cx, apex_y, 175, 125], fill="#dce3fd",
                     outline=SHAPE_STROKE, width=2)
    c.create_text(cx, apex_y - 8, text="apex", fill=SHAPE_DIM,
                  font=(FONT_UI, 8))
    c.pack(anchor="w", pady=(0, 10))
    return c


def draw_prism(parent):
    c = _shape_canvas(parent, width=220, height=145)
    # triangular prism
    # front triangle
    fp = [30, 115, 105, 20, 105, 115]
    c.create_polygon(fp, fill=SHAPE_FILL, outline=SHAPE_STROKE, width=2)
    # back triangle (offset)
    bp = [30 + 90, 115, 105 + 90, 20, 105 + 90, 115]
    c.create_polygon(bp, fill="#d6ddfc", outline=SHAPE_STROKE, width=1)
    # connecting lines
    for (x1, y1), (x2, y2) in zip(zip(fp[0::2], fp[1::2]),
                                    zip(bp[0::2], bp[1::2])):
        c.create_line(x1, y1, x2, y2, fill=SHAPE_STROKE, width=2)
    c.create_text(105, 130, text="length", fill=SHAPE_STROKE,
                  font=(FONT_UI, 9))
    c.pack(anchor="w", pady=(0, 10))
    return c


# Map image_key → draw function
SHAPE_DRAWERS = {
    "circle":    draw_circle,
    "ccircle":   draw_circle,   # circumference uses same circle
    "rectangle": draw_rectangle,
    "square":    draw_square,
    "triangle":  draw_triangle,
    "rhombus":   draw_rhombus,
    "kite":      draw_kite,
    "parallelogram": draw_parallelogram,
    "trapezium": draw_trapezium,
    "theorem":   draw_right_triangle,
    "cylinder":  draw_cylinder,
    "cone":      draw_cone,
    "sphere":    draw_sphere,
    "cuboid":    draw_cuboid,
    "pyramid":   draw_pyramid,
    "prism":     draw_prism,
}


# ──────────────────────────────────────────────────────────────────────────── #
#  Solve descriptor
# ──────────────────────────────────────────────────────────────────────────── #
class Solve:
    """One 'solve for ___' branch of a formula-calculator page."""
    __slots__ = ("label", "fields", "compute", "unit", "note")

    def __init__(self, label, fields, compute, unit="", note=None):
        self.label   = label
        self.fields  = fields
        self.compute = compute
        self.unit    = unit
        self.note    = note


# ──────────────────────────────────────────────────────────────────────────── #
#  App
# ──────────────────────────────────────────────────────────────────────────── #
class BillSikesApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        w, h = WINDOW_SIZE
        self.root.geometry(f"{w}x{h}")
        self.root.resizable(True, True)
        self.root.configure(bg=BG_DEEP)
        self._calc_window = None
        self._sqrt_window = None
        self._apply_style()
        self._build_chrome(w, h)
        self._build_menu()
        self.show_home()

    def run(self):
        self.root.mainloop()

    # ── ttk style ─────────────────────────────────────────────────────────── #
    def _apply_style(self):
        s = ttk.Style()
        try:
            s.theme_use("clam")
        except Exception:
            pass
        s.configure("TCombobox",
                     fieldbackground="white",
                     background="white",
                     foreground=TEXT_DARK,
                     selectbackground=ACCENT_LIGHT,
                     selectforeground=TEXT_DARK,
                     padding=4)
        s.configure("TSeparator", background=CARD_BORDER)
        s.configure("TScrollbar", background=CARD_BORDER, troughcolor=CARD_BG,
                     arrowcolor=TEXT_MID)

    # ── Window chrome (header bar + content card) ──────────────────────────── #
    def _build_chrome(self, w, h):
        # Thin top accent bar
        tk.Frame(self.root, bg=ACCENT, height=3).pack(fill="x", side="top")

        # Header strip
        header = tk.Frame(self.root, bg=BG_DEEP, height=52)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)
        tk.Label(header, text="BillSikes", font=(FONT_UI, 16, "bold"),
                 bg=BG_DEEP, fg=TEXT_WHITE).pack(side="left", padx=20, pady=12)
        tk.Label(header, text="Math Toolkit", font=(FONT_UI, 10),
                 bg=BG_DEEP, fg=TEXT_MUTED).pack(side="left", pady=12)

        # Main content area (white card)
        self.content_frame = tk.Frame(self.root, bg=CARD_BG)
        self.content_frame.pack(fill="both", expand=True,
                                 padx=16, pady=(0, 14))

        # Scrollable inner frame
        self._canvas_scroll = tk.Canvas(self.content_frame, bg=CARD_BG,
                                         highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical",
                                   command=self._canvas_scroll.yview)
        self._canvas_scroll.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self._canvas_scroll.pack(side="left", fill="both", expand=True)

        self.content = tk.Frame(self._canvas_scroll, bg=CARD_BG)
        self._scroll_win = self._canvas_scroll.create_window(
            (0, 0), window=self.content, anchor="nw")

        def _on_configure(event):
            self._canvas_scroll.configure(
                scrollregion=self._canvas_scroll.bbox("all"))

        def _on_canvas_resize(event):
            self._canvas_scroll.itemconfig(self._scroll_win, width=event.width)

        self.content.bind("<Configure>", _on_configure)
        self._canvas_scroll.bind("<Configure>", _on_canvas_resize)

        # Mouse-wheel scrolling
        def _mousewheel(event):
            self._canvas_scroll.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.root.bind_all("<MouseWheel>", _mousewheel)

    # ── helpers ───────────────────────────────────────────────────────────── #
    def clear_content(self):
        for w in self.content.winfo_children():
            w.destroy()
        self._canvas_scroll.yview_moveto(0)

    def start_page(self, title, show_home_button=True):
        """Wipe the card, add a title bar, return body frame."""
        self.clear_content()
        self.root.title(f"{APP_TITLE} — {title}")

        # Title bar row
        bar = tk.Frame(self.content, bg=CARD_BG)
        bar.pack(fill="x", padx=24, pady=(18, 0))

        left = tk.Frame(bar, bg=CARD_BG)
        left.pack(side="left")
        tk.Label(left, text=title, font=T_DISPLAY, bg=CARD_BG,
                 fg=TEXT_DARK).pack(side="left")

        if show_home_button:
            btn = tk.Button(bar, text="⌂  Home", command=self.show_home,
                            bg=ACCENT, fg=TEXT_WHITE,
                            activebackground=ACCENT_DARK,
                            activeforeground=TEXT_WHITE,
                            relief="flat", padx=14, pady=6,
                            cursor="hand2", font=(FONT_UI, 10, "bold"),
                            bd=0)
            btn.pack(side="right")

        # Separator
        sep_frame = tk.Frame(self.content, bg=CARD_BORDER, height=1)
        sep_frame.pack(fill="x", padx=24, pady=(10, 0))

        body = tk.Frame(self.content, bg=CARD_BG)
        body.pack(fill="both", expand=True, padx=24, pady=16)
        return body

    # ── number formatting ──────────────────────────────────────────────────── #
    def fmt_num(self, x):
        if isinstance(x, complex):
            return str(x)
        if isinstance(x, float):
            if math.isnan(x):   return "undefined"
            if math.isinf(x):   return "infinite"
        if abs(x - round(x)) < 1e-9:
            return f"{int(round(x)):,}"
        return f"{x:,.4f}".rstrip("0").rstrip(".")

    def parse_float(self, entry, field_name):
        txt = entry.get().strip()
        if txt == "":
            raise ValueError(f'Please enter a value for "{field_name}".')
        try:
            return float(txt)
        except ValueError:
            raise ValueError(f'"{txt}" is not a number for "{field_name}".')

    # ── widget helpers ─────────────────────────────────────────────────────── #
    def add_labeled_entry(self, parent, label_text, width=16, default=""):
        row = tk.Frame(parent, bg=CARD_BG)
        row.pack(fill="x", pady=4)
        tk.Label(row, text=label_text + ":", font=T_BODY, bg=CARD_BG,
                 fg=TEXT_MID, width=28, anchor="w").pack(side="left")
        ent = tk.Entry(row, font=T_BODY, width=width,
                       relief="solid", bd=1,
                       highlightthickness=1,
                       highlightbackground=CARD_BORDER,
                       highlightcolor=ACCENT,
                       fg=TEXT_DARK)
        if default:
            ent.insert(0, default)
        ent.pack(side="left")
        return ent

    def add_dropdown(self, parent, label_text, values, width=18):
        row = tk.Frame(parent, bg=CARD_BG)
        row.pack(fill="x", pady=4)
        tk.Label(row, text=label_text + ":", font=T_BODY, bg=CARD_BG,
                 fg=TEXT_MID, width=28, anchor="w").pack(side="left")
        var = tk.StringVar(value=values[0] if values else "")
        combo = ttk.Combobox(row, textvariable=var, state="readonly",
                              values=values, width=width, font=T_BODY)
        combo.pack(side="left")
        return var, combo

    def add_result_label(self, parent):
        var = tk.StringVar()
        result_frame = tk.Frame(parent, bg=ACCENT_LIGHT,
                                 highlightthickness=1,
                                 highlightbackground=ACCENT)
        result_frame.pack(anchor="w", pady=(12, 0), fill="x")
        tk.Label(result_frame, textvariable=var, font=T_RESULT,
                 bg=ACCENT_LIGHT, fg=ACCENT_DARK,
                 wraplength=800, justify="left",
                 padx=12, pady=8).pack(anchor="w")
        return var

    def add_action_buttons(self, parent, calc_command, clear_command=None):
        row = tk.Frame(parent, bg=CARD_BG)
        row.pack(anchor="w", pady=(14, 4))

        calc_btn = tk.Button(row, text="Calculate", command=calc_command,
                             bg=ACCENT, fg=TEXT_WHITE,
                             activebackground=ACCENT_DARK,
                             activeforeground=TEXT_WHITE,
                             relief="flat", padx=18, pady=7,
                             cursor="hand2", font=(FONT_UI, 10, "bold"), bd=0)
        calc_btn.pack(side="left")

        if clear_command:
            clear_btn = tk.Button(row, text="Clear", command=clear_command,
                                  bg="#f1f5f9", fg=TEXT_MID,
                                  activebackground=CARD_BORDER,
                                  activeforeground=TEXT_DARK,
                                  relief="flat", padx=14, pady=7,
                                  cursor="hand2", font=(FONT_UI, 10), bd=0)
            clear_btn.pack(side="left", padx=(8, 0))
        return row

    def safe_run(self, fn, result_var):
        try:
            fn()
        except ValueError as exc:
            msg = str(exc)
            if "math domain error" in msg or not msg:
                msg = ("Those numbers don't work for this formula — "
                       "e.g. a square root of a negative. Please check inputs.")
            messagebox.showerror("Check your input", msg)
        except ZeroDivisionError:
            messagebox.showerror("Math error",
                                  "That calculation divides by zero — check inputs.")
        except Exception as exc:
            messagebox.showerror("Error", f"Couldn't compute ({exc}).")

    # ── formula-page builder ───────────────────────────────────────────────── #
    def build_formula_ui(self, body, options, image_key=None,
                          formula_text=None, intro=None):
        top = tk.Frame(body, bg=CARD_BG)
        top.pack(fill="x")

        left_col = tk.Frame(top, bg=CARD_BG)
        left_col.pack(side="left", anchor="nw", padx=(0, 20))

        # Shape canvas or formula box
        if image_key and image_key in SHAPE_DRAWERS:
            SHAPE_DRAWERS[image_key](left_col)
        elif formula_text:
            fb = tk.Frame(left_col, bg=ACCENT_LIGHT,
                           highlightthickness=1,
                           highlightbackground=ACCENT)
            fb.pack(anchor="w", pady=(0, 10))
            tk.Label(fb, text=formula_text, font=T_FORMULA,
                     bg=ACCENT_LIGHT, fg=ACCENT_DARK,
                     padx=14, pady=8).pack()

        if intro:
            tk.Label(body, text=intro, font=T_BODY, bg=CARD_BG,
                     fg=TEXT_MID, wraplength=780,
                     justify="left").pack(anchor="w", pady=(0, 10))

        # "Solve for" dropdown
        selector = tk.Frame(body, bg=CARD_BG)
        selector.pack(fill="x", pady=(4, 4))
        tk.Label(selector, text="I want to find:", font=T_BODY,
                 bg=CARD_BG, fg=TEXT_MID).pack(side="left", padx=(0, 10))
        choice_var = tk.StringVar()
        combo = ttk.Combobox(selector, textvariable=choice_var,
                              state="readonly",
                              values=[o.label for o in options],
                              width=34, font=T_BODY)
        combo.pack(side="left")

        dynamic = tk.Frame(body, bg=CARD_BG)
        dynamic.pack(fill="both", expand=True, pady=(10, 0))

        def render(event=None):
            for w in dynamic.winfo_children():
                w.destroy()
            opt = next(o for o in options if o.label == choice_var.get())
            entries = {}
            form = tk.Frame(dynamic, bg=CARD_BG)
            form.pack(anchor="w")
            for field in opt.fields:
                row = tk.Frame(form, bg=CARD_BG)
                row.pack(fill="x", pady=4)
                tk.Label(row, text=field + ":", font=T_BODY, bg=CARD_BG,
                         fg=TEXT_MID, width=28, anchor="w").pack(side="left")
                ent = tk.Entry(row, font=T_BODY, width=16,
                               relief="solid", bd=1,
                               highlightthickness=1,
                               highlightbackground=CARD_BORDER,
                               highlightcolor=ACCENT,
                               fg=TEXT_DARK)
                ent.pack(side="left")
                entries[field] = ent
            if opt.note:
                tk.Label(form, text=opt.note, font=T_NOTE,
                         bg=CARD_BG, fg=TEXT_MUTED,
                         wraplength=720, justify="left").pack(anchor="w",
                                                               pady=(6, 0))
            if opt.fields:
                entries[opt.fields[0]].focus_set()

            result_var = tk.StringVar()

            def calc():
                values = [self.parse_float(entries[f], f) for f in opt.fields]
                result = opt.compute(*values)
                unit = f" {opt.unit}" if opt.unit else ""
                result_var.set(f"{opt.label} = {self.fmt_num(result)}{unit}")

            def clear():
                for ent in entries.values():
                    ent.delete(0, tk.END)
                result_var.set("")
                if opt.fields:
                    entries[opt.fields[0]].focus_set()

            self.add_action_buttons(dynamic,
                                     lambda: self.safe_run(calc, result_var),
                                     clear)

            result_frame = tk.Frame(dynamic, bg=ACCENT_LIGHT,
                                     highlightthickness=1,
                                     highlightbackground=ACCENT)
            result_frame.pack(anchor="w", pady=(4, 0), fill="x")
            tk.Label(result_frame, textvariable=result_var, font=T_RESULT,
                     bg=ACCENT_LIGHT, fg=ACCENT_DARK,
                     wraplength=800, justify="left",
                     padx=12, pady=8).pack(anchor="w")

            for ent in entries.values():
                ent.bind("<Return>", lambda e: self.safe_run(calc, result_var))

        combo.bind("<<ComboboxSelected>>", render)
        if options:
            combo.current(0)
            render()

    # ──────────────────────────────────────────────────────────────────────── #
    #  Home page
    # ──────────────────────────────────────────────────────────────────────── #
    def show_home(self):
        body = self.start_page("Math Toolkit", show_home_button=False)

        # Hero blurb
        tk.Label(body,
                 text="Your complete school-math companion.",
                 font=(FONT_UI, 13),
                 bg=CARD_BG, fg=TEXT_MID).pack(anchor="w", pady=(2, 20))

        # Quick-start tiles
        tk.Label(body, text="Quick start", font=T_SECTION,
                 bg=CARD_BG, fg=TEXT_DARK).pack(anchor="w")

        tile_area = tk.Frame(body, bg=CARD_BG)
        tile_area.pack(anchor="w", pady=(10, 0))

        shortcuts = [
            ("◯  Area of a circle",   self.area_circle),
            ("△  Pythagorean theorem", self.pythagoras_page),
            ("▦  Calculator",          self.open_calculator),
            ("√  Square root",         self.open_square_root),
            ("%  Simple interest",     self.simple_interest_page),
            ("⇄  Conversions",         lambda: self.conversions_page("Length")),
        ]
        for i, (label, cmd) in enumerate(shortcuts):
            btn = tk.Button(tile_area, text=label, command=cmd,
                            bg=ACCENT_LIGHT, fg=ACCENT_DARK,
                            activebackground="#d9e0fd",
                            activeforeground=ACCENT_DARK,
                            relief="flat", padx=16, pady=12,
                            cursor="hand2", font=(FONT_UI, 10),
                            anchor="w", bd=0,
                            highlightthickness=1,
                            highlightbackground=ACCENT,
                            width=26)
            btn.grid(in_=tile_area,
                     row=i // 3, column=i % 3,
                     padx=6, pady=6, sticky="ew")

        # Topic overview
        tk.Frame(body, bg=CARD_BORDER, height=1).pack(
            fill="x", pady=(24, 16))
        tk.Label(body, text="Topics covered by this toolkit:",
                 font=T_SECTION, bg=CARD_BG, fg=TEXT_DARK).pack(anchor="w")

        topics = [
            "Figures (Shapes) — area, perimeter, surface area, volume, polygons, Pythagorean theorem",
            "Percentages — simple interest, discount, commission, depreciation, VAT, NHIL, insurance",
            "Ratio & Proportion — direct/inverse proportion, ratio sharing, financial partnership",
            "Rigid Motion — translation, reflection, rotation, enlargement",
            "Probability — basic rules",
            "Conversions — length, mass, time, volume",
            "Rates — speed, density, general rate",
            "Bearings & Vectors — bearings, magnitude/direction, vector addition",
        ]
        for t in topics:
            row = tk.Frame(body, bg=CARD_BG)
            row.pack(fill="x", pady=2, anchor="w")
            tk.Label(row, text="▸", bg=CARD_BG, fg=ACCENT,
                     font=(FONT_UI, 10, "bold")).pack(side="left",
                                                      padx=(0, 6))
            tk.Label(row, text=t, bg=CARD_BG, fg=TEXT_MID,
                     font=T_BODY, justify="left").pack(side="left",
                                                        anchor="w")

    # ──────────────────────────────────────────────────────────────────────── #
    #  Figures (Shapes)
    # ──────────────────────────────────────────────────────────────────────── #
    def area_circle(self):
        body = self.start_page("Area of a Circle")
        self.build_formula_ui(body, image_key="circle", options=[
            Solve("Area (from radius)",   ["Radius (r)"],
                  lambda r: math.pi * r ** 2),
            Solve("Area (from diameter)", ["Diameter (d)"],
                  lambda d: math.pi * (d / 2) ** 2),
            Solve("Radius (from area)",   ["Area (A)"],
                  lambda a: math.sqrt(a / math.pi)),
            Solve("Diameter (from area)", ["Area (A)"],
                  lambda a: 2 * math.sqrt(a / math.pi)),
        ])

    def circumference_page(self):
        body = self.start_page("Circumference of a Circle")
        self.build_formula_ui(body, image_key="ccircle", options=[
            Solve("Circumference (from radius)",   ["Radius (r)"],
                  lambda r: 2 * math.pi * r),
            Solve("Circumference (from diameter)", ["Diameter (d)"],
                  lambda d: math.pi * d),
            Solve("Radius (from circumference)",   ["Circumference (C)"],
                  lambda c: c / (2 * math.pi)),
            Solve("Diameter (from circumference)", ["Circumference (C)"],
                  lambda c: c / math.pi),
        ])

    def area_rectangle(self):
        body = self.start_page("Area of a Rectangle")
        self.build_formula_ui(body, image_key="rectangle", options=[
            Solve("Area", ["Length (L)", "Breadth (B)"], lambda l, b: l * b),
            Solve("Length (from area & breadth)", ["Area (A)", "Breadth (B)"],
                  lambda a, b: a / b),
            Solve("Breadth (from area & length)", ["Area (A)", "Length (L)"],
                  lambda a, l: a / l),
        ])

    def area_square(self):
        body = self.start_page("Area of a Square")
        self.build_formula_ui(body, image_key="square", options=[
            Solve("Area",            ["Side (s)"],  lambda s: s ** 2),
            Solve("Side (from area)", ["Area (A)"], lambda a: math.sqrt(a)),
        ])

    def area_triangle(self):
        body = self.start_page("Area of a Triangle")
        self.build_formula_ui(body, image_key="triangle", options=[
            Solve("Area", ["Base (b)", "Height (h)"], lambda b, h: 0.5 * b * h),
            Solve("Base (from area & height)", ["Area (A)", "Height (h)"],
                  lambda a, h: 2 * a / h),
            Solve("Height (from area & base)", ["Area (A)", "Base (b)"],
                  lambda a, b: 2 * a / b),
        ])

    def area_rhombus(self):
        body = self.start_page("Area of a Rhombus")
        self.build_formula_ui(body, image_key="rhombus",
                               intro="A rhombus's area is half the product of its two diagonals.",
                               options=[
            Solve("Area", ["Diagonal 1 (d₁)", "Diagonal 2 (d₂)"],
                  lambda d1, d2: 0.5 * d1 * d2),
            Solve("Diagonal 1 (from area & d₂)", ["Area (A)", "Diagonal 2 (d₂)"],
                  lambda a, d2: 2 * a / d2),
            Solve("Diagonal 2 (from area & d₁)", ["Area (A)", "Diagonal 1 (d₁)"],
                  lambda a, d1: 2 * a / d1),
        ])

    def area_kite(self):
        body = self.start_page("Area of a Kite")
        self.build_formula_ui(body, image_key="kite",
                               intro="A kite's area is half the product of its two diagonals.",
                               options=[
            Solve("Area", ["Diagonal 1 (d₁)", "Diagonal 2 (d₂)"],
                  lambda d1, d2: 0.5 * d1 * d2),
            Solve("Diagonal 1 (from area & d₂)", ["Area (A)", "Diagonal 2 (d₂)"],
                  lambda a, d2: 2 * a / d2),
            Solve("Diagonal 2 (from area & d₁)", ["Area (A)", "Diagonal 1 (d₁)"],
                  lambda a, d1: 2 * a / d1),
        ])

    def area_parallelogram(self):
        body = self.start_page("Area of a Parallelogram")
        self.build_formula_ui(body, image_key="parallelogram", options=[
            Solve("Area", ["Base (b)", "Height (h)"], lambda b, h: b * h),
            Solve("Base (from area & height)", ["Area (A)", "Height (h)"],
                  lambda a, h: a / h),
            Solve("Height (from area & base)", ["Area (A)", "Base (b)"],
                  lambda a, b: a / b),
        ])

    def area_trapezium(self):
        body = self.start_page("Area of a Trapezium")
        self.build_formula_ui(body, image_key="trapezium",
                               intro="a and b are the two parallel sides; h is the perpendicular height.",
                               options=[
            Solve("Area", ["Parallel side a", "Parallel side b", "Height (h)"],
                  lambda a, b, h: 0.5 * (a + b) * h),
            Solve("Height (from area & both sides)",
                  ["Area (A)", "Parallel side a", "Parallel side b"],
                  lambda A, a, b: 2 * A / (a + b)),
            Solve("Side a (from area, side b & height)",
                  ["Area (A)", "Parallel side b", "Height (h)"],
                  lambda A, b, h: 2 * A / h - b),
            Solve("Side b (from area, side a & height)",
                  ["Area (A)", "Parallel side a", "Height (h)"],
                  lambda A, a, h: 2 * A / h - a),
        ])

    # ── Perimeter ────────────────────────────────────────────────────────────
    def perimeter_rectangle(self):
        body = self.start_page("Perimeter of a Rectangle")
        self.build_formula_ui(body, image_key="rectangle",
                               formula_text="Perimeter = 2 × (L + B)", options=[
            Solve("Perimeter", ["Length (L)", "Breadth (B)"],
                  lambda l, b: 2 * (l + b)),
            Solve("Length (from perimeter & breadth)", ["Perimeter (P)", "Breadth (B)"],
                  lambda p, b: p / 2 - b),
            Solve("Breadth (from perimeter & length)", ["Perimeter (P)", "Length (L)"],
                  lambda p, l: p / 2 - l),
        ])

    def perimeter_square(self):
        body = self.start_page("Perimeter of a Square")
        self.build_formula_ui(body, image_key="square",
                               formula_text="Perimeter = 4 × side", options=[
            Solve("Perimeter",         ["Side (s)"],      lambda s: 4 * s),
            Solve("Side (from perimeter)", ["Perimeter (P)"], lambda p: p / 4),
        ])

    def perimeter_triangle(self):
        body = self.start_page("Perimeter of a Triangle")
        self.build_formula_ui(body, image_key="triangle",
                               formula_text="Perimeter = a + b + c", options=[
            Solve("Perimeter", ["Side a", "Side b", "Side c"],
                  lambda a, b, c: a + b + c),
            Solve("Side a (from perimeter, b & c)", ["Perimeter (P)", "Side b", "Side c"],
                  lambda p, b, c: p - b - c),
            Solve("Side b (from perimeter, a & c)", ["Perimeter (P)", "Side a", "Side c"],
                  lambda p, a, c: p - a - c),
            Solve("Side c (from perimeter, a & b)", ["Perimeter (P)", "Side a", "Side b"],
                  lambda p, a, b: p - a - b),
        ])

    # ── Surface area ─────────────────────────────────────────────────────────
    def surface_area_cuboid(self):
        body = self.start_page("Surface Area of a Cuboid")
        self.build_formula_ui(body, image_key="cuboid",
                               formula_text="SA = 2(LB + BH + HL)", options=[
            Solve("Surface area", ["Length (L)", "Breadth (B)", "Height (H)"],
                  lambda l, b, h: 2 * (l * b + b * h + h * l)),
        ])

    def surface_area_cylinder(self):
        body = self.start_page("Surface Area of a Cylinder")
        self.build_formula_ui(body, image_key="cylinder",
                               formula_text="SA = 2πr(r + h)", options=[
            Solve("Surface area", ["Radius (r)", "Height (h)"],
                  lambda r, h: 2 * math.pi * r * (r + h)),
            Solve("Height (from SA & radius)", ["Surface area (SA)", "Radius (r)"],
                  lambda sa, r: sa / (2 * math.pi * r) - r),
        ])

    def surface_area_cone(self):
        body = self.start_page("Surface Area of a Cone")
        self.build_formula_ui(body, image_key="cone",
                               formula_text="SA = πr(r + l)",
                               intro="l is the slant height (base edge to apex).",
                               options=[
            Solve("Surface area", ["Radius (r)", "Slant height (l)"],
                  lambda r, l: math.pi * r * (r + l)),
            Solve("Slant height (from SA & radius)", ["Surface area (SA)", "Radius (r)"],
                  lambda sa, r: sa / (math.pi * r) - r),
        ])

    def surface_area_pyramid(self):
        body = self.start_page("Surface Area of a Pyramid")
        self.build_formula_ui(body, image_key="pyramid",
                               formula_text="SA = Base area + ½ × perimeter × slant height",
                               intro="Use the area and perimeter of the base shape, and the slant height.",
                               options=[
            Solve("Surface area", ["Base area", "Base perimeter", "Slant height"],
                  lambda a, p, l: a + 0.5 * p * l),
        ])

    def surface_area_prism(self):
        body = self.start_page("Surface Area of a Prism")
        self.build_formula_ui(body, image_key="prism",
                               formula_text="SA = 2 × Base area + Base perimeter × height",
                               intro="Use the area and perimeter of the cross-section, and the length.",
                               options=[
            Solve("Surface area", ["Base area", "Base perimeter", "Length (height)"],
                  lambda a, p, h: 2 * a + p * h),
        ])

    def surface_area_sphere(self):
        body = self.start_page("Surface Area of a Sphere")
        self.build_formula_ui(body, image_key="sphere",
                               formula_text="SA = 4πr²", options=[
            Solve("Surface area", ["Radius (r)"],
                  lambda r: 4 * math.pi * r ** 2),
            Solve("Radius (from SA)", ["Surface area (SA)"],
                  lambda sa: math.sqrt(sa / (4 * math.pi))),
        ])

    # ── Volume ───────────────────────────────────────────────────────────────
    def volume_cuboid(self):
        body = self.start_page("Volume of a Cuboid")
        self.build_formula_ui(body, image_key="cuboid",
                               formula_text="V = L × B × H", options=[
            Solve("Volume", ["Length (L)", "Breadth (B)", "Height (H)"],
                  lambda l, b, h: l * b * h),
            Solve("Length (from V, B & H)", ["Volume (V)", "Breadth (B)", "Height (H)"],
                  lambda v, b, h: v / (b * h)),
            Solve("Breadth (from V, L & H)", ["Volume (V)", "Length (L)", "Height (H)"],
                  lambda v, l, h: v / (l * h)),
            Solve("Height (from V, L & B)", ["Volume (V)", "Length (L)", "Breadth (B)"],
                  lambda v, l, b: v / (l * b)),
        ])

    def volume_cylinder(self):
        body = self.start_page("Volume of a Cylinder")
        self.build_formula_ui(body, image_key="cylinder",
                               formula_text="V = πr²h", options=[
            Solve("Volume", ["Radius (r)", "Height (h)"],
                  lambda r, h: math.pi * r ** 2 * h),
            Solve("Height (from V & radius)", ["Volume (V)", "Radius (r)"],
                  lambda v, r: v / (math.pi * r ** 2)),
            Solve("Radius (from V & height)", ["Volume (V)", "Height (h)"],
                  lambda v, h: math.sqrt(v / (math.pi * h))),
        ])

    def volume_cone(self):
        body = self.start_page("Volume of a Cone")
        self.build_formula_ui(body, image_key="cone",
                               formula_text="V = ⅓πr²h", options=[
            Solve("Volume", ["Radius (r)", "Height (h)"],
                  lambda r, h: (1 / 3) * math.pi * r ** 2 * h),
            Solve("Height (from V & radius)", ["Volume (V)", "Radius (r)"],
                  lambda v, r: 3 * v / (math.pi * r ** 2)),
            Solve("Radius (from V & height)", ["Volume (V)", "Height (h)"],
                  lambda v, h: math.sqrt(3 * v / (math.pi * h))),
        ])

    def volume_pyramid(self):
        body = self.start_page("Volume of a Pyramid")
        self.build_formula_ui(body, image_key="pyramid",
                               formula_text="V = ⅓ × Base area × height", options=[
            Solve("Volume", ["Base area", "Height (h)"],
                  lambda a, h: (1 / 3) * a * h),
            Solve("Height (from V & base area)", ["Volume (V)", "Base area"],
                  lambda v, a: 3 * v / a),
            Solve("Base area (from V & height)", ["Volume (V)", "Height (h)"],
                  lambda v, h: 3 * v / h),
        ])

    def volume_prism(self):
        body = self.start_page("Volume of a Prism")
        self.build_formula_ui(body, image_key="prism",
                               formula_text="V = Base area × height", options=[
            Solve("Volume", ["Base area", "Length (height)"],
                  lambda a, h: a * h),
            Solve("Height (from V & base area)", ["Volume (V)", "Base area"],
                  lambda v, a: v / a),
            Solve("Base area (from V & height)", ["Volume (V)", "Length (height)"],
                  lambda v, h: v / h),
        ])

    def volume_sphere(self):
        body = self.start_page("Volume of a Sphere")
        self.build_formula_ui(body, image_key="sphere",
                               formula_text="V = ⁴⁄₃πr³", options=[
            Solve("Volume",          ["Radius (r)"],
                  lambda r: (4 / 3) * math.pi * r ** 3),
            Solve("Radius (from V)", ["Volume (V)"],
                  lambda v: (3 * v / (4 * math.pi)) ** (1 / 3)),
        ])

    # ── Pythagorean theorem & polygons ────────────────────────────────────────
    def pythagoras_page(self):
        body = self.start_page("Pythagorean Theorem")

        def leg_from(hyp, other):
            if hyp <= other:
                raise ValueError(
                    "The hypotenuse (c) must be longer than the other side.")
            return math.sqrt(hyp ** 2 - other ** 2)

        self.build_formula_ui(body, image_key="theorem", options=[
            Solve("Hypotenuse (c)",      ["Side a", "Side b"],
                  lambda a, b: math.sqrt(a ** 2 + b ** 2)),
            Solve("Side a (from b & c)", ["Side b", "Hypotenuse (c)"],
                  lambda b, c: leg_from(c, b)),
            Solve("Side b (from a & c)", ["Side a", "Hypotenuse (c)"],
                  lambda a, c: leg_from(c, a)),
        ])

    def polygons_page(self):
        body = self.start_page("Polygons")
        self.build_formula_ui(
            body,
            intro="Works for any polygon with n sides. The 'each angle' options assume a regular polygon.",
            options=[
                Solve("Sum of interior angles", ["Number of sides (n)"],
                      lambda n: (n - 2) * 180, unit="°"),
                Solve("Each interior angle (regular polygon)", ["Number of sides (n)"],
                      lambda n: (n - 2) * 180 / n, unit="°"),
                Solve("Each exterior angle (regular polygon)", ["Number of sides (n)"],
                      lambda n: 360 / n, unit="°"),
                Solve("Number of sides (from interior angle)", ["Interior angle"],
                      lambda a: 360 / (180 - a)),
                Solve("Number of sides (from exterior angle)", ["Exterior angle"],
                      lambda e: 360 / e),
            ])

    # ──────────────────────────────────────────────────────────────────────── #
    #  Percentages
    # ──────────────────────────────────────────────────────────────────────── #
    def simple_interest_page(self):
        body = self.start_page("Simple Interest")
        self.build_formula_ui(body,
                               formula_text="Interest = P × R × T ÷ 100",
                               intro="P = principal, R = rate per period (%), T = number of periods.",
                               options=[
            Solve("Simple Interest",
                  ["Principal (P)", "Rate (% per period)", "Time (periods)"],
                  lambda p, r, t: p * r * t / 100),
            Solve("Amount (Principal + Interest)",
                  ["Principal (P)", "Rate (% per period)", "Time (periods)"],
                  lambda p, r, t: p + p * r * t / 100),
            Solve("Principal (from interest, rate & time)",
                  ["Interest (I)", "Rate (% per period)", "Time (periods)"],
                  lambda i, r, t: i * 100 / (r * t)),
            Solve("Rate (from interest, principal & time)",
                  ["Interest (I)", "Principal (P)", "Time (periods)"],
                  lambda i, p, t: i * 100 / (p * t), unit="% per period"),
            Solve("Time (from interest, principal & rate)",
                  ["Interest (I)", "Principal (P)", "Rate (% per period)"],
                  lambda i, p, r: i * 100 / (p * r), unit="periods"),
        ])

    def discount_page(self):
        body = self.start_page("Discount")
        self.build_formula_ui(body,
                               formula_text="Discount = Marked price × rate ÷ 100",
                               options=[
            Solve("Discount amount", ["Marked price", "Discount rate (%)"],
                  lambda mp, r: mp * r / 100),
            Solve("Selling price",   ["Marked price", "Discount rate (%)"],
                  lambda mp, r: mp - mp * r / 100),
            Solve("Discount rate (from marked & selling price)",
                  ["Marked price", "Selling price"],
                  lambda mp, sp: (mp - sp) / mp * 100, unit="%"),
            Solve("Marked price (from selling price & rate)",
                  ["Selling price", "Discount rate (%)"],
                  lambda sp, r: sp / (1 - r / 100)),
        ])

    def commission_page(self):
        body = self.start_page("Commission")
        self.build_formula_ui(body,
                               formula_text="Commission = Sales × rate ÷ 100",
                               options=[
            Solve("Commission", ["Sales amount", "Commission rate (%)"],
                  lambda s, r: s * r / 100),
            Solve("Sales amount (from commission & rate)",
                  ["Commission", "Commission rate (%)"],
                  lambda c, r: c * 100 / r),
            Solve("Commission rate (from commission & sales)",
                  ["Commission", "Sales amount"],
                  lambda c, s: c / s * 100, unit="%"),
        ])

    def depreciation_page(self):
        body = self.start_page("Depreciation")
        self.build_formula_ui(body,
                               formula_text="Depreciation = Original value × rate × time ÷ 100",
                               intro="Straight-line depreciation: value lost is the same each year.",
                               options=[
            Solve("Depreciation",
                  ["Original value", "Rate (% per year)", "Time (years)"],
                  lambda p, r, t: p * r * t / 100),
            Solve("Book value (after depreciation)",
                  ["Original value", "Rate (% per year)", "Time (years)"],
                  lambda p, r, t: p - p * r * t / 100),
            Solve("Original value (from depreciation, rate & time)",
                  ["Depreciation", "Rate (% per year)", "Time (years)"],
                  lambda d, r, t: d * 100 / (r * t)),
        ])

    def vat_page(self):
        body = self.start_page("VAT")
        note = ("Enter the VAT rate that applies — tax rates change over time, "
                "so check the latest figure.")
        self.build_formula_ui(body,
                               formula_text="VAT = Price × VAT rate ÷ 100",
                               options=[
            Solve("VAT amount",
                  ["Price (before VAT)", "VAT rate (%)"],
                  lambda p, r: p * r / 100, note=note),
            Solve("Total price (including VAT)",
                  ["Price (before VAT)", "VAT rate (%)"],
                  lambda p, r: p + p * r / 100, note=note),
            Solve("Price before VAT (from total & rate)",
                  ["Total price", "VAT rate (%)"],
                  lambda t, r: t / (1 + r / 100), note=note),
        ])

    def nhil_page(self):
        body = self.start_page("NHIL")
        note = ("Enter the NHIL rate that applies — tax rates change over time, "
                "so check the latest figure.")
        self.build_formula_ui(body,
                               formula_text="NHIL = Price × NHIL rate ÷ 100",
                               options=[
            Solve("NHIL amount",
                  ["Price (before NHIL)", "NHIL rate (%)"],
                  lambda p, r: p * r / 100, note=note),
            Solve("Total price (including NHIL)",
                  ["Price (before NHIL)", "NHIL rate (%)"],
                  lambda p, r: p + p * r / 100, note=note),
            Solve("Price before NHIL (from total & rate)",
                  ["Total price", "NHIL rate (%)"],
                  lambda t, r: t / (1 + r / 100), note=note),
        ])

    def insurance_page(self):
        body = self.start_page("Insurance")
        self.build_formula_ui(body,
                               formula_text="Premium = Sum insured × rate ÷ 100",
                               options=[
            Solve("Premium", ["Sum insured", "Premium rate (%)"],
                  lambda s, r: s * r / 100),
            Solve("Sum insured (from premium & rate)",
                  ["Premium", "Premium rate (%)"],
                  lambda p, r: p * 100 / r),
            Solve("Premium rate (from premium & sum insured)",
                  ["Premium", "Sum insured"],
                  lambda p, s: p / s * 100, unit="%"),
        ])

    # ──────────────────────────────────────────────────────────────────────── #
    #  Ratio & Proportion
    # ──────────────────────────────────────────────────────────────────────── #
    def direct_proportion_page(self):
        body = self.start_page("Direct Proportion")
        self.build_formula_ui(body,
                               formula_text="x₁ ÷ y₁ = x₂ ÷ y₂",
                               intro="If x and y vary directly, their ratio stays constant. "
                                     "Enter any three known values to find the fourth.",
                               options=[
            Solve("x₂ (from x₁, y₁, y₂)", ["x₁", "y₁", "y₂"],
                  lambda x1, y1, y2: x1 * y2 / y1),
            Solve("y₂ (from x₁, y₁, x₂)", ["x₁", "y₁", "x₂"],
                  lambda x1, y1, x2: y1 * x2 / x1),
            Solve("x₁ (from y₁, x₂, y₂)", ["y₁", "x₂", "y₂"],
                  lambda y1, x2, y2: y1 * x2 / y2),
            Solve("y₁ (from x₁, x₂, y₂)", ["x₁", "x₂", "y₂"],
                  lambda x1, x2, y2: x1 * y2 / x2),
        ])

    def inverse_proportion_page(self):
        body = self.start_page("Inverse Proportion")
        self.build_formula_ui(body,
                               formula_text="x₁ × y₁ = x₂ × y₂",
                               intro="If x and y vary inversely, their product stays constant. "
                                     "Enter any three known values to find the fourth.",
                               options=[
            Solve("x₂ (from x₁, y₁, y₂)", ["x₁", "y₁", "y₂"],
                  lambda x1, y1, y2: x1 * y1 / y2),
            Solve("y₂ (from x₁, y₁, x₂)", ["x₁", "y₁", "x₂"],
                  lambda x1, y1, x2: x1 * y1 / x2),
            Solve("x₁ (from y₁, x₂, y₂)", ["y₁", "x₂", "y₂"],
                  lambda y1, x2, y2: x2 * y2 / y1),
            Solve("y₁ (from x₁, x₂, y₂)", ["x₁", "x₂", "y₂"],
                  lambda x1, x2, y2: x2 * y2 / x1),
        ])

    def _ratio_share_ui(self, body):
        tk.Label(body,
                 text="Enter a ratio like 2:3 or 2:3:5, and optionally a total amount to share.",
                 font=T_BODY, bg=CARD_BG, fg=TEXT_MID,
                 wraplength=760, justify="left").pack(anchor="w", pady=(0, 12))
        ratio_entry = self.add_labeled_entry(body, "Ratio (e.g. 2:3:5)", width=20)
        total_entry = self.add_labeled_entry(body, "Total amount (optional)", width=20)
        result_var  = self.add_result_label(body)

        def parse_ratio(text):
            parts_txt = [p.strip() for p in re.split(r"[:,]", text.strip())
                         if p.strip() != ""]
            if len(parts_txt) < 2:
                raise ValueError("Enter a ratio with at least two parts, like 2:3.")
            try:
                parts = [float(p) for p in parts_txt]
            except ValueError:
                raise ValueError("Ratio parts must be numbers, like 2:3:5.")
            if any(p <= 0 for p in parts):
                raise ValueError("Ratio parts must be positive numbers.")
            return parts

        def simplify(parts):
            if all(p == int(p) for p in parts):
                ints = [int(p) for p in parts]
                g = ints[0]
                for n in ints[1:]:
                    g = math.gcd(g, n)
                if g > 1:
                    return [n // g for n in ints]
                return ints
            smallest = min(parts)
            return [round(p / smallest, 4) for p in parts]

        def calc():
            parts = parse_ratio(ratio_entry.get())
            simplified = simplify(parts)
            lines = [f"Simplified ratio: {':'.join(str(s) for s in simplified)}"]
            total_txt = total_entry.get().strip()
            if total_txt:
                try:
                    total = float(total_txt)
                except ValueError:
                    raise ValueError('"Total amount" must be a number.')
                total_parts = sum(parts)
                for i, p in enumerate(parts, start=1):
                    share = total * p / total_parts
                    lines.append(f"Share {i} = {self.fmt_num(share)}")
            result_var.set("\n".join(lines))

        self.add_action_buttons(body, lambda: self.safe_run(calc, result_var))

    def ratio_page(self):
        body = self.start_page("Ratio")
        self._ratio_share_ui(body)

    def proportional_division_page(self):
        body = self.start_page("Proportional Division")
        self._ratio_share_ui(body)

    def financial_partnership_page(self):
        body = self.start_page("Financial Partnership")
        tk.Label(body,
                 text="Profit is shared between partners in proportion to capital × time. "
                      "Leave Partner C blank for two partners.",
                 font=T_BODY, bg=CARD_BG, fg=TEXT_MID,
                 wraplength=760, justify="left").pack(anchor="w", pady=(0, 12))
        cap_a  = self.add_labeled_entry(body, "Partner A — capital")
        time_a = self.add_labeled_entry(body, "Partner A — time invested (optional)")
        cap_b  = self.add_labeled_entry(body, "Partner B — capital")
        time_b = self.add_labeled_entry(body, "Partner B — time invested (optional)")
        cap_c  = self.add_labeled_entry(body, "Partner C — capital (optional)")
        time_c = self.add_labeled_entry(body, "Partner C — time invested (optional)")
        profit_entry = self.add_labeled_entry(body, "Total profit to share")
        result_var   = self.add_result_label(body)

        def calc():
            partners = []
            for label, cap_e, time_e in [("A", cap_a, time_a),
                                          ("B", cap_b, time_b),
                                          ("C", cap_c, time_c)]:
                cap_txt = cap_e.get().strip()
                if cap_txt == "":
                    continue
                cap = self.parse_float(cap_e, f"Partner {label} capital")
                time_txt = time_e.get().strip()
                time_val = self.parse_float(time_e,
                    f"Partner {label} time invested") if time_txt else 1.0
                partners.append((label, cap, time_val))
            if len(partners) < 2:
                raise ValueError("Enter capital for at least two partners.")
            profit  = self.parse_float(profit_entry, "Total profit")
            weights = [cap * t for _, cap, t in partners]
            total_w = sum(weights)
            lines   = []
            for (label, cap, t), w in zip(partners, weights):
                share = profit * w / total_w
                lines.append(f"Partner {label} share = {self.fmt_num(share)}")
            result_var.set("\n".join(lines))

        self.add_action_buttons(body, lambda: self.safe_run(calc, result_var))

    # ──────────────────────────────────────────────────────────────────────── #
    #  Rigid motion
    # ──────────────────────────────────────────────────────────────────────── #
    def translation_page(self):
        body = self.start_page("Translation")
        tk.Label(body,
                 text="Move a point (x, y) by vector (a, b): image = (x + a, y + b).",
                 font=T_BODY, bg=CARD_BG, fg=TEXT_MID,
                 wraplength=760, justify="left").pack(anchor="w", pady=(0, 12))
        x_e = self.add_labeled_entry(body, "x")
        y_e = self.add_labeled_entry(body, "y")
        a_e = self.add_labeled_entry(body, "Vector a (x-shift)")
        b_e = self.add_labeled_entry(body, "Vector b (y-shift)")
        result_var = self.add_result_label(body)

        def calc():
            x = self.parse_float(x_e, "x")
            y = self.parse_float(y_e, "y")
            a = self.parse_float(a_e, "Vector a")
            b = self.parse_float(b_e, "Vector b")
            result_var.set(
                f"Image point = ({self.fmt_num(x + a)}, {self.fmt_num(y + b)})")

        self.add_action_buttons(body, lambda: self.safe_run(calc, result_var))

    def reflection_page(self):
        body = self.start_page("Reflection")
        tk.Label(body, text="Reflect a point (x, y) in a line of symmetry.",
                 font=T_BODY, bg=CARD_BG, fg=TEXT_MID,
                 wraplength=760, justify="left").pack(anchor="w", pady=(0, 10))
        x_e = self.add_labeled_entry(body, "x")
        y_e = self.add_labeled_entry(body, "y")
        line_options = ["x-axis (y = 0)", "y-axis (x = 0)", "line y = x",
                         "line y = -x", "line x = k", "line y = k"]
        line_var, line_combo = self.add_dropdown(body, "Line of reflection",
                                                  line_options, width=22)
        k_holder = tk.Frame(body, bg=CARD_BG)
        k_holder.pack(fill="x")
        k_ref = {"entry": None}

        def refresh_k_field(event=None):
            for w in k_holder.winfo_children():
                w.destroy()
            if line_var.get() in ("line x = k", "line y = k"):
                k_ref["entry"] = self.add_labeled_entry(k_holder, "k", width=12)
            else:
                k_ref["entry"] = None

        line_combo.bind("<<ComboboxSelected>>", refresh_k_field)
        refresh_k_field()
        result_var = self.add_result_label(body)

        def calc():
            x = self.parse_float(x_e, "x")
            y = self.parse_float(y_e, "y")
            choice = line_var.get()
            if   choice == "x-axis (y = 0)": nx, ny = x, -y
            elif choice == "y-axis (x = 0)": nx, ny = -x, y
            elif choice == "line y = x":     nx, ny = y, x
            elif choice == "line y = -x":    nx, ny = -y, -x
            elif choice == "line x = k":
                k = self.parse_float(k_ref["entry"], "k")
                nx, ny = 2 * k - x, y
            else:
                k = self.parse_float(k_ref["entry"], "k")
                nx, ny = x, 2 * k - y
            result_var.set(
                f"Image point = ({self.fmt_num(nx)}, {self.fmt_num(ny)})")

        self.add_action_buttons(body, lambda: self.safe_run(calc, result_var))

    def rotation_page(self):
        body = self.start_page("Rotation")
        tk.Label(body,
                 text="Rotate a point (x, y) about a centre by a given angle. "
                      "Leave centre blank to rotate about the origin (0, 0).",
                 font=T_BODY, bg=CARD_BG, fg=TEXT_MID,
                 wraplength=760, justify="left").pack(anchor="w", pady=(0, 10))
        x_e  = self.add_labeled_entry(body, "x")
        y_e  = self.add_labeled_entry(body, "y")
        cx_e = self.add_labeled_entry(body, "Centre of rotation, x (default 0)")
        cy_e = self.add_labeled_entry(body, "Centre of rotation, y (default 0)")
        ang_var, _ = self.add_dropdown(body, "Angle of rotation",
                                        ["90° clockwise", "90° anti-clockwise",
                                         "180°", "Custom angle (degrees)"], width=28)
        custom_holder = tk.Frame(body, bg=CARD_BG)
        custom_holder.pack(fill="x")
        custom_ref = {"entry": None}

        def refresh_custom(event=None):
            for w in custom_holder.winfo_children():
                w.destroy()
            if ang_var.get() == "Custom angle (degrees)":
                custom_ref["entry"] = self.add_labeled_entry(
                    custom_holder, "Angle (degrees, + = anti-clockwise)", width=12)
            else:
                custom_ref["entry"] = None

        _ = self.add_dropdown.__self__ if hasattr(self.add_dropdown, '__self__') else None
        # wire the dropdown event after packing
        for child in body.winfo_children():
            if isinstance(child, tk.Frame):
                for w2 in child.winfo_children():
                    if isinstance(w2, ttk.Combobox) and w2.cget("values") and \
                       "90° clockwise" in str(w2.cget("values")):
                        w2.bind("<<ComboboxSelected>>", refresh_custom)
                        break

        result_var = self.add_result_label(body)

        def calc():
            x  = self.parse_float(x_e,  "x")
            y  = self.parse_float(y_e,  "y")
            cx_txt = cx_e.get().strip()
            cy_txt = cy_e.get().strip()
            cx = float(cx_txt) if cx_txt else 0.0
            cy = float(cy_txt) if cy_txt else 0.0
            choice = ang_var.get()
            dx, dy = x - cx, y - cy
            if   choice == "90° clockwise":       angle = -90
            elif choice == "90° anti-clockwise":  angle =  90
            elif choice == "180°":                angle = 180
            else:
                angle = self.parse_float(custom_ref["entry"], "Angle")
            rad = math.radians(angle)
            nx = cx + dx * math.cos(rad) - dy * math.sin(rad)
            ny = cy + dx * math.sin(rad) + dy * math.cos(rad)
            result_var.set(
                f"Image point = ({self.fmt_num(nx)}, {self.fmt_num(ny)})")

        self.add_action_buttons(body, lambda: self.safe_run(calc, result_var))

    def enlargement_page(self):
        body = self.start_page("Enlargement")
        tk.Label(body,
                 text="Scale a point (x, y) from a centre of enlargement by a scale factor k.",
                 font=T_BODY, bg=CARD_BG, fg=TEXT_MID,
                 wraplength=760, justify="left").pack(anchor="w", pady=(0, 10))
        x_e  = self.add_labeled_entry(body, "x")
        y_e  = self.add_labeled_entry(body, "y")
        ex_e = self.add_labeled_entry(body, "Centre of enlargement, x (default 0)")
        ey_e = self.add_labeled_entry(body, "Centre of enlargement, y (default 0)")
        k_e  = self.add_labeled_entry(body, "Scale factor (k)")
        result_var = self.add_result_label(body)

        def calc():
            x  = self.parse_float(x_e,  "x")
            y  = self.parse_float(y_e,  "y")
            ex_txt = ex_e.get().strip()
            ey_txt = ey_e.get().strip()
            ex = float(ex_txt) if ex_txt else 0.0
            ey = float(ey_txt) if ey_txt else 0.0
            k  = self.parse_float(k_e, "Scale factor")
            nx = ex + k * (x - ex)
            ny = ey + k * (y - ey)
            result_var.set(
                f"Image point = ({self.fmt_num(nx)}, {self.fmt_num(ny)})")

        self.add_action_buttons(body, lambda: self.safe_run(calc, result_var))

    # ──────────────────────────────────────────────────────────────────────── #
    #  Probability
    # ──────────────────────────────────────────────────────────────────────── #
    def probability_page(self):
        body = self.start_page("Probability")
        prob_note = "All probabilities must be between 0 and 1."
        self.build_formula_ui(body,
                               formula_text="0 ≤ P(event) ≤ 1",
                               options=[
            Solve("P(A) from frequency",
                  ["Frequency of A", "Total trials"],
                  lambda f, t: f / t, note=prob_note),
            Solve("P(not A)  —  complement",
                  ["P(A)"],
                  lambda a: 1 - a, note=prob_note),
            Solve("P(A or B)  —  mutually exclusive",
                  ["P(A)", "P(B)"],
                  lambda a, b: a + b, note=prob_note),
            Solve("P(A or B)  —  not mutually exclusive",
                  ["P(A)", "P(B)", "P(A and B)"],
                  lambda a, b, ab: a + b - ab, note=prob_note),
            Solve("P(A and B)  —  independent events",
                  ["P(A)", "P(B)"],
                  lambda a, b: a * b, note=prob_note),
        ])

    # ──────────────────────────────────────────────────────────────────────── #
    #  Conversions
    # ──────────────────────────────────────────────────────────────────────── #
    def conversions_page(self, category=None):
        units = {
            "Length": [
                ("millimetre (mm)", 0.001), ("centimetre (cm)", 0.01),
                ("metre (m)", 1.0), ("kilometre (km)", 1000.0),
                ("inch (in)", 0.0254), ("foot (ft)", 0.3048),
                ("yard (yd)", 0.9144), ("mile (mi)", 1609.344)],
            "Mass": [
                ("milligram (mg)", 1e-6), ("gram (g)", 0.001),
                ("kilogram (kg)", 1.0), ("tonne (t)", 1000.0),
                ("ounce (oz)", 0.0283495), ("pound (lb)", 0.45359237)],
            "Time": [
                ("second (s)", 1.0), ("minute (min)", 60.0),
                ("hour (hr)", 3600.0), ("day", 86400.0)],
            "Volume": [
                ("millilitre (ml)", 0.001), ("litre (l)", 1.0),
                ("cubic metre (m³)", 1000.0),
                ("US gallon (gal)", 3.78541), ("US pint (pt)", 0.473176)],
        }
        cat_names = list(units.keys())
        body = self.start_page("Conversions")
        tk.Label(body, text="Convert a value between units of the same kind.",
                 font=T_BODY, bg=CARD_BG, fg=TEXT_MID,
                 wraplength=760, justify="left").pack(anchor="w", pady=(0, 10))

        cat_var, cat_combo = self.add_dropdown(body, "Category", cat_names, width=18)
        if category in cat_names:
            cat_var.set(category)

        unit_row_holder = tk.Frame(body, bg=CARD_BG)
        unit_row_holder.pack(fill="x")
        value_entry = self.add_labeled_entry(body, "Value to convert")
        result_var  = self.add_result_label(body)
        refs        = {"from_var": None, "to_var": None}

        def build_unit_dropdowns(event=None):
            for w in unit_row_holder.winfo_children():
                w.destroy()
            names = [n for n, _ in units[cat_var.get()]]
            from_var, _ = self.add_dropdown(unit_row_holder, "From unit",
                                             names, width=20)
            to_var,   _ = self.add_dropdown(unit_row_holder, "To unit",
                                             names, width=20)
            if len(names) > 1:
                to_var.set(names[1])
            refs["from_var"] = from_var
            refs["to_var"]   = to_var

        cat_combo.bind("<<ComboboxSelected>>", build_unit_dropdowns)
        build_unit_dropdowns()

        def calc():
            value   = self.parse_float(value_entry, "Value to convert")
            factors = dict(units[cat_var.get()])
            from_u  = refs["from_var"].get()
            to_u    = refs["to_var"].get()
            base    = value * factors[from_u]
            conv    = base / factors[to_u]
            result_var.set(
                f"{self.fmt_num(value)} {from_u} = {self.fmt_num(conv)} {to_u}")

        self.add_action_buttons(body, lambda: self.safe_run(calc, result_var))

    # ──────────────────────────────────────────────────────────────────────── #
    #  Rates
    # ──────────────────────────────────────────────────────────────────────── #
    def speed_page(self):
        body = self.start_page("Speed")
        self.build_formula_ui(body, formula_text="Speed = Distance ÷ Time",
                               options=[
            Solve("Speed",                    ["Distance", "Time"],
                  lambda d, t: d / t),
            Solve("Distance (from speed & time)", ["Speed", "Time"],
                  lambda s, t: s * t),
            Solve("Time (from distance & speed)",  ["Distance", "Speed"],
                  lambda d, s: d / s),
        ])

    def density_page(self):
        body = self.start_page("Density")
        self.build_formula_ui(body, formula_text="Density = Mass ÷ Volume",
                               options=[
            Solve("Density",                  ["Mass", "Volume"],
                  lambda m, v: m / v),
            Solve("Mass (from density & volume)", ["Density", "Volume"],
                  lambda d, v: d * v),
            Solve("Volume (from mass & density)", ["Mass", "Density"],
                  lambda m, d: m / d),
        ])

    def general_rate_page(self):
        body = self.start_page("Rate")
        self.build_formula_ui(body, formula_text="Rate = Amount ÷ Time",
                               intro="Use for any 'per unit time' quantity — pay rate, "
                                     "flow rate, production rate, etc.",
                               options=[
            Solve("Rate",                     ["Amount", "Time"],
                  lambda a, t: a / t),
            Solve("Amount (from rate & time)", ["Rate", "Time"],
                  lambda r, t: r * t),
            Solve("Time (from amount & rate)", ["Amount", "Rate"],
                  lambda a, r: a / r),
        ])

    # ──────────────────────────────────────────────────────────────────────── #
    #  Bearings and vectors
    # ──────────────────────────────────────────────────────────────────────── #
    def bearing_page(self):
        body = self.start_page("Bearing Between Two Points")
        tk.Label(body,
                 text="Bearings are measured clockwise from North, 0° to 360°.",
                 font=T_BODY, bg=CARD_BG, fg=TEXT_MID,
                 wraplength=760, justify="left").pack(anchor="w", pady=(0, 12))
        x1_e = self.add_labeled_entry(body, "Point 1, x")
        y1_e = self.add_labeled_entry(body, "Point 1, y")
        x2_e = self.add_labeled_entry(body, "Point 2, x")
        y2_e = self.add_labeled_entry(body, "Point 2, y")
        result_var = self.add_result_label(body)

        def calc():
            x1 = self.parse_float(x1_e, "Point 1, x")
            y1 = self.parse_float(y1_e, "Point 1, y")
            x2 = self.parse_float(x2_e, "Point 2, x")
            y2 = self.parse_float(y2_e, "Point 2, y")
            dx, dy = x2 - x1, y2 - y1
            if dx == 0 and dy == 0:
                raise ValueError("The two points must be different.")
            bearing = (90 - math.degrees(math.atan2(dy, dx))) % 360
            back    = (bearing + 180) % 360
            result_var.set(
                f"Bearing of point 2 from point 1 = {self.fmt_num(bearing)}°\n"
                f"Back bearing (point 1 from point 2) = {self.fmt_num(back)}°")

        self.add_action_buttons(body, lambda: self.safe_run(calc, result_var))

    def vector_magnitude_page(self):
        body = self.start_page("Vector Magnitude & Direction")
        tk.Label(body,
                 text="Enter the x and y components of a vector to find its size and direction.",
                 font=T_BODY, bg=CARD_BG, fg=TEXT_MID,
                 wraplength=760, justify="left").pack(anchor="w", pady=(0, 12))
        x_e = self.add_labeled_entry(body, "x-component")
        y_e = self.add_labeled_entry(body, "y-component")
        result_var = self.add_result_label(body)

        def calc():
            x = self.parse_float(x_e, "x-component")
            y = self.parse_float(y_e, "y-component")
            mag = math.sqrt(x ** 2 + y ** 2)
            if x == 0 and y == 0:
                result_var.set("Magnitude = 0 (the zero vector has no direction)")
                return
            direction = (90 - math.degrees(math.atan2(y, x))) % 360
            result_var.set(f"Magnitude = {self.fmt_num(mag)}\n"
                            f"Direction (bearing) = {self.fmt_num(direction)}°")

        self.add_action_buttons(body, lambda: self.safe_run(calc, result_var))

    def vector_addition_page(self):
        body = self.start_page("Vector Addition")
        tk.Label(body,
                 text="Add two vectors to find the resultant, its magnitude, and direction.",
                 font=T_BODY, bg=CARD_BG, fg=TEXT_MID,
                 wraplength=760, justify="left").pack(anchor="w", pady=(0, 12))
        x1_e = self.add_labeled_entry(body, "Vector 1, x")
        y1_e = self.add_labeled_entry(body, "Vector 1, y")
        x2_e = self.add_labeled_entry(body, "Vector 2, x")
        y2_e = self.add_labeled_entry(body, "Vector 2, y")
        result_var = self.add_result_label(body)

        def calc():
            x1 = self.parse_float(x1_e, "Vector 1, x")
            y1 = self.parse_float(y1_e, "Vector 1, y")
            x2 = self.parse_float(x2_e, "Vector 2, x")
            y2 = self.parse_float(y2_e, "Vector 2, y")
            rx, ry = x1 + x2, y1 + y2
            mag = math.sqrt(rx ** 2 + ry ** 2)
            lines = [f"Resultant vector = ({self.fmt_num(rx)}, {self.fmt_num(ry)})",
                     f"Magnitude = {self.fmt_num(mag)}"]
            if not (rx == 0 and ry == 0):
                direction = (90 - math.degrees(math.atan2(ry, rx))) % 360
                lines.append(f"Direction (bearing) = {self.fmt_num(direction)}°")
            result_var.set("\n".join(lines))

        self.add_action_buttons(body, lambda: self.safe_run(calc, result_var))

    # ──────────────────────────────────────────────────────────────────────── #
    #  Tools: Calculator & Square root
    # ──────────────────────────────────────────────────────────────────────── #
    def open_calculator(self):
        if self._calc_window is not None and self._calc_window.winfo_exists():
            self._calc_window.lift()
            self._calc_window.focus_set()
            return

        win = tk.Toplevel(self.root)
        self._calc_window = win
        win.title("Calculator")
        win.resizable(False, False)
        win.configure(bg=BG_DEEP)
        win.protocol("WM_DELETE_WINDOW", lambda: self._close_calc(win))

        # Display
        display_var = tk.StringVar(value="0")
        display = tk.Entry(win, textvariable=display_var,
                           font=("Helvetica", 20), justify="right",
                           bd=0, relief="flat", bg="#0f1629",
                           fg=TEXT_WHITE, insertbackground=TEXT_WHITE)
        display.grid(row=0, column=0, columnspan=4,
                     sticky="ew", padx=10, pady=12, ipady=12)

        state = {"expr": ""}
        allowed_chars = set("0123456789.+-*/() ")

        def update_display():
            display_var.set(state["expr"] if state["expr"] else "0")

        def press(token):
            state["expr"] += token
            update_display()

        def clear():
            state["expr"] = ""
            update_display()

        def backspace():
            state["expr"] = state["expr"][:-1]
            update_display()

        def equals():
            expr = state["expr"].strip()
            if not expr:
                return
            if not set(expr) <= allowed_chars:
                messagebox.showerror("Calculator",
                                      "Only numbers and + - * / ( ) allowed.")
                return
            try:
                result = eval(expr, {"__builtins__": {}}, {})
            except ZeroDivisionError:
                messagebox.showerror("Calculator", "Can't divide by zero.")
                return
            except Exception:
                messagebox.showerror("Calculator",
                                      "That expression isn't valid.")
                return
            state["expr"] = (self.fmt_num(result)
                              if isinstance(result, (int, float))
                              else str(result))
            update_display()

        buttons = [
            ("C",  clear),     ("⌫", backspace),
            ("(",  lambda: press("(")), (")", lambda: press(")")),
            ("7",  lambda: press("7")), ("8", lambda: press("8")),
            ("9",  lambda: press("9")), ("÷", lambda: press("/")),
            ("4",  lambda: press("4")), ("5", lambda: press("5")),
            ("6",  lambda: press("6")), ("×", lambda: press("*")),
            ("1",  lambda: press("1")), ("2", lambda: press("2")),
            ("3",  lambda: press("3")), ("−", lambda: press("-")),
            ("0",  lambda: press("0")), (".", lambda: press(".")),
            ("=",  equals),            ("+", lambda: press("+")),
        ]
        r, c = 1, 0
        for lbl, cmd in buttons:
            if lbl == "=":
                bg, fg, abg = ACCENT, TEXT_WHITE, ACCENT_DARK
            elif lbl in ("C", "⌫"):
                bg, fg, abg = "#2a3555", TEXT_WHITE, "#3a4570"
            else:
                bg, fg, abg = "#1a2340", TEXT_WHITE, "#263050"

            tk.Button(win, text=lbl, command=cmd,
                      font=("Helvetica", 14), bg=bg, fg=fg,
                      activebackground=abg, activeforeground=TEXT_WHITE,
                      relief="flat", width=4, height=2,
                      cursor="hand2", bd=0).grid(row=r, column=c,
                                                  padx=4, pady=4)
            c += 1
            if c > 3:
                c = 0
                r += 1

        win.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def _close_calc(self, win):
        self._calc_window = None
        win.destroy()

    def open_square_root(self):
        if self._sqrt_window is not None and self._sqrt_window.winfo_exists():
            self._sqrt_window.lift()
            self._sqrt_window.focus_set()
            return

        win = tk.Toplevel(self.root)
        self._sqrt_window = win
        win.title("Square Root")
        win.resizable(False, False)
        win.configure(bg=CARD_BG)
        win.protocol("WM_DELETE_WINDOW", lambda: self._close_sqrt(win))

        tk.Label(win, text="Square Root", font=T_TITLE,
                 bg=CARD_BG, fg=TEXT_DARK).pack(padx=24, pady=(18, 6))

        row = tk.Frame(win, bg=CARD_BG)
        row.pack(padx=24, pady=4)
        tk.Label(row, text="Number:", font=T_BODY, bg=CARD_BG,
                 fg=TEXT_MID).pack(side="left", padx=(0, 10))
        entry = tk.Entry(row, font=T_BODY, width=18,
                         relief="solid", bd=1,
                         highlightthickness=1,
                         highlightbackground=CARD_BORDER,
                         highlightcolor=ACCENT,
                         fg=TEXT_DARK)
        entry.pack(side="left")
        entry.focus_set()

        result_var = tk.StringVar()
        result_frame = tk.Frame(win, bg=ACCENT_LIGHT,
                                 highlightthickness=1,
                                 highlightbackground=ACCENT)
        result_frame.pack(padx=24, pady=(12, 0), fill="x")
        tk.Label(result_frame, textvariable=result_var, font=T_RESULT,
                 bg=ACCENT_LIGHT, fg=ACCENT_DARK,
                 padx=12, pady=8).pack(anchor="w")

        def calc():
            value = self.parse_float(entry, "Number")
            if value < 0:
                raise ValueError(
                    "Can't take the square root of a negative number.")
            result_var.set(
                f"√{self.fmt_num(value)} = {self.fmt_num(math.sqrt(value))}")

        btn_row = tk.Frame(win, bg=CARD_BG)
        btn_row.pack(pady=(12, 18))
        tk.Button(btn_row, text="Calculate",
                  command=lambda: self.safe_run(calc, result_var),
                  bg=ACCENT, fg=TEXT_WHITE,
                  activebackground=ACCENT_DARK,
                  activeforeground=TEXT_WHITE,
                  relief="flat", padx=18, pady=7,
                  cursor="hand2", font=(FONT_UI, 10, "bold"), bd=0
                  ).pack(side="left", padx=(0, 8))
        tk.Button(btn_row, text="Clear",
                  command=lambda: (entry.delete(0, tk.END),
                                   result_var.set("")),
                  bg="#f1f5f9", fg=TEXT_MID,
                  activebackground=CARD_BORDER,
                  relief="flat", padx=14, pady=7,
                  cursor="hand2", font=(FONT_UI, 10), bd=0
                  ).pack(side="left")
        entry.bind("<Return>", lambda e: self.safe_run(calc, result_var))

    def _close_sqrt(self, win):
        self._sqrt_window = None
        win.destroy()

    # ──────────────────────────────────────────────────────────────────────── #
    #  Menu bar
    # ──────────────────────────────────────────────────────────────────────── #
    def _build_menu(self):
        menubar = tk.Menu(self.root, bg=BG_MID, fg=TEXT_WHITE,
                           activebackground=ACCENT,
                           activeforeground=TEXT_WHITE)
        self.root.config(menu=menubar)

        def menu(parent, label):
            m = tk.Menu(parent, tearoff=0, bg=CARD_BG, fg=TEXT_DARK,
                         activebackground=ACCENT_LIGHT,
                         activeforeground=ACCENT_DARK)
            parent.add_cascade(label=label, menu=m)
            return m

        def sub(parent, label):
            m = tk.Menu(parent, tearoff=0, bg=CARD_BG, fg=TEXT_DARK,
                         activebackground=ACCENT_LIGHT,
                         activeforeground=ACCENT_DARK)
            parent.add_cascade(label=label, menu=m)
            return m

        # ── Figures (Shapes) ────────────────────────────────────────────────
        shapes = menu(menubar, "Figures (Shapes)")

        area = sub(shapes, "Area")
        for lbl, cmd in [
            ("Circle",        self.area_circle),
            ("Rectangle",     self.area_rectangle),
            ("Square",        self.area_square),
            ("Triangle",      self.area_triangle),
            ("Rhombus",       self.area_rhombus),
            ("Parallelogram", self.area_parallelogram),
            ("Kite",          self.area_kite),
            ("Trapezium",     self.area_trapezium),
        ]:
            area.add_command(label=lbl, command=cmd)

        perim = sub(shapes, "Perimeter")
        for lbl, cmd in [
            ("Rectangle", self.perimeter_rectangle),
            ("Square",    self.perimeter_square),
            ("Triangle",  self.perimeter_triangle),
        ]:
            perim.add_command(label=lbl, command=cmd)

        surf = sub(shapes, "Surface Area")
        for lbl, cmd in [
            ("Prism",    self.surface_area_prism),
            ("Cone",     self.surface_area_cone),
            ("Cylinder", self.surface_area_cylinder),
            ("Pyramid",  self.surface_area_pyramid),
            ("Cuboid",   self.surface_area_cuboid),
            ("Sphere",   self.surface_area_sphere),
        ]:
            surf.add_command(label=lbl, command=cmd)

        vol = sub(shapes, "Volume")
        for lbl, cmd in [
            ("Prism",    self.volume_prism),
            ("Cone",     self.volume_cone),
            ("Cylinder", self.volume_cylinder),
            ("Pyramid",  self.volume_pyramid),
            ("Cuboid",   self.volume_cuboid),
            ("Sphere",   self.volume_sphere),
        ]:
            vol.add_command(label=lbl, command=cmd)

        shapes.add_separator()
        shapes.add_command(label="Pythagorean Theorem",
                            command=self.pythagoras_page)
        shapes.add_command(label="Circumference of a Circle",
                            command=self.circumference_page)
        shapes.add_command(label="Polygons", command=self.polygons_page)

        # ── Percentages ─────────────────────────────────────────────────────
        pct = menu(menubar, "Percentages")
        for lbl, cmd in [
            ("Simple Interest", self.simple_interest_page),
            ("Discount",        self.discount_page),
            ("Commission",      self.commission_page),
            ("Depreciation",    self.depreciation_page),
            ("VAT",             self.vat_page),
            ("NHIL",            self.nhil_page),
            ("Insurance",       self.insurance_page),
        ]:
            pct.add_command(label=lbl, command=cmd)

        # ── Ratio & Proportion ───────────────────────────────────────────────
        ratio = menu(menubar, "Ratio & Proportion")
        prop = sub(ratio, "Proportion")
        prop.add_command(label="Direct",  command=self.direct_proportion_page)
        prop.add_command(label="Inverse", command=self.inverse_proportion_page)
        ratio.add_separator()
        ratio.add_command(label="Ratio",                command=self.ratio_page)
        ratio.add_command(label="Proportional Division",
                           command=self.proportional_division_page)
        ratio.add_command(label="Financial Partnership",
                           command=self.financial_partnership_page)

        # ── Rigid motion ─────────────────────────────────────────────────────
        rigid = menu(menubar, "Rigid Motion")
        for lbl, cmd in [
            ("Translation", self.translation_page),
            ("Reflection",  self.reflection_page),
            ("Rotation",    self.rotation_page),
            ("Enlargement", self.enlargement_page),
        ]:
            rigid.add_command(label=lbl, command=cmd)

        # ── Probability ──────────────────────────────────────────────────────
        prob = menu(menubar, "Probability")
        prob.add_command(label="Probability Rules",
                          command=self.probability_page)

        # ── Conversions ──────────────────────────────────────────────────────
        conv = menu(menubar, "Conversions")
        for lbl in ("Length", "Mass", "Time", "Volume"):
            conv.add_command(label=lbl,
                              command=lambda c=lbl: self.conversions_page(c))

        # ── Rates ────────────────────────────────────────────────────────────
        rates = menu(menubar, "Rates")
        rates.add_command(label="Speed",        command=self.speed_page)
        rates.add_command(label="Density",      command=self.density_page)
        rates.add_command(label="Rate (general)", command=self.general_rate_page)

        # ── Bearings and vectors ─────────────────────────────────────────────
        bear = menu(menubar, "Bearings & Vectors")
        bear.add_command(label="Bearing between two points",
                          command=self.bearing_page)
        bear.add_command(label="Vector magnitude & direction",
                          command=self.vector_magnitude_page)
        bear.add_command(label="Vector addition",
                          command=self.vector_addition_page)

        # ── Tools ────────────────────────────────────────────────────────────
        tools = menu(menubar, "Tools")
        tools.add_command(label="Calculator",  command=self.open_calculator)
        tools.add_command(label="Square Root", command=self.open_square_root)


# ──────────────────────────────────────────────────────────────────────────── #
if __name__ == "__main__":
    BillSikesApp().run()