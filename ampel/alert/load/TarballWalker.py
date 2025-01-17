#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File:                Ampel-alerts/ampel/alert/load/TarballWalker.py
# License:             BSD-3-Clause
# Author:              jvs
# Date:                14.02.2019
# Last Modified Date:  30.01.2020
# Last Modified By:    valery brinnel <firstname.lastname@gmail.com>

import tarfile

class TarballWalker:
	"""
	"""

	def __init__(self, tarpath, start=0, stop=None):
		"""
		"""
		self.tarpath = tarpath
		self.start = start
		self.stop = stop


	def get_files(self):

		tar_file = open(self.tarpath, 'rb')
		count = -1

		for fileobj in self._walk(tar_file):

			count += 1
			if count < self.start:
				continue
			if self.stop is not None and count > self.stop:
				break
			yield fileobj

		tar_file.close()


	def _walk(self, fileobj):
		"""
		"""
		archive = tarfile.open(fileobj=fileobj, mode='r:gz')
		for info in archive:
			if info.isfile():
				fo = archive.extractfile(info)
				if info.name.endswith('.avro'):
					yield fo
				elif info.name.endswith('.tar.gz'):
					yield from self._walk(fo)
