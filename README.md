# cicd-quality-demo

![CI](https://github.com/<YOUR_USERNAME>/cicd-quality-demo/actions/workflows/ci.yml/badge.svg)

A hands-on learning project for CI/CD pipeline development with code quality enforcement.

## Tools Used

| Tool | Purpose |
|------|---------|
| **Black** | Code formatter (opinionated, zero-config) |
| **isort** | Import statement organizer |
| **Flake8** | PEP 8 linter |
| **MyPy** | Static type checker |
| **Bandit** | Security vulnerability scanner (SAST) |
| **pip-audit** | Dependency vulnerability scanner |
| **GitHub Actions** | CI/CD pipeline automation |

## Project Structure

```
my-cicd-project/
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── operations.py        ← typed Python with real logic
├── tests/
│   └── test_operations.py       ← pytest tests
├── .github/
│   └── workflows/
│       └── ci.yml               ← GitHub Actions pipeline
├── pyproject.toml               ← Black + isort + MyPy config
├── .flake8                      ← Flake8 config
├── requirements-dev.txt         ← dev / quality tool deps
└── README.md
```

## Getting Started

### 1. Set up your environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements-dev.txt
```

### 2. Run quality tools locally

```bash
# Formatter
black --check .
black .                        # auto-fix

# Import organizer
isort --check-only .
isort .                        # auto-fix

# Linter
flake8 src/ tests/

# Type checker
mypy src/

# Security scanner
bandit -r src/ -ll
```

### 3. Run tests

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

### 4. Install pre-commit hooks (optional but recommended)

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files    # test manually
```

## Learning Path

| Day | Focus |
|-----|-------|
| 1 | Install tools, Black + isort exercises |
| 2 | Flake8 + MyPy + Bandit exercises |
| 3 | Create project scaffold + config files |
| 4 | Write typed source + pytest tests |
| 5 | Git init + push to GitHub |
| 6 | Write GitHub Actions `ci.yml` |
| 7 | Debug pipeline, fix failing gates |
| 8 | Add pre-commit hooks |
| 9 | Branch protection + matrix testing |
| 10 | Review, polish README, add badges |

## CI/CD Pipeline

The pipeline follows a **best-practice multi-stage model**:

```
Build (+Security) → Test → Deploy → Post-Deploy
```

### CI Workflow (every push & PR)

| Stage | Job | What it does |
|-------|-----|-------------|
| **Build + Security** | `build` | Black, isort, Flake8, MyPy, Bandit SAST, pip-audit, build wheel |
| **Test** | `test` | Pytest with coverage, Codecov upload |
| **Summary** | `build-summary` | Consolidated pass/fail report |

### Deploy Workflows (QA & Production)

| Stage | What it does |
|-------|-------------|
| **Deploy** | Build wheel artifact, push to target environment |
| **Post-Deploy** | Smoke tests, health checks, verification |
| **Release** *(prod only)* | Git tag creation for audit trail |

## Branch Strategy

```
main          ← protected, only merged via PR
  └── feature/add-multiply   ← create PRs from here
```

```bash
git checkout -b feature/add-multiply
# make changes
git push origin feature/add-multiply
# open PR on GitHub → watch Actions run!
```
