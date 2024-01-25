const tf = require('@tensorflow/tfjs-node');
const { loadTokenizer } = require('./tokenizer-utils'); // Implement loadTokenizer based on your tokenizer saving/loading logic

async function loadModelAndTokenizer() {
  const model = await tf.loadLayersModel('./twitter_sentiment_model.keras');
  const tokenizer = loadTokenizer('./tokenizer.json');
  return { model, tokenizer };
}

module.exports = { loadModelAndTokenizer };
