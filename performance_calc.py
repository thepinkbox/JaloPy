from PIL import Image
from math import sin, radians

#file location can be just filename with extension if placed in designated folder
#car_height in metres
def frontal_area(file_location, car_height):
	white = (255, 255, 255)
	im = Image.open(file_location)
	pixelmap = list(im.getdata())
	size = im.size
	height_px = size[1]
	width_px = size[0]
	clear = 0 
	success = 0
	white_px = 0 
	other_px = 0
	pixelmap_final = [[pixelmap.pop() for i in range(width_px)] for j in range(height_px)]
	pixelmap = list(im.getdata())
	
	for height in range(height_px):
		for width in range(width_px):
			if pixelmap_final[height][width] == white:
				clear += 1
			if clear == width_px:
				success += 1
				clear = 0
		clear = 0
		
	car_height_px = height_px - success
	height_per_px = car_height / car_height_px
	
	for i in pixelmap:
		if i == white:
			white_px += 1
			
	other_px = (height_px * width_px) - white_px
	frontal_area = other_px * height_per_px**2
			
	with open('dump','w') as target:
		target.write(str(pixelmap))

	return frontal_area


#temp in deg C, press in hPa, rel_hum in %
def air_density(temp, rel_hum, press):
	press = press * 100
	tempk = temp + 273.15
	press_watervapor = rel_hum * 6.1078 * 10**(7.5 * temp / (237.3 + temp))
	press_dryair = press-press_watervapor
	density = (press_dryair / (287.05 * tempk)) + (press_watervapor / (461.495
			* tempk))
	return density

#frontal_area in m^2, car_vel and wind_vel in km/hr
def air_resistance(temp, rel_hum, press, file_location, car_height, drag_coeff, car_vel, wind_vel):
	air_resistance = 0.5 * air_density(temp, rel_hum, press) * frontal_area(file_location, 
					car_height) * drag_coeff * ((car_vel + wind_vel) / 3.6)**2
	return air_resistance
	
#vehicle_wt in kg
def rolling_resistance(roll_coeff, vehicle_wt):
	return roll_coeff * vehicle_wt * 9.81

#angle in degrees and vehicle_wt in kg
def gradient_resistance(incline_angle, vehicle_wt):
	return sin(radians(incline_angle)) * vehicle_wt * 9.81

#
def inertia_resistance()
	mass_equiv = 
	
		


	