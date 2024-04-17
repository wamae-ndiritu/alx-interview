#!/usr/bin/node
const process = require('process');
const axios = require('axios');

const movieId = process.argv[2];

function getFilmById (filmId) {
  return axios.get(`https://swapi-api.alx-tools.com/api/films/${filmId}/`).then(({ data }) => data.characters);
}

function printFilmCharacters (filmId) {
  getFilmById(filmId).then(characters => {
    characters.forEach(characterUrl => {
      axios.get(characterUrl).then(({ data }) => console.log(data.name)).catch(err => console.error(err));
    });
  }).catch(err => console.log(err));
}

if (!movieId) {
  process.exit(1);
}

printFilmCharacters(movieId);
