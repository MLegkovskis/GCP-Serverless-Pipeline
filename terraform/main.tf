terraform {
  backend "gcs" {}
}

provider "google" {
  project = "next-gate-tech-project"
  region  = "europe-west2"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
}

variable "function_zip_file" {
  description = "Name of the function zip file"
  type        = string
  default     = "function.zip"
}

data "google_storage_bucket" "function_bucket" {
  name = "next-gate-tech-project-functions"
}

resource "google_cloudfunctions_function" "function" {
  name        = "${var.environment}-hello_next_gate_tech"
  description = "My first function"
  runtime     = "python39"
  source_archive_bucket = data.google_storage_bucket.function_bucket.name
  source_archive_object = var.function_zip_file
  entry_point = "hello_next_gate_tech"
  trigger_http = true
  available_memory_mb = 128
  timeout = 60
  service_account_email = "github-actions-deploy@next-gate-tech-project.iam.gserviceaccount.com"

  lifecycle {
    create_before_destroy = true
  }
}

resource "google_cloudfunctions_function_iam_member" "unauth_invoker" {
  project        = google_cloudfunctions_function.function.project
  region         = google_cloudfunctions_function.function.region
  cloud_function = google_cloudfunctions_function.function.name
  role           = "roles/cloudfunctions.invoker"
  member         = "allUsers"
}
