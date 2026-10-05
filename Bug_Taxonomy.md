# Bug Taxonomy: Lumina Tasks Application

This taxonomy categorizes potential bugs that might be found during the testing of the Lumina Tasks application.

## 1. Functional Bugs (F)
Bugs related to the core functionality of the application not working as intended.
- **F-01: Data Integrity:** Issues with saving or retrieving data from local storage (e.g., tasks disappearing on reload).
- **F-02: State Management:** Incorrect state transitions (e.g., filtering shows wrong tasks, checkbox doesn't reflect actual state).
- **F-03: Input Handling:** Failure to handle specific inputs (e.g., extremely long strings, blank spaces, XSS payload execution).
- **F-04: Action Failure:** Buttons or interactive elements not triggering the intended action (e.g., delete button does nothing).

## 2. User Interface / User Experience (UI)
Bugs related to the visual presentation and user interaction flow.
- **UI-01: Layout/Alignment:** Elements misaligned, overlapping, or overflowing their containers (e.g., long text breaking the layout).
- **UI-02: Styling:** Incorrect colors, missing fonts, or broken glassmorphism effects.
- **UI-03: Animation/Transition:** Janky animations, missing hover states, or animations firing incorrectly.
- **UI-04: Responsiveness:** Application unusable or visually broken on smaller screen sizes.

## 3. Browser Compatibility (BC)
Bugs that appear in specific browsers but not others.
- **BC-01: CSS Support:** Modern CSS features (like backdrop-filter) not rendering correctly in older or specific browsers.
- **BC-02: JS Execution:** Differences in JavaScript engine execution causing runtime errors.

## 4. Performance (P)
While a lightweight app, performance issues can still occur.
- **P-01: DOM Manipulation Lag:** Sluggishness when adding/deleting many items due to unoptimized DOM updates.
- **P-02: Load Time:** Initial load time being excessive (unlikely for this app, but worth categorizing).

## Severity Levels
- **Critical (S1):** App crashes, total loss of data, core functionality completely broken (e.g., cannot add tasks).
- **High (S2):** Major feature broken but workaround exists, significant UI breakage (e.g., filtering doesn't work).
- **Medium (S3):** Minor functional issue, noticeable but non-blocking UI glitch (e.g., long text pushes delete button slightly).
- **Low (S4):** Cosmetic issues, typos, minor alignment problems (e.g., wrong shade of gray on hover).
