# Manages the GitHub repository itself as code — zero cloud cost.
# Auth: export GITHUB_TOKEN=<fine-grained PAT with repo admin>; in CI it's a secret.
terraform {
  required_version = ">= 1.6"
  required_providers {
    github = { source = "integrations/github", version = "~> 6.0" }
  }
}

provider "github" { owner = var.github_owner }

variable "github_owner" { type = string }
variable "repo_name"    { type = string, default = "resume-builder-skill" }

data "github_repository" "repo" { name = var.repo_name }

resource "github_branch_protection" "main" {
  repository_id  = data.github_repository.repo.node_id
  pattern        = "main"
  enforce_admins = false
  required_status_checks {
    strict   = true
    contexts = ["ci / test", "ci / lint"]
  }
  required_pull_request_reviews { required_approving_review_count = 0 }
  allows_deletions = false
  allows_force_pushes = false
}

locals {
  labels = {
    "playbook"        = "0e8a16"
    "rubric"          = "1d76db"
    "devops"          = "5319e7"
    "good first issue" = "7057ff"
    "region"          = "fbca04"
  }
}

resource "github_issue_label" "labels" {
  for_each   = local.labels
  repository = data.github_repository.repo.name
  name       = each.key
  color      = each.value
}

resource "github_repository_topics" "topics" {
  repository = data.github_repository.repo.name
  topics     = ["claude-skill", "resume", "ats", "github-actions", "kubernetes", "terraform", "devops"]
}
