output "primary_endpoint_address" {
  value = aws_elasticache_replication_group.this.primary_endpoint_address
}
output "reader_endpoint_address" {
  value = aws_elasticache_replication_group.this.reader_endpoint_address
}
