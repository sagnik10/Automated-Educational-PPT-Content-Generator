# Educational-Presentation-Automation-System

Automated system for generating structured, branded educational PowerPoint presentations with dynamically generated visual assets and story-based math content.

---

## Overview

This project is an automated PowerPoint generation system designed for educational content production.

It performs:

- PowerPoint merging
- Slide cleaning and text normalization
- Duplicate slide removal
- Branding integration (logo + scanner bar)
- Story-based slide injection
- Topic-based image generation
- Automated master presentation creation

The system transforms multiple source PPT files into a unified, styled, content-enhanced final presentation.

---

## Core Components

### 1. PPT.py

Main automation engine for presentation generation.

Capabilities:

- Merges multiple source PPT files
- Cleans slide text using regex filtering
- Removes unwanted phrases
- Detects and removes duplicate slides
- Preserves cover slide logic
- Automatically inserts educational “Story” slides
- Adds branding (logo + QR scanner bar)
- Applies structured layout formatting
- Exports final master presentation

Output:

- MASTER_FINAL_SAMPLESTYLE_LOGO_SCANNER_STORY.pptx

---

### 2. make_topic_images.py

Dynamic visual asset generator using Pillow (PIL).

Generates topic-based educational PNG assets including:

- Unit Rate visuals
- Speed (km/h) illustrations
- Liters per day graphics
- Fraction pizza model
- Fraction bar model
- 100-grid percent visualization
- Percent proportion formula
- Percent equation model
- Real-life math scenarios (tax, commission, product comparison)

All assets are saved inside structured topic folders:

```
assets_topic_images/
├── unit_rates/
├── fractions/
├── percent_proportion/
├── percent_equation/
└── real_life/
```

---

## System Workflow

1. Generate topic-based images
   - Run make_topic_images.py
   - Creates structured PNG assets

2. Place source PPT files in project directory

3. Run PPT.py
   - Cleans and processes slides
   - Merges content
   - Injects story-based math slides
   - Applies consistent branding
   - Exports final master presentation

---

## Features

- Automated educational storytelling integration
- Slide content deduplication using text signature hashing
- Regex-based text sanitization
- Custom layout rendering using python-pptx
- Dynamic visual asset creation using Pillow
- Branding automation (logo and scanner integration)
- Structured educational topic injection

---

## Technologies Used

- Python
- python-pptx
- Pillow (PIL)
- Regular Expressions
- Hashing (MD5 for deduplication)
- File system automation

---

## Installation

Install required dependencies:

```bash
pip install python-pptx pillow
```

---

## Usage

Generate visual assets:

```bash
python make_topic_images.py
```

Generate final presentation:

```bash
python PPT.py
```

Final output:

```
MASTER_FINAL_SAMPLESTYLE_LOGO_SCANNER_STORY.pptx
```

---

## Use Cases

- Automated curriculum generation
- Educational content production
- EdTech presentation automation
- Math lesson storytelling enhancement
- Branded presentation pipelines
- Instructional design automation

---

## Project Type

Educational Content Automation  
Presentation Engineering  
Instructional Design Automation  
EdTech Tooling

---

## License

This project is intended for educational and content automation purposes.
