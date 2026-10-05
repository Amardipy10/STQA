# Lumina Tasks - Web Testing & QA Project

## 📌 About The Project
This project is a complete **Software Testing and Quality Assurance (STQA)** implementation based on a modern, responsive web application called "Lumina Tasks". 

The project is divided into two main parts:
1. **The Application:** A beautiful, glassmorphism-styled To-Do List web application built with HTML, CSS, and JavaScript. It features local storage persistence, filtering, and smooth animations.
2. **The Testing Suite (Core Focus):** Comprehensive testing documentation and automated scripts to ensure the application's quality and stability.

### 🗂️ Project Structure
- **`index.html`, `style.css`, `script.js`**: The core application files.
- **`Bug_Taxonomy.md`**: A document categorizing potential bugs (Functional, UI, Browser, Performance) and their severity levels.
- **`Test_Plan.md` & `Test_Report.md`**: Strategic planning and the final report of all manual (exploratory) and automated testing results.
- **`regression_test.py`**: A Python script using Selenium WebDriver for automated end-to-end regression testing. (Includes a visually slowed-down "Demo Mode" for presentations).
- **`lumina_regression.side`**: A Selenium IDE recorded script (alternative to the Python script).

---

## 🚀 How to Run the Application
You don't need any special server to run the app itself.
1. Simply double-click the `index.html` file, or right-click and select **"Open with Google Chrome"** (or any modern browser).
2. The application will run locally.

---

## 🤖 How to Run the Automated Tests (Selenium)
The automated tests use Python and Selenium WebDriver to physically open a Chrome browser and test the application just like a human user would.

### Prerequisites
- Python 3.x installed on your system.
- Google Chrome browser installed.

### Step-by-Step Instructions (macOS/Linux & Windows)

**1. Open your terminal or command prompt and navigate to the project folder:**
```bash
cd path/to/project_folder
```

**2. Create a Virtual Environment (Recommended):**
This keeps the project dependencies isolated.
```bash
python3 -m venv venv
```

**3. Activate the Virtual Environment:**
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```
- **On Windows:**
  ```cmd
  venv\Scripts\activate
  ```

**4. Install Selenium:**
```bash
pip install selenium
```

**5. Run the Test Script:**
```bash
python regression_test.py
```

Sit back and watch! A new Chrome window will open automatically, and the script will add tasks, mark them as completed, filter them, and delete them to ensure everything is working correctly.

> **Note:** The `regression_test.py` file has a `DEMO_MODE = True` flag enabled at the top. This adds a slight delay (1.5 seconds) between actions so that teachers or evaluators can clearly see what the automated script is doing. If you want it to run at lightning speed, you can change it to `DEMO_MODE = False`.
