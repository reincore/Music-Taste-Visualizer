from api import LastFmAPI
from visualizer import MusicTasteVisualizer

def main():
    # Initialize the API
    api = LastFmAPI()

    # Get the user's music listening history
    history = api.get_user_history('orleanth')

    # Check if history is None
    if history is None:
        print("Failed to get user history.")
        return

    # Initialize the visualizer
    visualizer = MusicTasteVisualizer()

    # Create the visualization
    visualizer.create_visualization(history)

if __name__ == "__main__":
    main()
