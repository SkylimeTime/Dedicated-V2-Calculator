from tkinter import *

'''VERSION 0

CONTRIBUTORS:
- Vhou-Atroph
'''

#Variables
global lured
global organic
global sndDmg
global thrwDmg
global sqrtDmgg
global drpDmg
lured=0
organic=0
sndDmg=0
thrwDmg=0
sqrtDmg=0
drpDmg=0

#Window
global window
window=Tk()
window.title("Toontown Damage Calculator")
icon=PhotoImage(file="img/whole-cream-pie.png")
window.iconphoto(True, icon)

#Columns
col1=Frame(window) #Main content of the calculator
col2=Frame(window) #Will be used for calculation history

#Toggles
togBtns=Frame(col1)
orgBtn=Button(togBtns,text='Toggle Organic')
lurChk=Checkbutton(togBtns,text='Cog lured',variable=lured,onvalue=1,offvalue=0)
clrBtn=Button(togBtns,text='Clear Inputs')
clcBtn=Button(togBtns,text='Calculate',font=('Arial',10,'bold'))
emptLbl=Label(togBtns)

#The Gags
gagFrame=Frame(col1)
#Sound
sndFrame=Frame(gagFrame)
bHornImg=PhotoImage(file='img/bike-horn.png')
bHorn=Button(sndFrame,image=bHornImg)
whistleImg=PhotoImage(file='img/whistle.png')
whistle=Button(sndFrame,image=whistleImg)
bugleImg=PhotoImage(file='img/bugle.png')
bugle=Button(sndFrame,image=bugleImg)
aoogahImg=PhotoImage(file='img/aoogah.png')
aoogah=Button(sndFrame,image=aoogahImg)
eTrunkImg=PhotoImage(file='img/elephant-trunk.png')
eTrunk=Button(sndFrame,image=eTrunkImg)
fHornImg=PhotoImage(file='img/fog-horn.png')
fHorn=Button(sndFrame,image=fHornImg)
oSingerImg=PhotoImage(file='img/opera-singer.png')
oSinger=Button(sndFrame,image=oSingerImg)
#Throw
thrwFrame=Frame(gagFrame)
cCakeImg=PhotoImage(file='img/cupcake.png')
cCake=Button(thrwFrame,image=cCakeImg)
fPSliceImg=PhotoImage(file='img/fruit-pie-slice.png')
fPSlice=Button(thrwFrame,image=fPSliceImg)
cPSliceImg=PhotoImage(file='img/cream-pie-slice.png')
cPSlice=Button(thrwFrame,image=cPSliceImg)
wFPieImg=PhotoImage(file='img/whole-fruit-pie.png')
wFPie=Button(thrwFrame,image=wFPieImg)
wCPieImg=PhotoImage(file='img/whole-cream-pie.png')
wCPie=Button(thrwFrame,image=wCPieImg)
bCakeImg=PhotoImage(file='img/birthday-cake.png')
bCake=Button(thrwFrame,image=bCakeImg)
wCakeImg=PhotoImage(file='img/wedding-cake.png')
wCake=Button(thrwFrame,image=wCakeImg)
#Squirt
sqrtFrame=Frame(gagFrame)
sFlowerImg=PhotoImage(file='img/squirting-flower.png')
sFlower=Button(sqrtFrame,image=sFlowerImg)
gWaterImg=PhotoImage(file='img/glass-of-water.png')
gWater=Button(sqrtFrame,image=gWaterImg)
sGunImg=PhotoImage(file='img/squirt-gun.png')
sGun=Button(sqrtFrame,image=sGunImg)
sBottleImg=PhotoImage(file='img/seltzer-bottle.png')
sBottle=Button(sqrtFrame,image=sBottleImg)
fHoseImg=PhotoImage(file='img/fire-hose.png')
fHose=Button(sqrtFrame,image=fHoseImg)
sCloudImg=PhotoImage(file='img/storm-cloud.png')
sCloud=Button(sqrtFrame,image=sCloudImg)
geyserImg=PhotoImage(file='img/geyser.png')
geyser=Button(sqrtFrame,image=geyserImg)
#Drop
drpFrame=Frame(gagFrame)
fPotImg=PhotoImage(file='img/flower-pot.png')
fPot=Button(drpFrame,image=fPotImg)
sBagImg=PhotoImage(file='img/sandbag.png')
sBag=Button(drpFrame,image=sBagImg)
anvilImg=PhotoImage(file='img/anvil.png')
anvil=Button(drpFrame,image=fHoseImg)
bWeightImg=PhotoImage(file='img/big-weight.png')
bWeight=Button(drpFrame,image=bWeightImg)
safeImg=PhotoImage(file='img/safe.png')
safe=Button(drpFrame,image=safeImg)
gPianoImg=PhotoImage(file='img/grand-piano.png')
gPiano=Button(drpFrame,image=gPianoImg)
tTanicImg=PhotoImage(file='img/toontanic.png')
tTanic=Button(drpFrame,image=tTanicImg)
#Button list - used for mass configuring the gag buttons
gagBtns=(bHorn,whistle,bugle,aoogah,eTrunk,fHorn,oSinger,cCake,fPSlice,cPSlice,wFPie,wCPie,bCake,wCake,sFlower,gWater,sGun,sBottle,fHose,sCloud,geyser,fPot,sBag,anvil,bWeight,safe,gPiano,tTanic)

