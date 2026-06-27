console.log("ProductPulse AI Loaded");

const compareButton = document.getElementById("compare-btn");
const loadingSection = document.getElementById("loading-section");
const resultsSection = document.getElementById("results-section");

compareButton.addEventListener("click", async () => {

    const url1 = document.getElementById("app1-url").value.trim();
    const url2 = document.getElementById("app2-url").value.trim();

    if (!url1 || !url2) {
        alert("Please enter both Google Play Store URLs.");
        return;
    }

    loadingSection.style.display = "block";
    resultsSection.style.display = "none";

    try {

        const response = await fetch("/compare", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url1: url1,
                url2: url2
            })
        });

        if (!response.ok) {
            throw new Error("Backend Error");
        }

        const data = await response.json();

        loadingSection.style.display = "none";
        resultsSection.style.display = "block";

        // ----------------------------
        // App 1
        // ----------------------------

        document.getElementById("app1-name").innerText =
            data.product1.name;

        document.getElementById("app1-rating").innerText =
            data.product1.rating.toFixed(2);

        document.getElementById("app1-reviews").innerText =
            data.product1.reviews;

        // ----------------------------
        // App 2
        // ----------------------------

        document.getElementById("app2-name").innerText =
            data.product2.name;

        document.getElementById("app2-rating").innerText =
            data.product2.rating.toFixed(2);

        document.getElementById("app2-reviews").innerText =
            data.product2.reviews;

        // ----------------------------
        // Winner
        // ----------------------------

        document.getElementById("winner-name").innerText =
            data.winner;

        // ----------------------------
        // Executive Summary
        // ----------------------------

        document.getElementById("summary").innerHTML = `
<b>${data.product1.name}</b><br><br>
${data.product1.summary}

<hr>

<b>${data.product2.name}</b><br><br>
${data.product2.summary}
`;

        // ----------------------------
        // App 1 Pain Points
        // ----------------------------

        const pain1 = document.getElementById("app1-pain");
        pain1.innerHTML = "";

        data.product1.pain_points.forEach(point => {
            pain1.innerHTML += `<li>${point}</li>`;
        });

        // ----------------------------
        // App 2 Pain Points
        // ----------------------------

        const pain2 = document.getElementById("app2-pain");
        pain2.innerHTML = "";

        data.product2.pain_points.forEach(point => {
            pain2.innerHTML += `<li>${point}</li>`;
        });

        // ----------------------------
        // App 1 Feature Requests
        // ----------------------------

        const feature1 = document.getElementById("app1-features");
        feature1.innerHTML = "";

        data.product1.feature_requests.forEach(feature => {
            feature1.innerHTML += `<li>${feature}</li>`;
        });

        // ----------------------------
        // App 2 Feature Requests
        // ----------------------------

        const feature2 = document.getElementById("app2-features");
        feature2.innerHTML = "";

        data.product2.feature_requests.forEach(feature => {
            feature2.innerHTML += `<li>${feature}</li>`;
        });

    }

    catch (error) {

        console.error(error);

        loadingSection.style.display = "none";

        alert("Unable to connect to backend.");

    }

});