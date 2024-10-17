import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def load_points(file_path):
    points = []
    
    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.strip().strip('[]').split()
            pair = [float(numbers[0]), float(numbers[1])]
            points.append(pair)
    
    return np.array(points)

def distance(point, center):
    p_x = point[0]
    p_y = point[1]
    c_x = center[0]
    c_y = center[1]
    return np.sqrt((p_x - c_x)**2 + (p_y - c_y)**2)

def draw(cl_points, clusters, k):
    matplotlib.use('TkAgg')
    for cl in cl_points:
        plt.scatter(cl[:, 0], cl[:, 1])
    plt.scatter(clusters[:, 0], clusters[:, 1], marker="*", c = range(k))
    plt.show()

def calc_mean(points):
    x = np.sum(points[:, 0])/ (points[:, 0].size)
    y = np.sum(points[:, 1])/ (points[:, 1].size)

    return np.array([x, y])

def calc_variation(points, mean):
    sum_x = np.sum((points[:, 0] - mean[0])**2)
    variation_x = 1 / points[:, 0].size * sum_x
    
    sum_y = np.sum((points[:, 1] - mean[1])**2)
    variation_y = 1 / points[:, 1].size * sum_y
    
    return variation_x + variation_y

def distribute_points(points, clusters, k):
    cluster_points = [[] for _ in range(k)]
    for point in points:
        distances = [distance(point, cluster) for cluster in clusters]
        i = np.argmin(distances)
        cluster_points[i].append(np.array([point[0], point[1]]))

    cluster_points = [np.array(cluster) for cluster in cluster_points]
    return cluster_points

def clustering(path, k):
    points = load_points(path)
    min_x, max_x = np.min(points[:, 0]), np.max(points[:, 0])
    min_y, max_y = np.min(points[:, 1]), np.max(points[:, 1])

    clusters = []
    for _ in range(k):
        x = np.random.uniform(min_x, max_x)
        y = np.random.uniform(min_y, max_y)
        clusters.append(np.array([x, y]))
    
    clusters = np.array(clusters)
    changed = False

    while not changed:
        cluster_points = distribute_points(points, clusters, k)

        new_clusters = [[] for _ in range(k)]
        new_clusters = [calc_mean(cl_p) for cl_p in cluster_points]
        new_clusters = np.array(new_clusters)

        if (clusters == new_clusters).all():
            break
        else:
            clusters = new_clusters

    draw(cluster_points, new_clusters, k)

    variation = 0
    for cl_p in cluster_points:
        variation += calc_variation(cl_p, calc_mean(cl_p))
    print(variation)