import React, { useRef, useState } from 'react';
import './App.css';

const App = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [predictionResult, setPredictionResult] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);

  const imgRef = useRef(null);
  const defaultImageURL = "/shaq-default.jpg";

  // this function is called when the user selects an image
  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();

      // set the selected file
      reader.onloadend = () => {
        handleClear();
        setSelectedImage(reader.result);
        setSelectedFile(file);
        
      };
      reader.readAsDataURL(file);

      // set the selected image
    } else {
      setSelectedImage(defaultImageURL);
      setSelectedFile(null);
    }
  };

  // this function is called when the user clicks on the "Run Analysis" button
  const handleRunAnalysis = async () => {

    // check if the image has been selected
    if (!selectedImage) {
      setPredictionResult('Error: Image not selected.')
      console.error('Image not selected.');
      return;
    }

    // check if the file has been selected
    if (!selectedFile) {
      setPredictionResult('Error: File not selected.')
      console.error('File not selected.');
      return;
    }

    // send the image to the server
    const formData = new FormData();
    formData.append('image', selectedFile);

    try {
      const response = await fetch('http://127.0.0.1:8000/detect_shaq', {
        method: 'POST',
        body: formData,
      });

      const result = await response.json();

      if (result.error) {
        setPredictionResult(result.error);
        return;
      }

      // display the result
      setPredictionResult(result.shaq_probability > result.no_shaq_probability
        ? `Shaquille O'Neal detected with ${result.shaq_probability * 100}% probability!`
        : `No Shaquille O'Neal detected with ${result.no_shaq_probability * 100}% probability!`);
    } catch (error) {
      console.error('Error during inference:', error);
    }
  };

  // this function is called when the user clicks on the "Clear" button
  const handleClear = () => {
    setSelectedImage(defaultImageURL);
    setSelectedFile(null);
    setPredictionResult(null);
  };

  return (
    <div className="app-container">
      <header>
        <h1>Shaquille O'Neal Detector</h1>
      </header>

      <section className="main-content">
        <div className="upload-area">
          <label htmlFor="file-input" className="upload-label">
            <img
              ref={imgRef}
              src={selectedImage || defaultImageURL}
              alt="Selected"
              className="selected-image"
              onLoad={() => console.log('Image loaded successfully!')}
            />
            <input
              type="file"
              id="file-input"
              accept=".jpg"
              onChange={handleImageChange}
            />
            Choose Image
          </label>
          <div className="description">
            <p>
              Built with React, Flask, and TensorFlow
            </p>
            <p>
              Detect if Shaquille O'Neal is in your image.
            </p>
          </div>
        </div>

        <div className="action-buttons">
          <button onClick={handleRunAnalysis}>Run Analysis</button>
          <button onClick={handleClear}>Clear</button>
        </div>

        <section className="results">
          <h2>Results</h2>
          {predictionResult !== null ? (
            <p className="result-text">
              {predictionResult.includes('Error') ? (
                <>
                  <span className="error-highlight">Error</span>
                  {predictionResult.substring(5)}
                </>
              ) : (
                predictionResult
              )}
            </p>
          ) : (
            <p className="placeholder-text">Results will appear here</p>
          )}
        </section>

      <footer>
        <p>Author: Liam Jennings | Email: liamjennings009@gmail.com | LinkedIn: <a href="https://www.linkedin.com/in/liam-jennings-b54920248">Liam Jennings</a></p>
      </footer>
      </section>
    </div>
  );
};

export default App;
