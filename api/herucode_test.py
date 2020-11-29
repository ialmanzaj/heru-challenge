import unittest

from herucode import HeruCode


class HeruCodeTest(unittest.TestCase):
    def test_first(self):
        heru = HeruCode("shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx py en yco ienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi yrx qinexwo qx rqw wxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn cwj hysucxdqm ms hdmwpe igxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqh ihncrl mlceo udr fm ocxfsjdng sfoqmd pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd lwnepmcg xlmnfqry ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsild rfimdy mwd oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql")

        self.assertEqual(heru.get_total_prepositions(), 3)
        self.assertEqual(heru.get_total_verbs(), 36)
        self.assertEqual(heru.get_total_subjunctive_verbs(), 25)
        #self.assertIs(heru.get_vocabulary_list(),['sqflo,', 'spqinedf', 'sfoqmd', 'syejrqd', 'shoce', 'srdueqhgiy', 'sionpux', 'xclpedqmi', 'xlmnfqry', 'xrpmyenq', 'xrdng', 'ocxfsjdng', 'oewgjfr', 'ojxfqhernm', 'cop', 'coj', 'cmfur', 'cwj', 'cpqmxj', 'chwjlg', 'cejfugn', 'qx', 'qplfjnwidg', 'qhmoixw', 'ql', 'qdrulxogji', 'qinhmjul', 'qinexwo', 'qihmu', 'ncsepfl', 'nmodwsqijh', 'nwcrus', 'nfwh', 'nj', 'ng', 'ms', 'mw', 'mwd', 'mlceo', 'mjxdqfrnlg', 'wxflpdn', 'whc', 'wjuln', 'podciy', 'pq', 'py', 'phfer','prfmjicud', 'pdoymnwxei', 'fclgj', 'fm', 'fwdmslqn', 'fpwcnguieh', 'fdw', 'fgixsr', 'yco', 'ycqlinro', 'ylduwpsnh', 'yrx', 'yiq', 'hysucxdqm', 'hdmwpe', 'hgecdfj', 'en', 'emjocsild', 'epgdc', 'ermjdhsx', 'lwnepmcg', 'lgchqdin', 'jxhwe', 'rsogxd', 'rseoyl', 'rqw', 'rfimdy', 'rhfl', 'do', 'dcnql', 'dmqpchuyf', 'dwuch', 'dgsloqe', 'gcxr', 'ghepqyd', 'ghlyopuncw', 'ghu', 'grewyluhfs', 'us', 'uo', 'ucf', 'ujxqh', 'udr', 'icmqsdj', 'iw', 'ifl', 'iygsex', 'ihncrl', 'ienqm', 'irmcunfgx', 'igxweo', 'ignpeyf'])

    def test_number_conversion(self):
        self.assertIs(HeruCode().convert_word_to_number("gxjrc"), 605637)


if __name__ == "__main__":
    unittest.main()
