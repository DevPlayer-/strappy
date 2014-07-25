
import wx
import wx.lib.mixins.inspection
from framepanel import FramePanel


def log(*args, **kwargs):
	return print(*args, **kwargs)


#wx.ListBox(parent, id, pos, size, choices=[], style, validator=DefaultValidator, name=ListBoxNameStr
#wx.FlexGridSizer(int rows=1, int cols=0, int vgap=0, int hgap=0)


class MainFrame(wx.Frame):

	FramePanel = None

	def __init__(self, parent=None, id=wx.ID_ANY, title=wx.EmptyString, 
			pos=wx.DefaultPosition, size=wx.DefaultSize, 
			style=wx.DEFAULT_FRAME_STYLE, name="MainFrame"):

		wx.Frame.__init__(self, parent, id, title, pos, size, style, name)
		self.CreateFramePanel()
		self.CreateStatusBar()
		self.BindEvents()


	def CreateFramePanel(self):
		self.FramePanel = FramePanel(self)
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.FramePanel, 1, wx.EXPAND|wx.ALL, 0)
		self.SetSizer(sizer)

		
	def BindEvents(self):
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroyWindow)
		#self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)


	'''
	def OnLeftDown(self, event):
		log('MainFrame.OnLeftDown()')
		log('   ', self.FramePanel.GetPosition())
		log('   ', self.FramePanel.pageApps.GetPosition())
		log('   ', event.GetX(), ' ', event.GetY())
		event.Skip()
	'''

	def OnClose(self, event):
		log('MainFrame.OnClose()')
		event.Skip()


	def OnDestroyWindow(self, event):
		log('MainFrame.OnDestroyWindow()')
		event.Skip()


class MyWxApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
	data = {}
	MainFrame = None

	def OnPreInit(self):
		"""Load data access. Change this completely."""
		import data
		self.data = data.make_mock_data()

	def OnInit(self):
		self.InitInspection()  # for the InspectionMixin base class

		self.MainFrame = MainFrame(None, title="MainFrame")
		self.MainFrame.Show()
		return True


def main():
	app = MyWxApp()
	app.MainLoop()


if __name__ == "__main__":
	main()
