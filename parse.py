import g4f

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def create_prompt(dom_content, parse_description):
    return template.format(dom_content=dom_content, parse_description=parse_description)

def call_gpt_api(prompt):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        if isinstance(response, str):
            return response
        else:
            return "Unexpected response format. Please check the API response."
    except Exception as e:
        return f"An error occurred: {e}"

def parser(dom_content):
    formatted_prompt = create_prompt(dom_content, "Your description here")
    return call_gpt_api(formatted_prompt)

def process_prompt(prompt):
    return call_gpt_api(prompt)

# Example usage
if __name__ == "__main__":
    prompt = "Your small chunk prompt here"
    response = process_prompt(prompt)
    print(f"GPT: {response}")
