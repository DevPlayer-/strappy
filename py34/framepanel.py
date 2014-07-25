

# This file uses \t and not 4-space indents.

import wx       # Phoenix dev version as of 2014-July-24
import wx.html2 # not capable of loading groups.www.google.com
import random   # assists to identify highly repetitious log messages.

# wx.Notebook(parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name=NotebookNameStr)
# wx.Notebook.AddPage(page, text, select=False, imageId=wx.NO_IMAGE)
# wx.Panel(parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr)
# wx.Button(parent, id=wx.ID_ANY, label=wx.EmptyString, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, validator=wx.DefaultValidator, name=wx.ButtonNameStr)
# wx.WrapSizer(orient=wx.HORIZONTAL, flags=wx.WRAPSIZER_DEFAULT_FLAGS)
# wx.GridBagSizer(vgap=0, hgap=0)
# wx.GridBagSizer.Add(window, pos==(row,col), span=wx.DefaultSpan==(rows, cols), flag=0, border=0, userData=None)


def log(*args, **kwargs):
	"""Simple log for now."""
	return print(*args, **kwargs)


class FullPanel(wx.Panel):

	"""Just a simple place holder panel used during developement with some 
	identification text."""

	def __init__(self, parent, id=wx.ID_ANY, 
			pos=wx.DefaultPosition, size=wx.DefaultSize, 
			style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):

		wx.Panel.__init__(self, parent, id, pos, size, style, name)

		#self.SetBackgroundColour('white')

		st = wx.StaticText(self, label=self.GetName())
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(st, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTRE, 10)
		self.SetSizer(sizer)


class QuadTabNotebook(wx.Panel):

	"""wxPython/Phoenix at this time seems to not have "Tab" controls.
	With wxWidgets you create a tab control with CreateWindow() or 
	CreateWindowEx() and a class type of WC_TABCONTROL. The wx.Notebook
	class may well be a "tab" control. However I wanted to have tabs
	on top, bottom, left and right of clientarea. I made this panel with 
	buttons instead.

	Notes:
	http://msdn.microsoft.com/en-us/library/windows/desktop/hh298367(v=vs.85).aspx

	TODO:
		. Fix sizing.
		. Try wx.Wrapsizer instead of wx.BoxSizer.
		. FlexGridSizer and GridbagSizer didn't behave as I liked.
		. Adjust right side of frame to be on right side of right buttons.
	"""

	_pages = []
	_page = None
	_sizer = None
	_sizer_top = None
	_sizer_bottom = None
	_sizer_left = None
	_sizer_right = None
	_sizer_center = None


	def __init__(self, parent, id=wx.ID_ANY, 
			pos=wx.DefaultPosition, size=wx.DefaultSize, 
			style=wx.TAB_TRAVERSAL, name="QuadTabNotebook"):

		wx.Panel.__init__(self, parent, id, pos, size, style, name)

		#self._sizer_top = wx.WrapSizer(wx.HORIZONTAL)
		self._sizer_top = wx.BoxSizer(wx.HORIZONTAL)
		self._sizer_bottom = wx.BoxSizer(wx.HORIZONTAL)

		self._sizer_left = wx.BoxSizer(wx.VERTICAL)
		self._sizer_center = wx.BoxSizer(wx.HORIZONTAL)
		self._sizer_right = wx.BoxSizer(wx.VERTICAL)

		self._center_row = wx.BoxSizer(wx.HORIZONTAL)
		self._center_row.Add(self._sizer_left, 0, wx.EXPAND|wx.ALL, 0)
		self._center_row.Add(self._sizer_center, 1, wx.EXPAND|wx.ALL, 0)
		self._center_row.Add(self._sizer_right, 0, wx.EXPAND|wx.ALL, 0)

		self._grid_sizer = wx.GridBagSizer(vgap=0,hgap=0)
		self._grid_sizer.Add(self._sizer_top,    pos=(0,0), span=(0,0), flag=wx.EXPAND|wx.ALL, border=0, userData=None)
		self._grid_sizer.Add(self._center_row,   pos=(1,0), span=(0,0), flag=wx.EXPAND|wx.ALL, border=0, userData=None)
		self._grid_sizer.Add(self._sizer_bottom, pos=(2,0), span=(0,0), flag=wx.EXPAND|wx.ALL, border=0, userData=None)

		self._grid_sizer.AddGrowableRow(1)
		self._grid_sizer.AddGrowableCol(0)

		self._sizer = wx.BoxSizer(wx.VERTICAL)
		self._sizer.Add(self._grid_sizer, 1, wx.EXPAND|wx.ALL, 0)
		self.SetSizer(self._sizer)
		self.Layout()


	def AddTop(self, page, text, select=False, imageId=wx.NO_IMAGE):
		return self.AddPage(page=page, text=text, loc=wx.TOP, select=select, imageId=imageId)

	def AddBottom(self, page, text, select=False, imageId=wx.NO_IMAGE):
		return self.AddPage(page=page, text=text, loc=wx.BOTTOM, select=select, imageId=imageId)

	def AddLeft(self, page, text, select=False, imageId=wx.NO_IMAGE):
		return self.AddPage(page=page, text=text, loc=wx.LEFT, select=select, imageId=imageId)

	def AddRight(self, page, text, select=False, imageId=wx.NO_IMAGE):
		return self.AddPage(page=page, text=text, loc=wx.RIGHT, select=select, imageId=imageId)

	def AddPage(self, page, text, loc=wx.TOP, select=False, imageId=wx.NO_IMAGE):

		# create button associated with "page"
		button = wx.Button(self, label=text, name=page.GetName()+'_Button')
		button.SetBackgroundColour( page.GetBackgroundColour() )
		button.SetForegroundColour( page.GetForegroundColour() )

		if len(self._pages) == 0:
			page.Show()
		else:
			page.Hide()

		self._pages.append( (button, loc, page) )

		# add the page to the center gridbagsizer cell
		self._sizer_center.Add(page, 1, wx.EXPAND|wx.ALL, 0)

		# add the button to the sizer associated with the location.
		if loc == wx.TOP:
			self._sizer_top.Add(button, 0, wx.ALL, 0)
		elif loc == wx.BOTTOM:
			self._sizer_bottom.Add(button, 0, wx.ALL, 0)
		elif loc == wx.LEFT:
			self._sizer_left.Add(button, 0, wx.ALL, 0)
		elif loc == wx.RIGHT:
			self._sizer_right.Add(button, 0, wx.ALL, 0)
		else:
			self._sizer_top.Add(button, 0, wx.ALL, 0)

		self.Bind(wx.EVT_BUTTON, self._OnChangePage, button)

		return None # perhaps instead (button, loc, page)


	def _OnChangePage(self, event):

		"""Show the associated panel to button and hide the other panels."""

		event_button = event.GetEventObject()

		for page_button, loc, page in self._pages:
			if page_button == event_button:
				page.Show()
			else:
				page.Hide()
		self.Layout()
		
		# Change to a custom or different Event Type
		# so this event doesn't get passed up to parent
		event.Skip()


