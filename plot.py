import numpy as np
import customtkinter as ctk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from functions import *


class PlotFrame(ctk.CTkFrame):
	def __init__(self, master, input_frame):
		super().__init__(master)

		self.input_frame = input_frame

		self.grid_rowconfigure((0), weight=0)
		self.grid_rowconfigure((1), weight=1)
		self.grid_columnconfigure((0), weight=1)

		master_color_dark = self.cget('fg_color')[1]
		master_color_dark_name = master_color_dark.rstrip('0123456789')
		master_color_dark_percent = int(master_color_dark[len(master_color_dark_name):])
		master_color_dark_value = round((master_color_dark_percent / 100) * 255)
		master_color_dark_value_hex = hex(master_color_dark_value)[2:]
		master_color_dark_hex = f'#{master_color_dark_value_hex}{master_color_dark_value_hex}{master_color_dark_value_hex}'

		self.fig, self.ax = plt.subplots(facecolor=master_color_dark_hex, dpi=100)
		self.ax.set_facecolor(master_color_dark_hex)

		self.ax.axhline(linewidth=2, color='white')
		self.ax.axvline(linewidth=2, color='white')
		self.ax.set_xlabel('Time', color='white', fontsize=14)
		self.ax.set_ylabel('Position', color='white', fontsize=14)
		self.ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='#444444', grid_alpha=0.5)

		self.x_functions = {
			'Default': default_x_function,
			'Spiky': spiky_x_function,
			'Jitter': jitter_x_function
		}
		self.last_plots = None

		self.plot_selection = ctk.CTkComboBox(master=self, values=list(self.x_functions.keys()), state='readonly', font=('Cascadia Code', 16), command=self._combobox_callback)
		self.plot_selection.grid(row=0, column=0, padx=40, pady=(20, 0), sticky='nw')
		self.plot_selection.set('Default')

		self.canvas = FigureCanvasTkAgg(self.fig, master=self)
		self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=(0, 10), sticky='nsew')

		self._combobox_callback('Default')


	def set_x_function(self, x_function):
		self.x_function = x_function


	def update_plot(self):
		if not self.last_plots is None:
			for plot in self.last_plots: plot.remove()

		f = self.input_frame.f_var.get_value()
		z = self.input_frame.z_var.get_value()
		r = self.input_frame.r_var.get_value()
		ts = self.input_frame.ts_var.get_value()

		dt = 0.01
		T = np.arange(0.0, ts, dt)
		X_vec = np.vectorize(self.x_function)
		X = X_vec(T)

		k1 = z / (np.pi * f)
		k2 = 1.0 / ((2.0 * np.pi * f) * (2.0 * np.pi * f))
		k3 = (r * z) / (2.0 * np.pi * f)

		Y = np.zeros(shape=T.shape)
		Y[0] = X[0]
		yd = 0
		for i in range(1, Y.size):
			xd = (X[i] - X[i - 1]) / dt
			stable_k2 = max(k2, 0.5*dt*dt + 0.5*dt*k1, dt*k1)
			Y[i] = Y[i - 1] + dt * yd
			yd = yd + dt * (X[i] + k3*xd - Y[i] - k1*yd) / stable_k2

		plt.xlim(0.0, ts)
		plt.ylim(0, 1.5)
		plt.grid(visible=True, which='both')
		self.last_plots = self.ax.plot(T, X, color='#8EB173', linewidth=2.5)
		self.last_plots = self.last_plots + self.ax.plot(T, Y, color='#1F6AA5', linewidth=2.5)
		self.canvas.draw()


	def _combobox_callback(self, choice):
		self.set_x_function(self.x_functions[choice])
		self.update_plot()
