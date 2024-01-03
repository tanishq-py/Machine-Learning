import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline  only use in jupyter

# Simple Examples
x=np.arange(0,10)
y=np.arange(11,21)

#plotting using matplotlib 
#plt scatter
plt.scatter(x,y,c='g')   ## Scatter plot with green color
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Graph in 2D')
plt.savefig('Test.png')

y=x*x
# plt plot
plt.plot(x,y,'r*',linestyle='dashed',linewidth=2, markersize=12)  #plot style is set to red asterisks ('r*'),linestyle is set to dashed,linewidth is set to 2,markersize is set to 12.
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('2d Diagram')  

# Creating Subplots
plt.subplot(2,2,1)
plt.plot(x,y,'r--')
plt.subplot(2,2,2)
plt.plot(x,y,'g*--')
plt.subplot(2,2,3)
plt.plot(x,y,'bo')
plt.subplot(2,2,4)
plt.plot(x,y,'go')

x = np.arange(1,11) 
y = 3 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()

# Compute the x and y coordinates for points on a sine curve 
# Generate x values from 0 to 4*pi with a step of 0.1
x = np.arange(0, 4 * np.pi, 0.1)
# Calculate corresponding y values using the sine function
y = np.sin(x)
# Set the title of the plot
plt.title("Sine Wave Form")
# Plot the points using Matplotlib
plt.plot(x, y)
# Display the plot
plt.show()

#Subplot()
# Compute the x and y coordinates for points on sine and cosine curves 
x = np.arange(0, 5 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
   
# Set up a subplot grid that has height 2 and width 1, 
# and set the first such subplot as active. 
plt.subplot(2, 1, 1)
   
# Make the first plot 
plt.plot(x, y_sin,'r--') 
plt.title('Sine')  
   
# Set the second subplot as active, and make the second plot. 
plt.subplot(2, 1, 2) 
plt.plot(x, y_cos,'g--') 
plt.title('Cosine')  
   
# Show the figure. 
plt.show()


# Bar plot
x = [2,8,10] 
y = [11,16,9]  
x2 = [3,9,11] 
y2 = [6,15,7] 
plt.bar(x, y) 
plt.bar(x2, y2, color = 'g') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  
plt.show()


#Histograms
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
plt.hist(a) 
plt.title("histogram") 
plt.show()


#Box Plot using Matplotlib
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
# rectangular box plot
plt.boxplot(data,vert=True,patch_artist=False); 


# Pie Chart
# Data to plot
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.4, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False)
plt.axis('equal')
plt.show()
