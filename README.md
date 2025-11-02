# 🔍 Quantitative Financial Strategist - Hidden Stock Analysis

A sophisticated Streamlit application that employs All-Source Predictive Analytics to identify undervalued growth stocks with high potential returns using advanced Chain-of-Thought reasoning methodology.

## Overview

This application acts as an expert Quantitative Financial Strategist specializing in identifying "Hidden Stocks" - publicly traded companies that demonstrate high potential for undervalued growth and are projected to yield minimum 20% positive returns over 18 months while maintaining a Moderate Risk Profile.

## Methodology

The application employs a three-stage Chain-of-Thought analytical framework:

### Stage 1: Macro-Environmental & Sector Analysis (PESTLE/Trend Prediction)
- Identifies global sectors expected to outperform based on PESTLE framework
- Analyzes quantitative leading indicators for future revenue growth
- Projects market size and innovation trends

### Stage 2: Entity-Specific Anomaly Detection (All-Source Data Fusion)
- Selects mid-cap companies within identified sectors showing undervaluation
- Conducts Multi-INT Correlation Analysis:
  - **GEOINT/MASINT:** Physical footprint analysis via satellite imagery and MASINT data
  - **FININT:** Transactional and risk profile analysis via financial intelligence
  - **OSINT/TECHINT:** Reputation and innovation edge analysis via open-source and technical intelligence

### Stage 3: Risk Mitigation and Conclusion
- Justifies why stocks are "hidden" (market inefficiencies)
- Details primary risks and AI-driven mitigation strategies

## Features

- **Multi-Stock Analysis:** Generate analysis for 10-20 stocks simultaneously
- **Comprehensive Reporting:** Detailed Part A (summary table) and Part B (narrative analysis)
- **Risk Assessment:** AI-driven risk mitigation strategies for each recommendation
- **Export Capabilities:** Download analysis reports in CSV format
- **Customizable Parameters:** Adjust target returns, time horizons, and risk profiles

## Installation

1. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:

   ```bash
   streamlit run streamlit_app.py
   ```

## Usage

1. Configure analysis parameters in the sidebar:
   - Number of stocks to analyze (10-20)
   - Risk profile selection
   - Target return percentage
   - Time horizon

2. Click "Generate Analysis" to run the analysis

3. Review the results:
   - **Part A:** Summary table with all stock recommendations
   - **Part B:** Detailed narrative analysis for each stock including Multi-INT findings

4. Export results using the download button

## Output Format

### Part A: Hidden Stock Recommendation (Table Format)
Displays key metrics including:
- Sector
- Stock ticker and company name
- Current and target prices
- Expected return percentage
- Risk profile

### Part B: Justification and Analysis (Detailed Narrative)
For each stock:
- Stage 1 Summary (Macro trends and leading indicators)
- Stage 2 Multi-INT Findings (GEOINT, FININT, OSINT/TECHINT)
- Hidden Stock Justification
- Key Risks and AI Mitigation Strategies

## Technology Stack

- **Streamlit:** Web application framework
- **Pandas:** Data manipulation and analysis
- **Python:** Core programming language

## Disclaimer

This application is for educational and analytical purposes only. The analysis uses simulated/hypothetical data and should not be considered as financial advice. Always conduct your own research and consult with qualified financial advisors before making investment decisions.

## License

See LICENSE file for details.
