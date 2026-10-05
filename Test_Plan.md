# Test Plan: Lumina Tasks Application

## 1. Introduction
This test plan outlines the testing strategy, scope, resources, and schedule for the Lumina Tasks web application. The application is a simple, frontend-only To-Do list manager utilizing local storage.

## 2. Objectives
- Ensure the application functions correctly according to its requirements.
- Verify UI/UX responsiveness and aesthetic integrity.
- Guarantee data persistence using the browser's local storage.
- Identify and document any bugs before release.

## 3. Scope
**In-Scope:**
- Functional testing of core features (Add, Delete, Toggle Completion, Filtering).
- UI/UX testing across different states (empty state, populated state).
- Cross-browser compatibility (Chrome, Firefox, Safari).
- Data persistence testing (Local Storage).

**Out-of-Scope:**
- Backend testing (as it's a frontend-only app).
- Performance testing for large datasets (assumed lightweight usage).
- Security testing beyond basic XSS prevention in input.

## 4. Test Strategy
- **Unit Testing:** Handled during development (implicit).
- **Integration Testing:** Ensuring DOM elements interact correctly with JS logic.
- **System Testing:** End-to-end user flows.
- **Exploratory Testing:** Unscripted testing to find edge cases.
- **Automated Regression Testing:** Selenium WebDriver scripts to verify core functionality repeatedly.

## 5. Test Environment
- **OS:** macOS / Windows 11
- **Browsers:** Google Chrome (Primary), Mozilla Firefox, Safari.
- **Tools:** Selenium WebDriver (Python), Selenium IDE.

## 6. Test Deliverables
- Test Plan Document
- Bug Taxonomy
- Selenium WebDriver Scripts (`regression_test.py`)
- Selenium IDE Project (`lumina_regression.side`)
- Test Execution Report (including exploratory testing)

## 7. Features to be Tested
- F1: Adding a new task (Valid & Empty input).
- F2: Toggling a task as complete/incomplete.
- F3: Deleting a task.
- F4: Filtering tasks (All, Active, Completed).
- F5: Data persistence on page reload.
- F6: Empty state UI behavior.
