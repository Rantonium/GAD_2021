import os
import subprocess
import sys
from shutil import copyfile

docker_file_template = "FROM python:latest\nADD {script_full_name} /\nADD {script_input} /\nCMD [ \"python\", \"{script_name}\" ]\n"
docker_build_template = "docker build --quiet -t {dockerfile_location}"
docker_run_template = "docker run --name {docker_container} {docker_container}"

inputs = [sys.argv[1], sys.argv[2], sys.argv[3]]

user_id = inputs[0]
script_id = inputs[1]
input_name = inputs[2]

if input_name == "no_input":
    input_name = "none.txt"

docker_file_template = docker_file_template.replace("{script_full_name}", str(script_id) + ".py")
docker_file_template = docker_file_template.replace("{script_name}", str(script_id) + ".py")
docker_file_template = docker_file_template.replace("{script_input}", str(input_name))

## !!!!! USE OS PATH JOIN !!!!!!!! INSTEAD OF CONCATENATION

try:
    os.mkdir(os.getcwd() + "\\" + str(user_id) + "\\DockerFiles\\" + (str(user_id) + "_" + str(script_id) + "_" + str(input_name.split('.')[0])))
except:
    directory_already_exists = 1

docker_file_path = os.getcwd() + "\\" + str(user_id) + "\\DockerFiles\\" + (str(user_id) + "_" + str(script_id) + "_" + str(input_name.split('.')[0]))

copyfile(os.getcwd() + "\\" + str(user_id) + "\\" + "Scripts\\" + str(script_id) + ".py", docker_file_path + "\\" + str(script_id) + ".py")
copyfile(os.getcwd() + "\\" + str(user_id) + "\\" + "Inputs\\" + str(input_name), docker_file_path + "\\" + str(input_name))

new_docker_file = open(docker_file_path + "\\Dockerfile", "w")
new_docker_file.write(docker_file_template)
new_docker_file.close()

docker_build_template = docker_build_template.replace("{dockerfile_location}", (str(user_id) + "_" + str(script_id) + "_" + str(input_name.split('.')[0]) + " " + docker_file_path + "\\"))
docker_run_template = docker_run_template.replace("{docker_container}", (str(user_id) + "_" + str(script_id) + "_" + str(input_name.split('.')[0])))


build_process = subprocess.Popen(docker_build_template, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
build_process.communicate()
build_process.wait()

run_process = subprocess.Popen(docker_run_template, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output = run_process.communicate()[0]
run_process.wait()

remove_process = subprocess.Popen("docker rm " + (str(user_id) + "_" + str(script_id) + "_" + str(input_name.split('.')[0])))
remove_output = remove_process.communicate()

print(str("%%%%%" + str(output, "utf-8")), end="")
