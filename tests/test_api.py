import unittest
# import pytest

from api.main import app


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_empty_response(self):
        response = self.client.post('/parse')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {
            "message": "text is empty"
        })

    def test_all_text_is_invalid(self):
        response = self.client.post(
            '/parse', data=dict(
                text="lmplñ njaqe ufhadg zq jdjaaqqskfaoqw"
            ))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {
            "message": "words are invalid"
        })

    def test_success_text(self):
        response = self.client.post(
            '/parse', data=dict(
                text="shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx py en yco ienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi yrx qinexwo qx rqw wxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn cwj hysucxdqm ms hdmwpe igxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqh ihncrl mlceo udr fm ocxfsjdng sfoqmd pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd lwnepmcg xlmnfqry ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsild rfimdy mwd oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql"
            ))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            'prepositions': 3,
            'verbs': 36,
            'subjunctive_verbs': 25,
            'pretty_numbers': 22,
            'vocabulary_list': ['sqflo', 'spqinedf', 'sfoqmd', 'syejrqd', 'shoce', 'srdueqhgiy', 'sionpux', 'xclpedqmi', 'xlmnfqry', 'xrpmyenq', 'xrdng', 'ocxfsjdng', 'oewgjfr', 'ojxfqhernm', 'cop', 'coj', 'cmfur', 'cwj', 'cpqmxj', 'chwjlg', 'cejfugn', 'qx', 'qplfjnwidg', 'qhmoixw', 'ql', 'qdrulxogji', 'qinhmjul', 'qinexwo', 'qihmu', 'ncsepfl', 'nmodwsqijh', 'nwcrus', 'nfwh', 'nj', 'ng', 'ms', 'mw', 'mwd', 'mlceo', 'mjxdqfrnlg', 'wxflpdn', 'whc', 'wjuln', 'podciy', 'pq', 'py', 'phfer',
                                'prfmjicud', 'pdoymnwxei', 'fclgj', 'fm', 'fwdmslqn', 'fpwcnguieh', 'fdw', 'fgixsr', 'yco', 'ycqlinro', 'ylduwpsnh', 'yrx', 'yiq', 'hysucxdqm', 'hdmwpe', 'hgecdfj', 'en', 'emjocsild', 'epgdc', 'ermjdhsx', 'lwnepmcg', 'lgchqdin', 'jxhwe', 'rsogxd', 'rseoyl', 'rqw', 'rfimdy', 'rhfl', 'do', 'dcnql', 'dmqpchuyf', 'dwuch', 'dgsloqe', 'gcxr', 'ghepqyd', 'ghlyopuncw', 'ghu', 'grewyluhfs', 'us', 'uo', 'ucf', 'ujxqh', 'udr', 'icmqsdj', 'iw', 'ifl', 'iygsex', 'ihncrl', 'ienqm', 'irmcunfgx', 'igxweo', 'ignpeyf'],
        })


if __name__ == "__main__":
    unittest.main()
