import vertexai
from vertexai.generative_models import GenerativeModel

# model initialization
PROJECT_ID = "top-chassis-438719-g1"
vertexai.init(project=PROJECT_ID,  location="us-central1")
model = GenerativeModel("gemini-1.5-flash-002")

def ai_review(company_name: str, material: float, disposal: float, user_reviews: list) -> str:
    reviews_text = " ".join(user_reviews)

    message = "Based on the rating from a group of customers, the company, {}, has an average rating of {} out of 5 in terms of how sustainable the packagings are, and an average rating of {} out of 5 in terms of how convenience are those materials can be disposed. Here are some user reviews: {}. Write a summary review about the company's work on sustainable packaging, using information from the average ratings and the reviews provided from users.".format(company_name, material, disposal, reviews_text)

    response = model.generate_content(message)

    return response.text

