import customtkinter as ctk

from plot import PlotFrame
from input import InputsFrame


class App(ctk.CTk):
	def __init__(self):
		super().__init__()
		def _on_click_callback(event):
			event.widget.focus_set()
		self.bind_all('<Button-1>', lambda event: _on_click_callback(event))

		def _on_key_press_callback(event):
			if (event.char == '\r'):
				self.focus_set()
		self.bind('<KeyPress>', lambda event: _on_key_press_callback(event))

		self.title('Second Order Dynamics Tool')
		self.geometry('1366x768')
		self.grid_rowconfigure((0, 2), weight=0)
		self.grid_rowconfigure((1), weight=1)
		self.grid_columnconfigure((0), weight=1)
		self.grid_columnconfigure((1), weight=20)

		self.title_bar = ctk.CTkLabel(master=self, text='Second Order\nDynamics', font=('Cascadia Code', 26))
		self.title_bar.grid(row=0, column=0, padx=10, pady=10)

		self.input_frame = InputsFrame(master=self)
		self.plot_frame = PlotFrame(master=self, input_frame=self.input_frame)
		self.input_frame.set_plot_callback(self.plot_frame.update_plot)
		self.exit_button = ctk.CTkButton(master=self, text='Exit', font=('Cascadia Code', 16), command=self._exit_callback)

		self.input_frame.grid(row=1, column=0, padx=10, pady=(10, 5), sticky='nsew')
		self.plot_frame.grid(row=0, rowspan=2, column=1, padx=(5, 10), pady=(10, 5), sticky='nsew')
		self.exit_button.grid(row=2, column=0, padx=10, pady=(5, 10), sticky='sew')

		self.wm_protocol('WM_DELETE_WINDOW', self._quit)

		self.input_frame.register_validators()
		self.plot_frame.update_plot()


	def _exit_callback(self):
		self._quit()


	def _quit(self):
		self.withdraw()
		self.quit()


if __name__ == '__main__':
	ctk.set_appearance_mode('dark')
	app = App()
	app.mainloop()
