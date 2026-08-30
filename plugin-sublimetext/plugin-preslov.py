import sublime
import sublime_plugin
import py2srbcyr


class PreslovTextCommand(sublime_plugin.TextCommand):

	def __init__(self, view):
		self.view = view
		self.selection = view.sel()
		self.cir = py2srbcyr.SerbCyr()


	def run(self, edit, direction):
		# Determine direction of transliteration
		if direction == "c2l":
			fn = getattr(self.cir, 'text_to_latin')
		else:
			fn = getattr(self.cir, 'text_to_cyrillic')

		for reg in self.selection:
			selectedText = self.view.substr(reg)
			self.view.replace(edit, reg, fn(selectedText))
