async function startScan() {
    const target = document.getElementById("target").value;
    const response = await fetch("http://localhost:5000/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ target: target })
    });
    const data = await response.json();

    // Display scan results
    document.getElementById("results").textContent = JSON.stringify(data.results, null, 2);
    document.getElementById("results").classList.add("fadeIn");

    // Set report download link
    document.getElementById("downloadLink").href = `http://localhost:5000/download_report`;
}