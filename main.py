#imports
import numpy as np
import pandas as pd

#Input variables
pressure = float(input("Set pressure: "))
temperature = float(input("Set temperature: "))
distance = float(input("Set distance to the target: "))
ownElevation = float(input("Set your elevation: "))
targetElevation = float(input("Set targets elevation: "))
sideWind = float(input("Set side wind speed: "))
wind = float(input("Set front/back wind (back wind is negative value): "))

#Placeholder space for switch to choose proper csv

#Temporary csv import
ballisticTable = pd.read_csv('BallisticData/Mk6_charge1.csv')

#print(ballisticTable.columns)
#print(ballisticTable.columns.size)
closestDistRowL = ballisticTable.loc[ballisticTable['Dystans'] <= distance].tail(1)

closestDistRowH = ballisticTable.loc[ballisticTable['Dystans'] > distance].head(1)

#Read of the csv
closestDistL = closestDistRowL['Dystans'].values
#print(closestDistL)
closestDistH = closestDistRowH['Dystans'].values
#print(closestDistH)
closestElevL = closestDistRowL['Elewacja'].values
closestElevH = closestDistRowH['Elewacja'].values
closestDElev100L = closestDistRowL['D elew/100m'].values
closestDElev100H = closestDistRowH['D elew/100m'].values
dFlightTimeL = closestDistRowL['D CzL/100'].values
dFlightTimeH = closestDistRowH['D CzL/100'].values
flightTimeL = closestDistRowL['CzL'].values
flightTimeH = closestDistRowH['CzL'].values
windageL = closestDistRowL['Azymut Xwiatr 1m/s'].values
windageH = closestDistRowH['Azymut Xwiatr 1m/s'].values

#Check if wind is frontal or from the back?
frontWindL = closestDistRowL['Czolowy'].values
frontWindH = closestDistRowH['Czolowy'].values
backWindL = closestDistRowL['Tylni'].values
backWindH = closestDistRowH['Tylni'].values

tempDecL = closestDistRowL['TempSpad.'].values
tempDecH = closestDistRowH['TempSpad.'].values
tempIncL = closestDistRowL['TempWzros.'].values
tempIncH = closestDistRowH['TempWzros.'].values
airDensDecL = closestDistRowL['AirSpad.'].values
airDensDecH = closestDistRowH['AirSpad.'].values
airDensIncL = closestDistRowL['AirWzros.'].values
airDensIncH = closestDistRowH['AirWzros.'].values

#Higher table temp variables
tempElevation=closestElevL-(((closestElevL-closestElevH)/(closestDistH-closestDistL))*(distance-closestDistL))
dElev100=closestDElev100L+(((closestDElev100H-closestDElev100L)/(closestDistH-closestDistL))*(distance-closestDistL))
dFlightTime=dFlightTimeL+(((dFlightTimeH-dFlightTimeL)/(closestDistH-closestDistL))*(distance-closestDistL))
tempFlightTime=flightTimeL-(((flightTimeL-flightTimeH)/(closestDistH-closestDistL))*(distance-closestDistL))
windage=float(windageL-(((windageL-windageH)/(closestDistH-closestDistL))*(distance-closestDistL)))
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
    heightDiffDeg=(float(int(heightDiff))/100)*dElev100
else:
    heightDiffDeg=(float(int(heightDiff))/100)*dElev100*(-1)

pressureDiff=pressure-1013.25
pressureDiffDeg=float(0)
if pressureDiff<0:
    pressureDiffDeg=(pressureDiff/1013.25*100)*airDensDec*(-1)
else:
    pressureDiffDeg=(pressureDiff/1013.25*100)*airDensInc*(-1)

temperatureDiff=temperature-15
temperatureDiffDeg=float(0)
if temperatureDiff<0:
    temperatureDiffDeg=float(int(temperatureDiff))*tempDec*(-1)
else:
    temperatureDiffDeg=float(int(temperatureDiff))*tempInc*(-1)

windCorrectionDeg=0
if wind<0:
    windCorrectionDeg=float(wind)*float(backWind)*(-1)
    if windCorrectionDeg<0:
        windCorrectionDeg*=-1
else:
    windCorrectionDeg=float(wind)*float(frontWind)*(-1)
    if windCorrectionDeg<0:
        windCorrectionDeg*=-1

#Displayed info
flightTime=tempFlightTime+(heightDiff/100*dFlightTime)
finalElevation=tempElevation+heightDiffDeg+temperatureDiffDeg+pressureDiffDeg+windCorrectionDeg
finalWindage=sideWind*windage

print("Flight time: "+str(flightTime)+"\n")
print("Final elevation: "+str(finalElevation)+"\n")
print("Final windage: "+str(finalWindage))