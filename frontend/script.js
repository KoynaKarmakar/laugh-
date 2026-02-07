// Backend API URL - update this when deploying
const API_URL = 'https://laugh-dkp4.onrender.com';

// Get DOM elements
const jokeText = document.getElementById('jokeText');
const getJokeBtn = document.getElementById('getJokeBtn');

// Function to fetch and display joke
async function getJoke() {
    try {
        // Show loading state
        jokeText.textContent = 'Loading...';
        jokeText.classList.add('loading'); // Add loading class
        getJokeBtn.disabled = true;

        // Fetch joke from backend
        const response = await fetch(API_URL);

        // Check if response is successful
        if (!response.ok) {
            throw new Error('Failed to fetch joke');
        }

        // Parse JSON response
        const data = await response.json();

        // Display the joke
        jokeText.textContent = data.joke;
        jokeText.classList.remove('loading'); // Remove loading class

    } catch (error) {
        // Handle errors
        console.error('Error fetching joke:', error);
        jokeText.textContent = 'Failed to fetch joke. Please try again.';
        jokeText.classList.remove('loading');
    } finally {
        // Re-enable button
        getJokeBtn.disabled = false;
    }
}

// Add click event listener to button
getJokeBtn.addEventListener('click', getJoke);