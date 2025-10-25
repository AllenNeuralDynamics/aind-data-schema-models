"""Script to grab protocol information from protocols.IO using the official API.

Requires you set PROTOCOLS_CLIENT_TOKEN environment variable with your API token, from
protocols.io/developers
"""

import requests
import pandas as pd
import os


OUTPUT_CSV = "src/aind_data_schema_models/_generators/models/protocols.csv"
WORKSPACE_URI = "allen-institute-for-neural-dynamics"
API_BASE = "https://www.protocols.io/api"


def get_access_token():
    """Get access token from environment variable."""
    token = os.environ.get("PROTOCOLS_CLIENT_TOKEN")
    if not token:
        raise RuntimeError("PROTOCOLS_CLIENT_TOKEN environment variable not set.")
    return token


def get_workspace_protocols(token, workspace_uri):
    """Get protocols from a given workspace."""
    headers = {"Authorization": f"Bearer {token}"}
    all_items = []
    page = 1
    while True:
        url = f"{API_BASE}/v3/workspaces/{workspace_uri}/protocols?page={page}&page_size=10000"
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        items = data.get("items", [])
        if not items:
            break
        all_items.extend(items)
        # Check pagination info
        pagination = data.get("pagination", {})
        total_pages = pagination.get("total_pages", 1)
        if page >= total_pages:
            break
        page += 1
    return all_items


def main():
    """Main function to fetch protocols and save to CSV."""
    token = get_access_token()
    print("Fetching protocols from workspace...")
    protocols = get_workspace_protocols(token, WORKSPACE_URI)
    print(f"Found {len(protocols)} protocols.")
    # Deduplicate by DOI
    results_by_doi = {}
    for p in protocols:
        title = p.get("title", "")
        doi = p.get("doi", "")
        # Strip URL prefix if present
        if doi.startswith("dx.doi.org/"):
            doi = doi[len("dx.doi.org/") :]  # Remove the prefix
        elif doi.startswith("https://dx.doi.org/"):
            doi = doi[len("https://dx.doi.org/") :]  # Remove the prefix
        authors = []
        for author in p.get("authors", []):
            name = author.get("name")
            if name:
                authors.append(name)
        authors_str = ", ".join(authors)
        # Only add if DOI is not already present
        if doi and doi not in results_by_doi:
            results_by_doi[doi] = {"title": title, "DOI": doi, "authors": authors_str}
    results = list(results_by_doi.values())
    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    # Write CSV using pandas
    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Saved {len(results)} protocols to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
