import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [original, setOriginal] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select an image");

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/api/upload",
        formData
      );

      setResult(`http://127.0.0.1:8000/${res.data.output_image}`);
    } catch (err) {
      alert("Upload failed");
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>🎨 CreativeGen Studio</h1>
      <p>AI Background Removal Demo</p>

      <input
        type="file"
        accept="image/*"
        onChange={(e) => {
          setFile(e.target.files[0]);
          setOriginal(URL.createObjectURL(e.target.files[0]));
        }}
      />

      <br /><br />

      <button onClick={handleUpload}>
        {loading ? "Processing..." : "Upload & Remove Background"}
      </button>

      <div style={{ display: "flex", gap: "40px", marginTop: "30px" }}>
        {original && (
          <div>
            <h3>Original</h3>
            <img src={original} width="300" />
          </div>
        )}

        {result && (
          <div>
            <h3>Result</h3>
            <img src={result} width="300" />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
