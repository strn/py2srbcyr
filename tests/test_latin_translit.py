# -*- coding: utf-8 -*-

from py2srbcyr import SerbCyr


class TestClass:

    def setup_class(self):
        self.cir = SerbCyr()

    def test_correct_transliteration_of_latin_digraphs(self):
        assert self.cir.text_to_cyrillic('Odjednom Tanjug reče da će nadživeti injekciju. Dodjavola, džangrizava njuška je bila u pravu.') == 'Од‌једном Тан‌југ рече да ће над‌живети ин‌јекцију. Дођавола, џангризава њушка је била у праву.'

    def test_proper_transliteration_case_of_latin_digraphs(self):
        assert self.cir.text_to_cyrillic('Ljubičasta LJOVISNA je ljankase') == 'Љубичаста ЉОВИСНА је љанкасе'
        assert self.cir.text_to_cyrillic('Njiše se njopajuće NJANJAVO') == 'Њише се њопајуће ЊАЊАВО'
        assert self.cir.text_to_cyrillic('Džangrizavi DŽUDISTA džemper odžakom Džodi daje.') == 'Џангризави ЏУДИСТА џемпер оџаком Џоди даје.'

    def test_proper_transliteration_of_latin_to_cyrillic(self):
        assert self.cir.text_to_cyrillic('brza vižljasta lija hoće da đipi preko lenjog flegmatičnog džukca.') == 'брза вижљаста лија хоће да ђипи преко лењог флегматичног џукца.'
        assert self.cir.text_to_cyrillic('LJUDI, JAZAVAC DŽEF TRČI PO ŠUMI GLOĐUĆI NEKO SUHO ŽBUNJE!') == 'ЉУДИ, ЈАЗАВАЦ ЏЕФ ТРЧИ ПО ШУМИ ГЛОЂУЋИ НЕКО СУХО ЖБУЊЕ!'
        assert self.cir.text_to_cyrillic('Ðavo je u detaǉima, nĳe da ti Čika Džoš nije rekao?') == 'Ђаво је у детаљима, није да ти Чика Џош није рекао?'

    def test_translit_double_vowels(self):
        assert self.cir.text_to_cyrillic('Džoov jednooka crnooka neeksplodirana poodrasla') == \
            'Џоов једноока црноока неексплодирана поодрасла'
        assert self.cir.text_to_cyrillic('aerodinamički aerodrom jedanaest') == 'аеродинамички аеродром једанаест'
        assert self.cir.text_to_cyrillic('dvanaest devetnaest poen ophrvan') == 'дванаест деветнаест поен опхрван'
        assert self.cir.text_to_cyrillic('poezija Izrael shema') == 'поезија Израел схема'

    def test_translit_intervjuu_ishit_neefi_rashla_statuu_ushit(self):
        assert self.cir.text_to_cyrillic('intervjuu ishitrena neefikasna rashlađen rashladni statuu vakuumiran ushit') == 'интервјуу исхитрена неефикасна расхлађен расхладни статуу вакуумиран усхит'

    def test_translit_snishod_shvat_shvaty_kontinuum_pasha(self):
        assert self.cir.text_to_cyrillic('snishodljiv shvatam shvatio shvaćam kontinuumu Pasha Pashu') == \
            'снисходљив схватам схватио схваћам континууму Пасха Пасху'

    def test_obeshrab_metjuu_ushicen_brushalter_alchajmerom(self):
        assert self.cir.text_to_cyrillic('obeshrabrenom ushićenom pedesettrogodišnjem Metjuu brushalter Alchajmerom') == \
            'обесхрабреном усхићеном педесеттрогодишњем Метјуу брусхалтер Алцхајмером'

    def test_43godisnji(self):
        assert self.cir.text_to_cyrillic('tridesettrogodiš četrdesettrogodišnji devedesettrogodiš') == \
            'тридесеттрогодиш четрдесеттрогодишњи деведесеттрогодиш'

    def test_sounds_scratches(self):
        assert self.cir.text_to_cyrillic('ŠKRRRRRR veeelike Isssuse dosjee hm 1hm hiperrealizam') == \
            'ШКРРРРРР вееелике Исссусе досјее хм 1hm хиперреализам'

    def test_roman_numerals(self):
        assert self.cir.text_to_cyrillic('i ii iii iv v vi vii viii ix x xi xii xiii xiv xv xvi xvii xviii xix xx') == \
            'и ii iii iv v ви vii viii ix x xi xii xiii xiv xv xvi xvii xviii xix xx'

    def test_line_breaks(self):
        cirt = """Први ред?
Други ред!
Трећи ред..."""
        assert self.cir.text_to_cyrillic("Prvi red?\nDrugi red!\nTreći red...") == cirt

    def test_polushva(self):
        assert self.cir.text_to_cyrillic("polushvaćen") == "полусхваћен"