#Toggle organic functions
def togOrgOff():
  organic=0
  print("Gags in calculations will no longer be organic!")
  orgBtn.configure(command=togOrgOn)
  for i in gagBtns:
    i.configure(bg='SystemButtonFace')
def togOrgOn():
  organic=1
  print("Gags in calculations will now be organic!")
  orgBtn.configure(command=togOrgOff)
  for i in gagBtns:
    i.configure(bg='darkorange')
orgBtn.configure(command=togOrgOn)

#Geometry - Main Columns
col1.grid(column=0,row=0,padx=10) #In retrospect I should have used 0 for the column name too, but it doesn't matter *that* much.
col2.grid(column=1,row=0)

#Geometry - Toggles
togBtns.grid(column=0,row=1,pady=10)
lurChk.grid(column=0,row=0,padx=5)
orgBtn.grid(column=1,row=0,padx=5)
clrBtn.grid(column=2,row=0,padx=5)
clcBtn.grid(column=4,row=0,padx=5)
emptLbl.grid(column=3,row=0,padx=15)

#Geometry - Gags
gagFrame.grid(column=0,row=2,pady=10)
#Sound
sndFrame.grid(column=0,row=0,pady=1)
bHorn.grid(column=0,row=0)
whistle.grid(column=1,row=0)
bugle.grid(column=2,row=0)
aoogah.grid(column=3,row=0)
eTrunk.grid(column=4,row=0)
fHorn.grid(column=5,row=0)
oSinger.grid(column=6,row=0)
#Throw
thrwFrame.grid(column=0,row=1,pady=1)
cCake.grid(column=0,row=0)
fPSlice.grid(column=1,row=0)
cPSlice.grid(column=2,row=0)
wFPie.grid(column=3,row=0)
wCPie.grid(column=4,row=0)
bCake.grid(column=5,row=0)
wCake.grid(column=6,row=0)
#Squirt
sqrtFrame.grid(column=0,row=2,pady=1)
sFlower.grid(column=0,row=0)
gWater.grid(column=1,row=0)
sGun.grid(column=2,row=0)
sBottle.grid(column=3,row=0)
fHose.grid(column=4,row=0)
sCloud.grid(column=5,row=0)
geyser.grid(column=6,row=0)
#Drop
drpFrame.grid(column=0,row=3,pady=1)
fPot.grid(column=0,row=0)
sBag.grid(column=1,row=0)
anvil.grid(column=2,row=0)
bWeight.grid(column=3,row=0)
safe.grid(column=4,row=0)
gPiano.grid(column=5,row=0)
tTanic.grid(column=6,row=0)

#Run
window.mainloop()