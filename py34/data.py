

"""
This will be changed to something like pymysql or sqlite3 or MySQL

"""

class Named(object):
	"""This Base Class offers a base attribute to many classes, 
	used for identification."""
	name = None
	def __init__(self, name):
		self.name = name


class Version(Named):
	"""Applications have versions. We use the "version" as a way to 
	represent in a single format all releases, patches, updates, 
	bug fixes, etc."""
	app = None
	available_mods = []


class Saves(Named):
	"""Contains only not app data but also meta"""
	app = None
	mods = []
	players = []
	avatars = []
	settings = []


class App(Named):
	"""An application; a collection of runnable programs, data and content."""
	bootstrap = None
	launcher = None
	download_server = (None, None, None, None, None) # host, port, user, passw, acct
	login_server = None
	wiki = None
	forums = None
	news = None
	website = None # website
	support_site = None # website
	support_email = None
	instance_server = None
	versions = None

	players = []
	avatars = []
	guilds = []
	versions = []
	mods = []


class Account(Named):
	"""A financial repository controlled by a real person or persons."""
	players = []
	handle = '' # the current selected alias
	history = []
	avatars = []
	players = []
	guilds = []
	saves = [] # single user home computer setups benefit from this


class Player(Named):
	"""A social identity spanning multiple apps, with mulitple avatars."""
	avatars = []
	handle = '' # the current selected alias
	image = None
	friends = []
	history = []


class Avatar(Named):
	"""Character used by a player or guild. In my company the Avatar
	can span multiple apps."""
	aliases = []
	handle = '' # the current selected alias
	image = None
	friends = []
	history = []
	stats = None


class Data(object):
	"""Use a db instead of this."""
	apps = {}
	accounts = {}
	players = {}
	avatars = {}


	# Relationships
	app_account = []
	account_app = []

	players_accounts = []
	accounts_playes = []

	guild_accounts = []
	accounts_guild = []

	app_saves = []
	saves_app = []

	players_saves = []
	saves_players = []

	avatars_accounts = []
	accounts_avatars = []

	avatars_players = []
	players_avatars = []

	avatars_app = []
	app_avatars = []


def make_mock_data():
	data = Data()
	data.apps['app1'] = App('app1')
	data.apps['app3'] = App('app3')
	data.apps['app3'].versions = ['v_00_00_00', 'v_00_00_01', 'v_00_00_02']

	data.accounts['acct0001'] = Account('acct0001')
	data.players['Superman'] = Player('Superman')
	data.avatars['ClarkKent'] = Avatar('ClarkKent')
	data.avatars['Kiel'] = Avatar('Kiel')

	data.accounts['acct0002'] = Account('acct0002')
	data.players['Spiderman'] = Player('Spiderman')
	data.avatars['PeterParker'] = Avatar('PeterParker')
	data.avatars['Spiderman'] = Avatar('Spiderman')

	return data


