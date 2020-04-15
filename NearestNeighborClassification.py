# PROJECT 2
# NAME: Rachel Moore

#Please put your code for Step 2 and Step 3 in this file.
import numpy as np
import matplotlib.pyplot as plt
import random

# FUNCTIONS
def openckdfile(): #function opens the file containing data
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification): #function creates an array of the data on a scale of 0 to 1
    hemoglobin_scaled = np.array((hemoglobin - h_min)/(h_max - h_min))
    glucose_scaled = np.array((glucose - g_min)/(g_max - g_min))
    return (glucose_scaled, hemoglobin_scaled) #scaled data will be easier to classify between class 1 and 0
    

def graphData(glucose, hemoglobin, classification): #function plots the unscaled data on a scatter plot
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1") #plots class 1 data
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0") #plots class 2 data
    plt.xlabel("Hemoglobin") #labels x axis as hemoglobin
    plt.ylabel("Glucose") #labels y axis as glucose

def createTestCase(): #function creates a random test case
    newhemoglobin = random.randint(0, int(h_max)) #newhemoglobin is the x-value of the test case; between 0 and the max hemoglobin
    newglucose = random.randint(0, int(g_max)) #newglucose is the y-value of the test case; between 0 and the max glucose
    return newglucose, newhemoglobin #function returns these random cordinates

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin): #function calculates the distances between the test case and the surrounding cases
    distances = np.array(np.sqrt((hemoglobin - newhemoglobin)**2 + (glucose - newglucose)**2)) #distance formula
    return distances #returns these distances as an array

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification): #function returns the classification of the nearest case to testcase
    min_index = np.argmin(distances) #finds the cases with the minimum distance between it and the testcase
    nearest_class = classification[min_index] #identifies the classification of this nearby case
    return nearest_class #returns the classification 

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification): #function plots the testcase on the original scatter plot
    graphData(glucose, hemoglobin, classification) #calls original scatter plot
    plt.plot(newhemoglobin, newglucose, 'g.', label = 'Test Case') #plots new test case
    plt.legend() #creates legend
    plt.show() #shows plot
    
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification): #identifies k nearest neighbors and returns the classification of the testcase dependent on mean
    distances = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin) #calls function to find all distances between testcase and data
    find = np.argsort(distances) #sorts the distances in increasing order (smallest distance first)
    k_distances = find[0:k] #picks out the first "k" distances from the sorted list
    k_nearest_class = classification[k_distances] #identifies the classification of these k nearest points
    mean = np.mean(k_nearest_class) #calculates the mean of the k number of classifications
    if mean > 0.5:  #if the mean of the classifications is greater than 0.5, the test case is class 1 (return value)
        return '1.0'
    else:           #if it is less than 0.5, it is class 0 (return value)
        return '0.0'
    return mean
   
# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
h_min = np.amin(hemoglobin)  #h_min through g_max identify the min and max values in the given data (used for scaling the data and generating random testcase)
h_max = np.amax(hemoglobin)
g_min = np.amin(glucose)
g_max = np.amax(glucose)
glucose_scaled, hemoglobin_scaled = normalizeData(glucose, hemoglobin, classification)
newglucose, newhemoglobin = createTestCase()
distances = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
nearest_class = nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
mean = kNearestNeighborClassifier(3, newglucose, newhemoglobin, glucose, hemoglobin, classification) #function was tested using k=3 (uses 3 nearest neighbors)
# all of the above main script is calling the functions to carry out their purposes