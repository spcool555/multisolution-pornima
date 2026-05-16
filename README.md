# DMML Static Website

This is the pure static HTML/CSS/JS version of the DMML corporate website. No frameworks (like React) or backend (like Java/Python) are required to run this website. The UI and UX have been strictly preserved.

## How to Run

Since the website is purely static, you have multiple easy ways to run it:

### Method 1: Direct File Open
Simply double-click the `index.html` file in the root directory to open it directly in your web browser. This works for almost all pages, though some features (like fetching external data if any) might require a local server.

### Method 2: VS Code Live Server
1. Open this directory in Visual Studio Code.
2. Install the **Live Server** extension.
3. Right-click on `index.html` and select **"Open with Live Server"**.
4. The site will automatically open in your browser at `http://127.0.0.1:5500`.

### Method 3: Python HTTP Server (if Python is installed)
1. Open a terminal/command prompt in this directory.
2. Run the following command:
   ```bash
   python -m http.server 8000
   ```
3. Open your browser and navigate to `http://localhost:8000`.

### Method 4: Node.js / NPX (if Node.js is installed)
1. Open a terminal/command prompt in this directory.
2. Run the following command:
   ```bash
   npx serve .
   ```
3. Open the URL provided in the terminal (usually `http://localhost:3000`).

## File Structure
- `index.html`: The main landing page.
- `styles.css`: The global stylesheet containing all UI designs.
- `main.js`: The JavaScript file handling interactive functionality.
- `clients/`: Contains logo images of partners and clients.
- `*.html`: Other standalone pages (about, contact, projects, etc.).
