const API_BASE = "https://api-ridewithus-project.onrender.com";  // Your backend

document.getElementById("rideForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const pickup = document.getElementById("pickup").value;
    const destination = document.getElementById("destination").value;

    document.getElementById("result").innerText = "🚕 Finding a ride...";

    try {
        const response = await fetch(`${API_BASE}/simulate`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ pickup, destination })
        });

        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        const data = await response.json();
        document.getElementById("result").innerText = 
            `✅ Ride confirmed!\nPickup: ${pickup}\nDestination: ${destination}\n\nResponse: ${JSON.stringify(data, null, 2)}`;
    } catch (error) {
        console.error("Error calling API:", error);
        document.getElementById("result").innerText = "❌ Failed to connect to backend.";
    }
});

