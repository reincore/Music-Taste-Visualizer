# Music Taste Visualizer
Music Taste Visualizer is a visualization project that leverages the Last.fm API to create unique, visually engaging representations of individual music listening habits and preferences. This tool is designed to transform the abstract concept of musical taste into tangible, visually appealing artworks, providing a new perspective on personal and shared musical journeys.

## Features
### Personalized Music Timeline: 
Generates a dynamic, color-coded timeline based on the user’s listening history. This feature maps different genres to specific colors, visually strikingly representing the user's music preferences over time.

### Genre Diversity Representation: 
Depicts the variety of music genres a user listens to, offering insights into their eclectic taste or genre loyalty.

### Interactive Data Visualization: 
Allows users to interact with music data, exploring different periods and genre specifics in detail.

### Shareable Visual Art: 
Users can create and share their musical taste as an abstract art piece, fostering connections through the visual representation of shared musical interests.

## Project Goals
To provide a unique, artistic way for music lovers to engage with and reflect on their listening habits.
To harness the power of data visualization in representing complex data (like music listening patterns) in an accessible and aesthetically pleasing manner.
To create a platform that encourages exploration and discussion about music tastes and preferences.

## Technology Stack
### Last.fm API: 
For fetching user-specific music listening data.
### Python: 
Primary programming language for data processing and visualization.


## Getting Started
For running locally for the default username, navigate to the repo and src/ folder, and run main.py.
Note that you will have to set the environment variable correctly. If you’re using a Unix-based system (like Linux or MacOS), you can set the environment variable in the terminal like this:
```
export LAST_FM_API_KEY=your_api_key
```
Replace your_api_key with your actual Last.fm API key. If you’re using Windows, the command is slightly different:
```
set LAST_FM_API_KEY=your_api_key
```
Again, replace your_api_key with your actual Last.fm API key. After setting the environment variable, try running main.py by 
```
python3 main.py
```

# Contributing
We welcome contributions to the Music Taste Visualizer! Whether it's improving the code, proposing new features, or reporting bugs, we appreciate your input in making this tool more engaging and useful for everyone.
