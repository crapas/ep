permu_list = []

for a1 in range(10):
	print("a1 : %d" % a1)
	for a2 in range(10):
		print("a2 : %d" % a2)
		for a3 in range(10):
			for a4 in range(10):
				for a5 in range(10):
					for a6 in range(10):
						for a7 in range(10):
							for a8 in range(10):
								for a9 in range(10):
									for a10 in range(10):
											if a1 not in [a2, a3, a4, a5, a6, a7, a8, a9, a10] and a2 not in [a1, a3, a4, a5, a6, a7, a8, a9, a10] and a3 not in [a1, a2, a4, a5, a6, a7, a8, a9, a10] and a4 not in [a1, a2, a3, a5, a6, a7, a8, a9, a10] and a5 not in [a1, a2, a3, a4, a6, a7, a8, a9, a10] and a6 not in [a1, a2, a3, a4, a5, a7, a8, a9, a10] and a7 not in [a1, a2, a3, a4, a5, a6, a8, a9, a10] and a8 not in [a1, a2, a3, a4, a5, a6, a7, a9, a10] and a9 not in [a1, a2, a3, a4, a5, a6, a7, a8, a10] and a10 not in [a1, a2, a3, a4, a5, a6, a7, a8, a9]:
												num_str = ""
												for v in [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]:
													num_str += str(v)

print(permu_list)
											 
