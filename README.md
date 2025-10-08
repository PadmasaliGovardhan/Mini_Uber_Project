🚕 Ride With Us — A Mini Uber Simulation
Welcome to Ride With Us, a sleek and exciting web-based simulation that brings the magic of ride-hailing platforms like Uber to life! This project showcases a real-time cab booking experience, complete with driver assignments, route planning, and fare calculations, all wrapped in a clean and intuitive UI. Whether you're a tech enthusiast or just curious about how ride-hailing apps work under the hood, this project is for you! 🎉

--------------------------------------------------------------------------------------------------------------------

🌟 Live Demo
Hop in and take it for a spin!  

Frontend (Client App): 🚗 [ridewithus.netlify.app](ridewithus.netlify.app)
Backend API (FastAPI): ⚙️ [api-ridewithus-project.onrender.com](api-ridewithus-project.onrender.com)

--------------------------------------------------------------------------------------------------------------------

🚖 What’s This All About?
“Ride With Us” is more than just a web app—it’s a smart transportation simulation that mimics the core mechanics of real-world ride-hailing systems. Here’s what makes it tick:

Smart Driver Assignment 🚖Matches you with the nearest available driver using a clever algorithm based on proximity and route efficiency.

City-to-City Routing 🗺️Maps out the shortest path between cities like Vijayawada, Mangalagiri, and Machilipatnam using Dijkstra’s Algorithm and real-world-inspired distances.

Dynamic Fare Calculation 💰Estimates your fare at ₹10/km based on the total trip distance.

Slick Frontend ⚡A user-friendly interface lets you pick your starting point and destination, then instantly see your driver, route, fare, and estimated travel time.

--------------------------------------------------------------------------------------------------------------------

🛠️ Tech Stack
Here’s the tech powering this ride-hailing adventure:



Area
Technology Used



Backend
🐍 Python, FastAPI


Frontend
🌐 HTML, CSS, JavaScript


Routing Algorithm
📊 Dijkstra’s Algorithm


Deployment
🚀 Render (Backend) & Netlify (Frontend)


Testing
🧪 Browser Console & API Endpoint Tests



🏙️ Cities in the Simulation
The app connects real cities from Andhra Pradesh, India, with realistic distances between them:

Vijayawada ↔ Mangalagiri ↔ Vaddeswaram ↔ Tadepalli ↔ Machilipatnam ↔ Chirala ↔ Bapatla

Each connection is a route segment, forming a graph that powers the ride-matching magic! 🛣️

⚙️ API Endpoints
The backend is built with FastAPI and offers these key endpoints:
GET /
Checks if the API is up and running.Response:
{ "message": "🚕 Mini Uber API is running" }

GET /ride?pickup=<city>&destination=<city>
Books a simulated ride between two cities.Example:https://api-ridewithus-project.onrender.com/ride?pickup=Vijayawada&destination=MachilipatnamResponse:
{
  "status": "confirmed",
  "driver_assigned": {
    "name": "Driver2",
    "vehicle": "Hatchback",
    "rating": 4.5
  },
  "trip_route": ["Vijayawada", "Tadepalli", "Machilipatnam"],
  "distance_km": 80,
  "estimated_time_hr": 2.0,
  "estimated_fare_inr": 800
}

--------------------------------------------------------------------------------------------------------------------

🚀 How It Works (The Magic Behind the Scenes)

Pick Your RideEnter your pickup and destination cities in the frontend.

API CallThe frontend sends a request to the FastAPI backend using fetch().

Route PlanningThe backend runs Dijkstra’s Algorithm on a graph of connected cities to find the shortest route.

Driver AssignmentA driver is randomly selected from a pool of available drivers, prioritizing proximity.

Fare & Time CalculationThe backend calculates the fare (₹10/km) and estimated travel time, then sends everything back as JSON.

Display ResultsThe frontend presents your ride details in a clean, user-friendly card.

--------------------------------------------------------------------------------------------------------------------

🌍 Deployment



Component
Platform
Link



Backend
Render
api-ridewithus-project.onrender.com


Frontend
Netlify
ridewithus.netlify.app

--------------------------------------------------------------------------------------------------------------------

🧑‍💻 Try It Locally
Want to tinker with the code yourself? Here’s how to set it up:

Clone the Repository  
git clone https://github.com/<your-username>/Mini_Uber_Project.git
cd Mini_Uber_Project/backend


Install Dependencies  
pip install -r requirements.txt


Run the FastAPI Server  
uvicorn backend.api:app --reload


Open the FrontendOpen index.html in your browser to start booking rides!

--------------------------------------------------------------------------------------------------------------------

🎨 Screenshots

<img width="1293" height="695" alt="image" src="https://github.com/user-attachments/assets/4ee3bd61-f855-453d-8c76-034497bcdf74" />



--------------------------------------------------------------------------------------------------------------------

👨‍💻 About the Author
Padmasali Govardhan🎓 Electronics and Communication Engineering (ECE) [LinkedIn](https://www.linkedin.com/in/govardhanpadmasali) 

--------------------------------------------------------------------------------------------------------------------

🌈 What’s Next?
This project is just the beginning! Here are some exciting ideas for future enhancements:

🧭 Google Maps Integration: Add real-world map-based routing.  
📱 Mobile-Friendly UI: Make the app fully responsive for phones.  
🤖 Live Driver Tracking: Simulate driver movement with WebSockets.  
💬 Chatbot Assistant: Add a conversational bot for ride bookings.

--------------------------------------------------------------------------------------------------------------------

⭐ Show Some Love
If you enjoyed this project or learned something new, give it a ⭐ on GitHub and share it with your friends! Let’s build the future of transportation together. 🚗💨
