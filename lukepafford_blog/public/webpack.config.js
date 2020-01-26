module.exports = {
  entry: "./src/index.js",
  output: {
		path: __dirname + "/dist/js",
    filename: "bundle.js"
  },
  module: {
    rules: [
      { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" }
    ]
  },
  externals: {
    "jquery": "jQuery"
  }
}

