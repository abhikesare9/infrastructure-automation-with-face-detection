provider "aws" {
    region = "ap-south-1"
    access_key = ""
    secret_key = "" 
  
}
resource "aws_instance" "instance"{

  ami = "ami-0ad704c126371a549"
  instance_type = "t2.micro"

}
resource "aws_ebs_volume" "example" {
  availability_zone = aws_instance.instance.availability_zone
  size              = 5

  tags = {
    Name = "extra_volume"
  }
}


resource "aws_volume_attachment" "attachement" {

  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.example.id
  instance_id = aws_instance.instance.id

}
