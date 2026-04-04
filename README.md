<!DOCTYPE html>
<html>
<body>
<div style="font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%); color: #eef2ff; border-radius: 24px;">

<!-- HEADER SECTION -->
<div style="text-align: center; padding: 2rem 1rem 1rem 1rem;">
    <h1 style="font-size: 3rem; font-weight: 800; background: linear-gradient(135deg, #FF6B6B, #FFD93D); -webkit-background-clip: text; background-clip: text; color: transparent; margin: 0;">🚗 AI Car Recommendation System</h1>
    <p style="font-size: 1.2rem; color: #a0a8c0; margin-top: 0.5rem;">Content‑Based Filtering • FastAPI • MongoDB Atlas • Production‑Ready REST API</p>
    <div style="margin-top: 1.5rem;">
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🐍 Python</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🚀 FastAPI</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🍃 MongoDB Atlas</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🤖 Scikit‑learn</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">📊 Cosine Similarity</span>
    </div>
</div>

<hr style="border-color: #2a2f45; margin: 20px 0;">

<!-- PROJECT OVERVIEW -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📌 What I Built</h2>
    <p>An AI‑powered car recommendation system that suggests similar cars based on <strong>category</strong> and <strong>price</strong> fully integrated with a live MongoDB database and exposed via a <strong>FastAPI REST API</strong>. The system uses <strong>content‑based filtering</strong> (cosine similarity) and dynamically adapts to any categories added by the admin.</p>
</div>

<!-- DAY BY DAY WORK (8 Days) -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📅 Day‑by‑Day Work</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem;">
        <div style="background: #0b0f1c; padding: 0.8rem; border-radius: 16px;"><strong>📆 Day 1 – Setup & Planning</strong><br>Python env, libraries, GitHub repo, architecture planning.</div>
        <div style="background: #0b0f1c; padding: 0.8rem; border-radius: 16px;"><strong>📆 Day 2 – Data Understanding</strong><br>Analyzed SRS, identified datasets (Cars, Users, Bookings).</div>
        <div style="background: #0b0f1c; padding: 0.8rem; border-radius: 16px;"><strong>📆 Day 3 – Database & FastAPI</strong><br>Connected to MongoDB Atlas, inserted car data, retrieved as DataFrame.</div>
        <div style="background: #0b0f1c; padding: 0.8rem; border-radius: 16px;"><strong>📆 Day 4 – EDA</strong><br>Category distribution, price range, brand analysis, 6+ visualizations.</div>
        <div style="background: #0b0f1c; padding: 0.8rem; border-radius: 16px;"><strong>📆 Day 5 – Feature Engineering</strong><br>OneHotEncoder + MinMaxScaler → final feature matrix.</div>
        <div style="background: #0b0f1c; padding: 0.8rem; border-radius: 16px;"><strong>📆 Day 6 – Recommendation Model</strong><br>Cosine similarity engine – input (category, max_price) → top 5 similar car IDs.</div>
        <div style="background: #0b0f1c; padding: 0.8rem; border-radius: 16px;"><strong>📆 Day 7 – FastAPI Endpoints</strong><br>Professional REST API with validation, error handling, CORS.</div>
        <div style="background: #0b0f1c; padding: 0.8rem; border-radius: 16px;"><strong>📆 Day 8 – Live MongoDB Integration</strong><br>Dynamic category handling – works with any admin‑added categories.</div>
    </div>
</div>

<!-- SYSTEM ARCHITECTURE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🏗️ System Architecture</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px; overflow-x: auto; color: #b0c4de; font-size: 0.9rem;">
User Request
     ↓
FastAPI Endpoint
/recommendation?category=SUV&max_price=100
     ↓
MongoDB Atlas → Live Car Data
     ↓
Feature Engineering (Dynamic)
     ↓
Cosine Similarity Calculation
     ↓
Top N Car IDs Returned
     ↓
Backend (Node.js) → React Frontend
    </pre>
</div>

