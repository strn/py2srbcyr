# -*- coding: utf-8 -*-

import py2srbcyr


class TestClass:

    def setup_class(self):
        self.cir = py2srbcyr.SerbCyr()

    def test_dj_exceptions(self):
        assert self.cir.text_to_cyrillic('nadjačati odjednom najdjelotvorniji predjelo') == \
            'над\u200cјачати од\u200cједном најд\u200cјелотворнији пред\u200cјело'
