from scipy.spatial import ConvexHull, convex_hull_plot_2d
import numpy as np
import matplotlib.pyplot as plt

# input files
debug_input_file = "debuginput9.1.txt"
task_input_file = "input.txt"
test_input_file = "bigboy8.txt"
plotting = True

# read in coordinates list of tiles to connect (tiles now called points)
with open(task_input_file, 'r') as ifp:
    lines = ifp.read().splitlines()
    points = np.array([tuple(int(num) for num in line.split(',')) for line in lines])#[(int(x), int(y), int(z) for line.split(',')) for line in lines]
print(f"Number of input points: {len(points)}")

# find the convex hull of all point (inner points will yield lower areas)
hull = ConvexHull(points)
if plotting == True:
    plt.plot(points[:, 0], points[:, 1], 'o', ms=1)
    plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
    #plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
    plt.show()

# calculate the centre of gravity of all hull points.
hull_points = points[hull.vertices, :]
centroid_location_x = np.mean([hull_points[:, 0]])
centroid_location_y = np.mean([hull_points[:, 1]])
print(f"Centre_of_gravity of hull: {centroid_location_x}, {centroid_location_y}")

#print(hull_points)

# split the hull domain into quarters by using masks, and check if all have contents:
mask_q0 = (hull_points[:, 0] >= centroid_location_x) & (hull_points[:, 1] >= centroid_location_y)
mask_q1 = (hull_points[:, 0] >= centroid_location_x) & (hull_points[:, 1] < centroid_location_y)
mask_q2 = (hull_points[:, 0] < centroid_location_x) & (hull_points[:, 1] < centroid_location_y)
mask_q3 = (hull_points[:, 0] < centroid_location_x) & (hull_points[:, 1] >= centroid_location_y)
hull_points_quarters = [hull_points[mask_q0], hull_points[mask_q1], hull_points[mask_q2], hull_points[mask_q3]]
all_quarters_exist = all(len(x)>0 for x in hull_points_quarters)
print(f"All quarters exist: {all_quarters_exist}")


all_quarters_exist = False # overriding because I think splitting by centre of gravity can give false results

# Find maximum achieveable area. Add +1 to the dimensions because we use integer wide bins as shown in the problem
if all_quarters_exist == True:
    pass
    #print(hull_points_quarters) If hull can be split in quarters, only search opposing arrays
    num_results_0_2 = len(hull_points_quarters[0]) * len(hull_points_quarters[2])
    num_results_1_3 = len(hull_points_quarters[1]) * len(hull_points_quarters[3])
    areas = np.zeros(num_results_0_2 + num_results_1_3, np.int32)
    
    # Q0 and Q2
    for i, p1 in enumerate(hull_points_quarters[0]):
        for j, p2 in enumerate(hull_points_quarters[2]):
            print(i*len(hull_points_quarters[2]) + j)
            areas[i*len(hull_points_quarters[2]) + j] = np.abs((p2[0]-p1[0]+1) * (p2[1]-p1[1]+1))
    # Q1 and Q3
    for i, p1 in enumerate(hull_points_quarters[1]):
        for j, p2 in enumerate(hull_points_quarters[3]):
            areas[i*len(hull_points_quarters[3]) + j + num_results_0_2] = np.abs((p2[0]-p1[0]+1) * (p2[1]-p1[1]+1))
else:
    areas = np.zeros((len(hull_points), len(hull_points)), np.int64)
    print(np.shape(areas))
    for i, p1 in enumerate(hull_points):
        for j, p2 in enumerate(hull_points):
            areas[i, j] = np.abs((p2[0]-p1[0]+1) * (p2[1]-p1[1]+1))

#print(areas)
print(f"The task 1 maximum area found is {np.max(areas)}")