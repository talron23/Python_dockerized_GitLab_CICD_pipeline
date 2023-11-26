sleep 25
aws ec2 describe-network-interfaces --network-interface-ids $(aws ecs describe-tasks --cluster ecs-joke-app --tasks $(aws ecs list-tasks --cluster ecs-joke-app --query "taskArns" --output text) | grep -i eni | awk -F'"' '{print $4}') | grep PublicIp | awk "NR < 2"

