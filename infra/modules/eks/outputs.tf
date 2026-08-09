output "cluster_id" {
  value = aws_eks_cluster.this.id
}
output "cluster_endpoint" {
  value = aws_eks_cluster.this.endpoint
}
output "cluster_security_group_id" {
  value = aws_eks_cluster.this.vpc_config[0].cluster_security_group_id
}
output "node_role_arn" {
  value = aws_iam_role.node.arn
}
