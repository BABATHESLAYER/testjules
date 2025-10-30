document.getElementById('upload-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.querySelector('input[type="file"]');
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const results = await response.json();
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '<h2>Analysis Results</h2>';

    if (results.error) {
        resultsDiv.innerHTML += `<p>Error: ${results.error}</p>`;
    } else {
        const table = document.createElement('table');
        table.innerHTML = `
            <thead>
                <tr>
                    <th>Threat Name</th>
                    <th>Industry</th>
                    <th>Country</th>
                    <th>Threat Type</th>
                    <th>Severity</th>
                </tr>
            </thead>
            <tbody>
            </tbody>
        `;
        const tbody = table.querySelector('tbody');
        results.forEach(threat => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${threat.name}</td>
                <td>${threat.industry}</td>
                <td>${threat.country}</td>
                <td>${threat.threat_type}</td>
                <td class="severity-${threat.severity.toLowerCase()}">${threat.severity}</td>
            `;
            tbody.appendChild(row);
        });
        resultsDiv.appendChild(table);
        document.getElementById('download-link').classList.remove('hidden');
    }
});
