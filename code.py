## Coded by a small group at CVM - www.cedarvalleymakers.org


from adafruit_circuitplayground.express import cpx
mspeed = 15 # change between 10 - 100 increase for faster mouse speed

while True:
switchStatus = cpx.switch
if switchStatus == True:
pixel = [0,1,2,3,4,5,6,7,8,9]
for i in pixel:
cpx.pixels[i] = (0, 30, 0)

x, y, z = cpx.acceleration
xrange = round(x*15) # muliply and round to turn float into a integer usable
#by mouse move.
yrange = round(y*15) # decrease
zrange = z

#reverses x moves
if xrange < 0:
xrange = xrange * -1

elif xrange > 0:
xrange = xrange * -1

print(xrange, yrange, zrange)
m.move(xrange,yrange)
time.sleep(.01) # number determines sample rate and effects smoothness
# of mousemove

else:  ## when switch state False, turn pixels red
print("false")
pixel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in pixel:
cpx.pixels[i] = (30, 0, 0)
