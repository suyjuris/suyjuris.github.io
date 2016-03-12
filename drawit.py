# coding: utf-8

import numpy as np
from scipy import interpolate, signal
import tkinter as tk
import cairo


# Coords:
# Wurzel
# 4 70
# 17 64
# 38 111
# 51 26
# 117 26
# 117 35
# Männchen
# 68 107
# 81 78
# 95 107

# 63 73
# 81 52
# 81 70
# 98 73
# 81 43

import sys
if len(sys.argv) <= 1:
    f1,f2,f3=60,0.025,30
else:
    f1,f2,f3=int(sys.argv[1]),float(sys.argv[2]),int(sys.argv[3])

def draw_stuff(**kw):
    ctx.set_line_width(0.04)
    
    if 1:
        kw.update({'xlim':(0,121), 'ylim':(8,129)})
        draw_line([4,17,38,51,117,117],[70,64,111,26,26,35], **kw)
    else:
        kw.update({'xlim':(8,129), 'ylim':(8,129)})
        draw_line([14,25,38,51,117,117],[64,64,111,26,26,35], **kw)
    
    ctx.set_line_width(0.03)
    draw_line([68,81,95],[107,78,107], **kw)
    draw_line([81,81],[78,58], **kw)
    draw_line([63,81,98],[73,58,73], **kw)
    draw_circle(81, 47, 9, **kw)
    
def draw_line(x, y, **kw):
    x, y = xkcd_line(x, y, **kw)
    ctx.move_to(x[0], y[0])
    for i,j in zip(x[1:],y[1:]):
        ctx.line_to(i, j)
    ctx.stroke()
    
def draw_circle(px, py, r, **kw):
    u = np.linspace(0,2*np.pi,16)
    draw_line(np.sin(u)*r+px, np.cos(u)*r+py, **kw)

def xkcd_line(x, y, xlim=None, ylim=None, mag=1.0, f1=30, f2=0.05, f3=15):
    x = np.asarray(x)
    y = np.asarray(y)
    
    # get limits for rescaling
    if xlim is None:
        xlim = (x.min(), x.max())
    if ylim is None:
        ylim = (y.min(), y.max())

    if xlim[1] == xlim[0]:
        xlim = ylim
        
    if ylim[1] == ylim[0]:
        ylim = xlim

    # scale the data
    x_scaled = (x - xlim[0]) * 1. / (xlim[1] - xlim[0])
    y_scaled = (y - ylim[0]) * 1. / (ylim[1] - ylim[0])

    # compute the total distance along the path
    dx = x_scaled[1:] - x_scaled[:-1]
    dy = y_scaled[1:] - y_scaled[:-1]
    dist_tot = np.sum(np.sqrt(dx * dx + dy * dy))

    # number of interpolated points is proportional to the distance
    Nu = int(200 * dist_tot)
    u = np.arange(-1, Nu + 1) * 1. / (Nu - 1)

    # interpolate curve at sampled points
    k = min(1, len(x) - 1)
    res = interpolate.splprep([x_scaled, y_scaled], s=0, k=k)
    x_int, y_int = interpolate.splev(u, res[0]) 

    # we'll perturb perpendicular to the drawn line
    dx = x_int[2:] - x_int[:-2]
    dy = y_int[2:] - y_int[:-2]
    dist = np.sqrt(dx * dx + dy * dy)

    # create a filtered perturbation
    coeffs = mag * np.random.normal(0, 0.01, len(x_int) - 2)
    b = signal.firwin(f1, f2 * dist_tot, window=('kaiser', f3))
    response = signal.lfilter(b, 1, coeffs)

    x_int[1:-1] += response * dy / dist
    y_int[1:-1] += response * dx / dist

    # un-scale data
    x_int = x_int[1:-1]
    y_int = y_int[1:-1]
    #x_int = x_int[1:-1] * (xlim[1] - xlim[0])*scale + xlim[0]
    #y_int = y_int[1:-1] * (ylim[1] - ylim[0])*scale + ylim[0]
    
    return x_int, y_int
    
def do_cairo():
    global ctx
    w, h = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(surface)
    ctx.scale(w, h)
    ctx.rectangle(0, 0, 1, 1)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    draw_stuff()
    surface.write_to_png("out.png")
    
    t = tk.Tk()
    t.bind('<Escape>', lambda x: t.destroy())
    i=tk.Image('photo', file='out.png')
    l=tk.Label(image=i)
    l.pack()
    t.wait_window()
    
def do_cairo2():
    global ctx
    w, h = 256, 256
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w*4, h*2)
    ctx = cairo.Context(surface)
    ctx.scale(w, h)
    ctx.rectangle(0, 0, 4, 2)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    
    f=1.5
    
    draw_stuff(f1=f1*f, f2=f2, f3=f3)
    ctx.translate(1,0)
    draw_stuff(f1=f1, f2=f2*f, f3=f3)
    ctx.translate(1,0)
    draw_stuff(f1=f1, f2=f2, f3=f3*f)
    ctx.translate(-2,1)
    draw_stuff(f1=f1/f, f2=f2, f3=f3)
    ctx.translate(1,0)
    draw_stuff(f1=f1, f2=f2/f, f3=f3)
    ctx.translate(1,0)
    draw_stuff(f1=f1, f2=f2, f3=f3/f)
    ctx.translate(1,-0.5)
    draw_stuff(f1=f1, f2=f2, f3=f3)
    
    surface.write_to_png("out.png")
    t = tk.Tk()
    t.bind('<Escape>', lambda x: t.destroy())
    i=tk.Image('photo', file='out.png')
    l=tk.Label(image=i)
    l.pack()
    t.wait_window()
    
#do_cairo()
do_cairo2()









