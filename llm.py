
import vertexai
from vertexai.generative_models import GenerativeModel

# model initialization
PROJECT_ID = "top-chassis-438719-g1"
vertexai.init(project=PROJECT_ID,  location="us-central1")
model = GenerativeModel("gemini-1.5-flash-002")

def ai_review(company_name: str, material: float, disposal: float) -> str:
	message = "Based on the rating from a group of customers, the company, {}, has an average rating of {} out of 5 in terms of how sustainable the packagings are, and an average rating of {} out of 5 in terms of how convenience are those materials can be disposed. Write a review about the company's work on sustainable packaging.".format(company_name, material, disposal)
	
	response = model.generate_content(message)

	return response.text

