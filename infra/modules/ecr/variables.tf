variable "project" {
  type = string
}
variable "environment" {
  type = string
}
variable "repositories" {
  type = list(string)
}
variable "tags" {
  type    = map(string)
  default = {}
}
