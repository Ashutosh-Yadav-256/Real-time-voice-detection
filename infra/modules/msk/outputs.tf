output "bootstrap_brokers_iam" {
  value = aws_msk_cluster.this.bootstrap_brokers_sasl_iam
}
output "zookeeper_connect_string" {
  value = aws_msk_cluster.this.zookeeper_connect_string
}
