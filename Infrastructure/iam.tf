resource "aws_iam_role" "stock_role" {
    name = "stock_role"
    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = "sts:AssumeRole"
                Effect = "Allow"
                Principal = {
                    Service = ["lambda.amazonaws.com", "redshift-serverless.amazonaws.com", "redshift.amazonaws.com"]
                }
            },
        ]
    })
}

resource "aws_iam_role_policy" "stock_role_policy" {
    name = "stock-role-policy"
    role = aws_iam_role.stock_role.id
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Effect = "Allow"
                Action = "s3:ListBucket"
                Resource = aws_s3_bucket.agent_stock_bucket.arn
            },
            {
                Effect = "Allow"
                Action = ["s3:PutObject", "s3:GetObject"]
                Resource = "${aws_s3_bucket.agent_stock_bucket.arn}/*"
            }
        ]
    })
}