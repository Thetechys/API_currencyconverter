import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import floor





root = tk.Tk()
root.title("Pyplot Plot in Tkinter")
root.geometry('800x800')




raw_date_data = {'2022-12-15': {'MYR': 3.246966}, '2022-12-16': {'MYR': 3.255457}, '2022-12-17': {'MYR': 3.255936}, '2022-12-18': {'MYR': 3.255667}, '2022-12-19': {'MYR': 3.262764}, '2022-12-20': {'MYR': 3.281108}, '2022-12-21': {'MYR': 3.284121}, '2022-12-22': {'MYR': 3.273136}, '2022-12-23': {'MYR': 3.274401}, '2022-12-24': {'MYR': 3.274401}, '2022-12-25': {'MYR': 3.276593}, '2022-12-26': {'MYR': 3.284676}, '2022-12-27': {'MYR': 3.280952}, '2022-12-28': {'MYR': 3.277539}, '2022-12-29': {'MYR': 3.291991}, '2022-12-30': {'MYR': 3.285862}, '2022-12-31': {'MYR': 3.285862}, '2023-01-01': {'MYR': 3.289836}, '2023-01-02': {'MYR': 3.283105}, '2023-01-03': {'MYR': 3.274861}, '2023-01-04': {'MYR': 3.284556}, '2023-01-05': {'MYR': 3.260857}, '2023-01-06': {'MYR': 3.29504}, '2023-01-07': {'MYR': 3.29504}, '2023-01-08': {'MYR': 3.301308}, '2023-01-09': {'MYR': 3.289563}, '2023-01-10': {'MYR': 3.282719}, '2023-01-11': {'MYR': 3.285286}, '2023-01-12': {'MYR': 3.295954}, '2023-01-13': {'MYR': 3.28685}, '2023-01-14': {'MYR': 3.287348}, '2023-01-15': {'MYR': 3.28482}, '2023-01-16': {'MYR': 3.269333}, '2023-01-17': {'MYR': 3.27635}, '2023-01-18': {'MYR': 3.267468}, '2023-01-19': {'MYR': 3.260558}, '2023-01-20': {'MYR': 3.247322}, '2023-01-21': {'MYR': 3.247322}, '2023-01-22': {'MYR': 3.244071}, '2023-01-23': {'MYR': 3.25003}, '2023-01-24': {'MYR': 3.246212}, '2023-01-25': {'MYR': 3.265799}, '2023-01-26': {'MYR': 3.237266}, '2023-01-27': {'MYR': 3.230836}, '2023-01-28': {'MYR': 3.231082}, '2023-01-29': {'MYR': 3.23437}, '2023-01-30': {'MYR': 3.227845}, '2023-01-31': {'MYR': 3.245682}, '2023-02-01': {'MYR': 3.26836}, '2023-02-02': {'MYR': 3.239768}, '2023-02-03': {'MYR': 3.217004}, '2023-02-04': {'MYR': 3.21749}, '2023-02-05': {'MYR': 3.213906}, '2023-02-06': {'MYR': 3.212294}, '2023-02-07': {'MYR': 3.250712}, '2023-02-08': {'MYR': 3.247213}, '2023-02-09': {'MYR': 3.255132}, '2023-02-10': {'MYR': 3.256043}, '2023-02-11': {'MYR': 3.256778}, '2023-02-12': {'MYR': 3.259247}, '2023-02-13': {'MYR': 3.284733}, '2023-02-14': {'MYR': 3.273156}, '2023-02-15': {'MYR': 3.289163}, '2023-02-16': {'MYR': 3.293695}, '2023-02-17': {'MYR': 3.314656}, '2023-02-18': {'MYR': 3.314818}, '2023-02-19': {'MYR': 3.314717}, '2023-02-20': {'MYR': 3.316973}, '2023-02-21': {'MYR': 3.307084}, '2023-02-22': {'MYR': 3.312597}, '2023-02-23': {'MYR': 3.302082}, '2023-02-24': {'MYR': 3.284654}, '2023-02-25': {'MYR': 3.285306}, '2023-02-26': {'MYR': 3.286235}, '2023-02-27': {'MYR': 3.326346}, '2023-02-28': {'MYR': 3.328032}, '2023-03-01': {'MYR': 3.409971}, '2023-03-02': {'MYR': 3.321546}, '2023-03-03': {'MYR': 3.327405}, '2023-03-04': {'MYR': 3.327405}, '2023-03-05': {'MYR': 3.326688}, '2023-03-06': {'MYR': 3.327363}, '2023-03-07': {'MYR': 3.306269}, '2023-03-08': {'MYR': 3.34328}, '2023-03-09': {'MYR': 3.340613}, '2023-03-10': {'MYR': 3.350749}, '2023-03-11': {'MYR': 3.350501}, '2023-03-12': {'MYR': 3.353953}, '2023-03-13': {'MYR': 3.337642}, '2023-03-14': {'MYR': 3.335696}, '2023-03-15': {'MYR': 3.318495}, '2023-03-16': {'MYR': 3.346116}, '2023-03-17': {'MYR': 3.343389}, '2023-03-18': {'MYR': 3.343638}, '2023-03-19': {'MYR': 3.345979}, '2023-03-20': {'MYR': 3.353517}, '2023-03-21': {'MYR': 3.345348}, '2023-03-22': {'MYR': 3.350394}, '2023-03-23': {'MYR': 3.326825}, '2023-03-24': {'MYR': 3.322099}, '2023-03-25': {'MYR': 3.322099}, '2023-03-26': {'MYR': 3.324066}, '2023-03-27': {'MYR': 3.321922}, '2023-03-28': {'MYR': 3.32073}, '2023-03-29': {'MYR': 3.324784}, '2023-03-30': {'MYR': 3.33032}, '2023-03-31': {'MYR': 3.315668}, '2023-04-01': {'MYR': 3.315668}, '2023-04-02': {'MYR': 3.308878}, '2023-04-03': {'MYR': 3.331453}, '2023-04-04': {'MYR': 3.324937}, '2023-04-05': {'MYR': 3.311151}, '2023-04-06': {'MYR': 3.306178}, '2023-04-07': {'MYR': 3.311293}, '2023-04-08': {'MYR': 3.311044}, '2023-04-09': {'MYR': 3.316192}, '2023-04-10': {'MYR': 3.310934}, '2023-04-11': {'MYR': 3.316099}, '2023-04-12': {'MYR': 3.324079}, '2023-04-13': {'MYR': 3.330383}, '2023-04-14': {'MYR': 3.314155}}
list_date_data = [i for i in raw_date_data]
np_date = np.array(list_date_data)
print(np_date)