<!-- AI TECHNIQUE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🤖 AI Technique Used</h2>
    <p><strong>Content‑Based Filtering using Cosine Similarity</strong></p>
    <ul>
        <li><strong>Input</strong> → category + max_price</li>
        <li><strong>Output</strong> → [car_id_1, car_id_2, car_id_3...]</li>
        <li>Similarity computed on normalized features (category one‑hot + scaled price)</li>
    </ul>
</div>

<!-- API ENDPOINTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🔗 API Endpoints</h2>
    <table style="width:100%; border-collapse: collapse; color: #ddd;">
        <tr style="background: #0b0f1c;">
            <th style="padding: 10px; text-align: left;">Endpoint</th>
            <th style="padding: 10px; text-align: left;">Method</th>
            <th style="padding: 10px; text-align: left;">Description</th>
        </tr>
        <tr><td style="padding: 8px; border-bottom: 1px solid #2a2f45;"><code>/</code></td><td style="padding: 8px;">GET</td><td style="padding: 8px;">API status + available categories</td></tr>
        <tr><td style="padding: 8px; border-bottom: 1px solid #2a2f45;"><code>/recommendation</code></td><td style="padding: 8px;">GET</td><td style="padding: 8px;">Get car recommendations (category, max_price)</td></tr>
        <tr><td style="padding: 8px; border-bottom: 1px solid #2a2f45;"><code>/cars</code></td><td style="padding: 8px;">GET</td><td style="padding: 8px;">All cars from database</td></tr>
        <tr><td style="padding: 8px;"><code>/databases</code></td><td style="padding: 8px;">GET</td><td style="padding: 8px;">DB structure explorer</td></tr>
    </table>
</div>

<!-- TECHNOLOGIES USED -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🛠️ Technologies Used</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0.8rem;">
        <div><strong>🐍 Language</strong><br>Python 3.10+</div>
        <div><strong>🤖 AI/ML</strong><br>Scikit‑learn, Pandas, NumPy</div>
        <div><strong>🚀 API</strong><br>FastAPI, Uvicorn</div>
        <div><strong>🍃 Database</strong><br>MongoDB Atlas, PyMongo</div>
        <div><strong>📊 Data Analysis</strong><br>Matplotlib, Seaborn, Jupyter</div>
        <div><strong>🔐 Environment</strong><br>dotenv, certifi</div>
        <div><strong>🐙 Version Control</strong><br>Git, GitHub</div>
    </div>
</div>

<!-- KEY ACHIEVEMENTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">✅ Key Achievements</h2>
    <ul>
        <li>✅ Live MongoDB integration — real data, not CSV</li>
        <li>✅ Dynamic categories — no hardcoding</li>
        <li>✅ Professional API with validation & error handling</li>
        <li>✅ CORS enabled for React frontend</li>
        <li>✅ Team coordination with backend developers</li>
    </ul>
</div>

<!-- CHALLENGES SOLVED -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">⚡ Challenges Solved</h2>
    <ol>
        <li><strong>MongoDB SSL Error</strong> – Solved using <code>certifi</code> for SSL certificate handling.</li>
        <li><strong>Hardcoded Categories Problem</strong> – Made categories dynamic; automatically read from database.</li>
        <li><strong>Missing car_id in DB</strong> – Generated car_id from DataFrame index.</li>
        <li><strong>Feature Matrix Mismatch</strong> – Kept two separate DataFrames – one for filtering, one for similarity.</li>
    </ol>
</div>

<!-- GITHUB LINK -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0; text-align: center;">
    <h2 style="color: #FFD93D; margin-top: 0;">📁 GitHub Repository</h2>
    <a href="https://github.com/RehmanAhmad333/car-rental-recommendation-system" target="_blank" style="background: #FF6B6B; color: white; padding: 12px 28px; border-radius: 50px; text-decoration: none; font-weight: 600; display: inline-block;">🔗 View on GitHub</a>
</div>

<!-- FOOTER / AUTHOR -->
<div style="text-align: center; padding: 1.5rem 0; border-top: 1px solid #2a2f45; margin-top: 20px; color: #6f7a9e;">
    <p>Built with dedication during <strong>AI Developer Internship</strong> at TechNexus Virtual University</p>
    <p>👤 <strong>Rehman Ahmad</strong> | AI Developer Intern</p>
</div>

</div>
</body>
</html>