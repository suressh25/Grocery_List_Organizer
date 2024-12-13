import ollama
import os

model = "llama3.2"

input_file = "grocery_list.txt"
output_file = "categorized_grocery_list.txt"

if not os.path.exists(input_file):
    print(f"Input file '{input_file}' not found.")
    exit(1)

with open(input_file, "r") as f:
    items = f.read().strip()

prompt = f"""
You are an assistant that categorizes and sorts grocery items.
Here is a list of grocery items:
{items}
Please:
1.Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, Frozen, Canned, Snacks, Condiments, etc.
2.Sort the items in each category alphabetically.
3.Present the categorized list in a clear and organized manner,using bullet points or numbering.
"""

try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print("Categorized grocery list:\n")
    print(generated_text)

    with open(output_file, "w") as f:
        f.write(generated_text.strip())

    print(f"Categorized grocery list has been saved to '{output_file}'.")
except Exception as e:
    print(f"An error occurred:", str(e))
