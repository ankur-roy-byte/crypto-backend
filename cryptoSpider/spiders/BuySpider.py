import os
import scrapy
import json
from mailjet_rest import Client
from buysell.models import SmsStats, Profile, MyCoin
from ..utils import currencyInfo


# Time zone list / Epoch to time zone converter
# todo
class BuySpider(scrapy.Spider):
    name = "buy"
    emailBody = ""
    emailbodyLength = 0
    subject="Crypto Email"
    totalRowForMyCoinInDataBase = 0
    headers = {
        'authorization': 'dc949dd906091babcd612d7b46012474d47c5341546d88adfe67b24a231eb907',

    }
    currentMycurrencyInfo = {}

    def start_requests(self):
        print("hii")
        urlsList = []
        limit = 300
        # create dynamic url for each coin in db
        dataBAseMyCoinData = MyCoin.objects.all().values()
        self.totalRowForMyCoinInDataBase = len(dataBAseMyCoinData)
        for item in dataBAseMyCoinData:
            # print(item)
            overallCodeSymbol = item['coinCode']
            itemObj = {}
            itemObj['item'] = item
            itemObj['url'] = 'https://min-api.cryptocompare.com/data/v2/histominute?fsym=' + self.getCoinCode(
                overallCodeSymbol) + '&tsym=' + self.getCoinCurrency(overallCodeSymbol) + '&limit=' + str(limit)
            urlsList.append(itemObj)
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", urlsList)

        # url = "https://coinswitch.co/proxy/in/api/v1/coins"
        for itemurl in urlsList:
            yield scrapy.Request(itemurl['url'], callback=self.parse, headers=self.headers,
                                 cb_kwargs=dict(itemData=itemurl['item']))

    def parse(self, response, itemData):
        jsonresponse = json.loads(response.body_as_unicode())
        dataArray = jsonresponse['Data']['Data']
        # print(response.url, "hii =========================================================================",
        #       len(dataArray), itemData)
        # api response values after calculation
        halfHourpercentage = self.calculatePercentageForTimeRange(dataArray, 270, 300)
        oneHourpercentage = self.calculatePercentageForTimeRange(dataArray, 240, 300)
        twoHourpercentage = self.calculatePercentageForTimeRange(dataArray, 180, 300)
        threeHourpercentage = self.calculatePercentageForTimeRange(dataArray, 120, 300)
        fourHourpercentage = self.calculatePercentageForTimeRange(dataArray, 60, 300)
        fiveHourpercentage = self.calculatePercentageForTimeRange(dataArray, 0, 300)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",halfHourpercentage, oneHourpercentage,
                                                 twoHourpercentage, threeHourpercentage, fourHourpercentage,
                                                 fiveHourpercentage,"itemData --------------",itemData)
        self.emailbodyLength = self.emailbodyLength +1
        if (itemData['buyOrSell'] == 'SELL'):
            self.checkandUpdateSubjectForAlarm()
            self.checkandUpdateSubjectForGoodNews()
            if (itemData['andConditionOr'] == 'OR'):
                if (halfHourpercentage >= itemData['halfHourPercentage'] or oneHourpercentage >= itemData[
                    'One1HourPercentage'] or twoHourpercentage >= itemData[
                    'two2HourPercentage'] or threeHourpercentage >= itemData[
                    'three3HourPercentage'] or fourHourpercentage >= itemData[
                    'four4HourPercentage'] or fiveHourpercentage >= itemData['five5HourPercentage']):
                    self.sellDataCreateEmailBody(itemData['coinCode'], itemData['buyOrSell'],
                                                 itemData['andConditionOr'], halfHourpercentage, oneHourpercentage,
                                                 twoHourpercentage, threeHourpercentage, fourHourpercentage,
                                                 fiveHourpercentage)
            # and condition for sell
            else:
                if (halfHourpercentage >= itemData['halfHourPercentage'] and oneHourpercentage >= itemData[
                    'One1HourPercentage'] and twoHourpercentage >= itemData[
                    'two2HourPercentage'] and threeHourpercentage >= itemData[
                    'three3HourPercentage'] and fourHourpercentage >= itemData[
                    'four4HourPercentage'] and fiveHourpercentage >= itemData['five5HourPercentage']):
                    self.sellDataCreateEmailBody()



        # buy
        else:
            if (itemData['andConditionOr'] == 'OR'):
                if (halfHourpercentage <= itemData['halfHourPercentage'] or oneHourpercentage <= itemData[
                    'One1HourPercentage'] or twoHourpercentage <= itemData[
                    'two2HourPercentage'] or threeHourpercentage <= itemData[
                    'three3HourPercentage'] or fourHourpercentage <= itemData[
                    'four4HourPercentage'] or fiveHourpercentage <= itemData['five5HourPercentage']):
                    self.buyDataCreateEmailBody()
            # and condition for sell
            else:
                if (halfHourpercentage <= itemData['halfHourPercentage'] and oneHourpercentage <= itemData[
                    'One1HourPercentage'] and twoHourpercentage <= itemData[
                    'two2HourPercentage'] and threeHourpercentage <= itemData[
                    'three3HourPercentage'] and fourHourpercentage <= itemData[
                    'four4HourPercentage'] and fiveHourpercentage <= itemData['five5HourPercentage']):
                    self.buyDataCreateEmailBody()

        # self.sendEmail()

    def checkandUpdateSubjectForAlarm(self):
        self.subject+=""

    def checkandUpdateSubjectForGoodNews(self):
        self.subject+=""

    def sellDataCreateEmailBody(self,coinCode,buyOrSell,andConditionOr,halfHourpercentage, oneHourpercentage,
                                                 twoHourpercentage, threeHourpercentage, fourHourpercentage,
                                                 fiveHourpercentage):
        print("#################################################################################",self.totalRowForMyCoinInDataBase , self.emailbodyLength)
        self.emailBody += """<b style=" font-size: larger; ">     %s </b>&nbsp; <b>     %s </b>&nbsp; <b>     %s </b>  <table>     <tr>       <th>Time</th>       <th>Difference</th>            </tr>     <tr>       <td>1/2 HOUR</td>       <td>%s</td>            </tr>     <tr>       <td>1 HOUR</td>       <td>%s</td>            </tr>     <tr>       <td>2 HOUR</td>       <td>%s</td>          </tr>     <tr>       <td>3 HOUR</td>       <td>%s</td>             </tr>     <tr>       <td> 4 HOUR</td>       <td>%s</td>            </tr>     <tr>       <td>5 HOUR</td>       <td>%s</td>       </tr>   </table>   """%(coinCode,buyOrSell,andConditionOr,halfHourpercentage, oneHourpercentage,
                                                 twoHourpercentage, threeHourpercentage, fourHourpercentage,
                                                 fiveHourpercentage)
        if(self.totalRowForMyCoinInDataBase == self.emailbodyLength):
            self.sendEmail(self.emailBody,self.subject)




    def returnPercentage(self, baseValue, currentValue):
        return (currentValue - baseValue) / baseValue * 100

    def calculatePercentageForTimeRange(self, data, baseIndex, currentIndex):
        return self.returnPercentage(data[baseIndex]['close'], data[currentIndex]['close'])

    def getCoinCode(self, overallCodeSymbol):
        return currencyInfo[overallCodeSymbol]['base_unit'].upper()

    def getCoinCurrency(self, overallCodeSymbol):
        return currencyInfo[overallCodeSymbol]['quote_unit'].upper()

    def buyDataCreateEmailBody(self):
        pass



    def sendEmail(self,html,subject):
        api_key = '4abd4af5752a5d07b0d66628e8bf7316'
        api_secret = '8d42312aaa75809baa6d8d5ba49225df'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "amritkumar047@gmail.com",
                        "Name": "Amrit"
                    },
                    "To": [
                        {
                            "Email": "amritkumar047@gmail.com",
                            "Name": "Amrit"
                        }
                    ],
                    "Subject": subject,
                    "TextPart": "My first Mailjet email",
                    "HTMLPart":html ,     # "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
                    "CustomID": "AppGettingStartedTest"
                }
            ]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)

        print(result.json())
