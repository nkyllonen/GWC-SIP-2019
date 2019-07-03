def main():
	while True:
		do_macarena()

def do_macarena():
	raise_hands()
	flip_hands()
	cross_arms()
	# etc....

def raise_hands():
	# code for how to raise hands
	extend_arms_straight()
	flip_hands()

def flip_hands():
	keep_arms_out()
	if palms_down:
		flip_palms_up()
	else:
		flip_palms_down()

def cross_arms():
	place_left_palm_on_right_shoulder()
	place_right_palm_on_left_shoulder()

if __name__ == "__main__":
	main()