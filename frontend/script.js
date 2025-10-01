const API_BASE = "https://api-ridewithus-project.onrender.com";

document.getElementById("rideForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const pickup = document.getElementById("pickup").value;
  const destination = document.getElementById("destination").value;
  const resultDiv = document.getElementById("result");

  resultDiv.textContent = "⏳ Finding your ride...";

  try {
    const res = await fetch(`${API_BASE}/ride?pickup=${pickup}&destination=${destination}`);
    if (!res.ok) {
      throw new Error("API error");
    }

    const data = await res.json();
    resultDiv.textContent = `✅ Driver Found: ${data.driver}, ETA: ${data.eta} mins, Cost: ₹${data.cost}`;
  } catch (err) {
    resultDiv.textContent = "❌ Could not fetch ride. Try again.";
    console.error(err);
  }
});

