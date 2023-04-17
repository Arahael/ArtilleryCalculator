#Input variables
pressure=1
temperature=1
distance=1
ownElevation=1
targetElevation=1
sideWind=1
wind=1

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
else
    heightDiffDeg=(int(heightDiff)/100)*dElev100*(-1)
temperatureDiff=temperature-pressureDiff
temperatureDiffDeg=0
if temperatureDiff<0:
    temperatureDiffDeg=int(temperatureDiff)*tempDec*(-1)
else
    temperatureDiffDeg=int(temperatureDiff)*tempInc*(-1)
pressureDiff=pressure-1013.25
pressureDiffDeg=0
if pressureDiff<0:
    pressureDiffDeg=(pressureDiff/1013.25*100)*airDensDec*(-1)
else
    pressureDiffDeg=(pressureDiff/1013.25*100)*airDensInc*(-1)
windCorrectionDeg=0
if Wind<0:
    windCorrectionDeg=int(Wind)*backWind*(-1)
else
    windCorrectionDeg=int(Wind)*frontWind*(-1)

#Displayed info
flightTime=tempFlightTime+(heightDiff/100*dFlightTime)
finalElevation=tempElevation+heightDiffDeg+temperatureDiffDeg+pressureDiffDeg+windCorrectionDeg
finalWindage=sideWind+windage
