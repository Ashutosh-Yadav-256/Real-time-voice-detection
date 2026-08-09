output "audio_bucket_id" {
  value = aws_s3_bucket.audio.id
}
output "models_bucket_id" {
  value = aws_s3_bucket.models.id
}
output "artifacts_bucket_id" {
  value = aws_s3_bucket.artifacts.id
}
