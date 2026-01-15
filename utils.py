def normalize_rgba(red: int, green: int, blue: int, alpha: int= 1) -> list[float]:
	red_norm = red / 255
	green_norm = green / 255
	blue_norm = blue / 255
	
	rgba_list = [red_norm, green_norm, blue_norm, alpha]
	output = [float(number) for number in rgba_list]

	return output

