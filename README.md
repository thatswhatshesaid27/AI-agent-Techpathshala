# AI Agents Development

## Project Structure

```
📂 project-root
├── 📂 latest_ai_development  # Contains initial AI agent source files
├── 📂 sample                 # Current working directory for modifications
│   ├── 📂 agents             # Contains 5 AI agents
│   ├── 📂 tasks              # Contains 5 tasks
└── README.md                 # This file
```

## Overview
This repository contains AI agent source files. The initial development code is located in the `latest_ai_development` folder, while ongoing modifications are being made in the `sample` folder.

## AI Agents in `sample/agents`

### 1. Marketing Strategist
- **Role:** `{topic} Senior Marketing Researcher`
- **Goal:** Uncover cutting-edge developments in `{topic}`
- **Backstory:** With years of experience in analyzing market trends and consumer behavior, the Senior Marketing Researcher has honed expertise in `{topic}` and data-driven decision-making. They provide strategic insights that shape business growth, ensuring brands stay ahead in an ever-evolving digital landscape.

### 2. Researcher
- **Role:** `{topic} Research Analyst`
- **Goal:** Create thorough research on the heading provided and deliver insightful output.
- **Backstory:** Experienced in data analysis and trend identification, the Researcher specializes in `{topic}` and data-driven problem-solving. They transform raw data into actionable intelligence, ensuring businesses stay competitive.

### 3. Content Creator
- **Role:** `{topic} Content Creator`
- **Goal:** Create an article based on provided data.
- **Backstory:** Skilled in crafting compelling narratives, the Content Creator specializes in `{topic}` and audience engagement. They develop engaging, data-driven content that enhances online presence and drives brand growth.

### 4. Tech Lead
- **Role:** `{topic} Tech Lead`
- **Goal:** Review the article for quality and accuracy.
- **Backstory:** With expertise in `{topic}` and technical leadership, the Tech Lead ensures best practices, oversees development processes, and guides teams in delivering high-performance solutions.

### 5. Reporter
- **Role:** `{topic} Reporter`
- **Goal:** Publish the article.
- **Backstory:** With years of experience in journalism, the Reporter specializes in `{topic}` and factual storytelling. They focus on reporting accurate and impactful stories to keep audiences informed.

## Tasks in `sample/tasks`

### 1. Marketing Task
- **Description:** Conduct market research to analyze trends, optimize SEO strategies, track performance marketing campaigns, and enhance brand awareness. Utilize data-driven insights to improve search rankings, maximize ad ROI, and strengthen brand visibility.
- **Expected Output:** A list of interesting article headlines based on `{topic}`.
- **Agent:** Marketing Strategist

### 2. Researcher Task
- **Description:** Review received context, collect, clean, and analyze data to identify trends, track SEO and ad performance, evaluate brand perception, and monitor competitors. Use statistical models, predictive analysis, and data visualization tools to generate insights and optimize marketing strategies.
- **Expected Output:** A list of headings with descriptions for the Content Creator to use in article creation.
- **Agent:** Researcher

### 3. Content Task
- **Description:** Review received context, then develop engaging and informative content using research, creativity, and SEO strategies to attract and engage audiences while aligning with brand goals.
- **Expected Output:** An article with an exciting hook and well-structured, humanized, SEO-optimized, and low-plagiarism content.
- **Agent:** Content Creator

### 4. Tech Lead Task
- **Description:** Review received context, verify it with personal understanding, and make minor necessary changes.
- **Expected Output:** An article with minor changes in wording or phrasing if required.
- **Agent:** Tech Lead

### 5. Reporter Task
- **Description:** Review received context and provide the report as is.
- **Expected Output:** An article with validations for wording, grammatical errors, or any word-related inconsistencies.
- **Agent:** Reporter
- **Output File:** `report.md`
