# Author: CRS 9/21/21
currentStatesPop = 331832432
ratePerMin = 60 / 25
ratePerHour = ratePerMin * 60
ratePerDay = ratePerHour * 24
ratePerYear = ratePerDay * 365
popOneYear = currentStatesPop + ratePerYear + ratePerDay
print(popOneYear)
