import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from typing import List, Tuple

def load_points(file_path: str) -> np.ndarray:
    points: List[List[float]] = []
    
    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.strip().strip('[]').split()
            pair = [float(numbers[0]), float(numbers[1])]
            points.append(pair)
    
    return np.array(points)

def distance(point: np.ndarray, center: np.ndarray) -> float:
    p_x, p_y = point[0], point[1]
    c_x, c_y = center[0], center[1]
    return np.sqrt((p_x - c_x)**2 + (p_y - c_y)**2)

def draw(cl_points: List[np.ndarray], clusters: np.ndarray, k: int) -> None:
    matplotlib.use('TkAgg')
    for cl in cl_points:
        plt.scatter(cl[:, 0], cl[:, 1])
    plt.scatter(clusters[:, 0], clusters[:, 1], marker="*", c=range(k))
    plt.show()

def calc_mean(points: np.ndarray) -> np.ndarray:
    if len(points) == 0:
        return np.array([0.0, 0.0])
    x = np.sum(points[:, 0]) / points[:, 0].size
    y = np.sum(points[:, 1]) / points[:, 1].size
    return np.array([x, y])

def calc_variation(points: np.ndarray, mean: np.ndarray) -> float:
    if len(points) == 0:
        return 0.0
    sum_x = np.sum((points[:, 0] - mean[0])**2)
    variation_x = sum_x / points[:, 0].size

    sum_y = np.sum((points[:, 1] - mean[1])**2)
    variation_y = sum_y / points[:, 1].size

    return variation_x + variation_y

def distribute_points(points: np.ndarray, clusters: np.ndarray, k: int) -> List[np.ndarray]:
    cluster_points: List[List[np.ndarray]] = [[] for _ in range(k)]
    for point in points:
        distances = [distance(point, cluster) for cluster in clusters]
        i = np.argmin(distances)
        cluster_points[i].append(np.array([point[0], point[1]]))
    
    return [np.array(cluster) for cluster in cluster_points]

def clustering(path: str, k: int) -> None:
    points: np.ndarray = load_points(path)
    min_x, max_x = np.min(points[:, 0]), np.max(points[:, 0])
    min_y, max_y = np.min(points[:, 1]), np.max(points[:, 1])

    clusters: List[np.ndarray] = []
    for _ in range(k):
        x = np.random.uniform(min_x, max_x)
        y = np.random.uniform(min_y, max_y)
        clusters.append(np.array([x, y]))
    
    clusters = np.array(clusters)
    changed: bool = False

    while not changed:
        cluster_points: List[np.ndarray] = distribute_points(points, clusters, k)
        new_clusters: List[np.ndarray] = [calc_mean(cl_p) for cl_p in cluster_points]
        new_clusters = np.array(new_clusters)

        if (clusters == new_clusters).all():
            break
        else:
            clusters = new_clusters

    draw(cluster_points, new_clusters, k)

    variation: float = 0.0
    for cl_p in cluster_points:
        variation += calc_variation(cl_p, calc_mean(cl_p))
    print("Variation:", variation)
