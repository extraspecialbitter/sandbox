pburl = 'https://www.powerball.com/api/v1/numbers/powerball/recent10?_format=json'

int[] my_raw_numbers = {1, 8, 16, 28, 44, 8}
int[] my_numbers = Arrays.copyOfRange(my_raw_numbers, 0, 5)
int[] my_powerball = my_raw_numbers[5]
matches = 0
pb_matches = 0


