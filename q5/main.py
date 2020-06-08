# all imports below
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import urllib.request as ur
import os
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

"""
Any extra lines of code (if required)
as helper for this function.
"""

class ScraperXRT:
	'''
	Description
	-----------
	A class to scrap XRT files from the telescope archive.
	'''

	def __init__(self, typeof_file, startime, endtime):
		'''
		Parameters
		----------
		typeof_file: A `string`
		startime: A `~datetime.datetime` instance
		endtime: A `~datetime.datetime` instance
		'''
		self.typeof_file = typeof_file
		self.startime = startime
		self.endtime = endtime
	
	def matches(self, url):
		urlList = url.split('_')
		if len(urlList)==4:
			_, typeof_file, date, curtime = urlList
			curtime = curtime.split('.')[0]
		elif len(urlList)==5:
			_, typeof, f, date, curtime = urlList
			typeof_file, curtime = typeof + '_' + f, curtime.split('.')[0]
		else:
			return False

		curDateTime = datetime.strptime(date+ " " + curtime, "%Y%m%d %H%M%S")
		
		return typeof_file == self.typeof_file and self.startime <= curDateTime and self.endtime >= curDateTime


	def query(self):
		'''
		Returns
		-------
		A `list` of strings of URLs.
		'''
		url = "http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/"
		page = requests.get(url).text
		soup = BeautifulSoup(page, 'html.parser')
		return [url + node.get('href') for node in soup.find_all('a') if self.matches(node.get('href'))]

	def get(self):
		'''
		Returns
		-------
		A `list` of strings for files.
		'''
		cwd = os.getcwd()
		fileAddresses = []
		
		opener = ur.URLopener()
		for file in self.query():
			filename = file.split('/')[-1]
			opener.retrieve(file, filename)
			fileAddresses.append(cwd + '/' + filename)
		return fileAddresses

	def view(self, filepath):
		'''
		Parameters
		----------
		filepath: A `string` representing absolute path of file in system.

		Returns
		-------
		An instance of `matplotlib.image.AxesImage`, returned using `plt.imshow(data)`.
		'''
		image_file = get_pkg_data_filename(filepath)
		image_data = fits.getdata(image_file, ext=0)
		plt.figure()
		return plt.imshow(image_data, cmap='gray')
