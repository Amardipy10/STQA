import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_regression_tests():
    # Set this to True to slow down the tests for a demo presentation
    DEMO_MODE = True
    DELAY = 1.5 if DEMO_MODE else 0.5

    # Setup WebDriver (Using Chrome in this example)
    # Ensure chromedriver is installed or selenium manager will handle it in newer versions
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Uncomment to run in headless mode
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Get the absolute path to the local index.html
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_url = f"file://{current_dir}/index.html"
        
        print(f"Opening: {file_url}")
        driver.get(file_url)
        wait = WebDriverWait(driver, 10)
        
        print("\n--- Starting Regression Tests ---")

        # Test 1: Verify Initial State
        print("Test 1: Verifying Initial State...")
        empty_state = wait.until(EC.presence_of_element_located((By.ID, "empty-state")))
        assert not "hidden" in empty_state.get_attribute("class"), "Empty state should be visible initially"
        print("✓ Test 1 Passed")

        # Test 2: Add a Task
        time.sleep(DELAY)
        print("Test 2: Adding a new task...")
        input_field = driver.find_element(By.ID, "todo-input")
        time.sleep(DELAY)
        input_field.send_keys("Buy groceries")
        time.sleep(DELAY)
        driver.find_element(By.ID, "add-btn").click()
        time.sleep(DELAY) # Wait for animation
        
        # Verify task is added
        todo_list = driver.find_element(By.ID, "todo-list")
        tasks = todo_list.find_elements(By.TAG_NAME, "li")
        assert len(tasks) == 1, "There should be exactly 1 task"
        assert "Buy groceries" in tasks[0].text, "Task text does not match"
        print("✓ Test 2 Passed")

        # Test 3: Add another task and test Enter key
        time.sleep(DELAY)
        print("Test 3: Adding task via Enter key...")
        input_field.send_keys("Read a book")
        time.sleep(DELAY)
        input_field.send_keys(Keys.RETURN)
        time.sleep(DELAY) # Wait for animation
        
        tasks = driver.find_elements(By.CSS_SELECTOR, ".todo-item")
        assert len(tasks) == 2, "There should be exactly 2 tasks"
        print("✓ Test 3 Passed")

        # Test 4: Mark Task as Completed
        time.sleep(DELAY)
        print("Test 4: Marking task as completed...")
        first_task = tasks[0]
        checkbox = first_task.find_element(By.CSS_SELECTOR, ".todo-checkbox")
        # Click the label to trigger the checkbox visually as well
        first_task.find_element(By.CSS_SELECTOR, ".checkmark").click()
        
        # Verify it has completed class
        time.sleep(DELAY)
        first_task = driver.find_elements(By.CSS_SELECTOR, ".todo-item")[0] # Re-fetch after DOM update
        assert "completed" in first_task.get_attribute("class"), "Task should have 'completed' class"
        print("✓ Test 4 Passed")

        # Test 5: Filtering
        time.sleep(DELAY)
        print("Test 5: Testing Filters...")
        # Click Active filter
        driver.find_element(By.CSS_SELECTOR, "button[data-filter='active']").click()
        time.sleep(DELAY)
        visible_tasks = driver.find_elements(By.CSS_SELECTOR, ".todo-item:not(.hidden)") # Simplified check, our app removes from DOM on filter
        # Actually in our app, the JS re-renders the list. Let's count DOM elements.
        current_tasks = driver.find_elements(By.CSS_SELECTOR, ".todo-item")
        assert len(current_tasks) == 1, "Active filter should show 1 task"
        
        # Click Completed filter
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, "button[data-filter='completed']").click()
        time.sleep(DELAY)
        current_tasks = driver.find_elements(By.CSS_SELECTOR, ".todo-item")
        assert len(current_tasks) == 1, "Completed filter should show 1 task"

        # Click All filter
        time.sleep(DELAY)
        driver.find_element(By.CSS_SELECTOR, "button[data-filter='all']").click()
        time.sleep(DELAY)
        current_tasks = driver.find_elements(By.CSS_SELECTOR, ".todo-item")
        assert len(current_tasks) == 2, "All filter should show 2 tasks"
        print("✓ Test 5 Passed")

        # Test 6: Data Persistence (Local Storage)
        time.sleep(DELAY)
        print("Test 6: Testing Data Persistence (Reload)...")
        driver.refresh()
        wait.until(EC.presence_of_element_located((By.ID, "todo-list")))
        time.sleep(DELAY)
        current_tasks = driver.find_elements(By.CSS_SELECTOR, ".todo-item")
        assert len(current_tasks) == 2, "Tasks should persist after page reload"
        print("✓ Test 6 Passed")

        # Test 7: Delete a Task
        time.sleep(DELAY)
        print("Test 7: Deleting a task...")
        # Hover to reveal delete button might be needed depending on CSS, but selenium can click hidden if we use JS, 
        # or we just find it. The CSS opacity is 0 on idle, but it's in DOM.
        delete_btn = current_tasks[0].find_element(By.CSS_SELECTOR, ".delete-btn")
        driver.execute_script("arguments[0].click();", delete_btn)
        time.sleep(DELAY * 2) # wait for fade out animation
        
        current_tasks = driver.find_elements(By.CSS_SELECTOR, ".todo-item")
        assert len(current_tasks) == 1, "There should be 1 task left after deletion"
        print("✓ Test 7 Passed")

        print("\n--- All Regression Tests Passed Successfully! ---")

    except Exception as e:
        print(f"\n❌ Test Failed: {e}")
    finally:
        time.sleep(2) # Keep browser open briefly to see final state
        driver.quit()

if __name__ == "__main__":
    run_regression_tests()
