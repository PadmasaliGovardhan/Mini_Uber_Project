document.getElementById("rideForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const pickup = document.getElementById("pickup").value;
  const destination = document.getElementById("destination").value;

  try {
    const response = await fetch(
      `https://ridewithus-project.onrender.com/ride?pickup=${encodeURIComponent(pickup)}&destination=${encodeURIComponent(destination)}`
    );

    if (!response.ok) {
      throw new Error("Failed to fetch ride data");
    }

    const data = await response.json();

    document.getElementById("output").innerHTML = `
      <p><strong>Driver:</strong> ${data.driver}</p>
      <p><strong>ETA:</strong> ${data.eta} mins</p>
      <p><strong>Pickup:</strong> ${pickup}</p>
      <p><strong>Destination:</strong> ${destination}</p>
    `;
  } catch (error) {
    document.getElementById("output").innerHTML = `<p style="color:red;">Error: ${error.message}</p>`;
  }
});

