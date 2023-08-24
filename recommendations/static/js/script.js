const recommendationsContainer = document.getElementById("recommendations");

fetchRecommendations();

async function fetchRecommendations() {
  try {
    const response = await fetch(`/get_recommendations`);
    const data = await response.json();

    if (data.success) {
      const recommendations = data.recommendations;
      recommendationsContainer.innerHTML = recommendations.join("<br>");
    } else {
      recommendationsContainer.innerHTML = "Error fetching recommendations.";
    }
  } catch (error) {
    recommendationsContainer.innerHTML = "An error occurred.";
    console.error("Error fetching data:", error);
  }
}
