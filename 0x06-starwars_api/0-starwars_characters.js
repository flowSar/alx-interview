#!/usr/bin/node

const request = require('request');

// Fetch characters from the Star Wars API based on the movie ID
function fetchCharacters(movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(movieUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error(`Error fetching movie data: ${error.message}`);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: Movie with ID ${movieId} not found.`);
      return;
    }

    // Get the list of character URLs
    const characters = body.characters;

    // Fetch and print each character's name in order
    characters.forEach((characterUrl) => {
      request(characterUrl, { json: true }, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(`Error fetching character data: ${charError.message}`);
          return;
        }

        if (charResponse.statusCode === 200) {
          console.log(charBody.name);
        }
      });
    });
  });
}

// Get movie ID from command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.log('Usage: node star_wars_characters.js <movie_id>');
  process.exit(1);
}

fetchCharacters(movieId);
