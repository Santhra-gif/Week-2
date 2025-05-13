api_key = 'AIzaSyAKbj_m5q8HQh8PHoEKxfGokT60oQ6BS6o'
import google.generativeai as genai
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# To generate a response
def generate_text(prompt):
    return model.generate_content(prompt)

def text_summarization(text):
    return model.generate_content('Summarize this : {text}')

prompt = "Explain the theory of relativity in simple terms."
print(generate_text(prompt).text)

text = "The quick brown fox jumps over the lazy dog"
print(generate_text(text).text)