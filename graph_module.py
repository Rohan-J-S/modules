from matplotlib import pyplot

def plot(l_x,l_y,name,x_axis,y_axis,title):

  
    fig = pyplot.figure()
    fig.patch.set_facecolor((0,0.8,0.75,0.8))
    ax = pyplot.axes()
    pyplot.style.use("dark_background")
    ax.set_facecolor("black")
    pyplot.plot(l_x,l_y,color = (0.5,1,0,0.8),marker = "o",linewidth=3,label=name)

 
    pyplot.xlabel(x_axis)
    pyplot.ylabel(y_axis)
    pyplot.title(title)
    pyplot.legend()
    pyplot.grid(True)
    pyplot.tight_layout()
    pyplot.show()

x = [2,4,6,8,9,10]
y = [2411,2573,2958,3390,3320,3277]
name = "india"
x_axis = "day(march)"
y_axis = "cases"
title = "new covid cases"
plot(x,y,name,x_axis,y_axis,title)