__author__ = 'nolanemirot'

import urllib
import urlparse
from urlparse import urlparse, parse_qs

#
# url = 'http://foo.appspot.com/abc?def=ghi'
# parsed = parse.urlparse(url)
# parse.parse_qs(parsed)['ghi'] = "toto"
# print(parse.parse_qs(parsed.query)['def'])

import urllib.parse

url = 'http://www.rentalcars.com/LoadingSearchResults.do?doMinute=00&driversAge=25&doHour=10&searchType=geosearch&puLocationType=airport&rateQualifier.rateCode=&puHour=10&rateQualifier.frequentTravelerIDNumber=&carCategory=&doCountryCode=&emptySearchResults=true&coordinates=37.618972%2C-122.374889&puDay=18&filterTo=49&fromFts=true&puSearchAgainInput=San+Francisco+Intl%2C+US+%28SFO%29&countryCode=us&doDay=20&serverName=&rateQualifier.discountNbr=&preferred_company=&filterFrom=0&puMonth=3&rateQualifier.partnerCode=&newSearchResults=true&puMinute=00&doMonth=3&puSearchInput=San+Francisco+Intl%2C+US+%28SFO%29&doYear=2015&rateQualifier.accountNo=&puYear=2015'
#print(urlparse(url).query)
#'uname=mark&pwd=test&age=20'



dic = urlparse.parse_qs(url)
print(dic)
#dic  = urlparse.parse_qs(urlparse.urlparse(url)[4])


#dic["doMonth"] = 4
#dic["doDay"] = 6

#url = parse.urlencode(dic, doseq=True)
#print("dic", dic)
#print("url:", url)
#{'age': ['20'], 'pwd': ['test'], 'uname': ['mark']}
