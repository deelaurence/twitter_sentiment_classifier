const fs = require('fs');

function loadTokenizer(tokenizerFilePath) {
  // Read the contents of the tokenizer file
  const tokenizerData = fs.readFileSync(tokenizerFilePath, 'utf-8');

  // Parse the JSON data to get the tokenizer object
  const tokenizer = JSON.parse(tokenizerData);

  return tokenizer;
}

module.exports = { loadTokenizer };
