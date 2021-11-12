import requests
# 0,1,2
cloudiness = "1"
Iglob = "300"
Tout = "10"

data = '{"controls":{' \
       '"gui.datetime":{"visible":1,"value":"2018-03-01T12:00"},' \
       '"gui.cloudiness":{"visible":1,' \
       f'"value":{cloudiness}' \
       '},' \
       '"gui.Iglob":{"visible":1,' \
       f'"value":{Iglob}' \
       '},' \
       '"gui.Tout":{"visible":1,' \
       f'"value":{Tout}' \
       '},' \
       '"gui.RHout":{"visible":1,"value":"60"},' \
       '"gui.Windsp":{"visible":1,"value":5},' \
       '"gui.crop":{"visible":1,"value":1},' \
       '"gui.LAI":{"visible":0,"value":3},' \
       '"gui.maxTransp":{"visible":0,"value":1000},' \
       '"gui.cover":{"visible":1,"value":0},' \
       '"gui.orientation":{"visible":0,"value":0},' \
       '"gui.spHeating":{"visible":1,"value":"18"},' \
       '"gui.spVent":{"visible":1,"value":"22"},' \
       '"gui.spHum":{"visible":0,"value":100},' \
       '"gui.minTpipe":{"visible":0,"value":"0"},' \
       '"gui.maxTpipe":{"visible":0,"value":90},' \
       '"gui.PbandTemp":{"visible":0,"value":5},' \
       '"gui.NaloopWnd":{"visible":0,"value":50},' \
       '"gui.PbandHum":{"visible":0,"value":5},' \
       '"gui.WinLee":{"visible":0,"value":"0"},' \
       '"gui.WinWnd":{"visible":0,"value":0},' \
       '"gui.WinMax":{"visible":0,"value":100},' \
       '"gui.screen1":{"visible":1,"value":0},' \
       '"gui.screen1Gap":{"visible":0,"value":0},' \
       '"gui.screen2":{"visible":0,"value":0},' \
       '"gui.screen2Gap":{"visible":0,"value":0},' \
       '"gui.screen3":{"visible":0,"value":0},' \
       '"gui.screen3Gap":{"visible":0,"value":0},' \
       '"gui.illum.top.type":{"visible":1,"value":0},' \
       '"gui.illum.top.value":{"visible":1,"value":100},' \
       '"gui.illum.int.type":{"visible":0,"value":0},' \
       '"gui.illum.int.value":{"visible":0,"value":50},' \
       '"gui.spCO2":{"visible":0,"value":800},' \
       '"gui.fogging.cap":{"visible":0,"value":0},' \
       '"gui.fogging.duration":{"visible":0,"value":2},' \
       '"gui.fogging.interval":{"visible":0,"value":60},' \
       '"gui.forcedvent.flow":{"visible":0,"value":"0"},' \
       '"gui.soilcooling.enabled":{"visible":0,"value":0},' \
       '"gui.soilcooling.setpoint":{"visible":0,"value":15},' \
       '"gui.leakage":{"visible":0,"value":0.1},' \
       '"gui.pipecount":{"visible":0,"value":1.25},' \
       '"gui.pipediam":{"visible":0,"value":51},' \
       '"gui.CO2dosecap":{"visible":0,"value":180},' \
       '"comp1.Balance.Soil":{"visible":0,"value":""},' \
       '"comp1.Balance.Illum":{"visible":0,"value":""},' \
       '"comp1.Balance.Balance":{"visible":0,"value":""},' \
       '"comp1.Balance.Convection":{"visible":0,"value":""},' \
       '"comp1.Balance.Latent":{"visible":0,"value":""},' \
       '"comp1.Balance.AbsSwr":{"visible":0,"value":""},' \
       '"comp1.Balance.RadLWR":{"visible":0,"value":""},' \
       '"comp1.Balance.Heating":{"visible":0,"value":""},' \
       '"label.Balance":{"visible":0,"value":""},' \
       '"comp1.LtoH2OCovdo":{"visible":0,"value":8},' \
       '"comp1.H2OCovdo.Wet":{"visible":0,"value":""},' \
       '"comp1.HFlrAir":{"visible":0,"value":-6.9},' \
       '"comp1.TFlr":{"visible":1,"value":"15"},' \
       '"comp1.RScr1Cov":{"visible":0,"value":"-"},' \
       '"comp1.RScr2Cov":{"visible":0,"value":"-"},' \
       '"comp1.RScr3Cov":{"visible":0,"value":"-"},' \
       '"comp1.TCov":{"visible":1,"value":19.6},' \
       '"common.H2Oout":{"visible":0,"value":"6.9"},' \
       '"common.RHout":{"visible":1,"value":40},' \
       '"common.Tout":{"visible":1,"value":"20"},' \
       '"common.Windsp":{"visible":1,"value":"4"},' \
       '"comp1.Flr.Info":{"visible":0,"value":""},' \
       '"comp1.HCovOut":{"visible":1,"value":-3.2},' \
       '"comp1.LtoH2OScr1do":{"visible":0,"value":""},' \
       '"comp1.LtoH2OScr2do":{"visible":0,"value":""},' \
       '"comp1.LtoH2OScr3do":{"visible":0,"value":""},' \
       '"comp1.RCovSky":{"visible":1,"value":51.5},' \
       '"comp1.Greenhouse.Uvalue":{"visible":1,"value":"0.0"},' \
       '"comp1.McAirCan2":{"visible":0,"value":0},' \
       '"comp1.H2OCan2up.Wet":{"visible":0,"value":""},' \
       '"comp1.Can2.VPD":{"visible":0,"value":0.241},' \
       '"comp1.LfromCan2":{"visible":0,"value":5.2},' \
       '"comp1.Can2.PAR":{"visible":0,"value":""},' \
       '"comp1.TCan2":{"visible":0,"value":15.7},' \
       '"comp1.MvTranspCan2":{"visible":0,"value":8},' \
       '"label.Layer3":{"visible":0,"value":""},' \
       '"comp1.H2OAir":{"visible":0,"value":11.5},' \
       '"comp1.Air.Dewpoint":{"visible":0,"value":13.5},' \
       '"comp1.Air.Enthalpy_kg":{"visible":0,"value":""},' \
       '"comp1.Air.DX":{"visible":0,"value":3.1},' \
       '"comp1.Cov.TrHemPAR":{"visible":0,"value":83},' \
       '"comp1.H2OScr1do.Wet":{"visible":0,"value":""},' \
       '"comp1.H2OScr2do.Wet":{"visible":0,"value":""},' \
       '"comp1.H2OScr3do.Wet":{"visible":0,"value":""},' \
       '"comp1.Cov.Info":{"visible":1,"value":"Helder\r\nThem PAR: 74.0%\r\nThem NIR: 75.2%\r\nThem FIR: 0.0%\r\nEmissiecoeff: 0.89"},' \
       '"comp1.McConAir":{"visible":1,"value":0},' \
       '"comp1.McAirCan1":{"visible":0,"value":0},' \
       '"comp1.H2OCan1up.Wet":{"visible":0,"value":""},' \
       '"comp1.Can1.VPD":{"visible":0,"value":0.223},' \
       '"comp1.LfromCan1":{"visible":0,"value":4.8},' \
       '"comp1.Can1.PAR":{"visible":0,"value":""},' \
       '"comp1.TCan1":{"visible":0,"value":15.6},' \
       '"comp1.MvTranspCan1":{"visible":0,"value":7},' \
       '"label.Layer2":{"visible":0,"value":""},' \
       '"common.Tsky":{"visible":1,"value":8.9},' \
       '"comp1.Out.Enthalpy_kg":{"visible":0,"value":""},' \
       '"comp1.Cov.TrDirPAR":{"visible":0,"value":81.8},' \
       '"comp1.McAirCan0":{"visible":0,"value":0},' \
       '"comp1.H2OCan0up.Wet":{"visible":0,"value":""},' \
       '"comp1.Can0.VPD":{"visible":0,"value":0.192},' \
       '"comp1.LfromCan0":{"visible":0,"value":4.2},' \
       '"comp1.Can0.PAR":{"visible":0,"value":""},' \
       '"comp1.TCan0":{"visible":0,"value":15.3},' \
       '"comp1.MvTranspCan0":{"visible":0,"value":6.2},' \
       '"label.Layer1":{"visible":0,"value":""},' \
       '"comp1.Tscr1":{"visible":0,"value":"-"},' \
       '"comp1.Tscr2":{"visible":0,"value":"-"},' \
       '"comp1.Tscr3":{"visible":0,"value":"-"},' \
       '"comp1.Air.ppm":{"visible":1,"value":347},' \
       '"comp1.Air.RH":{"visible":1,"value":85},' \
       '"comp1.TAir":{"visible":1,"value":22.7},' \
       '"comp1.Crop.Wet":{"visible":0,"value":""},' \
       '"comp1.Crop.SWRabs":{"visible":0,"value":"347.9"},' \
       '"comp1.Crop.Tavg":{"visible":1,"value":""},' \
       '"comp1.PARsensor.Above":{"visible":1,"value":""},' \
       '"comp1.Flr.PAR":{"visible":0,"value":""},' \
       '"comp1.Crop.GrossPhot":{"visible":0,"value":0},' \
       '"comp1.Crop.Latent":{"visible":0,"value":"223.1"},' \
       '"comp1.Photosynthesis.MaintResp":{"visible":0,"value":""},' \
       '"comp1.Photosynthesis.GrowthResp":{"visible":0,"value":""},' \
       '"comp1.Crop.Transp":{"visible":1,"value":209},' \
       '"label.Crop":{"visible":1,"value":""},' \
       '"comp1.Scr1Pos":{"visible":0,"value":""},' \
       '"comp1.Scr2Pos":{"visible":0,"value":""},' \
       '"comp1.Scr3Pos":{"visible":0,"value":""},' \
       '"common.SunSet":{"visible":0,"value":""},' \
       '"common.SunRise":{"visible":0,"value":""},' \
       '"comp1.Greenhouse.McInsOut":{"visible":0,"value":""},' \
       '"comp1.Greenhouse.HInsOut":{"visible":0,"value":""},' \
       '"comp1.Greenhouse.LatInsOut":{"visible":0,"value":"212.4"},' \
       '"comp1.Ventilation.Vent":{"visible":1,"value":"392.2"},' \
       '"comp1.Scr1.Info":{"visible":1,"value":"Diffuus\r\nThem PAR: 73.2%\r\nThem NIR: 74.0%\r\nThem FIR: 35.0%\r\nEmissiecoeff: 0.44"},' \
       '"comp1.Scr2.Info":{"visible":0,"value":""},' \
       '"comp1.Scr3.Info":{"visible":0,"value":""},' \
       '"comp1.Greenhouse.MvInsOut":{"visible":0,"value":""},' \
       '"label.Ventilation":{"visible":1,"value":""},' \
       '"comp1.MvFogAir":{"visible":0,"value":""},' \
       '"comp1.HFogAir":{"visible":0,"value":""},' \
       '"common.Azimuth":{"visible":0,"value":92.5},' \
       '"common.Elevation":{"visible":0,"value":30.4},' \
       '"comp1.ConPipes.TSupPipe1":{"visible":1,"value":"24.4"},' \
       '"comp1.ConPipes.TRetPipe1":{"visible":0,"value":""},' \
       '"comp1.Tpipe1.NetFlux":{"visible":0,"value":""},' \
       '"comp1.PARsensor.Transm":{"visible":1,"value":""},' \
       '"comp1.Pipe1.Info":{"visible":0,"value":""},' \
       '"comp1.H2OTop":{"visible":0,"value":"6.1"},' \
       '"comp1.Top.ppm":{"visible":0,"value":""},' \
       '"comp1.Top.Enthalpy_kg":{"visible":0,"value":""},' \
       '"comp1.Top.RH":{"visible":0,"value":""},' \
       '"comp1.TTop":{"visible":0,"value":""},' \
       '"comp1.Lmp1.Info":{"visible":1,"value":""},' \
       '"comp1.MVdehumOutAir":{"visible":0,"value":""},' \
       '"comp1.Cov.SWRup":{"visible":1,"value":"621"},' \
       '"common.Idiff":{"visible":1,"value":350},' \
       '"common.Iglob":{"visible":1,"value":"500"},' \
       '"comp1.NetRadSensor.NetRad":{"visible":0,"value":""},' \
       '"comp1.HLmp1Air":{"visible":0,"value":"-"},' \
       '"comp1.Lmp1.ActSWR":{"visible":1,"value":"-"},' \
       '"comp1.Tlmp1":{"visible":0,"value":""},' \
       '"comp1.WinLee":{"visible":1,"value":"30"},' \
       '"comp1.WinWnd":{"visible":1,"value":"0"},' \
       '"gui.transpFactor":{"visible":0,"value":1},' \
       '"gui.CO2dose":{"visible":1,"value":"0"},' \
       '"gui.fogging.dose":{"visible":0,"value":"0"},' \
       '"comp1.H2OCovdo":{"visible":0,"value":"wet"},' \
       '"comp1.LAI":{"visible":1,"value":""},' \
       '"comp1.Crop.Biomass":{"visible":1,"value":3.8},' \
       '"comp1.Crop.Maint":{"visible":0,"value":0.4},' \
       '"comp1.H2OScr1do":{"visible":0,"value":"dry"},' \
       '"comp1.H2OScr2do":{"visible":0,"value":"dry"},' \
       '"comp1.H2OScr3do":{"visible":0,"value":"dry"},' \
       '"comp1.Out.Enthalpy":{"visible":0,"value":"34.7"},' \
       '"comp1.Flr.uMol":{"visible":1,"value":""},' \
       '"comp1.Air.Enthalpy":{"visible":0,"value":"110.8"},' \
       '"comp1.LfromCan3":{"visible":0,"value":5.3},' \
       '"comp1.McAirCan3":{"visible":0,"value":0},' \
       '"comp1.H2OCan1up":{"visible":0,"value":"dry"},' \
       '"comp1.H2OCan2up":{"visible":0,"value":"dry"},' \
       '"comp1.H2OCan3up":{"visible":0,"value":"dry"},' \
       '"comp1.H2OCan0up":{"visible":0,"value":"dry"},' \
       '"comp1.Can0.uMol":{"visible":1,"value":""},' \
       '"comp1.Can1.uMol":{"visible":1,"value":""},' \
       '"comp1.Can2.uMol":{"visible":1,"value":""},' \
       '"comp1.Can3.uMol":{"visible":1,"value":""},' \
       '"comp1.PConPipe1":{"visible":1,"value":""},' \
       '"comp1.Can3.VPD":{"visible":0,"value":0.25},' \
       '"comp1.Top.Enthalpy":{"visible":0,"value":"33.6"},' \
       '"comp1.MvTranspCan3":{"visible":0,"value":8},' \
       '"comp1.TCan3":{"visible":0,"value":15.8},' \
       '"comp1.Crop.T":{"visible":0,"value":""},' \
       '"comp1.TPipe1":{"visible":1,"value":true},' \
       '"comp1.Cov.uMol":{"visible":1,"value":""},' \
       '"comp1.Lmp1.SWR":{"visible":0,"value":""},' \
       '"comp1.Cov.PARup":{"visible":1,"value":0},' \
       '"comp1.Can0.PARup":{"visible":0,"value":178},' \
       '"comp1.Can1.PARup":{"visible":0,"value":""},' \
       '"comp1.Can2.PARup":{"visible":0,"value":""},' \
       '"comp1.Can3.PARup":{"visible":0,"value":""},' \
       '"comp1.Flr.PARup":{"visible":0,"value":""},' \
       '"gui.forcedvent.capacity":{"visible":0,"value":0},' \
       '"comp1.Tnet1":{"visible":1,"value":26.7},' \
       '"comp1.Net1.Info":{"visible":0,"value":"Aantal: 1.25/m2\r\nDiameter: 51 mm\r\n"},' \
       '"comp1.PConNet1":{"visible":1,"value":"0.0"},' \
       '"gui.kpVent":{"visible":0,"value":"6"},' \
       '"gui.transpFactorCan0":{"visible":0,"value":"1"},' \
       '"gui.transpFactorCan1":{"visible":0,"value":1},' \
       '"gui.transpFactorCan2":{"visible":0,"value":1},' \
       '"gui.transpFactorCan3":{"visible":0,"value":1},' \
       '"comp1.Lmp1.NIR":{"visible":0,"value":"-"},' \
       '"comp1.Lmp1.PAR":{"visible":1,"value":"-"},' \
       '"comp1.ConPipe.Uvalue":{"visible":1,"value":6.1},' \
       '"gui.WinLeeMax":{"visible":1,"value":"100"},' \
       '"gui.WinWndMax":{"visible":1,"value":"100"},' \
       '"comp1.Lmp2.Info":{"visible":0,"value":""},' \
       '"comp1.HNet1Air":{"visible":0,"value":3.7},' \
       '"comp1.Ventilation.VentVoud":{"visible":1,"value":3.1},' \
       '"gui.TFlr":{"visible":0,"value":15},' \
       '"comp1.Cov.PARupUmol":{"visible":1,"value":224},' \
       '"comp1.Can0.PARupUmol":{"visible":1,"value":""},' \
       '"comp1.Can1.PARupUmol":{"visible":1,"value":""},' \
       '"comp1.Can2.PARupUmol":{"visible":1,"value":""},' \
       '"comp1.Can3.PARupUmol":{"visible":1,"value":""},' \
       '"comp1.Flr.PARupUmol":{"visible":0,"value":""},' \
       '"comp1.McAirOut":{"visible":0,"value":0.4},' \
       '"comp1.HAirOut":{"visible":1,"value":19.2},' \
       '"comp1.MvAirOut":{"visible":0,"value":21},' \
       '"comp1.Crop.LAI":{"visible":1,"value":3},' \
       '"common.Idir":{"visible":1,"value":150},' \
       '"gui.cooling.p":{"visible":1,"value":0},' \
       '"gui.controlHeating":{"visible":1,"value":1},' \
       '"gui.tpipe":{"visible":1,"value":"10"},' \
       '"comp1.PNet1Air":{"visible":1,"value":360.4},' \
       '"comp1.Cov.uMolUp":{"visible":1,"value":"0"},' \
       '"comp1.Can0.uMolUp":{"visible":1,"value":"100"},' \
       '"comp1.Can1.uMolUp":{"visible":1,"value":"56"},' \
       '"comp1.Can2.uMolUp":{"visible":1,"value":"31"},' \
       '"comp1.Can3.uMolUp":{"visible":1,"value":"17"},' \
       '"comp1.Flr.uMolUp":{"visible":1,"value":"9"},' \
       '"comp1.Can3.PAR":{"visible":1,"value":""},' \
       '"common.ConBoiler.Power":{"visible":1,"value":""},' \
       '"comp1.Pyrgeometer.NetRad":{"visible":1,"value":""},' \
       '"comp1.Kassim.Soil":{"visible":1,"value":""},' \
       '"comp1.Kassim.Illum":{"visible":1,"value":""},' \
       '"comp1.Kassim.Convection":{"visible":1,"value":""},' \
       '"comp1.Kassim.Latent":{"visible":1,"value":""},' \
       '"comp1.Kassim.AbsSwr":{"visible":1,"value":""},' \
       '"comp1.Kassim.RadLWR":{"visible":1,"value":""},' \
       '"comp1.Kassim.Heating":{"visible":1,"value":""},' \
       '"comp1.Kassim.CropRadiation":{"visible":1,"value":""}},' \
       '"general":{"name":"Basis","info":"Deze versie van KASSIM geeft een overzicht van de belangrijkste elementen van het kasklimaat.","language":0,"range":null,"owner":"aaea9e2c-66c6-4cf3-82c5-11a24453f4db","token":"d20df809-d90d-4084-8299-5a176df38d2d"}}'

def get_kassimoutput():
       headers = {'Content-Type': 'application/x-www-form-urlencoded'}
       requests_body = {
              "action": "run",
              "profile": data
       }
       response = requests.post(
              "https://www.digigreenhouse.wur.nl/edu/kassim2/model.aspx",
              data=requests_body, headers=headers)
       response = response.json()
       output = response["data"]
       return output

class Monitering():
    def __init__(self, kassimoutput):
        self.output = kassimoutput

    def compareoutput(self):
        para = self.getComparison("comp1.Crop.Tavg")
        pass

    def getComparison(self, parameter):
        return self.output[parameter]


if __name__ == "__main__":
    compare = Monitering(get_kassimoutput())
    compare.compareoutput()
