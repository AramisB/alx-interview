#!/usr/bin/node
// A script that prints all characters of a Star Wars movie in order

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Make the request to get the movie data
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body to JSON
  const characters = JSON.parse(body).characters;

  // Helper function to make requests sequentially
  function fetchCharacterName (index) {
    if (index >= characters.length) return; // Stop if all characters are fetched

    request(characters[index], function (error, response, body) {
      if (error) {
        console.error(error);
      } else {
        console.log(JSON.parse(body).name);
        fetchCharacterName(index + 1); // Fetch the next character
      }
    });
  }

  // Start fetching characters sequentially from index 0
  fetchCharacterName(0);
});
