This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Name: Rachel Moore
Instructor: Jenn Cross
ES 2 Project 2

There are 3 files: NearestNeighborClassification.py, KMeansClustering_functions.py, and 
KMeansClustering_driver.py. NearestNeighbor includes all the code for step 2 and 3. KMeansClustering_functions
includes all necessary code to run step 4. KMeansClustering_driver provides only the functions to call. 

To run NearestNeighborClassification.py, you have to choose a k value at the bottom of 
of the main script where it calls the function kNearestNeighborClassifier (k value currently
set at 3). If you just want to run nearest neighbor, not k nearest neighbor, you can comment 
out where I call kNearestNeighborClassifier at the bottom of main script. 
KMeansClustering is all set to run, but if you want to change K (currently set at 2), 
you can change it in the main script where it calls the select function.

If you run each file, you will see my results appear in the console and the variable 
explorer. Noteworthy variables in NearestNeighbor are: nearest_class, and mean (for
k nearest neighbor). Important variables in the KMeansClustering file are: newCentroids
and newAssignments.

NearestNeighbor functions from Jenn's starter code:
graphData - 3 arguments: glucose, hemoglobin, classification
    function graphs the data from the ckd file. no return value

NearestNeighbor custom functions: 
normalizeData - 3 arguments: glucose, hemoglobin, classification
    function alters data so it is on a scale of 0 to 1. Returns the scaled values, 
    glucose_scaled and hemoglobin_scaled.
createTestCase - 0 arguments
    function generates a random data point. returns the data point newglucose, newhemoglobin.
calculateDistanceArray - 4 arguments: newglucose, newhemoglobin, glucose, hemoglobin
    function calculates distances between the test case and all data points. returns
    an array of these distances.
nearestNeighborClassifier - 5 arguments: newglucose, newhemoglobin, glucose, hemoglobin, classification
    function identifies the class of the nearest data point to the test case. returns 
    the class, nearest_class.
kNearestNeighborClassifier - 6 arguments: k, newglucose, newhemoglobin, glucose, hemoglobin, classification
    function identifies the k number of nearest data points to the test case, identifies their
    classes, finds the mean of the classes, and returns the class depending on if the mean is 
    closer to 0 or 1. returns the mean classification.


KMeans functions from Jenn's sample/starter code:
select - 1 argument: K
    function creates K number of random centroids, return value is a K by 2 array
assign - 3 arguments: centroids, hemoglobin, glucose
    function assigns data points to a class depending on the random centroid it is closest
    to. Return value is the list of assignments.
graphingKMeans - 4 arguments: glucose, hemoglobin, assignment, centroids
    function graphs the clustered data, displaying the centroids. no return value.
    
Custom KMeans functions:
update - 4 arguments: centroids, assignments, hemoglobin, glucose
    function updates the centroids to be more imbedded in densely populated data. 
    return value is an array of the coordinates of the newCentroids.
iterate - 0 arguments
    function iterates between assign and update functions to get the most accurate 
    centroid locations. return value are the iterated newCentroids.
classify - 3 arguments: newCentroids, hemoglobin, glucose
    function creates a new list of assignments from the newCentroid locations.
    return value is the list of newAssignments.