#imports
import numpy as np
import pandas as pd

#Input variables
pressure = input("Set pressure: ")
temperature = input("Set temperature: ")
distance = 400
ownElevation = input("Set your elevation: ")
targetElevation = input("Set targets elevation: ")
sideWind = input("Set side wind speed: ")
wind = input("Set fron/back wind (back wind is negative value): ")

#Placeholder space for switch to choose proper csv

#Temporary csv import
ballisticTable = pd.read_csv('BallisticData/Mk6_charge1.csv')
print(ballisticTable.columns)
closestDistL = ballisticTable.loc[ballisticTable['Dystans'] <= distance].tail(1)

closestDistH = ballisticTable.loc[ballisticTable['Dystans'] > distance].head(1)

#Read of the csv
print("Closest smaller row:")
print(closestDistL)
print("\nClosest greater row:")
print(closestDistH)
#closestDistL=1
#closestDistH=1
closestElevL=1
closestElevH=1
closestDElev100L=1
closestDElev100H=1
dFlightTimeL=1
dFlightTimeH=1
flightTimeL=1
flightTimeH=1
windageL=1
windageH=1
frontWindL=1
frontWindH=1
backWindL=1
backWindH=1
tempDecL=1
tempDecH=1
tempIncL=1
tempIncH=1
airDensDecL=1
airDensDecH=1
airDensIncL=1
airDensIncH=1

#Higher table temp variables
tempElevation=closestDistL-(((closestElevL-closestElevH)/(closestDistH-closestDistL))*(distance-closestDistL))
dElev100=closestDElev100L+(((closestDElev100H-closestDElev100L)/(closestDistH-closestDistL))*(distance-closestDistL))
dFlightTime=dFlightTimeL+(((dFlightTimeH-dFlightTimeL)/(closestDistH-closestDistL))*(distance-closestDistL))
tempFlightTime=flightTimeL-(((flightTimeL-flightTimeH)/(closestDistH-closestDistL))*(distance-closestDistL))
windage=windageL(((windageL-windageH)/(closestDistH-closestDistL))*(distance-closestDistL))
frontWind=frontWindL+(((frontWindH-frontWindL)/(closestDistH-closestDistL))*(distance-closestDistL))
backWind=backWindL+(((backWindH-backWindL)/(closestDistH-closestDistL))*(distance-closestDistL))
tempDec=tempDecL+(((tempDecH-tempDecL)/(closestDistH-closestDistL))*(distance-closestDistL))
tempInc=tempIncL+(((tempIncH-tempIncL)/(closestDistH-closestDistL))*(distance-closestDistL))
airDensDec=airDensDecL+(((airDensDecH-airDensDecL)/(closestDistH-closestDistL))*(distance-closestDistL))
airDensInc=airDensIncL+(((airDensIncH-airDensIncL)/(closestDistH-closestDistL))*(distance-closestDistL))

#Calculated variables
heightDiff=ownElevation-targetElevation
heightDiffDeg=0
if ownElevation>targetElevation:
    heightDiffDeg=(int(heightDiff)/100)*dElev100
else:
    heightDiffDeg=(int(heightDiff)/100)*dElev100*(-1)
pressureDiff=pressure-1013.25
pressureDiffDeg=0
if pressureDiff<0:
    pressureDiffDeg=(pressureDiff/1013.25*100)*airDensDec*(-1)
else:
    pressureDiffDeg=(pressureDiff/1013.25*100)*airDensInc*(-1)
temperatureDiff=temperature-pressureDiff
temperatureDiffDeg=0
if temperatureDiff<0:
    temperatureDiffDeg=int(temperatureDiff)*tempDec*(-1)
else:
    temperatureDiffDeg=int(temperatureDiff)*tempInc*(-1)
windCorrectionDeg=0
if wind<0:
    windCorrectionDeg=int(wind)*backWind*(-1)
else:
    windCorrectionDeg=int(wind)*frontWind*(-1)

#Displayed info
flightTime=tempFlightTime+(heightDiff/100*dFlightTime)
finalElevation=tempElevation+heightDiffDeg+temperatureDiffDeg+pressureDiffDeg+windCorrectionDeg
finalWindage=sideWind+windage
