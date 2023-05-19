from flask import Flask, jsonify, request
from recommendation_system import RecommendationSystem  # ваш модуль с рекомендательной системой

app = Flask(__name__)
rec_system = RecommendationSystem()

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json
    recommendations = rec_system.recommend(user_input)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
