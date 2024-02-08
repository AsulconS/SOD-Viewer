import numpy as np
import customtkinter as ctk

from re import match


class InputVarFrame(ctk.CTkFrame):
	def __init__(self, master, name, default_val=0.0, slider_range=(0, 1), assignment_char=' =', font_size=26):
		super().__init__(master)

		self.grid_rowconfigure((0), weight=1)
		self.grid_columnconfigure((0), weight=1)
		self.grid_columnconfigure((1), weight=1)
		self.grid_columnconfigure((2), weight=5)

		self.slider_from, self.slider_to = slider_range
		number_of_steps = (self.slider_to - self.slider_from) * 100
		self.label  = ctk.CTkLabel (master=self, text=f'{name}{assignment_char}', font=('Cascadia Code', font_size))
		self.entry  = ctk.CTkEntry (master=self, placeholder_text=f'{default_val}', font=('Cascadia Code', 16), justify='center', width=50)
		self.slider = ctk.CTkSlider(master=self, from_=self.slider_from, to=self.slider_to, number_of_steps=number_of_steps, command=self._slider_modify_callback)

		self.entry.insert(0, str(default_val))
		self.slider.set(np.clip(default_val, self.slider_from, self.slider_to))

		self.label.grid (row=0, column=0, padx=(20, 0), sticky='ew')
		self.entry.grid (row=0, column=1, sticky='ew')
		self.slider.grid(row=0, column=2, padx=(10, 20), sticky='ew')

		self.cached_entry_content = '0.0'
		self.entry.bind('<FocusIn>', lambda event: self._on_entry_focus_in_callback(event))
		self.entry.bind('<FocusOut>', lambda event: self._on_entry_focus_out_callback(event))


	def get_value(self):
		return self.slider.get()


	def set_plot_callback(self, plot_callback):
		self.plot_callback = plot_callback


	def register_validator(self):
		entry_assert_command = self.register(self._entry_modify_callback)
		self.entry.configure(validate='all', validatecommand=(entry_assert_command, '%d', '%V', '%P'))


	def _on_entry_focus_in_callback(self, event):
		self.cached_entry_content = self.entry.get()


	def _on_entry_focus_out_callback(self, event):
		entry_content = self.entry.get()
		if (entry_content == '' or entry_content == '.'):
			formatted_entry_val = float(self.cached_entry_content)
		else:
			formatted_entry_val = round(float(entry_content), 2)
		formatted_entry_val = np.clip(formatted_entry_val, self.slider_from, self.slider_to)
		formatted_entry = str(formatted_entry_val)
		self.entry.delete(0, len(entry_content))
		self.entry.insert(0, formatted_entry)


	def _entry_modify_callback(self, action, reason, pending_mod):
		if pending_mod == '' or pending_mod == '.':
			return True

		is_valid_match = match(r'^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$', pending_mod)
		if is_valid_match is None:
			return False

		parsed_value = float(pending_mod)
		parsed_value = np.clip(parsed_value, self.slider_from, self.slider_to)
		self.slider.set(parsed_value)
		self.plot_callback()
		return True


	def _slider_modify_callback(self, value):
		self.entry.delete(0, len(self.entry.get()))
		self.entry.insert(0, f'{round(value, 2)}')
		self.plot_callback()


class InputsFrame(ctk.CTkFrame):
	def __init__(self, master):
		super().__init__(master)

		self.grid_rowconfigure((0, 1, 2, 4, 5), weight=1)
		self.grid_rowconfigure((3), weight=5)
		self.grid_columnconfigure((0), weight=1)

		self.f_var  = InputVarFrame(master=self, name='f', default_val=1.0, slider_range=(0.01, 6.0))
		self.z_var  = InputVarFrame(master=self, name='ζ', default_val=0.5, slider_range=(0.0, 6.0))
		self.r_var  = InputVarFrame(master=self, name='r', default_val=2.0, slider_range=(-3.0, 3.0))
		self.ts_var = InputVarFrame(master=self, name='Time Span', default_val=6.0, slider_range=(0.01, 10.0), assignment_char=':', font_size=20)

		self.f_var.grid (row=0, column=0, padx=10, pady=(10,  5), sticky='nsew')
		self.z_var.grid (row=1, column=0, padx=10, pady=( 5,  5), sticky='nsew')
		self.r_var.grid (row=2, column=0, padx=10, pady=( 5,  5), sticky='nsew')
		self.ts_var.grid(row=5, column=0, padx=10, pady=( 5, 10), sticky='nsew')


	def set_plot_callback(self, plot_callback):
		self.f_var.set_plot_callback(plot_callback)
		self.z_var.set_plot_callback(plot_callback)
		self.r_var.set_plot_callback(plot_callback)
		self.ts_var.set_plot_callback(plot_callback)


	def register_validators(self):
		self.f_var.register_validator()
		self.z_var.register_validator()
		self.r_var.register_validator()
		self.ts_var.register_validator()
