# -*- coding: utf-8 -*-

from py2srbcyr import txt2cyr


class TestClass:

	def test_poluuzd(self):
		assert txt2cyr('poluuzdignut poluuzdignutoj poluuzdignutom poluuzdignutim') \
			== 'полууздигнут полууздигнутој полууздигнутом полууздигнутим'

	def test_shizofr(self):
		assert txt2cyr('shizofren shizofrenoj shizofrenom shizofrenim') == \
			'схизофрен схизофреној схизофреном схизофреним'
		
	def test_othram(self):
		assert txt2cyr('othrama') == 'отхрама'