class FramePanel(QuadTabNotebook):

	def __init__(self, parent, id=wx.ID_ANY, 
			pos=wx.DefaultPosition, size=wx.DefaultSize, 
			style=wx.TAB_TRAVERSAL, name="FramePanel"):

		QuadTabNotebook.__init__(self, parent, id, pos, size, style, name)

		#top buttones
		self.pageApps = FullPanel(self, name='pageApps')
		self.pageApps.SetBackgroundColour('white')
		self.AddTop( self.pageApps, 'Apps')

		self.pageAccounts = FullPanel(self, name='pageAccounts')
		self.AddTop( self.pageAccounts, 'Accounts')

		self.pagePlayers = FullPanel(self, name='pagePlayers')
		self.AddTop( self.pagePlayers, 'Players')

		self.pageAvatars = FullPanel(self, name='pageAvatars')
		self.AddTop( self.pageAvatars, 'Avatars')

		self.pageSaves = FullPanel(self, name='pageSaves')
		self.AddTop( self.pageSaves, 'Saves')

		self.pageGuilds = FullPanel(self, name='pageGuilds')
		self.AddTop( self.pageGuilds, 'Guilds/Clans/Memberships')

		# activated by bottom buttons
		self.pageNews = wx.html2.WebView.New(self, name='pageNews')
		self.pageNews.LoadURL('http://www.google.com')
		self.AddBottom( self.pageNews, 'News')

		self.pageWiki = wx.html2.WebView.New(self, name='pageWiki')
		self.pageWiki.LoadURL('http://www.google.com')
		self.AddBottom( self.pageWiki, 'wiki')

		self.pageWeb = wx.html2.WebView.New(self, name='pageWeb')
		self.pageWeb.LoadURL('http://www.google.com')
		self.AddBottom( self.pageWeb, 'Web')

		self.pageForums = wx.html2.WebView.New(self, name='pageForums')
		self.pageForums.LoadURL('http://www.google.com')
		self.AddBottom( self.pageForums, 'Forums')

		self.pageSupport = wx.html2.WebView.New(self, name='pageSupport')
		self.pageSupport.LoadURL('http://www.google.com')
		self.AddBottom( self.pageSupport, 'Support')

		self.pageChat = FullPanel(self, name='pageChat')
		self.AddBottom( self.pageChat, 'Chat')


		# activated by left buttons
		self.pageGoogle = wx.html2.WebView.New(self, name='pageGoogle')
		self.pageGoogle.LoadURL('http://www.www.google.com')
		self.AddLeft( self.pageGoogle, 'Google')

		# doesn't work at all
		#self.pageGoogleGroups = wx.html2.WebView.New(self, name='pageGoogleGroups')
		#self.pageGoogleGroups.LoadURL('https://groups.www.google.com')
		#self.pageGoogleGroups.LoadURL('https://groups.www.google.com/forum/#!overview')
		#self.pageGoogleGroups.LoadURL('https://groups.www.google.com/forum/#!forum/wxpython-users')
		#self.AddLeft( self.pageGoogleGroups, 'GoogleGroups')

		self.pageTwitter = wx.html2.WebView.New(self, name='pageTwitter')
		self.pageTwitter.LoadURL('http://www.twitter.com')
		self.AddLeft( self.pageTwitter, 'Twitter')


		# activated by right buttons
		self.pageExplorer = FullPanel(self, name='pageExplorer')
		self.AddRight( self.pageExplorer, 'Explorer')

		self.pagePySlice = FullPanel(self, name='pagePySlice')
		self.AddRight( self.pagePySlice, 'PySlice')

		self.pagePyCrust = FullPanel(self, name='pagePyCrust')
		self.AddRight( self.pagePyCrust, 'PyCrust')

		# self.pagePyShell = wx.py.shell.Shell(self, introText=intro, name='pagePyShell')
		# old version of Shell() raises NameError Exception for 
		# xrange not defined when using CTRL+ENTER to "execute" 
		intro='Hello.'
		self.pagePyShell = wx.py.shell.Shell(self, introText=intro)
		self.AddRight( self.pagePyShell, 'PyShell')


