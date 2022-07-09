# -*- coding: utf-8 -*-

import py2srbcyr.py2srbcyr

class TestClass:

    def setup_class(self):
        self.cir = py2srbcyr.py2srbcyr.SerbCyr()

    def test_trim_excessive_characters(self):
        assert self.cir.trim_excessive_characters("  !?:;.*-—~`'„”“”‘’(){}[]<>«»a!?:;.*-—~`'„”“”‘’()/\\") == "a"

    def test_word_contains_measurement_unit(self):
        assert self.cir.word_contains_measurement_unit('32°C') == True

    def test_transliteration_index_of_word_starts_with(self):
        assert self.cir.transliteration_index_of_word_starts_with('dj-evi', self.cir.whole_foreign_words, '-') == 3
        assert self.cir.transliteration_index_of_word_starts_with('makeup-om', self.cir.whole_foreign_words, '-') == 7
