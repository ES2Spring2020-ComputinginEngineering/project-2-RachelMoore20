#Please place your FUNCTION code for step 4 here.
import NearestNeighborClassification as ncc
import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np

glucose, hemoglobin, classification = kmc.openckdfile()
meanGlucose = np.mean(glucose)
meanHemoglobin = np.mean(hemoglobin)
glucose_scaled, hemoglobin_scaled = ncc.normalizeData(glucose, hemoglobin, classification)
centroids = kmc.select(K) #choose K value
assignments = kmc.assign(centroids, hemoglobin_scaled, glucose_scaled)
newCentroids = kmc.update(centroids, assignments, hemoglobin, glucose)
kmc.iterate()
kmc.graphingKMeans(glucose, hemoglobin, assignments, newCentroids)
newAssignments = kmc.classify(newCentroids, hemoglobin, glucose)