# Threat Analyzer

This is a machine learning application that analyzes PDF documents to extract and classify cybersecurity threats. It uses a Flask-based web interface for uploading PDFs, a machine learning model for classifying threats, and a dashboard for displaying the results.

## Features

-   **PDF Text Extraction:** Extracts plain text from uploaded PDF files.
-   **Threat Classification:** Uses a Naive Bayes classifier to identify the type of threat (e.g., malware, phishing, DDoS).
-   **Information Extraction:** Uses spaCy for Named Entity Recognition to identify potential threat actors and targets.
-   **Web Dashboard:** Displays the analysis results in a clean, color-coded interface.
-   **CSV Export:** Allows you to download a summary of the analysis.

## Running with Docker

This application is containerized using Docker for easy setup and deployment.

### Prerequisites

-   [Docker](https://docs.docker.com/get-docker/) installed on your machine.

### Build the Docker Image

To build the Docker image, run the following command from the root of the repository:

```bash
docker build -t threat-analyzer .
```

### Run the Docker Container

Once the image is built, you can run the application in a Docker container with this command:

```bash
docker run -p 5000:5000 threat-analyzer
```

The application will be accessible in your web browser at `http://localhost:5000`.
