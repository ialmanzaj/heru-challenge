import unittest

from api.herucode import HeruCodeFactory


class HeruCodeTest(unittest.TestCase):

    def test_all_words_invalid(self):
        with self.assertRaises(ValueError):
            HeruCodeFactory.create("lmplñ njaqe ufhadg zq jdjaaqqskfaoqw")

    def test_weird_characters(self):
        with self.assertRaises(ValueError):
            HeruCodeFactory.create(
                "cmfur.´?=qdrulxogji ¿whc ermjdhsx= lmplñ njaqe {ufhadg zq jdjaaqqskfaoqw")

    def test_all_words_valid(self):
        heru = HeruCodeFactory.create("shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx py en yco ienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi yrx qinexwo qx rqw wxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn cwj hysucxdqm ms hdmwpe igxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqh ihncrl mlceo udr fm ocxfsjdng sfoqmd pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd lwnepmcg xlmnfqry ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsild rfimdy mwd oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql")
        self.assertIs(heru.get_total_prepositions(), 3)

    def test_first(self):
        heru = HeruCodeFactory.create("shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx py en yco ienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi yrx qinexwo qx rqw wxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn cwj hysucxdqm ms hdmwpe igxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqh ihncrl mlceo udr fm ocxfsjdng sfoqmd pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd lwnepmcg xlmnfqry ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsild rfimdy mwd oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql")

        self.assertEqual(heru.get_total_prepositions(), 3)
        self.assertEqual(heru.get_total_verbs(), 36)
        self.assertEqual(heru.get_total_subjunctive_verbs(), 25)
        self.assertEqual(heru.get_pretty_number(), 22)
        self.assertEqual(heru.convert_word_to_number("gxjrc"), 605637)
        self.assertEqual(heru.sort_word_topo("gxjrc"), "xcjrg")

        self.assertEqual(heru.get_vocabulary_list(), ['sqflo', 'spqinedf', 'sfoqmd', 'syejrqd', 'shoce', 'srdueqhgiy', 'sionpux', 'xclpedqmi', 'xlmnfqry', 'xrpmyenq', 'xrdng', 'ocxfsjdng', 'oewgjfr', 'ojxfqhernm', 'cop', 'coj', 'cmfur', 'cwj', 'cpqmxj', 'chwjlg', 'cejfugn', 'qx', 'qplfjnwidg', 'qhmoixw', 'ql', 'qdrulxogji', 'qinhmjul', 'qinexwo', 'qihmu', 'ncsepfl', 'nmodwsqijh', 'nwcrus', 'nfwh', 'nj', 'ng', 'ms', 'mw', 'mwd', 'mlceo', 'mjxdqfrnlg', 'wxflpdn', 'whc', 'wjuln', 'podciy', 'pq', 'py', 'phfer',
                                                      'prfmjicud', 'pdoymnwxei', 'fclgj', 'fm', 'fwdmslqn', 'fpwcnguieh', 'fdw', 'fgixsr', 'yco', 'ycqlinro', 'ylduwpsnh', 'yrx', 'yiq', 'hysucxdqm', 'hdmwpe', 'hgecdfj', 'en', 'emjocsild', 'epgdc', 'ermjdhsx', 'lwnepmcg', 'lgchqdin', 'jxhwe', 'rsogxd', 'rseoyl', 'rqw', 'rfimdy', 'rhfl', 'do', 'dcnql', 'dmqpchuyf', 'dwuch', 'dgsloqe', 'gcxr', 'ghepqyd', 'ghlyopuncw', 'ghu', 'grewyluhfs', 'us', 'uo', 'ucf', 'ujxqh', 'udr', 'icmqsdj', 'iw', 'ifl', 'iygsex', 'ihncrl', 'ienqm', 'irmcunfgx', 'igxweo', 'ignpeyf'])

    def test_second(self):
        heru = HeruCodeFactory.create("dufqwh ndis eqclrnguo ceqrugs meod eofxlrd uqpwmni xrhm qgro hlwgimn fjnomcledi silruxh efwh uxfrpsnqd fyejhi fxdn swfruc eopq hcgeox lhimoynsr rwjxecpmfl gimqxwuyr eujh rfs qncuyiel hwuiqlne umyldn uwflpqc gywlc oxmegsdi sqemywlg cnfimrgows hnxyfd exmdnos djpsogiy xyp myngercj yeujqcoih sgljco xy lruneodc frqog hqsgcy wmi hyfgqj iecusqjp ugnmqfypsd yp rxoew lqeshijndg umynehjsci rnc xhrjyocde mnefpj rcyihwxq oihjwrup gquscxhw ucrfdsoeq drg nqhodjsm snp cwoen ehyldsnmf pmrs cghuwpfxly ifwpnx wqdgrl xocpjedsfm oegli url rylnsph ijucmxw jwispgefdo heixgmcy gm sdhfnoxg hc jqwpdo eo hmypjfu xuedl nqpge cnyosu dniefl lf xcdupho wixmhcuynj poy ous jwroheqm xchm jnufdshiqe liyrexhmu cjlxoiquef fwqrijemcd csxpy eqxghfry fhnwomgyuq yj euhxmosc")

        self.assertEqual(heru.get_total_prepositions(), 3)
        self.assertEqual(heru.get_total_verbs(), 46)
        self.assertEqual(heru.get_total_subjunctive_verbs(), 26)
        self.assertEqual(heru.get_pretty_number(), 21)
        self.assertEqual(heru.get_vocabulary_list(),  ['sqemywlg', 'snp', 'swfruc', 'sdhfnoxg', 'sgljco', 'silruxh', 'xocpjedsfm', 'xchm', 'xcdupho', 'xy', 'xyp', 'xhrjyocde', 'xrhm', 'xuedl', 'oxmegsdi', 'oegli', 'ous', 'oihjwrup', 'csxpy', 'cnfimrgows', 'cnyosu', 'cwoen', 'ceqrugs', 'cjlxoiquef', 'cghuwpfxly', 'qncuyiel', 'qgro', 'nqpge', 'nqhodjsm', 'ndis', 'mnefpj', 'myngercj', 'meod', 'wqdgrl', 'wmi', 'wixmhcuynj', 'poy', 'pmrs', 'fxdn', 'fwqrijemcd', 'fyejhi', 'fhnwomgyuq', 'fjnomcledi', 'frqog', 'yp', 'yeujqcoih', 'yj', 'hc', 'hcgeox', 'hqsgcy',
                                                       'hnxyfd', 'hmypjfu', 'hwuiqlne', 'hyfgqj', 'heixgmcy', 'hlwgimn', 'exmdnos', 'eo', 'eopq', 'eofxlrd', 'eqxghfry', 'eqclrnguo', 'efwh', 'ehyldsnmf', 'euhxmosc', 'eujh', 'lqeshijndg', 'lf', 'lhimoynsr', 'lruneodc', 'liyrexhmu', 'jqwpdo', 'jnufdshiqe', 'jwroheqm', 'jwispgefdo', 'rxoew', 'rcyihwxq', 'rnc', 'rwjxecpmfl', 'rfs', 'rylnsph', 'dniefl', 'djpsogiy', 'drg', 'dufqwh', 'gquscxhw', 'gm', 'gywlc', 'gimqxwuyr', 'uxfrpsnqd', 'ucrfdsoeq', 'uqpwmni', 'umynehjsci', 'umyldn', 'uwflpqc', 'url', 'ugnmqfypsd', 'ifwpnx', 'iecusqjp', 'ijucmxw'])


if __name__ == "__main__":
    unittest.main()
