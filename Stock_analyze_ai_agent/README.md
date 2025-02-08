# Setting Up the Virtual Environment and Installing Dependencies

Follow these steps to set up a virtual environment and install the required libraries for this project:

## Step 1: Create a Virtual Environment

1. Open a terminal or command prompt.
2. Navigate to the project directory:
    ```sh
    cd /c:/Users/Ritik Karir/Downloads/AI_Project/Stocks_analyze_AI_agent_main
    ```
3. Create a virtual environment named `venv`:
    ```sh
    python -m venv venv
    ```

## Step 2: Activate the Virtual Environment

- On Windows:
    ```sh
    venv\Scripts\activate
    ```
- On macOS and Linux:
    ```sh
    source venv/bin/activate
    ```

## Step 3: Install the Required Libraries

1. Ensure the virtual environment is activated.
2. Install the libraries listed in `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

## Step 4: Verify the Installation

1. Check that the libraries are installed correctly:
    ```sh
    pip list
    ```

You should now have all the necessary dependencies installed and can proceed with running the project.