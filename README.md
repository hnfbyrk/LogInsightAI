# LogInsightAI

A lightweight Python project that analyzes text-based logs, summarizes event severity, classifies system status, and creates reusable reports.

> The current version uses deterministic rules. AI-assisted anomaly detection is planned for a future version.

## Why This Project?

Operational logs can be difficult to review quickly. LogInsightAI turns a simple log file into a concise health summary that can support monitoring and troubleshooting workflows.

## Current Features

- Reads UTF-8 text logs
- Counts `ERROR`, `WARNING`, and `INFO` records
- Calculates the overall error rate
- Classifies system status as `NORMAL`, `UYARI`, or `KRITIK`
- Generates a human-readable text report
- Generates a structured JSON report
- Appends timestamped history to text and JSONL files
- Handles a missing input file with a clear error message
- Validates core functions and saved report data with assertions

## Status Rules

| ERROR count | Status |
| ---: | --- |
| 0–2 | `NORMAL` |
| 3–4 | `UYARI` |
| 5 or more | `KRITIK` |

## Project Structure

```text
LogInsightAI/
├── main.py       # Log analysis, reporting, and validation
├── sample.log    # Anonymized example input
├── .gitignore    # Generated reports and local files
└── README.md     # Project documentation
```

The following files are generated when the program runs and are intentionally excluded from Git:

```text
rapor.json
rapor.txt
rapor_gecmisi.jsonl
rapor_gecmisi.txt
```

## Requirements

- Python 3
- No third-party packages

## Run the Project

Clone the repository:

```bash
git clone https://github.com/hnfbyrk/LogInsightAI.git
cd LogInsightAI
```

Run on Windows:

```powershell
py main.py
```

Or run with Python directly:

```bash
python main.py
```

## Input Format

Each line should include a timestamp, severity level, and message:

```text
2026-08-20 10:01:12 INFO Sistem baslatildi
2026-08-20 10:03:25 WARNING 192.0.2.25 basarisiz giris
2026-08-20 10:04:18 ERROR Veritabani baglantisi kurulamadi
```

The included IP address belongs to a documentation-only address range and does not identify a real system.

## Example Output

```text
TOPLAM LOG: 8
ERROR ORANI: %62.5
ERROR sayisi: 5
WARNING sayisi: 1
INFO sayisi: 2
DURUM: KRITIK
JSON raporu kaydedildi.
JSONL gecmis kaydi dogrulandi.
JSON icerigi dogrulandi.
Rapor, rapor.txt dosyasina kaydedildi.
Rapor gecmise eklendi.
TUM OTOMATIK TESTLER BASARILI.
```

## Validation

The current version contains assertions for:

- Status classification thresholds
- Error-rate calculation
- Empty-log handling
- Log-level counting
- JSON report verification
- JSONL history verification

A dedicated test suite is planned as the project grows.

## Roadmap

- Separate application logic from command-line execution
- Add unit tests with `pytest`
- Support configurable input and output paths
- Add structured and regex-based log parsing
- Export CSV reports
- Add visual summaries
- Explore anomaly-detection methods
- Add continuous integration with GitHub Actions

## Security and Privacy

The repository uses fictional sample data. Do not commit production logs, credentials, private IP inventories, internal domain names, or personally identifiable information.

## Project Status

Active learning project focused on Python, system monitoring, structured reporting, and testable automation.
