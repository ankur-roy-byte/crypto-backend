from django.core.validators import EmailValidator
from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import AbstractUser
# from rest_framework import settings
from django.core.validators import RegexValidator
from django.conf import settings


class User(AbstractUser):

    email = models.EmailField(max_length=254, validators=[EmailValidator], unique=True, blank=False)



class SmsStats(models.Model):
    coinName = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    limitReached = models.BooleanField(default=False)
    limit = models.IntegerField()
    currentRate = models.DecimalField(max_digits=19, decimal_places=10)

class WazirXData(models.Model):
    epochTimestamp = models.BigIntegerField()
    allCoinsData = JSONField(null=True)
    currentTime = models.DateTimeField(auto_now_add=True, blank=True)

class MyCoin(models.Model):
    CURRENCYCHOICE=[('INR','INR'),('USD','USD')]
    SMS_OR_EMAIL = [
        ('SMS', 'SMS'),
        ('EMAIL', 'EMAIL'),
        ('BOTH', 'BOTH'),

    ]
    BUYSELLCHOICE=[('BUY','BUY'),('SELL','SELL')]
    ANDORCHOICE=[('AND','AND'),('OR','OR')]
    # options
    coinCodes = [('1inchinr', '1inchinr'), ('1inchusdt', '1inchusdt'), ('1inchwrx', '1inchwrx'), ('aaveusdt', 'aaveusdt'), ('achinr', 'achinr'), ('achusdt', 'achusdt'), ('adabtc', 'adabtc'), ('adainr' , 'adainr'), ('adausdt', 'adausdt'), ('adawrx', 'adawrx'), ('adxusdt', 'adxusdt'), ('agldusdt', 'agldusdt'), ('aionusdt', 'aionusdt'), ('algoinr', 'algoinr'), ('algousdt', 'algousdt'),  ('aliceinr', 'aliceinr'), ('aliceusdt', 'aliceusdt'), ('alpacainr', 'alpacainr'), ('alpacausdt', 'alpacausdt'), ('alphainr', 'alphainr'), ('alphausdt', 'alphausdt'), ('ampinr', 'ampin r'), ('ampusdt', 'ampusdt'), ('ankrusdt', 'ankrusdt'), ('antusdt', 'antusdt'), ('anyusdt', 'anyusdt'), ('ardrinr', 'ardrinr'), ('ardrusdt', 'ardrusdt'), ('arinr', 'arinr'), ('arkinr', 'arkinr'), ('arkusdt', 'arkusdt'), ('arusdt', 'arusdt'), ('atausdt', 'atausdt'), ('atombtc', 'atombtc'), ('atominr', 'atominr'), ('atomusdt', 'atomusdt'), ('auctionusdt', 'auctionusdt' ), ('audiousdt', 'audiousdt'), ('avausdt', 'avausdt'), ('avaxinr', 'avaxinr'), ('avaxusdt', 'avaxusdt'), ('axsinr', 'axsinr'), ('axsusdt', 'axsusdt'), ('bakeusdt', 'bakeusdt'), ('balin r', 'balinr'), ('balusdt', 'balusdt'), ('bandusdt', 'bandusdt'), ('batbtc', 'batbtc'), ('batinr', 'batinr'), ('batusdt', 'batusdt'), ('batwrx', 'batwrx'), ('bcdusdt', 'bcdusdt'), ('bch inr', 'bchinr'), ('bchsvusdt', 'bchsvusdt'), ('bchusdt', 'bchusdt'), ('beamusdt', 'beamusdt'), ('betausdt', 'betausdt'), ('bicoinr', 'bicoinr'), ('bicousdt', 'bicousdt'), ('blzusdt', ' blzusdt'), ('bnbbtc', 'bnbbtc'), ('bnbinr', 'bnbinr'), ('bnbusdt', 'bnbusdt'), ('bnbwrx', 'bnbwrx'), ('bntusdt', 'bntusdt'), ('brdusdt', 'brdusdt'), ('btcinr', 'btcinr'), ('btcusdt', ' btcusdt'), ('btgusdt', 'btgusdt'), ('btsusdt', 'btsusdt'), ('bttcinr', 'bttcinr'), ('bttcusdt', 'bttcusdt'), ('burgerusdt', 'burgerusdt'), ('busdinr', 'busdinr'), ('busdusdt', 'busdusd t'), ('cakeinr', 'cakeinr'), ('cakeusdt', 'cakeusdt'), ('celrbtc', 'celrbtc'), ('celrinr', 'celrinr'), ('celrusdt', 'celrusdt'), ('cfxusdt', 'cfxusdt'), ('chessusdt', 'chessusdt'), ('c hrinr', 'chrinr'), ('chrusdt', 'chrusdt'), ('chrwrx', 'chrwrx'), ('chzusdt', 'chzusdt'), ('ckbinr', 'ckbinr'), ('ckbusdt', 'ckbusdt'), ('clvusdt', 'clvusdt'), ('cocosinr', 'cocosinr'),  ('cocosusdt', 'cocosusdt'), ('compinr', 'compinr'), ('compusdt', 'compusdt'), ('cosusdt', 'cosusdt'), ('cotiinr', 'cotiinr'), ('cotiusdt', 'cotiusdt'), ('creaminr', 'creaminr'), ('cre amusdt', 'creamusdt'), ('crvinr', 'crvinr'), ('crvusdt', 'crvusdt'), ('ctsiinr', 'ctsiinr'), ('ctsiusdt', 'ctsiusdt'), ('ctxcinr', 'ctxcinr'), ('ctxcusdt', 'ctxcusdt'), ('cvcinr', 'cvc inr'), ('cvcusdt', 'cvcusdt'), ('dashbtc', 'dashbtc'), ('dashinr', 'dashinr'), ('dashusdt', 'dashusdt'), ('datainr', 'datainr'), ('datausdt', 'datausdt'), ('dcrinr', 'dcrinr'), ('dcrus dt', 'dcrusdt'), ('degousdt', 'degousdt'), ('dentinr', 'dentinr'), ('dentusdt', 'dentusdt'), ('dexeusdt', 'dexeusdt'), ('dgbinr', 'dgbinr'), ('dgbusdt', 'dgbusdt'), ('dntinr', 'dntinr' ), ('dntusdt', 'dntusdt'), ('dockinr', 'dockinr'), ('dockusdt', 'dockusdt'), ('dockwrx', 'dockwrx'), ('dodousdt', 'dodousdt'), ('dogeinr', 'dogeinr'), ('dogeusdt', 'dogeusdt'), ('dogew rx', 'dogewrx'), ('dotinr', 'dotinr'), ('dotusdt', 'dotusdt'), ('duskinr', 'duskinr'), ('duskusdt', 'duskusdt'), ('dydxusdt', 'dydxusdt'), ('egldinr', 'egldinr'), ('egldusdt', 'egldusd t'), ('enjinr', 'enjinr'), ('enjusdt', 'enjusdt'), ('enjwrx', 'enjwrx'), ('ensinr', 'ensinr'), ('ensusdt', 'ensusdt'), ('eosbtc', 'eosbtc'), ('eosinr', 'eosinr'), ('eosusdt', 'eosusdt' ), ('eoswrx', 'eoswrx'), ('etcinr', 'etcinr'), ('etcusdt', 'etcusdt'), ('ethbtc', 'ethbtc'), ('ethinr', 'ethinr'), ('ethusdt', 'ethusdt'), ('ethwrx', 'ethwrx'), ('ezinr', 'ezinr'), ('e zusdt', 'ezusdt'), ('fetbtc', 'fetbtc'), ('fetusdt', 'fetusdt'), ('fidausdt', 'fidausdt'), ('filinr', 'filinr'), ('filusdt', 'filusdt'), ('firousdt', 'firousdt'), ('flowusdt', 'flowusd t'), ('frontinr', 'frontinr'), ('frontusdt', 'frontusdt'), ('ftminr', 'ftminr'), ('ftmusdt', 'ftmusdt'), ('fttbtc', 'fttbtc'), ('fttinr', 'fttinr'), ('fttusdt', 'fttusdt'), ('funusdt',  'funusdt'), ('galainr', 'galainr'), ('galausdt', 'galausdt'), ('glmrusdt', 'glmrusdt'), ('glmusdt', 'glmusdt'), ('gnousdt', 'gnousdt'), ('grsusdt', 'grsusdt'), ('grtinr', 'grtinr'), ( 'grtusdt', 'grtusdt'), ('gtoinr', 'gtoinr'), ('gtousdt', 'gtousdt'), ('gxsinr', 'gxsinr'), ('gxsusdt', 'gxsusdt'), ('hbarinr', 'hbarinr'), ('hbarusdt', 'hbarusdt'), ('hiveusdt', 'hiveu sdt'), ('hntinr', 'hntinr'), ('hntusdt', 'hntusdt'), ('hotinr', 'hotinr'), ('hotusdt', 'hotusdt'), ('icpinr', 'icpinr'), ('icpusdt', 'icpusdt'), ('icxbtc', 'icxbtc'), ('icxusdt', 'icxu sdt'), ('idexusdt', 'idexusdt'), ('ilvusdt', 'ilvusdt'), ('injusdt', 'injusdt'), ('iostbtc', 'iostbtc'), ('iostinr', 'iostinr'), ('iostusdt', 'iostusdt'), ('iotausdt', 'iotausdt'), ('i otxinr', 'iotxinr'), ('iotxusdt', 'iotxusdt'), ('jasmyusdt', 'jasmyusdt'), ('jstusdt', 'jstusdt'), ('kavausdt', 'kavausdt'), ('keyusdt', 'keyusdt'), ('klayusdt', 'klayusdt'), ('kmdinr' , 'kmdinr'), ('kmdusdt', 'kmdusdt'), ('kncusdt', 'kncusdt'), ('ksminr', 'ksminr'), ('ksmusdt', 'ksmusdt'), ('laziousdt', 'laziousdt'), ('linkinr', 'linkinr'), ('linkusdt', 'linkusdt'),  ('linkwrx', 'linkwrx'), ('loomusdt', 'loomusdt'), ('lrcinr', 'lrcinr'), ('lrcusdt', 'lrcusdt'), ('lskusdt', 'lskusdt'), ('ltcbtc', 'ltcbtc'), ('ltcinr', 'ltcinr'), ('ltcusdt', 'ltcusd t'), ('ltcwrx', 'ltcwrx'), ('lunainr', 'lunainr'), ('lunausdt', 'lunausdt'), ('lunawrx', 'lunawrx'), ('manainr', 'manainr'), ('manausdt', 'manausdt'), ('maskusdt', 'maskusdt'), ('matic btc', 'maticbtc'), ('maticinr', 'maticinr'), ('maticusdt', 'maticusdt'), ('maticwrx', 'maticwrx'), ('mboxinr', 'mboxinr'), ('mboxusdt', 'mboxusdt'), ('mdxinr', 'mdxinr'), ('mdxusdt', ' mdxusdt'), ('mftusdt', 'mftusdt'), ('minausdt', 'minausdt'), ('mirinr', 'mirinr'), ('mirusdt', 'mirusdt'), ('mkrinr', 'mkrinr'), ('mkrusdt', 'mkrusdt'), ('mlnusdt', 'mlnusdt'), ('mtlus dt', 'mtlusdt'), ('nasusdt', 'nasusdt'), ('nbsusdt', 'nbsusdt'), ('ncashusdt', 'ncashusdt'), ('nearinr', 'nearinr'), ('nearusdt', 'nearusdt'), ('neousdt', 'neousdt'), ('nkninr', 'nknin r'), ('nknusdt', 'nknusdt'), ('nmrusdt', 'nmrusdt'), ('nulsbtc', 'nulsbtc'), ('nulsusdt', 'nulsusdt'), ('oceanusdt', 'oceanusdt'), ('ogninr', 'ogninr'), ('ognusdt', 'ognusdt'), ('omgbt c', 'omgbtc'), ('omginr', 'omginr'), ('omgusdt', 'omgusdt'), ('oneinr', 'oneinr'), ('oneusdt', 'oneusdt'), ('ontinr', 'ontinr'), ('ontusdt', 'ontusdt'), ('ookiinr', 'ookiinr'), ('ookiu sdt', 'ookiusdt'), ('oxtusdt', 'oxtusdt'), ('paxginr', 'paxginr'), ('paxgusdt', 'paxgusdt'), ('perpusdt', 'perpusdt'), ('phainr', 'phainr'), ('phausdt', 'phausdt'), ('pntinr', 'pntinr' ), ('pntusdt', 'pntusdt'), ('polybtc', 'polybtc'), ('polyinr', 'polyinr'), ('polyusdt', 'polyusdt'), ('portousdt', 'portousdt'), ('powrusdt', 'powrusdt'), ('pundixusdt', 'pundixusdt'),  ('pushinr', 'pushinr'), ('pushusdt', 'pushusdt'), ('qiusdt', 'qiusdt'), ('qkcbtc', 'qkcbtc'), ('qkcusdt', 'qkcusdt'), ('qntinr', 'qntinr'), ('qntusdt', 'qntusdt'), ('qtumusdt', 'qtumu sdt'), ('quickinr', 'quickinr'), ('quickusdt', 'quickusdt'), ('radusdt', 'radusdt'), ('rareusdt', 'rareusdt'), ('rayusdt', 'rayusdt'), ('reefinr', 'reefinr'), ('reefusdt', 'reefusdt'),  ('reninr', 'reninr'), ('renusdt', 'renusdt'), ('repusdt', 'repusdt'), ('reqbtc', 'reqbtc'), ('reqinr', 'reqinr'), ('requsdt', 'requsdt'), ('rlcinr', 'rlcinr'), ('rlcusdt', 'rlcusdt'),  ('roseinr', 'roseinr'), ('roseusdt', 'roseusdt'), ('rsrusdt', 'rsrusdt'), ('runeinr', 'runeinr'), ('runeusdt', 'runeusdt'), ('runewrx', 'runewrx'), ('rvnbtc', 'rvnbtc'), ('rvnusdt', ' rvnusdt'), ('sandinr', 'sandinr'), ('sandusdt', 'sandusdt'), ('santosusdt', 'santosusdt'), ('scinr', 'scinr'), ('scrtusdt', 'scrtusdt'), ('scusdt', 'scusdt'), ('shibinr', 'shibinr'), ( 'shibusdt', 'shibusdt'), ('shibwrx', 'shibwrx'), ('sklusdt', 'sklusdt'), ('slpinr', 'slpinr'), ('slpusdt', 'slpusdt'), ('sntbtc', 'sntbtc'), ('sntusdt', 'sntusdt'), ('snxinr', 'snxinr' ), ('snxusdt', 'snxusdt'), ('solinr', 'solinr'), ('solusdt', 'solusdt'), ('spellusdt', 'spellusdt'), ('srmusdt', 'srmusdt'), ('steemusdt', 'steemusdt'), ('stmxbtc', 'stmxbtc'), ('stmxu sdt', 'stmxusdt'), ('storjusdt', 'storjusdt'), ('stptusdt', 'stptusdt'), ('straxusdt', 'straxusdt'), ('stxinr', 'stxinr'), ('stxusdt', 'stxusdt'), ('sunusdt', 'sunusdt'), ('superusdt',  'superusdt'), ('sushiinr', 'sushiinr'), ('sushiusdt', 'sushiusdt'), ('sxpinr', 'sxpinr'), ('sxpusdt', 'sxpusdt'), ('sysusdt', 'sysusdt'), ('tfuelinr', 'tfuelinr'), ('tfuelusdt', 'tfue lusdt'), ('thetabtc', 'thetabtc'), ('thetausdt', 'thetausdt'), ('tkoinr', 'tkoinr'), ('tkousdt', 'tkousdt'), ('tlminr', 'tlminr'), ('tlmusdt', 'tlmusdt'), ('tomousdt', 'tomousdt'), ('t rbinr', 'trbinr'), ('trbusdt', 'trbusdt'), ('trxbtc', 'trxbtc'), ('trxinr', 'trxinr'), ('trxusdt', 'trxusdt'), ('trxwrx', 'trxwrx'), ('tusdusdt', 'tusdusdt'), ('uftinr', 'uftinr'), ('u ftusdt', 'uftusdt'), ('umainr', 'umainr'), ('umausdt', 'umausdt'), ('uniinr', 'uniinr'), ('uniusdt', 'uniusdt'), ('usdcusdt', 'usdcusdt'), ('usdpusdt', 'usdpusdt'), ('usdtinr', 'usdtin r'), ('vetinr', 'vetinr'), ('vetusdt', 'vetusdt'), ('vgxusdt', 'vgxusdt'), ('vibusdt', 'vibusdt'), ('viteinr', 'viteinr'), ('viteusdt', 'viteusdt'), ('voxelusdt', 'voxelusdt'), ('waves usdt', 'wavesusdt'), ('waxpusdt', 'waxpusdt'), ('wininr', 'wininr'), ('winusdt', 'winusdt'), ('wrxbtc', 'wrxbtc'), ('wrxinr', 'wrxinr'), ('wrxusdt', 'wrxusdt'), ('wtcusdt', 'wtcusdt'),  ('xecinr', 'xecinr'), ('xecusdt', 'xecusdt'), ('xeminr', 'xeminr'), ('xemusdt', 'xemusdt'), ('xlminr', 'xlminr'), ('xlmusdt', 'xlmusdt'), ('xmrbtc', 'xmrbtc'), ('xmrusdt', 'xmrusdt'),  ('xnousdt', 'xnousdt'), ('xrpbtc', 'xrpbtc'), ('xrpinr', 'xrpinr'), ('xrpusdt', 'xrpusdt'), ('xrpwrx', 'xrpwrx'), ('xtzusdt', 'xtzusdt'), ('xvginr', 'xvginr'), ('xvgusdt', 'xvgusdt'),  ('xvsinr', 'xvsinr'), ('xvsusdt', 'xvsusdt'), ('yfiiinr', 'yfiiinr'), ('yfiinr', 'yfiinr'), ('yfiiusdt', 'yfiiusdt'), ('yfiiwrx', 'yfiiwrx'), ('yfiusdt', 'yfiusdt'), ('yfiwrx', 'yfiwr x'), ('zecinr', 'zecinr'), ('zecusdt', 'zecusdt'), ('zilbtc', 'zilbtc'), ('zilinr', 'zilinr'), ('zilusdt', 'zilusdt'), ('zrxbtc', 'zrxbtc'), ('zrxinr', 'zrxinr'), ('zrxusdt', 'zrxusdt' )]
    coinCode = models.CharField(max_length=70,choices=coinCodes, blank=False, default='')
    currency=models.CharField(max_length=70,choices=CURRENCYCHOICE, blank=False, default='INR',null=False)
    buyOrSell=models.CharField(max_length=70,choices=BUYSELLCHOICE, blank=False, default='SELL',null=False)
    andConditionOr=models.CharField(max_length=70,choices=ANDORCHOICE, blank=False, default='OR',null=False)

    description = models.CharField(max_length=200, blank=True, default='')
    halfHourPercentage = models.IntegerField(default=5,blank=True)
    One1HourPercentage = models.IntegerField(blank=False)
    two2HourPercentage = models.IntegerField(default=5,blank=True)
    three3HourPercentage = models.IntegerField(default=5,blank=True)
    four4HourPercentage = models.IntegerField(default=5,blank=True)
    five5HourPercentage = models.IntegerField(default=5,blank=True)
    sms_or_email_notification = models.CharField(
        max_length=25,
        choices=SMS_OR_EMAIL,
        default='EMAIL',
    )
    alarmPercentage = models.IntegerField(default=10, blank=True)
    goodNewsPercentage = models.IntegerField(default=10, blank=True)
    myprice=models.DecimalField(default=0.0, max_digits=19, decimal_places=10)


class Profile(models.Model):
    SMS = 'SMS'
    EMAIL = 'EMAIL'
    SMS_OR_EMAIL = [
        (SMS, 'SMS'),
        (EMAIL, 'EMAIL'),

    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )
    username = models.CharField(max_length=25, unique=True, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)
    name = models.CharField(max_length=200)

    # widgets location and data about coins for each user
    currentState = JSONField(null=True)
    sellRecordData = JSONField(null=True)
    buyRecordData = JSONField(null=True)
    need_notification = models.BooleanField(default=False)
    smsSentPerDay = models.PositiveIntegerField(default=0)
    sms_or_email_notification = models.CharField(
        max_length=25,
        choices=SMS_OR_EMAIL,
        default=SMS,
    )

