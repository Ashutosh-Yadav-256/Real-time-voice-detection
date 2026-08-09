variable "cluster_name" {
  type = string
}
variable "kafka_version" {
  type = string
}
variable "broker_count" {
  type = number
}
variable "broker_instance_type" {
  type = string
}
variable "subnet_ids" {
  type = list(string)
}
variable "vpc_id" {
  type = string
}
variable "ebs_volume_size" {
  type = number
}
variable "kms_key_arn" {
  type = string
}
variable "tags" {
  type    = map(string)
  default = {}
}
