word = {}
word[1] = 3 	# one
word[2] = 3		# two
word[3] = 5		# three
word[4] = 4		# four
word[5] = 4		# five
word[6] = 3		# six
word[7] = 5		# seven
word[8] = 5		# eight
word[9] = 4		# nine
word[10] = 3	# ten
word[11] = 6	# eleven
word[12] = 6	# twelve
word[13] = 8	# thirteen
word[14] = 8	# fourteen
word[15] = 7	# fifteen
word[16] = 7
word[17] = 9
word[18] = 8
word[19] = 8
word[20] = 6
word[30] = 6
word[40] = 5
word[50] = 5
word[60] = 5
word[70] = 7
word[80] = 6
word[90] = 6
word[100] = 10	# hundred and

sum_1_9 = 0
for i in range(1, 10):
	sum_1_9 += word[i]
sum_10_19 = 0
for i in range(10, 20):
	sum_10_19 += word[i]

sum_20_90_in_10 = 0
for i in range(20, 100, 10):
	sum_20_90_in_10 += word[i]

sum_1_99 = sum_1_9 + sum_10_19 + sum_20_90 * 10 + sum_1_9 * 8


