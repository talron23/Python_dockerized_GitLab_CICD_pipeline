// app.js
async function getJoke() {
    try {
        const response = await fetch('/get_joke');
        const jokeData = await response.json();

        document.getElementById('setup').innerText = `Setup: ${jokeData.joke}`;
        document.getElementById('delivery').innerText = `Punchline: ${jokeData.punchline}`;
    } catch (error) {
        console.error('Failed to fetch joke:', error);
        alert('Failed to fetch joke. Please try again.');
    }
}
