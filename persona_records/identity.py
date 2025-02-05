from langchain_ollama.llms import OllamaLLM
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import csv

# Initialize Ollama model
ollama_model = OllamaLLM(
    model="llama3.1",
    base_url="http://localhost:11434",
    num_predict=500
    )  

# Set up memory to handle personal information contextually
memory = ConversationBufferMemory()

# Create a conversation chain
conversation = ConversationChain(
    llm = ollama_model,
    memory = memory,
    verbose = False
    )

# Function to handle personal information
def collect_personal_info():
    personal_info = {
        "Full Name": "Jane Lila",
        "Address": "123 Main Street, Springfield, USA",
        "Phone Number": "+1-555-123-4567",
        "Email Address": "jane.lila@example.com",
        "Date of Birth": "1990-04-15",
        "Gender": "Female",
        "Nationality": "American",
        "Marital Status": "Single",
        "Social Security Number (SSN)": "123-45-6789",
        "Passport Number": "X1234567",
        "Driver's License Number": "D1234567",
        "National ID Card Number": "NID-987654321",
        "Tax Identification Number": "TIN-1122334455",
        "Employee ID Number": "EMP-55667788",
        "Student ID Number": "STU-33445566",
    }
    
    return personal_info

# Collect personal information
user_info = collect_personal_info()

# Save personal information to CSV
with open('jane_lila_info.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Field", "Value"])
    for key, value in user_info.items():
        writer.writerow([key, value])

# Display collected information
for key, value in user_info.items():
    print(f"{key}: {value}")