rate_data = [3.246966, 3.255457, 3.255936, 3.255667, 3.262764, 3.281108, 3.284121, 3.273136, 3.274401, 3.274401, 3.276593, 3.284676, 3.280952, 3.277539, 3.291991, 3.285862, 3.285862, 3.289836, 3.283105, 3.274861, 3.284556, 3.260857, 3.29504, 3.29504, 3.301308, 3.289563, 3.282719, 3.285286, 3.295954, 3.28685, 3.287348, 3.28482, 3.269333, 3.27635, 3.267468, 3.260558, 3.247322, 3.247322, 3.244071, 3.25003, 3.246212, 3.265799, 3.237266, 3.230836, 3.231082, 3.23437, 3.227845, 3.245682, 3.26836, 3.239768, 3.217004, 3.21749, 3.213906, 3.212294, 3.250712, 3.247213, 3.255132, 3.256043, 3.256778, 3.259247, 3.284733, 3.273156, 3.289163, 3.293695, 3.314656, 3.314818, 3.314717, 3.316973, 3.307084, 3.312597, 3.302082, 3.284654, 3.285306, 3.286235, 3.326346, 3.328032, 3.409971, 3.321546, 3.327405, 3.327405, 3.326688, 3.327363, 3.306269, 3.34328, 3.340613, 3.350749, 3.350501, 3.353953, 3.337642, 3.335696, 3.318495, 3.346116, 3.343389, 3.343638, 3.345979, 3.353517, 3.345348, 3.350394, 3.326825, 3.322099, 3.322099, 3.324066, 3.321922, 3.32073, 3.324784, 3.33032, 3.315668, 3.315668, 3.308878, 3.331453, 3.324937, 3.311151, 3.306178, 3.311293, 3.311044, 3.316192, 3.310934, 3.316099, 3.324079, 3.330383, 3.314225]
np_rate = np.array(rate_data)





fig = plt.figure()

ax = fig.add_subplot(111)

ax.plot(np_date, np_rate)



the_canvas = FigureCanvasTkAgg(fig, master=root)
the_canvas.draw()
the_canvas.grid()