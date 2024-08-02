# Immoweb-App

I have created an app to calculate the price of a house in Belgium
I used streamlit
The regression I used was the KNeighborgs as it was the most accurate calculating the price of a house in Belgium. I did not use apartments this time.
To include the price per square meter per district, I created a dictionary with the list of districts and the price per square meter of each one. Then I added a bar (list) to choose a district because it is the main feature that determines the price of a house in Belgium, the district selected is then associated with the price per square meter and sends it to the final dictionary (thanks Antoine for your help!). I tried to implement a button for each district, but it was messy, so I found a code for list and implemented it (https://blog.streamlit.io/analyzing-real-estate-properties-with-streamlit/). For the rest of the characteristics of a house I used slide bars with the min and max calculated per each feature.

