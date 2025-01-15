# Contributing to MetaEarth AI

We’re excited that you’re interested in contributing to **MetaEarth AI**! This document outlines the guidelines for contributing to this project, ensuring a smooth and productive collaboration.

---

## How to Contribute

### 1. Fork the Repository
Start by forking the repository to your GitHub account. This allows you to make changes without affecting the main repository.

### 2. Clone the Forked Repository
```bash
git clone https://github.com/your-username/MetaEarth-AI.git
cd MetaEarth-AI
```

### 3. Set Up Your Development Environment
Install the required dependencies and set up the development environment:

# Install Python dependencies
pip install -r env/requirements.txt

# Optional: Set up Docker
docker-compose up

### 4. Create a New Branch
Work on a feature or fix in a new branch:

git checkout -b feature-or-fix-name

### 5. Test Your Changes
# Run Python tests
pytest tests/

# Run Solidity tests (requires Hardhat or Truffle)
npx hardhat test

### 6. Commit Your Changes
git commit -m "feat: Add AI agent tracking module"

### 7. Push and Submit a Pull Request
Push your branch to your forked repository:

git push origin feature-or-fix-name

### Contribution Guidelines
Code Style: Follow PEP 8 for Python code and Solidity Style Guide for smart contracts.
Testing: Ensure your code is well-tested and passes all existing tests.
Documentation: Update or create relevant documentation for any features you implement or modify.
Pull Requests: Ensure pull requests are clear, concise, and include a detailed description of the changes.

### Community Code of Conduct
By contributing to this project, you agree to abide by our community code of conduct:

Be respectful to all contributors and maintain a welcoming environment.
Provide constructive feedback when reviewing pull requests or issues.
Avoid personal attacks or inflammatory language.

### Getting Help
If you have any questions about contributing, feel free to open an issue in the repository, and a maintainer will assist you.

Thank you for contributing to MetaEarth AI!

