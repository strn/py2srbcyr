# -*- coding: utf-8 -*-

from py2srbcyr import txt2lat, text_to_lat


class TestClass:

    def test_cyr_to_latin(self):
        assert txt2lat('Љубазни фењерџија чађавог лица хоће да ми покаже штос') == \
            'Ljubazni fenjerdžija čađavog lica hoće da mi pokaže štos'

    def test_multiline_cyr_to_latin(self):
        cyrt = """Први ред-
Други ред:
Трећи ред;"""
        latt = """Prvi red-
Drugi red:
Treći red;"""
        assert text_to_lat(cyrt) == latt
