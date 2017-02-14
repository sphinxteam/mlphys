"""
    common

    Implement a number of functions which we will use repeatedly throughout 
    the course.
"""
from matplotlib import rc, pyplot as plt
import seaborn as sns
import numpy as np
from IPython.core.display import HTML

def initialize_figures():
    """
        initialize_figures()

        Set the common pyplot.rc paramters for the figures. This includes
        setting the font and figure size, etc.
    """
    rc('text', usetex=True)
    rc('font', family='serif')
    rc('xtick', labelsize=18)
    rc('ytick', labelsize=18)
    rc('figure', figsize=(15, 15))
    rc('patch', edgecolor='none')
    sns.set(style='white', palette='muted')
    HTML("""
    <style>
    .output_png {
        display: table-cell;
        text-align: center;
        vertical-align: middle;
    }
    </style>
    """)

def scatter_plot(x, y, labels=None, ax=None):
    """
        scatter_plot()

        Operates much like the normal scatter plot, just gives us some 
        conveniences. Returns the list of plot handles.
    """

    if ax is None:
        plt.figure(1, figsize=(10, 10))
        ax = plt.gca()

    # Get the number of classes
    if labels is not None:
        classes = np.unique(labels)
    else:
        classes = np.array([1,])
        labels = np.ones(len(x))        

    # Find data ranges... used to set axes
    center_x = np.mean(x)        
    radius_x = max(center_x - min(x), max(x) - center_x)
    radius_x *= 1.025 
    center_y = np.mean(y)
    radius_y = max(center_y - min(y), max(y) - center_y)
    radius_y *= 1.025

    for cls in classes:
        ax.plot(x[labels == cls], y[labels == cls], 'o', label="Class {}".format(cls))

    # Turn off labelling
    ax.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
    ax.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
    ax.set_xlim((center_x - radius_x, center_x + radius_x))
    ax.set_ylim((center_y - radius_y, center_y + radius_y))

    # Create Legend
    plt.legend(bbox_to_anchor=(1, 0.5), loc='center left', ncol=1, fontsize=18)
