import HtmlHelper as htmlHelper
import datetime as dt
import ToastHelper as toast


baseUrl = "https://www.formula1.com"

parser = htmlHelper.HtmlParserHelper("{}/en/racing/2019.html".format(baseUrl))
allElements = parser.GetElements()


def ClearRaceDateValue(values):
    dateValues = values.split("-")
    raceDay = dateValues[len(dateValues) - 1].strip()
    return raceDay


def CheckRaceDateIsToday(raceDate):
    todayDate = dt.datetime.now()
    day = todayDate.strftime("%d")
    month = todayDate.strftime("%b")
    mergedDate = "{} {}".format(day, month)
    return True if mergedDate == raceDate else False


for element in allElements:
    href = element.get("href")
    if href != "" or href is not None:
        result = parser.GetPelementFromHref("{}{}".format(baseUrl, href))
        if result is not None:
            value = result.get("value")
            if value != "" or value != None:
                lastDate = ClearRaceDateValue(result.text)
                result = CheckRaceDateIsToday(lastDate)
                if result == True:
                    toast.ShowToastMessage(lastDate)

