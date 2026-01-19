"""
Week 2 Mini-Project: Test Data Organizer 🗂️

Goal: Build a tool to manage LLM test cases using Python data structures.
Learnings Applied: Lists, Dictionaries, Sets, Tuples, Basic Functions.

"""
Week 2 Mini-Project: Test Data Organizer 🗂️

Goal: Build a tool to manage LLM test cases using Python data structures.
Learnings Applied: Lists, Dictionaries, Sets, Tuples, Basic Functions.
"""

test_cases = []

def create_test_case(tc_id, prompt, category) -> dict:
    """
    Creates a dictionary representing a test case.
    
    Args:
        tc_id (str): Unique ID (e.g., "TC001")
        prompt (str): The input prompt for the LLM
        category (str): The type of test (e.g., "safety", "accuracy")
        
    Returns:
        dict: A test case dictionary with keys: id, prompt, category, status, run_count
    """
    """
    # Initialize 'status' to "pending" and 'run_count' to 0 (int)
    return {
            "tc_id": tc_id,
            "prompt": prompt,
            "category": category,
            "status": "pending",
            "run_count": 0
    }

def add_test_case():
    """
    Prompts user for input and adds a new test case to the global list.
    """
    print("\n--- Add New Test Case ---")
    
    """
    tc_id = input("Enter Test ID: ")
    prompt = input("Enter Test Prompt: ")
    category = input("Enter Test Category: ")
    test_cases.append(create_test_case(tc_id, prompt, category))

def view_all_test_cases():
    """
    Iterates through all test cases and prints their details.
    """
    print("\n--- All Test Cases ---")
    
    """
    if not test_cases:
        print("No test cases found.")
        return
    for tc in test_cases:
        print(f"ID: {tc['tc_id']}, Prompt: {tc['prompt']}, Category: {tc['category']}, Status: {tc['status']}, Run Count: {tc['run_count']}")

def update_test_status():
    """
    Finds a test case by ID and updates its status.
    """
    print("\n--- Update Test Status ---")
    target_id = input("Enter Test ID to update: ")
    
    """
    for tc in test_cases:
        if tc['tc_id'] == target_id:
            new_status = input("Enter new status (passed/failed): ")
            tc['status'] = new_status
            tc['run_count'] += 1
            print(f"Test case {target_id} updated successfully.")
            return
    print(f"Test case {target_id} not found.")

def show_statistics():
    """
    Calculates and prints statistics about the test data.
    """
    print("\n--- Statistics 📊 ---")
    
    """
    count_passed = len([t for t in test_cases if t['status'] == 'passed'])
    count_failed = len([t for t in test_cases if t['status'] == 'failed'])
    print(f"Total Test Cases: {len(test_cases)}")
    print(f"Passed: {count_passed}")
    print(f"Failed: {count_failed}")    

def main():
    """
    Main menu loop.
    """
    while True:
        print("\n=== TEST DATA ORGANIZER ===")
        print("1. Add Test Case")
        print("2. View All Test Cases")
        print("3. Update Test Status")
        print("4. Show Statistics")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            add_test_case()
        elif choice == '2':
            view_all_test_cases()
        elif choice == '3':
            update_test_status()
        elif choice == '4':
            show_statistics()
        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
