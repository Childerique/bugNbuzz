#!/usr/bin/env python2
#from subprocess import Popen, PIPE

from liblo import *
target = Address("localhost",10000)


def touch2bug(dst, path, args):
	if dst == "ardour":
		splited = path.split("/")
		ard_path = "/" + splited[1] + "/" + splited[2] + "/" + splited[3]
		

		multiple = int(splited[4]) - 1
		
		if splited[3] == "gainabs":
			if multiple == 317:
				track == 318
			else:
				track = multiple * 8 + int(splited[5]) + multiple
			arg = float(args[0])
		
		elif splited[3] == "mute":
			track = multiple * 8 + int(splited[6]) + multiple
			arg = int(args[0])
		
#	 	Adrour      REGISTER_CALLBACK (serv, "/ardour/routes/plugin/parameter", "iiif", route_plugin_parameter);
#					params are Route-ID Plugin-Number Parameter-Number Value */
#		Touchosc	/ardour/route/plugin/parameter/[tracknumer]/[Plugin-number]/[Parameter-number] [arg]
		elif splited[3] == "plugin":
			ard_path = ard_path + splited[4]
			track = int(splited[5])
			plugin = int(splited[6])
			parm = int(splited[7])
			arg = plugin, parm, float(arg[0])
		
		return ard_path, track, arg
		
	if dst =="carla":
		splited = path.split("/")
		carla_path = "/" + splited[1] + "/" + str(int(splited[4]) - 1) + "/" + splited[2]
		arg = int(args[0])
		return carla_path, arg
		
	
	if dst =="mplayer":
		splited = path.split("/")
		if splited[1] == "play":
			tracknbr = int(args[1])
			send(target, "/deck/load","0"+tracknbr+".mp3")
			send(target, "/deck/play")
		if splited[1] == "stop":
			send(target, "/deck/stop")


if __name__ == '__main__':
	touch2bug()
