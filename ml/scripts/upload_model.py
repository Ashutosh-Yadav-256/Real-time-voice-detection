import argparse
import json
import os
from datetime import datetime, timezone

import boto3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_path", type=str, required=True)
    parser.add_argument("--bucket", type=str, required=True)
    parser.add_argument("--model_name", type=str, required=True)
    parser.add_argument("--version", type=str, required=True)
    args = parser.parse_args()

    s3 = boto3.client("s3")
    s3_key = f"models/{args.model_name}/{args.version}/{os.path.basename(args.file_path)}"
    
    s3.upload_file(args.file_path, args.bucket, s3_key)
    
    metadata = {
        "model_name": args.model_name,
        "version": args.version,
        "uploaded_at": datetime.now(timezone.utc).isoformat(),
        "s3_path": f"s3://{args.bucket}/{s3_key}"
    }
    
    metadata_path = "metadata.json"
    with open(metadata_path, "w") as f:
        json.dump(metadata, f)
        
    s3.upload_file(metadata_path, args.bucket, f"models/{args.model_name}/{args.version}/metadata.json")

if __name__ == "__main__":
    main()
