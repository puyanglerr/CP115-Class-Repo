numNight = float(input())
basicrate = 250 * numNight
servicecharge = float(15) / 100 * basicrate
totalPayment = basicrate + servicecharge
print(totalPayment)
