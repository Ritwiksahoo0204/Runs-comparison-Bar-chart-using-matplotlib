import matplotlib.pyplot as plt
import numpy as np
import random

#year list
years= list(range(2010,2015)) 

#taking random runs between 500 to 3000
sachin=list(random.randint(500,3000) for _ in range(5))
kohli=list(random.randint(500,3000) for _ in range(5))
sehwag=list(random.randint(500,3000) for _ in range(5))

# taking years as index
x=np.arange(len(years))

# setting the bar width
width=0.25

# ploting the data
plt.bar(x-width,sachin,width=width,label="Sachin",color="skyblue") #sachin's data
plt.bar(x,kohli,width=width,label="Kohli",color="green") # kohli's data
plt.bar(x+width,sehwag,width=width,label="Sehwag",color="red") # sehwag's Data

#set axis label title
plt.xlabel("Years")
plt.ylabel("Runs")
plt.title("Runs Comparison")

# adding legend with title
plt.legend(title="Players")

#adding actual years instate of index
plt.xticks(x,years)

# Adjust layout
plt.tight_layout()

#show the barchart
plt.show()
