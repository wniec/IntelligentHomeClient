import sys

import Ice

import generated

communicator = Ice.initialize(sys.argv)

server0 = "tcp -h 127.0.0.2 -p 10000 -z : udp -h 127.0.0.2 -p 10000 -z"
server1 = "tcp -h 127.0.0.3 -p 10000 -z : udp -h 127.0.0.3 -p 10000 -z"
servers = (server0, server1)
server = server0

camera = communicator.stringToProxy("camera/camera:"+server)
central_heating = communicator.stringToProxy("heating/heating:"+server)
fridge = communicator.stringToProxy("fridge/fridge:"+server)
garage = communicator.stringToProxy("garage/garage:"+server)
garden_camera = communicator.stringToProxy("garden/garden:"+server)
lamp_4 = communicator.stringToProxy("lamp/4:"+server)


camera = generated.CameraPrx.checkedCast(camera)
central_heating = generated.CentralHeatingPrx.checkedCast(central_heating)
fridge = generated.FridgePrx.checkedCast(fridge)
garage = generated.GaragePrx.checkedCast(garage)
garden_camera = generated.GardenCameraPrx.checkedCast(garden_camera)
lamp_4 = generated.LampPrx.checkedCast(lamp_4)

if not camera or not central_heating or not fridge or not garage or not garden_camera or not lamp_4:
    raise RuntimeError("Invalid proxy")