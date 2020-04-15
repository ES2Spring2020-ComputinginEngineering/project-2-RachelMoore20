# Project 2
# NAME: Rachel Moore

#Please place your FUNCTION code for step 4 here.
import numpy as np
import matplotlib.pyplot as plt
import random
import NearestNeighborClassification as ncc #imports functions from other file for use in this file

# FUNCTIONS
def openckdfile():      #function opens the file containing data
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def select(K): 
    return np.random.random((K, 2)) #creates a random array of possible centroid points
    

def assign(centroids, hemoglobin, glucose): #function assigns data points to a class depending on the random centroid it is closest to
    K = centroids.shape[0]
    distances = np.zeros((K, len(hemoglobin))) #creates array of zeros
    for i in range(K): 
        g = centroids[i,1] #2nd column of array (y-value for centroid)
        h = centroids[i,0] #1st column of array (x-value for centroid)
        distances[i] = np.sqrt((hemoglobin-h)**2+(glucose-g)**2) #distance formula finds distance from centroids 
        
    assignments = np.array(np.argmin(distances, axis = 0)) #finds minimum distance  
    print(assignments) 
    return assignments #returns list of data assignments


def update(centroids, assignments, hemoglobin, glucose): # function updates the centroids to be more imbedded in densely populated data.
    K = centroids.shape[0]
    newCentroids = np.zeros((K, 2)) #creates K by 2 array of zeros 
    for i in range(K):
        newHemoglobin = np.mean(hemoglobin[assignments == i]) #finds mean of hemoglobin and glucose
        newGlucose = np.mean(glucose[assignments == i])
        newCentroids[i,1] = newGlucose #finds new centroid points depending on the means above
        newCentroids[i,0] = newHemoglobin
    
    return newCentroids #returns the new centroid coordinates
    

def iterate(): #function iterates between assign and update functions to get most accurate centroid points
    while np.all(newCentroids) != np.all(centroids): 
        assign(centroids, hemoglobin, glucose)
        update(centroids, assignments, hemoglobin, glucose)
        if np.all(newCentroids) == np.all(centroids): #most accurate centroids reached when newCentroids = centroids
            return newCentroids #returns most accurate newCentroid points


def graphingKMeans(glucose, hemoglobin, assignment, centroids): #graphs the data with the clusters color coordinated and centroids distinguishable
    plt.figure()
    for i in range(assignment.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor, markersize=8)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()  #no return value
    
def classify(newCentroids, hemoglobin, glucose): #creates a list of assignments of the data from the newCentroids
    K = newCentroids.shape[0]
    K_distances = np.zeros((K, len(hemoglobin)))
    for i in range(K):
        g = newCentroids[i,1]
        h = newCentroids[i,0]
        K_distances[i] = np.sqrt((hemoglobin-h)**2+(glucose-g)**2)
    newAssignments = np.array(np.argmin(K_distances, axis = 0))
    print(newAssignments)
    return newAssignments     #same code from assign is used but newCentroids replaces centroids, K_distances for distances, and newAssignments for assignments
                              #returns list: newAssignments

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()

# the below code plots the initial data, before clusters
plt.figure()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()

meanGlucose = np.mean(glucose)
meanHemoglobin = np.mean(hemoglobin)

glucose_scaled, hemoglobin_scaled = ncc.normalizeData(glucose, hemoglobin, classification)
centroids = select(2) #currently set to create 2 clusters/centroids
assignments = assign(centroids, hemoglobin_scaled, glucose_scaled)
newCentroids = update(centroids, assignments, hemoglobin, glucose)
iterate()
graphingKMeans(glucose, hemoglobin, assignments, newCentroids)
newAssignments = classify(newCentroids, hemoglobin, glucose)
#above code calls all functions in the desirable order