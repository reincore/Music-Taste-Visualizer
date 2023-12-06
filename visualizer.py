import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

class MusicTasteVisualizer:
    def __init__(self):
        self.colors = {
            'rock': 'red',
            'pop': 'blue',
            'jazz': 'green',
            'classical': 'yellow'
            # Add more genres and colors as needed
        }

    def create_visualization(self, history):
        # Extract the tags and dates from the history
        tags = [tag for track in history['recenttracks']['track'] for tag in track['tags']]
        dates = [track['date']['#text'] for track in history['recenttracks']['track'] for _ in track['tags']]

        # Convert dates to datetime objects
        dates = [datetime.strptime(date, '%d %b %Y, %H:%M') for date in dates]

        # Convert datetime objects to numerical values
        dates = [date.timestamp() for date in dates]

        # Initialize a label encoder
        encoder = LabelEncoder()

        # Fit the encoder and transform the tags to numerical values
        tags = encoder.fit_transform(tags)

        # Create a 2D histogram
        hist, xedges, yedges = np.histogram2d(dates, tags, bins=[50, 50])

        # Normalize the histogram
        hist = hist / np.max(hist)

        # Create a color map
        cmap = mcolors.LinearSegmentedColormap.from_list("n",["red", "yellow", "green"])

        # Create a heatmap
        plt.imshow(hist, cmap=cmap, aspect='auto')

        # Save the plot to a file
        plt.savefig('music_taste_visualization.png')

        # Display the plot
        plt.show()
