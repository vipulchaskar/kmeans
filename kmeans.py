import matplotlib.pyplot as plt
import numpy as np
import math

# Number of features in each training example. Default of 2 for now
# 2 helps visualize data better
n = 2

# Name of input file (if in the same directory) or path
input_filename = "input.txt"

# Minimum and maximum values of input features X1 and X2.
# Helps in setting the range for random initializations.
X1_min = float('inf')
X1_max = float('-inf')
X2_min = float('inf')
X2_max = float('-inf')

# List of colour codes for each cluster. The length of this list should be <= number of clusters entered
colors = ["red", "green", "blue", "brown", "orange", "violet", "black"]

'''
Reads an input file where each line is one training example.
Each line consists of space separated values of 'n' features.
'''
def read_input_file():
	global X1_min
	global X1_max
	global X2_min
	global X2_max

	X1 = []
	X2 = []
	m = 0

	for line in open(input_filename, "r"):
		line_int = [float(x) for x in line.split()]

		# Calculate the maximum and minimum values of each feature
		if line_int[0] < X1_min:
			X1_min = line_int[0]
		if line_int[0] > X1_max:
			X1_max = line_int[0]

		if line_int[1] < X2_min:
			X2_min = line_int[1]
		if line_int[1] > X2_min:
			X2_max = line_int[1]

		X1.append(line_int[0])
		X2.append(line_int[1])
		m += 1

	return X1, X2, m


'''
Display the scatterplot of training examples before clustering.
This might help in choosing 'k', the number of clusters to form.
'''
def display_initial_plot(X1, X2):

	plt.scatter(X1, X2, color="red")
	plt.xlabel("X1")
	plt.ylabel("X2")
	plt.grid(True)
	plt.title("Before running k-means...")
	plt.show()

'''
Accept the number of clusters to create. The global list 'colors' should have
either equal to or more colors than this since each cluster is assigned a unique color.
'''
def accept_cluster_no():
	k = 0
	while k <= 0:
		k = int(input("Please enter the number of clusters : "))
		if k > len(colors):
			print "Please enter", k, "or more colors in 'colors' variable."
			exit(0)
	return k

'''
Find euclidean distance between points (x1, y1) and (x2, y2)
'''
def calculate_distance(x1, y1, x2, y2):
	return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

'''
Actual implementation of k-means
'''
def run_k_means(X1, X2, m, k):

	print "Running k-means algorithm..."

	C = [None] * m

	time_to_stop = False

	iteration = 0

	while not time_to_stop:

		# Randomly initialize cluster centres
		C1 = (X1_max - X1_min) * np.random.random_sample(k) + X1_min
		C2 = (X2_max - X2_min) * np.random.random_sample(k) + X2_min

		point_reassigned = False
		for i in range(m):

			min_dist = np.inf
			min_c = 0
			for j in range(k):
				# Calculate euclidean distance between each data point and each Cluster centre
				temp = calculate_distance(X1[i], X2[i], C1[j], C2[j])

				# Keep track of the closest cluster centre for each point
				if temp < min_dist:
					min_dist = temp
					min_c = j

			if min_c != C[i]:
				point_reassigned = True
			C[i] = min_c

		# If no points have been reassigned from one cluster centre to the other in current iteration
		# Then singularity is achieved, break out of the loop.
		if point_reassigned == False:
			time_to_stop = True
			break

		points_in_c = [0] * k
		C1_new = [0] * k
		C2_new = [0] * k

		# Find number of points in each cluster and also sum of individual feature values
		for i in range(m):
			points_in_c[C[i]] += 1

			C1_new[C[i]] += X1[i]
			C2_new[C[i]] += X2[i]

		# If some cluster doesn't get assigned any points, our random initialization failed (?),
		# Again randomly initialize and try...
		if any(elem is 0 for elem in points_in_c):
			continue

		# Calculate and assign new cluster centres based on average of the features of points in that cluster
		C1 = [C1_new[i]/points_in_c[i] for i in range(k)]
		C2 = [C2_new[i]/points_in_c[i] for i in range(k)]

		iteration += 1
		print "Iteration",iteration,"complete..."

	print "Final set of centres is : ", str(["("+str(C1[i])+","+str(C2[i])+")" for i in range(k)])
	#print "Final C is : ", str(C)

	return C, C1, C2

'''
Display the scatterplot of input data points colour coded according to cluster to which they belong.
Also display the corresponding cluster centres.
'''
def display_final_plot(X1, X2, m, C, C1, C2, k):
	# Display the points
	for i in range(m):
		plt.scatter(X1[i], X2[i], color=colors[C[i]])
	plt.xlabel("X1")
	plt.ylabel("X2")
	plt.grid(True)
	plt.title("After running k-means...")

	# Display the cluster centres
	for i in range(k):
		plt.scatter(C1[i], C2[i], c=colors[i], s=100, label="centroid", alpha = 1)
		plt.annotate('Centre-'+str(i+1), xy=(C1[i], C2[i]), xytext=(C1[i]+0.1, C2[i]+0.1))

	plt.show()

'''
Main function. Parses input file, displays initial plot, reads cluster number, runs k-means and displays
the clusters.
'''
def main():
	X1, X2, m = read_input_file()

	display_initial_plot(X1, X2)
	
	k = accept_cluster_no()
	
	C, C1, C2 = run_k_means(X1, X2, m, k)

	display_final_plot(X1, X2, m, C, C1, C2, k)


if __name__ == '__main__':
	main()
