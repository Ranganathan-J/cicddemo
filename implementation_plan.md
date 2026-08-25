# 3-Phase Manually Triggered Deployment Pipeline

## Background

The repo currently has two workflow files:

| File | Trigger | Status |
|---|---|---|
| [`ci.yml`](file:///c:/Users/Ranganathan.9703/Documents/learning/.github/workflows/ci.yml) | Auto — push/PR to `main` & feature branches | ✅ Keep as-is |
| [`deploy.yml`](file:///c:/Users/Ranganathan.9703/Documents/learning/.github/workflows/deploy.yml) | Push to `deploy` branch + `workflow_dispatch` | 🔄 Replace |

The existing `deploy.yml` mixes pre-deploy checks and deployment into one auto/manual hybrid. The goal is to **replace it** with 3 fully separate, manually triggered workflows — one per phase — each with a "Run workflow" button in the GitHub Actions UI.

---

## User Review Required

> [!IMPORTANT]
> The existing `deploy.yml` will be **deleted and replaced** by 3 new files. The `push: branches: [deploy]` auto-trigger will be removed. All deployment phases will be **manual-only** going forward.

> [!IMPORTANT]
> The **`production` environment** you already created in GitHub will be referenced in `deploy.yml` and `post-deploy.yml`. No new environment needs to be created. If you have **Required Reviewers** set on that environment, GitHub will pause the deploy job and wait for approval before running it.

---

## Proposed Changes

### Phase Overview

```
┌──────────────────────────────────────────────────────────┐
│  Manual trigger: pre-deploy.yml                          │
│  ✓ Black, isort, Flake8, MyPy, Bandit, pytest            │
│  → No environment (pure code validation)                 │
└───────────────────────┬──────────────────────────────────┘
                        │  You decide to proceed
                        ▼
┌──────────────────────────────────────────────────────────┐
│  Manual trigger: deploy.yml                              │
│  environment: production  ← your EXISTING GitHub env     │
│  → GitHub enforces protection rules (approvals, etc.)   │
│  → Pushes code / runs deploy command                    │
└───────────────────────┬──────────────────────────────────┘
                        │  Deploy done, you verify
                        ▼
┌──────────────────────────────────────────────────────────┐
│  Manual trigger: post-deploy.yml                         │
│  environment: production  ← your EXISTING GitHub env     │
│  → Smoke / integration tests against production          │
│  → Reports health status                                 │
└──────────────────────────────────────────────────────────┘
```

---

### Workflow Files

#### [DELETE] [`deploy.yml`](file:///c:/Users/Ranganathan.9703/Documents/learning/.github/workflows/deploy.yml)
Removed and replaced by the 3 files below.

---

#### [NEW] `pre-deploy.yml`
**Path:** `.github/workflows/pre-deploy.yml`

- Trigger: `workflow_dispatch` only (manual button in GitHub UI)
- Input: `environment` dropdown — `staging` | `production` (informational label, no env lock)
- Jobs:
  - Checkout + Python 3.11 setup + pip cache
  - Black format check
  - isort import order check
  - Flake8 lint check
  - MyPy type check
  - Bandit security scan
  - pytest with coverage report

---

#### [NEW] `deploy.yml`
**Path:** `.github/workflows/deploy.yml`

- Trigger: `workflow_dispatch` only
- Input: `environment` dropdown — `staging` | `production`
- Jobs:
  - `environment: production` — links to your existing GitHub environment, enforces protection rules
  - Checkout + Python 3.11 setup
  - Deploy step (currently a descriptive `echo` placeholder — replace with your real command when ready)
  - Success / failure notification steps

---

#### [NEW] `post-deploy.yml`
**Path:** `.github/workflows/post-deploy.yml`

- Trigger: `workflow_dispatch` only
- Input: `environment` dropdown — `staging` | `production`
- Jobs:
  - `environment: production` — same existing env, tracks deployment history
  - Checkout + Python 3.11 setup + install dev deps
  - Smoke test step (runs `pytest tests/ -m smoke` if smoke markers exist, else a health-check `echo`)
  - Summary report of pass/fail

---

## Verification Plan

### After creation
1. Push the 3 new files to GitHub
2. Go to **Actions tab** in your repo — you should see 3 new workflows listed with a **"Run workflow"** button each
3. Trigger `pre-deploy.yml` → confirm all quality gates pass
4. Trigger `deploy.yml` → confirm the production environment protection rules are enforced
5. Trigger `post-deploy.yml` → confirm smoke test step runs

### Manual Verification
- Each workflow should appear independently in the GitHub Actions sidebar
- The `deploy.yml` and `post-deploy.yml` jobs should show the **environment badge** (`production`) in the run UI
- If Required Reviewers is set on your `production` env, the deploy job should show a **"Waiting for review"** gate before executing
