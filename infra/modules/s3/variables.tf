variable "project" {
  type = string
}
variable "environment" {
  type = string
}
variable "kms_key_arn" {
  type = string
}
variable "tags" {
  type    = map(string)
  default = {}
}
