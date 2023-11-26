resource "aws_ecs_cluster" "app_cluster" {
  name = "ecs-joke-app"
}

resource "aws_ecs_task_definition" "app_task" {
  family                   = "joke-app-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"

  container_definitions = jsonencode([{
    name  = "joke_app"
    image = var.image_uri
    portMappings = [
      {
        containerPort = 5000,
        hostPort      = 5000,
      },
    ]
  }])
}

resource "aws_default_subnet" "default_az1" {
  availability_zone = "us-east-1a"
}

resource "aws_ecs_service" "app_service" {
  name            = "joke-app-service"
  cluster         = aws_ecs_cluster.app_cluster.id
  task_definition = aws_ecs_task_definition.app_task.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  network_configuration {
    assign_public_ip = true
    subnets = [aws_default_subnet.default_az1.id] 
    security_groups = [aws_security_group.ecs_joke.id]
  }
}

resource "aws_security_group" "ecs_joke" {
  name = "sg_ecs_joke"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# resource "null_resource" "public_ip_of_app" {
#   depends_on = [aws_ecs_service.app_service]

#  provisioner "local-exec" {
#     command = "bash get_ip.sh"
#   }
# }