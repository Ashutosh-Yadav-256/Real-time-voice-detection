variable "identifier" {
  type = string
}
variable "engine_version" {
  type = string
}
variable "instance_class" {
  type = string
}
variable "allocated_storage" {
  type = number
}
variable "db_name" {
  type = string
}
variable "subnet_ids" {
  type = list(string)
}
variable "vpc_id" {
  type = string
}
variable "kms_key_arn" {
  type = string
}
variable "multi_az" {
  type = bool
}
variable "tags" {
  type    = map(string)
  default = {}
}
