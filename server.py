from flask import Flask, request, jsonify
from flask_cors import CORS
from llm import ai_review

app = Flask(__name__)
CORS(app) # Enable CORS

company_data = {}

@app.route("/api/data", methods=["POST"])

def receive_data():
    data = request.get_json()
    print("Received JSON data:", data)

    email = data.get("email")
    company = data.get("company")
    material_rating = int(data.get("material", 0))
    disposal_rating = int(data.get("disposal", 0))
    review = data.get("review", "")

    if company:
        if company not in company_data:
            company_data[company] = {
                "total_material": 0,
                "total_disposal": 0,
                "count": 0,
                "reviews": []
            }

        company_data[company]["total_material"] += material_rating
        company_data[company]["total_disposal"] += disposal_rating
        company_data[company]["count"] += 1

        if review:
            company_data[company]["reviews"].append({"email": email, "review": review})

    return jsonify({"message": "Data received successfully!"}), 200

@app.route("/api/rankings", methods=["GET"])
def get_rankings():
    rankings = []
    for company, data in company_data.items():
        if data["count"] > 0:
            avg_material = data["total_material"] / data["count"]
            avg_disposal = data["total_disposal"] / data["count"]
            print("AAAAAAAAAAAAAAAAAAAAA", data["total_material"])
            weighted_score = (avg_material * 0.5) + (avg_disposal * 0.5)

            rankings.append({
                "company": company,
                "average_material": round(avg_material, 2),
                "average_disposal": round(avg_disposal, 2),
                "weighted_score": round(weighted_score, 2),
                "reviews": data["reviews"],
				"ai_review": ai_review(company, round(avg_material, 2), round(avg_disposal, 2), data["reviews"])
            })

    rankings.sort(key=lambda x: x["weighted_score"], reverse=True)

    return jsonify(rankings), 200

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)

