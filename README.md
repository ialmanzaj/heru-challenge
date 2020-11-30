# heru-challenge

How to run?
```
brew install python3
make init
make test
make serve
```

## The Herucode Language

Archeologists found a scroll containing texts in the ancient and mysterious Herucode
language, remnants of a now-forgotten civilization: the Heruits.
After many years of study, linguists have learned some of the fundamental characteristics of
this language:

## Lexicographical Order
In Herucode, like in our system, words are always ordered lexicographically, but the
challenge is that the order of the letters in the Herucode alphabet is different from ours. Their
alphabet, in order, is: sxocqnmwpfyheljrdgui.
Letter Classification
Herucode letters are classified in two groups: the letters u, d, x, s, m, p, f are called "foo
letters" while the other letters are called "bar letters".
Prepositions
The linguists have discovered that in the Herucode language, the prepositions are the words
of exactly 6 letters which end in a foo letter and do not contain the letter u.
Verbs
Another interesting fact discovered by linguists is that, in the Herucode language, verbs are
words of 6 letters or more that end in a bar letter. Furthermore, if a verb starts in a bar letter,
then the verb is inflected in its subjunctive form.

## Numbers
Not that words aren't fun, but one could ask: how do Heruits represent the numbers? Well, in
Herucode, words also represent numbers given in base 20, where each letter is a digit. The
digits are ordered from the least significant to the most significant, which is the opposite of
our system. That is, the leftmost digit is the unit, the second digit is worth 20, the third one is
worth 400, and so on and so forth. The values of the letters are given by the order they
appear in the Herucode alphabet (which, as we saw, is ordered differently from our
alphabet). That is, the first letter of the Herucode alphabet represents the digit 0, the second
letter represents the digit 1, and the last one represents the digit 19.

As an example, the Herucode word **gxjrc** represents the number **605637.**
Heruits consider a number to be pretty if it satisfies all of the following properties:
- it is greater than or equal to 81827
- it is divisible by 3

## The Challenge
Write an API server with a single endpoint: POST /parse

This endpoint should receive as body the string parameter text containing a string of
Herucode. 

The endpoint should the return a JSON response with the following content:
- prepositions: Integer with the number of prepositions in the text.
- verbs: Integer with the number of verbs in the text.
- subjunctive_verbs: Integer with the number of subjunctive verbs.
- pretty_numbers: Integer with the number of distinct pretty numbers.
- vocabulary_list: List of strings containing all the **distinct** words in the text **ordered by Herucode’s alphabetical order.**

Remember to include detailed instructions on how to run your service. Feel free to add any
other features you may find interesting/useful. Use the test cases included to validate your
algorithm.

Test Cases

**Case A**
*Input*

`shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx
py en yco ienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi
yrx qinexwo qx rqw wxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn
cwj hysucxdqm ms hdmwpe igxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr
fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqh ihncrl mlceo udr fm ocxfsjdng sfoqmd
pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd lwnepmcg xlmnfqry
ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsild rfimdy mwd
oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql`

Expected Output

- There are 3 prepositions in the text
- There are 36 verbs in the text
- There are 25 subjunctive verbs in the text
- There are 22 distinct pretty numbers in the text
- Vocabulary list:

