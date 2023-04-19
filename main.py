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
tube=str(input("Which tube are you using: "))
charge=str(input("What charge power level are you using: "))

#Placeholder space for switch to choose proper csv
ballisticTable=0

match tube:
    case "Mk6":
        match charge:
            case "0":
                ballisticTable = pd.read_csv('BallisticData/Mk6_charge0.csv')
            case "1":
                ballisticTable = pd.read_csv('BallisticData/Mk6_charge1.csv')
            case "2":
                ballisticTable = pd.read_csv('BallisticData/Mk6_charge2.csv')
            case _:
                print("You didn't choose any proper power!")
    case "M252":
        match charge:
            case "0":
                ballisticTable = pd.read_csv('BallisticData/M252_charge0.csv')
            case "1":
                ballisticTable = pd.read_csv('BallisticData/M252_charge1.csv')
            case "2":
                ballisticTable = pd.read_csv('BallisticData/M252_charge2.csv')
            case _:
                print("You didn't choose any proper power!")
    case _:
        print("You didn't choose anything!")

#Find proper rows in ballistic chart
closestDistRowL = ballisticTable.loc[ballisticTable['Dystans'] <= distance].tail(1)
closestDistRowH = ballisticTable.loc[ballisticTable['Dystans'] > distance].head(1)

#Read of the constants from proper rows
closestDistL = closestDistRowL['Dystans'].values
closestDistH = closestDistRowH['Dystans'].values
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

#Shortcuts to not re-do so many operations
distanceDiff=closestDistH-closestDistL
distFromClosestL=distance-closestDistL

#Higher table temporary variables
tempElevation=closestElevL-(((closestElevL-closestElevH)/distanceDiff)*distFromClosestL)
dElev100=closestDElev100L+(((closestDElev100H-closestDElev100L)/distanceDiff)*distFromClosestL)
dFlightTime=dFlightTimeL+(((dFlightTimeH-dFlightTimeL)/distanceDiff)*distFromClosestL)
tempFlightTime=flightTimeL-(((flightTimeL-flightTimeH)/distanceDiff)*distFromClosestL)
windage=float(windageL-(((windageL-windageH)/distanceDiff)*distFromClosestL))
frontWind=frontWindL+(((frontWindH-frontWindL)/distanceDiff)*distFromClosestL)
backWind=backWindL+(((backWindH-backWindL)/distanceDiff)*distFromClosestL)
tempDec=tempDecL+(((tempDecH-tempDecL)/distanceDiff)*distFromClosestL)
tempInc=tempIncL+(((tempIncH-tempIncL)/distanceDiff)*distFromClosestL)
airDensDec=airDensDecL+(((airDensDecH-airDensDecL)/distanceDiff)*distFromClosestL)
airDensInc=airDensIncL+(((airDensIncH-airDensIncL)/distanceDiff)*distFromClosestL)

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

#Displayed info final math
flightTime=tempFlightTime+(heightDiff/100*dFlightTime)
finalElevation=tempElevation+heightDiffDeg+temperatureDiffDeg+pressureDiffDeg+windCorrectionDeg
finalWindage=sideWind*windage

#The earth is round, and so are some variables rounded
rFlightTime=round(float(flightTime),0)
rFinalElevation=round(float(finalElevation),0)
rFinalWindage=round(float(finalWindage),0)

#Display final info
print("---------------------------------")
print("Flight time: "+str(rFlightTime)+"\n")
print("Final elevation: "+str(rFinalElevation)+"\n")
print("Final windage: "+str(rFinalWindage)+"\n")