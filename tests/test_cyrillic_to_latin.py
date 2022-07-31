# -*- coding: utf-8 -*-

from py2srbcyr import SerbCyr


class TestClass:

    def setup_class(self):
        self.cir = SerbCyr()

    def test_cyr_to_latin(self):
        assert self.cir.text_to_latin('Љубазни фењерџија чађавог лица хоће да ми покаже штос') == \
            'Ljubazni fenjerdžija čađavog lica hoće da mi pokaže štos'

    def test_multiline_cyr_to_latin(self):
        cyrt = """Први ред-
Други ред:
Трећи ред;"""
        latt = """Prvi red-
Drugi red:
Treći red;"""
        assert self.cir.text_to_latin(cyrt) == latt