`['sqflo,', 'spqinedf', 'sfoqmd', 'syejrqd', 'shoce', 'srdueqhgiy', 'sionpux', 'xclpedqmi', 'xlmnfqry', 'xrpmyenq', 'xrdng', 'ocxfsjdng', 'oewgjfr', 'ojxfqhernm', 'cop', 'coj', 'cmfur', 'cwj', 'cpqmxj', 'chwjlg', 'cejfugn', 'qx', 'qplfjnwidg', 'qhmoixw', 'ql', 'qdrulxogji', 'qinhmjul', 'qinexwo', 'qihmu', 'ncsepfl', 'nmodwsqijh', 'nwcrus', 'nfwh', 'nj', 'ng', 'ms', 'mw', 'mwd', 'mlceo', 'mjxdqfrnlg', 'wxflpdn', 'whc', 'wjuln', 'podciy', 'pq', 'py', 'phfer', 'prfmjicud', 'pdoymnwxei', 'fclgj', 'fm', 'fwdmslqn', 'fpwcnguieh', 'fdw', 'fgixsr', 'yco', 'ycqlinro', 'ylduwpsnh', 'yrx', 'yiq', 'hysucxdqm', 'hdmwpe', 'hgecdfj', 'en', 'emjocsild', 'epgdc', 'ermjdhsx', 'lwnepmcg', 'lgchqdin', 'jxhwe', 'rsogxd', 'rseoyl', 'rqw', 'rfimdy', 'rhfl', 'do', 'dcnql', 'dmqpchuyf', 'dwuch', 'dgsloqe', 'gcxr', 'ghepqyd', 'ghlyopuncw', 'ghu', 'grewyluhfs', 'us', 'uo', 'ucf', 'ujxqh', 'udr', 'icmqsdj', 'iw', 'ifl', 'iygsex', 'ihncrl', 'ienqm', 'irmcunfgx', 'igxweo', 'ignpeyf']
`


**Case B**
*Input*

`dufqwh ndis eqclrnguo ceqrugs meod eofxlrd uqpwmni xrhm qgro hlwgimn fjnomcledi silruxh
efwh uxfrpsnqd fyejhi fxdn swfruc eopq hcgeox lhimoynsr rwjxecpmfl gimqxwuyr eujh rfs
qncuyiel hwuiqlne umyldn uwflpqc gywlc oxmegsdi sqemywlg cnfimrgows hnxyfd exmdnos
djpsogiy xyp myngercj yeujqcoih sgljco xy lruneodc frqog hqsgcy wmi hyfgqj iecusqjp
ugnmqfypsd yp rxoew lqeshijndg umynehjsci rnc xhrjyocde mnefpj rcyihwxq oihjwrup
gquscxhw ucrfdsoeq drg nqhodjsm snp cwoen ehyldsnmf pmrs cghuwpfxly ifwpnx wqdgrl
xocpjedsfm oegli url rylnsph ijucmxw jwispgefdo heixgmcy gm sdhfnoxg hc jqwpdo eo
hmypjfu xuedl nqpge cnyosu dniefl lf xcdupho wixmhcuynj poy ous jwroheqm xchm
jnufdshiqe liyrexhmu cjlxoiquef fwqrijemcd csxpy eqxghfry fhnwomgyuq yj euhxmosc`

Expected Output
- There are 3 prepositions in the text
- There are 46 verbs in the text
- There are 26 subjunctive verbs in the text
- There are 21 distinct pretty numbers in the text
- Vocabulary list:

`sqemywlg snp swfruc sdhfnoxg sgljco silruxh xocpjedsfm xchm xcdupho xy xyp xhrjyocde
xrhm xuedl oxmegsdi oegli ous oihjwrup csxpy cnfimrgows cnyosu cwoen ceqrugs cjlxoiquef
cghuwpfxly qncuyiel qgro nqpge nqhodjsm ndis mnefpj myngercj meod wqdgrl wmi
wixmhcuynj poy pmrs fxdn fwqrijemcd fyejhi fhnwomgyuq fjnomcledi frqog yp yeujqcoih yj hc
hcgeox hqsgcy hnxyfd hmypjfu hwuiqlne hyfgqj heixgmcy hlwgimn exmdnos eo eopq eofxlrd
eqxghfry eqclrnguo efwh ehyldsnmf euhxmosc eujh lqeshijndg lf lhimoynsr lruneodc
liyrexhmu jqwpdo jnufdshiqe jwroheqm jwispgefdo rxoew rcyihwxq rnc rwjxecpmfl rfs rylnsph
dniefl djpsogiy drg dufqwh gquscxhw gm gywlc gimqxwuyr uxfrpsnqd ucrfdsoeq uqpwmni
umynehjsci umyldn uwflpqc url ugnmqfypsd ifwpnx iecusqjp ijucmxw
`
