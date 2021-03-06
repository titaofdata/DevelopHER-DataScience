# DevelopHER-DataScience
Using data science to build a scheduling solution to address food security in urban areas in PH

# Prototype

Watch the demo of the Sagana app [here](https://tinyurl.com/sagana-app-demo).


## Pitch Deck

A brief presentation on Sagana, the AI-powered food distribution web app, can be viewed at the website below:

https://winning-the-amazon-echo-dot.netlify.app/

This prototype aims to support the Development Academy of the Philippines by deploying a food distribution web app that aims to aid the following [objectives](https://www.dap.edu.ph/coe-psp/innov_initiatives/listahanan-national-household-targeting-system-for-poverty-reduction-nhts-pr/):

1) Improve the design of government social assistance programs to  **maximize the benefit of the poor**
2) To **minimize wastage of resources** by ensuring that **only those who are deserving benefit** from social protection programs and services

## Data Cleaning

Performed cleaning and profiling on Barangay Food Terminals dataset. Jupyter notebook found [here](https://colab.research.google.com/drive/1NktA7Qtx2sJSr4AMvaYc9d4zIppdOt_9?usp=sharing)

The following were the datasets I used, most of these taken from data.gov.ph

1) [National Household Targeting System for Poverty Reduction (NHTS-PR) Statistics](https://data.gov.ph/?q=dataset/national-household-targeting-system-poverty-reduction-nhts-pr-statistics)
2) [National Household Targeting System for Poverty Reduction](https://data.gov.ph/?q=dataset/national-household-targeting-system-poverty-reduction)
3) [Nutritional Status of Filipino Children and Other Population Groups](https://data.gov.ph/?q=dataset/nutritional-status-filipino-children-and-other-population-groups)
4) [Disaster Report](https://data.gov.ph/?q=dataset/disaster-report)
5) [Metro Rail Transit Line 3 - Passenger Traffic (Sundays and Holidays)](https://data.gov.ph/?q=dataset/metro-rail-transit-line-3-passenger-traffic-sundays-and-holidays)
6) [Metro Rail Transit Line 3 - Passenger Traffic (Weekdays)](https://data.gov.ph/?q=dataset/metro-rail-transit-line-3-passenger-traffic-weekdays)
7) [Metro Rail Transit Line 3 - Passenger Traffic (Monthly)](https://data.gov.ph/?q=dataset/metro-rail-transit-line-3-passenger-traffic-monthly)
8) [Metro Rail Transit Line 3 - Passenger Traffic (Daily)](https://data.gov.ph/?q=dataset/metro-rail-transit-line-3-passenger-traffic-daily)
9) [Metro Rail Transit Line 3 - Passenger Traffic (Saturdays)](https://data.gov.ph/?q=dataset/metro-rail-transit-line-3-passenger-traffic-saturdays)
10) [2017 Ridership Statistics](https://data.gov.ph/?q=dataset/2017-ridership-statistics)
11) [Barangay Food Terminals (BFTs)](https://data.gov.ph/?q=dataset/barangay-food-terminals-bfts)
12) [PSGC database](https://psa.gov.ph/classification/psgc/)

Here's some prior art search on food security ideas:

1) [Food waste is the world's dumbest problem](https://www.youtube.com/watch?v=6RlxySFrkIM)
2) [The Food Bank's Emergency Feeding Program Network](https://www.foodbankwma.org/get-help/covid-19-food-pantry-meal-program-schedule/)
3) [Vehicle Routing Problem (AI-based Solution)](https://github.com/shlok57/VehicleRoutingProblem)
4) [Vehicle Routing Problem (Genetic Algorithm-based Solution)](https://github.com/iRB-Lab/py-ga-VRPTW)
5) [The power of gender equality for food security](https://www.wfp.org/publications/power-gender-equality-food-security)


# Other possible problems to be explored with the data.gov.ph datasets 

## PROBLEM: Cebu port struggles with congestion as volumes grow
https://www.portcalls.com/cebu-port-struggles-with-congestion-as-volumes-grow/

"The congestion is “the worst we’ve [seen]” since OPASCOR began working with CIP in 1990, Page said."

"Container dwell time, meanwhile, has also grown. In 2013, dwell time was only eight days, but this almost doubled in 2014 to 14 days, then further increased to 16 days in January 2015. Page noted that 67% of containers have been at the port for more than seven days."

"Due to the limited berth space, “when vessels simultaneously arrive at Cebu port, we have a problem,” Page pointed out."

"Bunching of trucks is yet another problem. “For some reason, trucks like to come only in the afternoon,” Page mused."

## DATASET AVAILABLE: Cebu Port Authority Statistics
https://data.gov.ph/?q=dataset/cebu-port-authority-cpa-statistics-2015

## SOLUTION: Cebu Port Vessel Scheduling System

1) Minimize container dwell time
2) Minimize bunching of trucks by implementing a number/color coding system for trucks similar to the Unified Vehicular Volume Reduction Program (UVVRP)
3) Optimize use of berth space by using ML to predict best departure, arrival and buffer time for each vessel 
4) Autonotification sent to concerned parties including schedule information

## CHALLENGE: Data Quality Issues 

The dataset available at data.gov.ph is in a per month basis. In order for the Cebu Port Vessel Scheduling System to be effective, we need a dataset with granularity on a daily basis. 

## TECH STACK: Google Cloud Platform

This scheduling system can be built using Google Cloud Platform's AutoML. The predictions can be stored on Firebase. Then, a notification channel can be configured on GCP where alerts including schedule information will be sent via SMS to concerned parties. The whole Vessel Scheduling System can be deployed on the cloud thru GCP. 

In the future, IoT can even be integrated on vessels. For instance, [ultrasonic sensors](https://www.mdpi.com/1424-8220/19/23/5181/htm) can be connected to each vessel. Data from sensors can be sent to Cloud Pub/Sub in real time. Then, data creation will trigger the execution of the Vessel Scheduling System and will sent alert notif once the optimal berth location for the specific vessel has been determined.   


## Hiring Data Scientists?

Visit us at www.ftwfoundation.org
