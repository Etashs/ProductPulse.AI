// =========================================
// ProductPulse AI
// Milestone 3 - Frontend JavaScript
// =========================================

console.log("✅ ProductPulse AI - Milestone 3 Loaded");

// ==============================
// DOM Elements
// ==============================

const compareButton = document.getElementById("compare-btn");

const loadingSection = document.getElementById("loading-section");

const resultsSection = document.getElementById("results-section");

const app1Input = document.getElementById("app1-url");

const app2Input = document.getElementById("app2-url");

// ==============================
// Compare Button Event
// ==============================

compareButton.addEventListener("click", function () {

    const app1 = app1Input.value.trim();

    const app2 = app2Input.value.trim();

    // Basic Validation
    if (app1 === "" || app2 === "") {

        alert("Please enter both Google Play Store URLs.");

        return;

    }

    // Hide previous dashboard
    resultsSection.style.display = "none";

    // Show loading spinner
    loadingSection.style.display = "block";

    console.log("Comparing Apps...");
    console.log("App 1:", app1);
    console.log("App 2:", app2);

    // =====================================
    // Temporary Simulation
    // Backend will replace this later
    // =====================================

    setTimeout(function () {

        loadingSection.style.display = "none";

        resultsSection.style.display = "block";

        console.log("Dashboard Loaded Successfully");

    }, 1500);

});

// ==============================
// Future Backend Function
// ==============================

async function compareApps() {

    /*
        This function will be implemented in
        Milestone 4.

        It will:

        POST /compare

        Send:

        {
            app1_url:"",
            app2_url:""
        }

        Receive JSON

        Update Dashboard
    */

}