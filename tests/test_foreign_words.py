# -*- coding: utf-8 -*-

import py2srbcyr


class TestClass:

    def setup_class(self):
        self.cir = py2srbcyr.SerbCyr()

    def test_words_w_foreign_chars_wont_be_transliterated(self):
        assert self.cir.text_to_cyrillic('Biografiju pošaljite kao Word dokument u docx formatu za Über Yahu.') == 'Биографију пошаљите као Word документ у docx формату за Über Yahu.'

    # Test it_wont_transliterate_to_cyrillic_some_of_the_most_common_foreign_words
    def test_it_wont_transliterate_to_cyrillic_some_of_the_most_common_foreign_words(self):
        assert self.cir.text_to_cyrillic('Moj DJ username Adobe Dacia po defaultu sve PDF dokumente šalje mailom Google developerima.') == 'Мој DJ username Adobe Dacia по defaultu све PDF документе шаље mailom Google developerima.'

    # Test it_wont_transliterate_to_cyrillic_words_with_foreign_character_combination
    def test_it_wont_transliterate_to_cyrillic_words_with_foreign_character_combination(self):
        assert self.cir.text_to_cyrillic('Naša pevačica, Jellena sa dva l, učestvovala u prethodnoj VII sezoni Big Brother muzzičkog festivalа na sajtu domen.com') == 'Наша певачица, Jellena са два л, учествовала у претходној VII сезони Биг Brother muzzičkog фестивала на сајту domen.com'

    def test_prslook_prekookeanski(self):
        assert self.cir.text_to_cyrillic('prslook prekookeanski') == 'prslook прекоокеански'

    def test_grenadirmarsh_naive_cd(self):
        assert self.cir.text_to_cyrillic('grenadýrmarš naïve cd') == 'grenadýrmarš naïve cd'
