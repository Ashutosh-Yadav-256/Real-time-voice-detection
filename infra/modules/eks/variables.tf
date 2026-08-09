variable "cluster_name" {
  type = string
}
variable "cluster_version" {
  type = string
}
variable "vpc_id" {
  type = string
}
variable "subnet_ids" {
  type = list(string)
}
variable "environment" {
  type = string
}
variable "tags" {
  type    = map(string)
  default = {}
}
