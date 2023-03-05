resource "aws_eip" "nat1" {
  depends_on = [
    aws_internet_gateway.eks_gateway
  ]
}

resource "aws_eip" "nat2" {
  depends_on = [
    aws_internet_gateway.eks_gateway
  ]
}

